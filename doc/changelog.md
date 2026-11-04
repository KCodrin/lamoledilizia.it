# Changelog

## 2026-11-04 · Tolte tutte le emoji
**Cosa:** tolte emoji e simboli dal sito: icone dei riquadri "Che problema hai?", fulmine e telefono nella barra in alto, icone dei punti nella testata (ora numeri 01-02-03), stelline nel badge e nelle recensioni, spunte negli elenchi (ora pallini oro disegnati in CSS).
**Perché:** regola del cliente: mai emoji. Aggiunta in `agent.md` e `brand/voice.md`.
**Verifica:** controllo automatico su pagine, script, CSS, JS e documentazione: nessuna emoji rimasta.

## 2026-11-04 · Hero home: da tutto schermo a riquadro
**Cosa:** quando si entra in home la testata è a tutto schermo, da bordo a bordo e senza angoli arrotondati. Scorrendo verso il basso (nei primi 250px) si stacca dai bordi e prende gli angoli arrotondati, diventando il riquadro di prima.
**Perché / Dettagli:** richiesto dal cliente. CSS in fondo a `style.css`, poche righe in `main.js`. Senza JavaScript resta il riquadro arrotondato. Tolta una vecchia regola CSS non più usata.
**Verifica:** controllati gli stili: all'apertura 0px di margine e angoli a 0 con testata alta quanto lo schermo; a scorrimento completato 16px di margine e angoli a 20px. Lo scorrimento reale non è stato provato (pannello del browser nascosto).

## 2026-11-04 · Angoli arrotondati uniformi
**Cosa:** tutti i riquadri, le foto, le card, la barra in alto, la testata della home e i campi del modulo hanno ora lo stesso arrotondamento dell'header (20px). Le icone piccole dentro i riquadri usano 12px. Tutti i bottoni sono a pillola, come quello dell'header.
**Perché:** richiesto dal cliente: gli arrotondamenti erano troppo diversi (6, 12, 14, 20, 28px).
**Verifica:** controllo dei valori nel CSS: restano solo i due token, le pillole e i cerchi.

## 2026-11-04 · Testi più chiari: cosa facciamo e per chi
**Cosa:** riscritta la home. Il titolo ora dice cosa facciamo ("Lavori su tetti e facciate senza ponteggi"). Aggiunte le sezioni "Che problema hai?" (8 problemi collegati al servizio giusto), "Come gli alpinisti, ma sul tuo palazzo" (cos'è l'edilizia su fune), "Per chi lavoriamo" (amministratori, aziende, privati), "Come lavoriamo" (4 passi) e "Domande frequenti" (6 domande). Riscritte le 12 pagine dei servizi con lo schema problema → cosa ricevi → come interveniamo, togliendo il gergo tecnico (grafene, robot, UV-C, nanotecnologie). La fascia finale di ogni servizio ora nomina quel servizio. Tolte le percentuali in contrasto tra loro (70% e 40% di risparmio).
**Perché:** il sito descriveva l'azienda più che i problemi che risolve; testi poco credibili e numeri incoerenti.
**Verifica:** pagine rigenerate, nessun link rotto; testo della home e di una pagina servizio controllato nel browser (screenshot non disponibili: pannello nascosto).

## 2026-11-04 · Header dentro la hero
**Cosa:** l'header a pillola ora sta dentro la testata con foto (sopra l'immagine) invece che sopra di essa, su tutte le pagine; continua a restare fisso scorrendo.
**Perché / Dettagli:** richiesto dal cliente. Solo CSS, in fondo a `assets/css/style.css`.
**Verifica:** controllo a schermo desktop e mobile.

## 2026-11-04 · Configurazione Vercel
**Cosa:** aggiunti `vercel.json` (sito statico: nessun framework, nessuna build, pagine servite dalla cartella principale) e `.vercelignore` (non pubblica `src/`, `doc/`, `CLAUDE.md`).
**Perché:** su Vercel il sito dava errore 404, probabile rilevamento sbagliato del tipo di progetto o della cartella di uscita.
**Verifica:** da controllare dopo il push con un nuovo deploy su Vercel.

