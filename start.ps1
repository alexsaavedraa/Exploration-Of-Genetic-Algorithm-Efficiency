$choice = Read-Host "Do you want to see a robot? (y/n)"
if ($choice.ToLower() -eq "y") {
    Start-Process python "display.py"
} elseif ($choice.ToLower() -eq "n") {
    Start-Process python "main.py"
} else {
    Write-Host "Invalid input. Please enter 'y' or 'n'."
}
