#####################################################################
#  Nom     : divers.ps1
#  Version : 1.0
#  Date de création : le 07/02/2022
#  Description : TP Powershell SEREW
#####################################################################


# Réponse de la question 1 à 4
$file = Get-ChildItem -Recurse -Include ('*.docx','*.html','secret.txt') | Where-Object {$_.LastWriteTime.Year -ge '2022'}  
$file 

# Réponse de la question 5
Compress-Archive $file -DestinationPath $env:UserProfile\Documents\mail.zip -CompressionLevel Fastest

# Réponse de la question 6
Get-Process WINWORD.EXE | Stop-Process

# Réponse de la question 7
$tab = @(“google.com”,”portal.office.com”,”microsoft.com”,"pcastuces.com","aidermicheline.com")
foreach ($item in $tab){
    If(Test-Connection -Quiet $item){
        Write-Host $item : "OK"

    }else{
        Write-Host $item : "KO"
        }
  }
