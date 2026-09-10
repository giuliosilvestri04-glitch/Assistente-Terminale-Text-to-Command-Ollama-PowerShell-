import ollama
from config import OLLAMA_MODEL, SYSTEM_PROMPT

def chiedi_a_ollama(richiesta_utente: str) -> str:
    """Invia la richiesta a Ollama e restituisce la risposta grezza."""
    risposta = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": richiesta_utente},
        ],
    )
    return risposta["message"]["content"]