## 2026-11-04 · Pubblicato su GitHub
**Cosa:** la cartella SITO NUOVO è diventata un repository git ed è stata caricata su GitHub (KCodrin/lamoledilizia.it, ramo main). Aggiunto `.gitignore`.
**Verifica:** push riuscito.

## 2026-11-04 · Barra in alto e header a pillola su tutte le pagine
**Cosa:** la barra blu in alto e l'header bianco a pillola, prima solo in home, ora sono su tutte le pagine. Tolto il vecchio header blu.
**Perché / Dettagli:** richiesto dal cliente. Funzione `header()` in `src/build.py`.
**Verifica:** pagine rigenerate, controllo a schermo su una pagina servizio (desktop e mobile).

## 2026-11-04 · Home: barra in alto, header a pillola, hero a tutto schermo
**Cosa:** solo in home, aggiunta una barra blu arrotondata in alto (senza ponteggi · Torino e tutta Italia · telefono), un header bianco a pillola che resta fisso scorrendo, con logo blu e bottone "Richiedi un preventivo", e una testata a tutto schermo con angoli arrotondati, badge, titolo grande e tre punti di forza. Tolta la fascia dei numeri sotto la testata, perché i punti ora sono dentro la testata. Le altre pagine non cambiano.
**Perché / Dettagli:** richiesto dal cliente su un riferimento grafico. Codice in `src/build.py` (header, home) e in fondo a `assets/css/style.css`. Il logo blu si ottiene colorando con il CSS il logo bianco esistente.
**Verifica:** controllo a schermo su desktop e mobile (375px), nessuno scorrimento orizzontale.

## 2026-11-04 · Colori del marchio
**Cosa:** il colore primario diventa il blu #282e69 (prima antracite #171a1a); il secondario resta l'oro #d39f6f. Adeguati di conseguenza fascia numeri, footer, velature sulle foto e grigio dei testi secondari.
**Perché / Dettagli:** colori indicati dal cliente; token in `assets/css/style.css`, aggiornati `design.md` e `agent.md`.
**Verifica:** controllo a schermo.

## 2026-11-04 · Meta Pixel
**Cosa:** aggiunto il codice Meta Pixel (3593393790961940) in tutte le pagine; aggiornata la pagina privacy.
**Perché / Dettagli:** richiesto dal cliente; inserito in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte e identico all'originale.

## 2026-11-04 · Verifica dominio Facebook
**Cosa:** aggiunto il codice di verifica del dominio di Facebook in tutte le pagine.
**Perché / Dettagli:** richiesto dal cliente; inserito in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte.

## 2026-11-04 · Google Analytics
**Cosa:** aggiunto il codice di Google Analytics (G-29DS1SS66B) in tutte le pagine. Aggiornata la frase della pagina privacy che diceva "nessun tracciamento".
**Perché / Dettagli:** richiesto dal cliente; inserito una volta sola in `src/build.py` (funzione `head`).
**Verifica:** rigenerate le pagine, codice presente in tutte.

## 2026-11-04 · Modulo contatti: resta via email
**Cosa:** deciso con il cliente che il modulo contatti continua ad aprire il programma di posta, senza servizi esterni. Aggiornati wiki, informazioni cliente e roadmap.
**Verifica:** nessuna modifica al sito, solo documentazione.

## 2026-11-04 · Nuovo sito
**Cosa:** rifatto il sito di La Mole Edilizia su Fune da zero, con nuova grafica, riportando tutti i testi, le immagini e i contatti del vecchio sito WordPress. Ogni pagina tiene lo stesso indirizzo di prima.
**Perché / Dettagli:** pagine generate da `src/build.py`; stile in `assets/css/style.css`; immagini ridimensionate in `assets/img/`. Aggiunte: briciole di percorso, link "altri servizi", tabella di confronto leggibile su telefono, bottone WhatsApp, sitemap. Corretti piccoli refusi dei testi (es. "al'edilizia", "piattaforme aree", "incompleta sospensione"). Pagina privacy segnaposto in attesa del testo legale.
**Verifica:** lo script controlla che nessun link sia rotto (OK, 24 pagine); controllo a schermo su desktop e mobile (375px), menu mobile funzionante, nessuno scorrimento orizzontale.
