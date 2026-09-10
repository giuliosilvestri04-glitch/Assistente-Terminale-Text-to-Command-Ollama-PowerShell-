"""
config.py
---------
Questo file contiene tutte le "impostazioni" del programma.

Perché un file a parte? Perché è una buona pratica di programmazione:
se domani vuoi cambiare il modello di Ollama o il testo delle istruzioni
per l'IA, non devi cercare in mezzo al codice principale (main.py),
ma modifichi solo questo file. main.py resta sempre pulito e stabile.
"""

# Nome del modello Ollama che vogliamo usare.
# "llama3.1:8b" è il modello richiesto di default.
# Se in futuro vuoi provare un altro modello (es. "mistral" o "phi3"),
# ti basta cambiare questa riga: tutto il resto del programma si adatta
# automaticamente, perché main.py legge questo valore da qui.
OLLAMA_MODEL = "llama3.1:8b"

# Il "delimitatore" è il simbolo che useremo per separare le 3 sezioni
# della risposta dell'IA (COMANDO, SPIEGAZIONE, RISCHIO).
# Lo teniamo come variabile (invece di scriverlo a mano più volte) così
# è facile da cambiare e lo riusiamo sia nel prompt sia nel codice che
# "smonta" la risposta (il cosiddetto parsing).
DELIMITATORE = "---"

# Questo è il "System Prompt": sono le istruzioni che diamo all'IA
# PRIMA di ogni conversazione, per dirle esattamente come comportarsi.
# Deve essere molto rigido, perché vogliamo che l'IA risponda SEMPRE
# nello stesso identico formato: solo così il nostro codice Python
# riesce a "leggere" la risposta in modo automatico e affidabile.
SYSTEM_PROMPT = f"""Sei un assistente esperto di Windows PowerShell. Il tuo unico compito è
tradurre una richiesta scritta in linguaggio naturale (in italiano) in UN SINGOLO
comando PowerShell valido.

REGOLE FERREE DA RISPETTARE SEMPRE, SENZA ECCEZIONI:
1. Rispondi SOLO ed ESCLUSIVAMENTE nel formato indicato sotto. Niente saluti,
   niente frasi introduttive, niente markdown, niente blocchi di codice con backtick.
2. Le 3 sezioni devono essere separate dal delimitatore "{DELIMITATORE}" da solo su una riga.
3. Il campo COMANDO deve contenere SOLO ed ESCLUSIVAMENTE il comando PowerShell,
   su una sola riga, senza commenti e senza backtick.
4. Il campo RISCHIO deve contenere UNA sola parola tra: SICURO, ATTENZIONE, PERICOLOSO.
   - SICURO: comandi di sola lettura, che non modificano o cancellano nulla (es. Get-ChildItem, Get-Process).
   - ATTENZIONE: comandi che modificano file o impostazioni, ma in modo reversibile o limitato.
   - PERICOLOSO: comandi che cancellano dati, formattano dischi, spengono/riavviano il PC,
     modificano il registro di sistema o eseguono operazioni irreversibili.

FORMATO OBBLIGATORIO DELLA RISPOSTA (rispetta esattamente questa struttura, riga per riga):
COMANDO: <qui il comando PowerShell>
{DELIMITATORE}
SPIEGAZIONE: <qui una breve spiegazione in italiano, massimo due frasi>
{DELIMITATORE}
RISCHIO: <SICURO oppure ATTENZIONE oppure PERICOLOSO>
"""
