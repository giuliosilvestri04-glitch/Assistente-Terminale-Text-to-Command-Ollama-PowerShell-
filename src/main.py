import sys
import httpx
import ollama
from colorama import init, Fore, Style

# Importazioni dai moduli separati
from config import OLLAMA_MODEL
from llm import chiedi_a_ollama
from parser import analizza_risposta, stampa_risultato
from executor import esegui_comando, chiedi_conferma

# Attivazione dei colori per Windows
init(autoreset=True)

def stampa_benvenuto():
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print(Fore.CYAN + Style.BRIGHT + "  ASSISTENTE TERMINALE TEXT-TO-COMMAND (Ollama + PowerShell)")
    print(Fore.CYAN + Style.BRIGHT + "=" * 62)
    print(Fore.WHITE + "Scrivi cosa vuoi fare, in italiano. Esempio:")
    print(Fore.WHITE + '  "Trova i file più grandi di 1GB nel disco C"')
    print(Fore.WHITE + "Scrivi 'esci' in qualsiasi momento per chiudere il programma.\n")

def main():
    stampa_benvenuto()

    while True:
        richiesta_utente = input(
            Fore.CYAN + Style.BRIGHT + "\nCosa vuoi fare? > " + Style.RESET_ALL
        ).strip()

        if richiesta_utente.lower() in ("esci", "exit", "quit"):
            print(Fore.CYAN + "Chiusura del programma. A presto!")
            sys.exit(0)

        if not richiesta_utente:
            continue

        try:
            testo_grezzo = chiedi_a_ollama(richiesta_utente)
            dati = analizza_risposta(testo_grezzo)
            stampa_risultato(dati)

            if chiedi_conferma():
                esegui_comando(dati["comando"])
            else:
                print(Fore.YELLOW + "Comando NON eseguito.")

        except ollama.ResponseError as errore:
            print(Fore.RED + f"\nErrore nella risposta di Ollama: {errore}")
            print(Fore.RED + "Verifica di aver scaricato il modello con: ollama pull " + OLLAMA_MODEL)
        except httpx.ConnectError:
            print(Fore.RED + "\nImpossibile contattare Ollama. È avviato sul tuo PC?")
            print(Fore.RED + "Prova ad aprire un terminale ed eseguire il comando: ollama serve")
        except ValueError as errore:
            print(Fore.RED + f"\nErrore nel formato della risposta: {errore}")
            print(Fore.RED + "Prova a riformulare la richiesta in modo più semplice e diretto.")
        except Exception as errore:
            print(Fore.RED + f"\nSi è verificato un errore imprevisto: {errore}")

if __name__ == "__main__":
    main()
