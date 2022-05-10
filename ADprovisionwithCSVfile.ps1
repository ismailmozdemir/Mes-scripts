#####################################################################
# Nom : [LPASSR]_OZDEMIR-Ismail_Rendu_Powershell_Active_Directory.ps1
# Version : 1.0
# Cree par: OZDEMIR Ismail
# Date de création : le 21/03/2022
# Date de modification : Aucun
# Modification par : Aucun
# Description : TP Powershell SEREW 4 Active Directory
######################################################################

# Importation du module Active Directory
Import-Module ActiveDirectory

# Initialisation des variables et des constantes
$domainDC = Get-ADDomain | Select-String "DC="
$OU = @("ITA","ESP","ALL","ENG")
$subOU = @("Direction","DSI","Securite","Compta")
$domain = $env:USERDNSDOMAIN.ToLower()
$CSV = "C:\users.csv"
$Account = "C:\comptes.txt"
$LogName = "Active_Directory"
$SourceName = "Creation_of_User"
$UserLogExist = "0"
$LogExists = [System.Diagnostics.Eventlog]::Exists($LogName)

# Dans le cas ou le journal n'existe pas, il faut le créer, sinon informer l'utilisateur qu'il existe
if($LogExists -eq $false){
    New-EventLog -LogName $LogName -Source $SourceName 
}else{
    Write-Output "`n`Le journal $LogName existe déjà"
}

# Si l'arborescence des OU n'existe pas, alors les créer grâce à une boucle imbriquée, sinon informer l'utilisateur qu'ils existent
try{
    for ($i=0;$i -lt $OU.Length;$i++){
        New-ADOrganizationalUnit -Name "$($OU[$i])" -Path $domainDC –ProtectedFromAccidentalDeletion $false

        for ($j=0;$j -lt $subOU.Length;$j++){
            New-ADOrganizationalUnit -Name "$($subOU[$j])" -Path "OU=$($OU[$i]),$domainDC" –ProtectedFromAccidentalDeletion $false    
        }
    }
}
catch [Microsoft.ActiveDirectory.Management.ADException]
{ 
Write-Host "`n`L'OU $OU existe déjà" 
}

# Fonction qui génère un mot de passe aléatoire
Function Get-MdpGen {
    for ($i=0;$i -lt 6;$i++){
        $lettre += ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z") | Get-Random
    }

    $nombre = Get-Random -Minimum 1 -Maximum 100
    $caracspec = ("`$","@","&","!") | Get-Random
    $pasString = $lettre+$nombre+$caracspec
    $lettre = $null
    return $pasString

}

# Importation du fichier CSV
Import-Csv -Delimiter ";" -Path $CSV |

# Boucle pour la création des utilisateurs en utilisant le fichier CSV
ForEach-Object {$i = 1} {

    # Initialisation des variables pour la création des utilisateurs grâce au fichier CSV
    $FirstName = $_.Prenom
    $LastName = $_.Nom
    $UserLog = ($FirstName).Substring(0,1).ToLower() + $LastName.ToLower()

    # Si le nom d'utilisateur existe déjà, alors créer un utilisateur avec comme nom son nom + 0 à la fin de celui-ci
    if (Get-ADUser -Filter "SamAccountName -eq '$UserLog'"){
        $LastName = $LastName + $UserLogExist
        $UserLog = ($FirstName).Substring(0,1).ToLower() + $LastName.ToLower()
        
    }

    $Name = "$FirstName $LastName"
    $pOU = $_.Pays
    $altOU = $_.Departement
    $UserOU= "OU=$altOU,OU=$pOU,$domainDC"
    $upn = "$UserLog@$domain"
    
    # Appel de la fonction pour générer le mot de passe de l'utilisateur
    $pass = Get-MdpGen

    # Écrire le mot de passe ainsi que le login de l'utilisateur dans un fichier txt 
    "$UserLog : $pass" | Out-File -Append $Account
    
    # Écriture des events pour la création de chaque utilisateur
    Write-EventLog –LogName $LogName –Source $SourceName –EntryType Information –EventID $i –Message "$SourceName $UserLog"

    # Compteur qui s'incrémente de 1 pour l'EventID 
    $i++
     
        # Création des utilisateurs en utilisant les variables initiées plus haut, si le login existe déjà, informer l'utilisateur
        try{
            New-ADUser  -Name "$Name" `
                -DisplayName "$Name" `
                -GivenName $FirstName `
                -Surname $LastName `
                -SamAccountName $UserLog `
                -UserPrincipalName "$upn" `
                -Path "$UserOU" `
                -AccountPassword (ConvertTo-SecureString $pass -AsPlainText -Force) `
                -ChangePasswordAtLogon $true `
                -Enabled $true

        }
            catch [Microsoft.ActiveDirectory.Management.ADIdentityAlreadyExistsException] 
        { 
            Write-Host "`n`L'utilisateur $UserLog existe déjà"

        }
}
