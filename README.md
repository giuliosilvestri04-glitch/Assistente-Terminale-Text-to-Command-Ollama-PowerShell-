# Assistente Terminale Text-to-Command (Ollama + PowerShell)

Un assistente da riga di comando che traduce richieste in linguaggio
naturale (in italiano) in comandi PowerShell, usando un modello di
Intelligenza Artificiale che gira interamente **in locale** grazie a
[Ollama](https://ollama.com). Nessun dato lascia mai il tuo PC.

## Indice

- [Come funziona](#come-funziona)
- [Funzionalità principali](#funzionalità-principali)
- [Prerequisiti](#prerequisiti)
- [Installazione](#installazione)
- [Avvio](#avvio)
- [Esempio d'uso](#esempio-duso)
- [Configurazione](#configurazione)
- [Avvertenze di sicurezza](#avvertenze-di-sicurezza)
- [Struttura del progetto](#struttura-del-progetto)
- [Risoluzione dei problemi](#risoluzione-dei-problemi)
- [Limiti noti](#limiti-noti)
- [Contribuire](#contribuire)
- [Licenza](#licenza)

## Come funziona

1. Scrivi cosa vuoi fare, in italiano normale.
2. Il programma manda la richiesta al modello Ollama installato sul tuo PC.
3. Il modello risponde con: il comando PowerShell, una spiegazione e un
   livello di rischio (SICURO / ATTENZIONE / PERICOLOSO).
4. Il programma ti mostra tutto e ti chiede conferma esplicita.
5. Solo dopo la tua conferma, il comando viene davvero eseguito.

## Funzionalità principali

- **100% locale**: nessuna chiamata a servizi cloud, nessuna API key richiesta.
- **Traduzione linguaggio naturale → PowerShell** tramite modello Ollama configurabile.
- **Valutazione del rischio** (SICURO / ATTENZIONE / PERICOLOSO) prima di ogni esecuzione.
- **Conferma esplicita obbligatoria**: nessun comando parte senza il tuo "sì".
- **Output a colori** nel terminale (tramite `colorama`) per leggere rapidamente comando, spiegazione e rischio.
- **Gestione robusta degli errori**: Ollama non avviato, modello non scaricato, risposta malformata sono tutti casi gestiti con messaggi chiari.
- **Avvio rapido su Windows** tramite doppio click su `Avvia_Assistente.bat`.

## Prerequisiti

- Windows 10 o 11
- Python 3.9 o superiore
- [Ollama](https://ollama.com/download) installato
- Il modello scaricato in locale:
  ```powershell
  ollama pull llama3.1:8b
  ```

## Installazione

```powershell
# 1. Entra nella cartella del progetto
cd ollama-terminal-assistant

# 2. (Consigliato, non obbligatorio) crea un ambiente virtuale
python -m venv venv
venv\Scripts\activate

# 3. Installa le dipendenze
pip install -r requirements.txt
```

## Avvio

Assicurati prima che Ollama sia in esecuzione (su molte installazioni
parte già automaticamente in background dopo l'installazione; in caso
contrario):

```powershell
ollama serve
```

Poi avvia l'assistente in uno dei due modi:

```powershell
# Da terminale
python src/main.py
```

oppure, su Windows, con doppio click sul file **`Avvia_Assistente.bat`**
nella cartella principale del progetto: apre automaticamente un
terminale nella cartella corretta, avvia lo script e mantiene la
finestra aperta anche in caso di errore, per poterlo leggere.

## Esempio d'uso

```
Cosa vuoi fare? > Trova i file più grandi di 1GB nel disco C

------------------------------------------------------------
COMANDO PROPOSTO:
  Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.Length -gt 1GB}

SPIEGAZIONE:
  Cerca ricorsivamente tutti i file nel disco C più grandi di 1 gigabyte.

LIVELLO DI RISCHIO:
  SICURO
------------------------------------------------------------

Vuoi eseguire questo comando? (s/n):
```

Scrivi `esci` in qualsiasi momento per chiudere il programma.

## Configurazione

Tutte le impostazioni si trovano in `src/config.py`:

- `OLLAMA_MODEL` — il modello da usare (default: `llama3.1:8b`). Cambialo
  se vuoi provare un altro modello scaricato con `ollama pull` (es.
  `mistral`, `phi3`, `qwen2.5:7b`). Modelli più piccoli sono più veloci
  ma seguono il formato di risposta richiesto in modo meno affidabile;
  modelli più grandi sono più lenti ma più precisi.
- `SYSTEM_PROMPT` — le istruzioni rigide date all'IA per farla rispondere
  sempre nel formato `COMANDO / SPIEGAZIONE / RISCHIO`.
- `DELIMITATORE` — il simbolo (`---`) usato per separare le 3 sezioni.
  Se lo cambi, valuta che non compaia già all'interno delle risposte
  tipiche del modello scelto.

## Avvertenze di sicurezza

- Leggi **sempre** il comando proposto e il livello di rischio prima di
  confermare l'esecuzione.
- I comandi con rischio **PERICOLOSO** possono cancellare dati, modificare
  il registro di sistema o eseguire operazioni irreversibili: valuta con
  molta attenzione prima di confermare.
- La classificazione del rischio è **una stima del modello**, non una
  verifica tecnica: un comando può essere valutato in modo errato.
  Non fidarti ciecamente dell'etichetta SICURO.
- Il comando viene eseguito con gli **stessi permessi del tuo utente
  Windows**: lo strumento non applica sandboxing o restrizioni aggiuntive
  oltre alla conferma manuale.
- L'IA può sbagliare o generare comandi non ottimali: questo strumento
  non sostituisce il buon senso né la comprensione di ciò che stai eseguendo.
- Essendo tutto locale, nessuna richiesta o risposta viene inviata fuori
  dal tuo PC: l'unico traffico di rete è quello locale verso Ollama.

## Struttura del progetto

```
ollama-terminal-assistant/
│
├── .gitignore
├── README.md
├── requirements.txt
├── Avvia_Assistente.bat   # Avvio rapido su Windows con doppio click
└── src/
    ├── __init__.py
    ├── main.py            # Punto di ingresso del programma
    ├── config.py          # Impostazioni generali
    ├── llm.py             # Interazione con il modello locale
    ├── parser.py          # Analisi e formattazione della risposta
    └── executor.py        # Esecuzione sicura dei comandi
```

## Risoluzione dei problemi

**"Impossibile contattare Ollama"**
Ollama non è in esecuzione. Apri un terminale ed esegui `ollama serve`,
poi riprova.

**"Errore nella risposta di Ollama" / modello non trovato**
Il modello configurato in `OLLAMA_MODEL` non è stato scaricato. Esegui
`ollama pull <nome-modello>` (es. `ollama pull llama3.1:8b`).

**"Errore nel formato della risposta"**
Il modello non ha risposto nel formato `COMANDO / SPIEGAZIONE / RISCHIO`
atteso — capita più spesso con modelli piccoli o richieste molto
ambigue. Prova a riformulare la richiesta in modo più semplice e diretto,
oppure prova un modello diverso.

**I colori non vengono visualizzati correttamente nel terminale**
Assicurati di usare un terminale che supporta i colori ANSI (PowerShell
moderno o Windows Terminal funzionano bene); `colorama` gestisce la
compatibilità automaticamente su Windows.

## Limiti noti

- Genera **un solo comando per volta**: non è pensato per script multi-step
  o pipeline complesse su più righe.
- L'affidabilità del comando generato dipende dal modello scelto: modelli
  piccoli (es. 7-8B) possono produrre comandi PowerShell non ottimali.
- Non mantiene una cronologia dei comandi eseguiti né offre un "annulla".
- Nessun log persistente delle esecuzioni.

## Contribuire

Segnalazioni di bug e proposte di miglioramento sono benvenute tramite
Issue o Pull Request.

## Licenza

Non è ancora presente un file di licenza in questo repository. Se vuoi
rendere il progetto open source, aggiungi un file `LICENSE` (ad esempio
con licenza MIT) prima della pubblicazione.