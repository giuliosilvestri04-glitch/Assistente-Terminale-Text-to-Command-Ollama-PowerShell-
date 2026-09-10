from colorama import Fore, Style
from config import DELIMITATORE

def analizza_risposta(testo_grezzo: str) -> dict:
    """Smonta la risposta grezza di Ollama nelle 3 sezioni."""
    sezioni = testo_grezzo.strip().split(DELIMITATORE)
    if len(sezioni) != 3:
        raise ValueError(
            "La risposta dell'IA non è nel formato atteso (3 sezioni separate dal delimitatore)."
        )
    def estrai_contenuto(testo: str) -> str:
        testo = testo.strip()
        if ":" in testo and len(testo.split(":", 1)[0]) < 20:
            return testo.split(":", 1)[1].strip()
        return testo

    comando = estrai_contenuto(sezioni[0])
    spiegazione = estrai_contenuto(sezioni[1])
    rischio = estrai_contenuto(sezioni[2]).upper()
    return {
        "comando": comando,
        "spiegazione": spiegazione,
        "rischio": rischio,
    }

def colore_per_rischio(rischio: str) -> str:
    """Restituisce il colore associato al livello di rischio."""
    if rischio == "SICURO":
        return Fore.GREEN
    elif rischio == "ATTENZIONE":
        return Fore.YELLOW
    elif rischio == "PERICOLOSO":
        return Fore.RED
    else:
        return Fore.WHITE

def stampa_risultato(dati: dict):
    """Stampa a schermo i risultati analizzati."""
    colore_rischio = colore_per_rischio(dati["rischio"])
    print("\n" + Fore.CYAN + "-" * 62)
    print(Fore.WHITE + Style.BRIGHT + "COMANDO PROPOSTO:")
    print(Fore.MAGENTA + f"  {dati['comando']}")
    print(Fore.WHITE + Style.BRIGHT + "\nSPIEGAZIONE:")
    print(Fore.WHITE + f"  {dati['spiegazione']}")
    print(Fore.WHITE + Style.BRIGHT + "\nLIVELLO DI RISCHIO:")
    print(colore_rischio + Style.BRIGHT + f"  {dati['rischio']}")
    print(Fore.CYAN + "-" * 62)
