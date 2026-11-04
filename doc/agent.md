# agent.md — Regole per chi lavora su La Mole Edilizia su Fune (persone e AI)

> Leggere questo file prima di toccare qualsiasi cosa. Per i dettagli: `design.md`, `brand/voice.md`.

## 1 · Ambito e permessi
- Cartelle: `SITO NUOVO/` (il sito), `SITO NUOVO/doc/` (documentazione, da tenere aggiornata), `SITO VECCHIO/` (sola lettura, archivio del sito WordPress).
- Le pagine `.html` sono **generate**: non si modificano a mano. Testi, header e footer si cambiano in `src/build.py`, poi `python3 src/build.py`.
- Si modifica ciò che l'utente chiede, e solo quello. Nel dubbio si chiede.
- `git commit` e `git push` **solo su richiesta esplicita**, mai `--force`.
- Prima di cancellare file o pagine si controlla dove sono usati. Gli indirizzi delle pagine (`nome.html`) restano uguali al vecchio sito per non perdere Google.
- Mai password, token o chiavi private nel codice, nel changelog o nei commit.
- I testi legali e i dati dell'azienda non si inventano: si inseriscono come forniti e si segnalano le incongruenze.

## 2 · Regola obbligatoria del changelog
Ogni modifica, anche piccola, va registrata in `doc/changelog.md` **nello stesso turno di lavoro**. Formato: `## AAAA-MM-GG · Titolo` + **Cosa / Perché / Verifica**.

## 3 · Design system
Fonte di verità: `assets/css/style.css` (token in `:root`). Non si inventano valori: si usano i token. Colori del marchio: primario blu `#282e69` e secondario oro `#d39f6f`; font Montserrat (locale, nessun Google Fonts).

## 4 · Stack
HTML + CSS + un piccolo JS, generati da uno script Python senza dipendenze. Nessuna libreria esterna a runtime, nessun CMS.

## 5 · Prima di dichiarare un lavoro finito
1. `python3 src/build.py` stampa `OK` (controlla anche i link rotti).
2. Controllato a schermo su desktop e su mobile.
3. `doc/` aggiornata.

## 6 · Regole del cliente (si aggiungono man mano)
- (nessuna ancora)
