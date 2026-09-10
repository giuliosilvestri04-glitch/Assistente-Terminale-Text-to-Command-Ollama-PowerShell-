import subprocess
from colorama import Fore, Style

def esegui_comando(comando: str):
    """Esegue il comando PowerShell sul sistema in modo sicuro."""
    print(Fore.CYAN + "\nEsecuzione in corso...\n")
    comando_completo = ["powershell.exe", "-NoProfile", "-Command", comando]
    risultato = subprocess.run(comando_completo, capture_output=True, text=True)

    if risultato.stdout:
        print(Fore.GREEN + "OUTPUT:")
        print(risultato.stdout)

    if risultato.stderr:
        print(Fore.RED + "ERRORI:")
        print(risultato.stderr)

    if risultato.returncode == 0:
        print(Fore.GREEN + "Comando eseguito con successo.\n")
    else:
        print(Fore.RED + f"Il comando è terminato con codice di errore: {risultato.returncode}\n")

def chiedi_conferma() -> bool:
    """Chiede all'utente di confermare l'esecuzione del comando."""
    risposta = input(
        Fore.YELLOW + Style.BRIGHT + "\nVuoi eseguire questo comando? (s/n): "
    ).strip().lower()
    return risposta == "s"
