#!/usr/bin/env python3
"""Genera le pagine HTML del sito in SITO NUOVO/. Uso: python3 src/build.py
Testi ripresi dal vecchio sito (SITO VECCHIO/). Header, footer e CTA sono qui, una volta sola."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent.parent
SITE = "https://www.lamoledilizia.it"  # da confermare: dominio con o senza www

TEL, TEL_LINK = "011 428 7322", "+390114287322"
CELL, WA = "327 448 1224", "https://wa.me/393274481224"
EMAIL = "fune@lamoledilizia.com"
ADDR = "Via Camillo Cenni 17, 10095 Grugliasco (TO)"
SOCIAL = [("Facebook", "https://www.facebook.com/lamoleediliziasufune/"),
          ("Instagram", "https://www.instagram.com/lamolediliziasufune/"),
          ("TikTok", "https://www.tiktok.com/@la_mole_edilizia_su_fune"),
          ("WhatsApp", WA)]

# --- Servizi: 4 categorie, ognuna con le sue pagine di dettaglio -----------------
CATS = [
    dict(slug="servizi-edilizia-su-fune-pulizia-e-manutenzione", title="Pulizia e Manutenzione", img="pulizia-e-manutenzione.jpg",
         desc="Pulizia e manutenzione vetri, grondaie, tetti e coperture: allontanamento volatili, check-up tetti senza ponteggi, interventi rapidi, sicuri e green.",
         intro="Interveniamo in sicurezza e senza ponteggi grazie all’edilizia su fune, offrendo servizi mirati di pulizia e manutenzione per edifici di ogni tipo. Dall’allontanamento volatili al lavaggio vetri, dalla pulizia di grondaie e tetti al check-up completo delle coperture: lavoriamo in quota con efficienza, precisione e rispetto per l’ambiente.",
         items=["servizi-allontanamento-volatili", "servizi-lavaggio-vetri", "servizi-pulizia-canali-gronda-e-tetti", "servizi-sicurezza-e-check-up-tetti"]),
    dict(slug="servizi-edilizia-su-fune-impermeabilizzazione", title="Impermeabilizzazione", img="impermeabilizzazione.jpg",
         desc="Impermeabilizziamo tetti, cornicioni e terrazzi senza ponteggi: barriere anti-infiltrazione, isolamento termico e lavori rapidi e sicuri con edilizia su fune.",
         intro="Con l’edilizia su fune realizziamo interventi di impermeabilizzazione su tetti, cornicioni e terrazzi senza l’impiego di ponteggi. Proteggiamo le superfici da infiltrazioni e agenti atmosferici, migliorando al tempo stesso l’isolamento termico e l’efficienza energetica degli edifici. Lavoriamo in sicurezza, con rapidità e precisione, anche nei punti più difficili da raggiungere.",
         items=["servizi-impermeabilizzazione-tetti-cornicioni-e-terrazzi", "servizi-isolamento-termico", "servizi-isolamento-e-rifacimento-tetti"]),
    dict(slug="servizi-edilizia-su-fune-sicurezza-in-quota", title="Sicurezza in quota", img="linee-vita.jpg",
         desc="Sicurezza in quota con edilizia su fune: installazione e revisione linee vita, messa in sicurezza rapida senza ponteggi, conforme UNI.",
         intro="Operiamo con tecniche di edilizia su fune per installare e revisionare linee vita, mettendo in sicurezza edifici e coperture senza l’utilizzo di ponteggi. Lavoriamo in altezza con la massima attenzione alle normative e alle esigenze specifiche di ogni contesto, assicurando interventi rapidi, precisi e a basso impatto.",
         items=["servizi-installazione-e-revisione-linee-vita", "servizi-messa-in-sicurezza"]),
    dict(slug="servizi-edilizia-su-fune-riqualificazione", title="Riqualificazione", img="riqualificazione.jpg",
         desc="Riqualificazione con edilizia su fune: riparazione infiltrazioni, rifacimento facciate e lattoneria rapida, non invasiva, che riduce tempi, costi e disagi.",
         intro="Attraverso l’edilizia su fune realizziamo interventi di riqualificazione efficienti e non invasivi. Ripariamo infiltrazioni, rinnoviamo facciate e curiamo ogni dettaglio di lattoneria edile, lavorando in sicurezza anche nei punti più complessi. Riduciamo tempi, costi e disagi, valorizzando ogni edificio con soluzioni su misura.",
         items=["servizi-ricerca-e-riparazione-infiltrazioni", "servizi-rifacimento-facciate", "servizi-lattoneria-edile"]),
]

SERVICES = {
    "servizi-allontanamento-volatili": dict(title="Allontanamento Volatili", img="allontanamento-volatili.jpg",
        desc="Allontanamento Volatili con reti UV e dissuasori acustici: materiali ecologici, estetica discreta, monitoraggio fotografico e protezione duratura.",
        lead="Proteggi il tuo edificio dai volatili con La Mole Edilizia Su Fune. Offriamo soluzioni intelligenti e discrete per allontanare piccioni e altri volatili, prevenendo danni e garantendo l’igiene del tuo immobile.",
        body="Proteggiamo edifici storici, complessi industriali e spazi urbani da piccioni, storni e altri volatili con sistemi dissuasivi intelligenti ed esteticamente discreti. Grazie a una combinazione di tecnologie passive e attive preveniamo la proliferazione di agenti patogeni e il degrado estetico, nel pieno rispetto della fauna e delle normative sulla tutela ambientale.",
        feats=[("Soluzioni ibride", "Integriamo reti in polietilene UV-resistenti con dissuasori elettroacustici a frequenza variabile e adattabili a ogni contesto architettonico. Offriamo soluzioni personalizzate per ogni tipo di edificio e di problema."),
               ("Materiali biocompatibili", "Utilizziamo componenti atossici (acciaio inox satinato, filamenti in PET riciclato) che non danneggiano gli animali e rispettano la fauna locale."),
               ("Analisi post-installazione", "Monitoriamo l’efficacia con report fotografici e termografici, garantendo interventi correttivi immediati se necessari e risultati duraturi e misurabili.")]),
    "servizi-lavaggio-vetri": dict(title="Lavaggio Vetri", img="lavaggio-vetri.jpg",
        desc="Lavaggio Vetri professionale per vetrate alte e facciate: sistemi ecologici a secco/umido, zero aloni, sicurezza su fune, sanificazione certificata.",
        lead="La luce che valorizza i tuoi spazi. Il nostro servizio di lavaggio vetri garantisce cristallinità e igiene impeccabili per vetrate di ogni dimensione, anche in contesti architettonici complessi o in altezza.",
        body="Grazie a sistemi di pulizia dinamici e sostenibili, eliminiamo residui organici, calcare e smog senza danneggiare superfici o interrompere le attività sottostanti, assicurando un risultato visibile e duraturo: vetrate senza aloni o macchie, che lasciano entrare la luce naturale e migliorano l’aspetto del tuo edificio.",
        feats=[("Tecnologia a secco e a umido", "Alterniamo metodi ecologici a basso consumo idrico con detergenti biodegradabili, adattandoci alle esigenze del vetro (stratificato, temperato, antiriflesso)."),
               ("Sicurezza attiva", "Operiamo anche con piattaforme aeree, dispositivi anticaduta e in completa sospensione, evitando rischi per personale e terzi, con attrezzature all’avanguardia e personale altamente qualificato."),
               ("Garanzia di brillantezza", "Offriamo un controllo qualità post-intervento con certificazione di avvenuta sanificazione.")]),
    "servizi-pulizia-canali-gronda-e-tetti": dict(title="Pulizia Canali Gronda e Tetti", img="pulizia-tetti.jpg",
        desc="Pulizia Canali Gronda e Tetti: rimozione detriti, igienizzazione UV-C, coating anti-sporco, report termografico e riciclo rifiuti al 98%.",
        lead="Mantieni il tuo edificio sano e protetto. Offriamo un servizio completo di pulizia e manutenzione di grondaie e tetti, per prevenire allagamenti, infiltrazioni e danni strutturali.",
        body="Con tecnologie non invasive e mappatura digitale rimuoviamo detriti, sedimenti e biofilm da grondaie, pluviali e tetti, anche in aree complesse o sensibili, garantendo un flusso idrico ottimale.",
        feats=[("Tecnologia robotica e analisi avanzata", "Utilizziamo robot telecomandati con testine rotanti a pressione regolabile e telecamere endoscopiche. Al termine verifichiamo il sistema di deflusso con termocamere a infrarossi per individuare eventuali criticità residue."),
               ("Eco-sostenibilità e gestione dei rifiuti", "Ricicliamo il 98% dei rifiuti raccolti tramite CSR Plastic Credit, il certificato digitale che dimostra la rimozione dei rifiuti plastici dall’ambiente."),
               ("Igienizzazione e protezione avanzata", "Schiume biodegradabili per sgrassare le superfici e raggi UV-C per decontaminare senza biocidi inquinanti. Applichiamo coating idrorepellenti nanostrutturati che riducono l’adesione di nuovi contaminanti fino al 70% per 5 anni."),
               ("Certificazione e consulenza tecnica", "Forniamo un rapporto tecnico di portata idrica pre/post intervento e consigli personalizzati per la durata e l’efficienza del sistema di smaltimento delle acque piovane.")]),
    "servizi-sicurezza-e-check-up-tetti": dict(title="Sicurezza e Check-up Tetti", img="check-up-tetti.jpg",
        desc="Check-up tetti e sicurezza con droni, accesso su fune e dossier manutenzione: rileviamo criticità senza ponteggi e proteggiamo coperture civili e industriali.",
        lead="Proteggi il cuore del tuo edificio: il tetto. Offriamo un servizio integrato di sicurezza e check-up che garantisce stabilità e integrità a ogni tipo di copertura, dalle abitazioni private ai complessi industriali.",
        body="Unendo messa in sicurezza e check-up avanzati assicuriamo una protezione completa, dalla valutazione preliminare alla manutenzione continua. Le nostre ispezioni non invasive si avvalgono di diagnostica ibrida per mappare lo stato del tetto e identificare le criticità prima che diventino emergenze.",
        feats=[("Progettazione e analisi su misura", "Ogni intervento è preceduto da una valutazione strutturale personalizzata e da rilievi accurati. Utilizziamo droni per identificare microfessure e altri problemi nascosti."),
               ("Tecniche senza ponteggi", "Sistemi su fune e piattaforme sospese riducono tempi e impatti sull’edificio: meno disagi per te, più efficienza nel lavoro."),
               ("Materiali e certificazione", "Impieghiamo leghe certificate e componenti antisismici, rilasciando un dossier completo con classe di rischio e piano di manutenzione personalizzato.")]),
    "servizi-impermeabilizzazione-tetti-cornicioni-e-terrazzi": dict(title="Impermeabilizzazione Tetti, Cornicioni e Terrazzi", img="impermeabilizzazione-tetti.jpg",
        desc="Impermeabilizzazione tetti, cornicioni e terrazzi con membrane nanotecnologiche autorigeneranti: stop infiltrazioni, resiste da -30° a +120°, garanzia 20 anni.",
        lead="Proteggi il tuo investimento. Realizziamo impermeabilizzazioni su misura per tetti, cornicioni e terrazzi, utilizzando nanotecnologie e materiali innovativi per una protezione duratura contro le infiltrazioni.",
        body="Proteggiamo le superfici orizzontali e verticali da infiltrazioni, umidità e degrado ambientale con sistemi di barriera attiva progettati su misura. Combiniamo nanotecnologie autorigeneranti, membrane polimeriche ad altissima adesività e trattamenti fotocatalitici per garantire tenuta idraulica, resistenza agli sbalzi termici (-30°C/+120°C) e integrazione estetica con qualsiasi contesto architettonico.",
        feats=[("Strati compositi intelligenti", "Utilizziamo film ibridi in grafene modificato e silossani, che reagiscono alle microlesioni ripristinando autonomamente l’impermeabilità."),
               ("Certificazione climatica", "Rilasciamo garanzie fino a 20 anni con mappatura digitale delle prestazioni, allineate agli standard ISO 14001 per l’edilizia sostenibile.")]),
    "servizi-isolamento-termico": dict(title="Isolamento Termico", img="isolamento-termico.jpg",
        desc="Isolamento Termico su misura con pannelli ad alta densità, schiume espandibili e posa a secco: −40 % dispersioni, comfort costante e certificazione UNI 11716.",
        lead="Crea il tuo comfort ideale. Progettiamo sistemi avanzati di isolamento termico su misura, per ottimizzare l’efficienza energetica del tuo edificio e migliorare il benessere abitativo.",
        body="Per edifici residenziali, industriali e beni culturali usiamo materiali innovativi a basso impatto ambientale e tecniche di posa non invasive: riduciamo le dispersioni termiche fino al 40%, garantendo comfort abitativo e bollette più leggere.",
        feats=[("Soluzioni integrate", "Combiniamo strati termoriflettenti, pannelli compositi ad alta densità e schiume poliuretaniche espandibili, selezionati in base alle caratteristiche strutturali dell’edificio."),
               ("Tecnologia a secco", "Evitiamo demolizioni grazie a sistemi di ancoraggio meccanico e lavori in completa sospensione, ideali per facciate delicate o vincolate."),
               ("Certificazione UNI 11716:2018", "Rilasciamo attestazioni di corretta posa dei sistemi di isolamento a cappotto secondo lo standard ETICS, in conformità alla norma UNI 11716:2018."),
               ("Monitoraggio post-intervento", "Su richiesta eseguiamo verifiche con termocamere a infrarossi per monitorare le prestazioni energetiche e identificare eventuali ponti termici residui.")]),
    "servizi-isolamento-e-rifacimento-tetti": dict(title="Isolamento e Rifacimento Tetti", img="isolamento-e-rifacimento-tetti.jpg",
        desc="Isolamento termico-acustico e rifacimento tetti: comfort, efficienza energetica e protezione garantiti, pratica incentivi e garanzia completa.",
        lead="Rinnova il tuo tetto: comfort, efficienza e protezione in un unico intervento. Trasformiamo la tua copertura in un elemento di pregio, capace di migliorare il comfort, ridurre i costi energetici e proteggere l’edificio dagli agenti atmosferici.",
        body="Siamo specializzati nell’isolamento termico e acustico e nel rifacimento completo di tetti residenziali, commerciali e industriali, dalle tradizionali tegole ai moderni sistemi a pannelli. Il nostro approccio comprende diagnosi preliminare, progettazione su misura, selezione dei materiali, esecuzione dei lavori e collaudo finale.",
        feats=[("Materiali isolanti di nuova generazione", "Lane minerali ecologiche, pannelli in fibra di legno, schiume poliuretaniche a spruzzo e membrane traspiranti. Con l’insufflaggio nelle intercapedini esistenti riduciamo tempi e disagi."),
               ("Rifacimento e personalizzazione", "Rimozione della vecchia copertura, riparazione delle strutture portanti, nuovi sistemi di impermeabilizzazione e ventilazione, manto in tegole, coppi, pannelli metallici o fotovoltaico integrato."),
               ("Incentivi fiscali e garanzia", "Ti supportiamo nella richiesta degli incentivi per la riqualificazione energetica e offriamo una garanzia completa su materiali e manodopera.")]),
    "servizi-installazione-e-revisione-linee-vita": dict(title="Installazione e Revisione Linee Vita", img="linee-vita.jpg",
        desc="Installazione e Revisione Linee Vita certificate UNI 11900: ancoraggi modulari, cavi inox, manutenzione predittiva e report digitali per massima sicurezza in quota.",
        lead="Lavora in sicurezza. Offriamo un servizio completo di installazione e revisione linee vita, per garantire la massima protezione durante i lavori in quota e la manutenzione del tuo edificio.",
        body="Installiamo e revisioniamo linee vita per lavori in quota, manutenzioni e accessi tecnici, con soluzioni personalizzate per coperture, facciate e strutture industriali, nel rispetto della norma UNI 11900.",
        feats=[("Certificazioni internazionali", "Ogni linea vita è testata in laboratori accreditati e dotata di documentazione CE, con schede aggiornate alle direttive europee."),
               ("Tecnologia modulare", "Ancoraggi fissi, rotaie guidate e cavi inox autobloccanti, compatibili con dispositivi di terzi."),
               ("Materiali resistenti", "Cavi in acciaio zincato-aramidico e giunti anticorrosione, progettati per resistere a carichi elevati."),
               ("Manutenzione predittiva", "Ispezioni periodiche con report digitali e sostituzione preventiva dei componenti usurati.")]),
    "servizi-messa-in-sicurezza": dict(title="Messa in sicurezza", img="messa-in-sicurezza.jpg",
        desc="Messa in sicurezza facciate con tecnica su fune: consolidamenti rapidi, reti in fibra e resine, documentazione e agibilità certificate.",
        lead="Proteggi l’involucro del tuo edificio. Siamo specialisti nella manutenzione delle facciate, un servizio completo per preservare la sicurezza del tuo immobile.",
        body="Interveniamo su facciate storiche e moderne a rischio di degrado: con la tecnica su fune trattiamo lesioni, distacchi o cedimenti, garantendo l’integrità delle pareti e delle strutture di sostegno anche dove l’accesso è difficile. Mettiamo in sicurezza subito l’edificio, così il rifacimento della facciata si può programmare con calma.",
        feats=[("Approccio integrato", "Combiniamo metodi di consolidamento tradizionali con tecniche innovative, come reti in fibra di vetro o iniezioni di resine stabilizzanti."),
               ("Certificazione di conformità", "Forniamo documentazione tecnica conforme alle normative nazionali e internazionali e rilascio di agibilità in condizione di sicurezza.")]),
    "servizi-ricerca-e-riparazione-infiltrazioni": dict(title="Ricerca e Riparazione Infiltrazioni", img="infiltrazioni-da-tetto.jpg",
        desc="Ricerca e Riparazione Infiltrazioni in tetti e muri con termocamere e idro-sonde non invasive. Sigilli nanoresina: stop muffe, danni e sprechi.",
        lead="Dì addio alle infiltrazioni. Con tecnologie avanzate e metodi non invasivi individuiamo e risolviamo le perdite idriche nascoste, proteggendo il tuo edificio da danni e sprechi.",
        body="Siamo i detective dell’acqua: scoviamo perdite nascoste in coperture, murature e strutture interrate. Con mappatura termoigrometrica e idro-sonde ad alta frequenza individuiamo anche le micro-fessure invisibili a occhio nudo, con riparazioni definitive che prevengono muffe, danni strutturali e sprechi energetici, senza demolire nulla.",
        feats=[("Diagnostica predittiva", "Metodologie di ultima generazione per mappare e individuare le infiltrazioni con precisione, riducendo tempi e costi e prevenendo danni futuri."),
               ("Riparazioni nanostrutturate", "Iniettiamo sigillanti espandibili a base di silicio attivo o resine epossidiche modificate, che aderiscono senza alterare permeabilità o aspetto delle superfici."),
               ("Verifica non distruttiva", "A fine intervento eseguiamo controlli non invasivi per certificare l’assenza di accumuli d’acqua, umidità residua o punti critici."),
               ("Sostenibilità integrata", "Recuperiamo e ricicliamo i liquidi estratti durante gli interventi, riducendo al minimo l’impatto ambientale.")]),
    "servizi-rifacimento-facciate": dict(title="Rifacimento Facciate", img="rifacimento-facciate.jpg",
        desc="Restauro completo di facciate residenziali, commerciali e storiche: diagnosi 3D, materiali innovativi, cappotto termico, permessi gestiti e garanzia totale.",
        lead="Dona nuova vita al volto del tuo edificio. Trasformiamo facciate obsolete e danneggiate combinando design, materiali di pregio e tecniche di riqualificazione all’avanguardia, per valorizzare l’estetica, migliorare l’efficienza energetica e proteggere il tuo immobile nel tempo.",
        body="Rifacciamo facciate di edifici residenziali, commerciali e storici, dal restauro conservativo di intonaci antichi al rivestimento con materiali innovativi. Il nostro approccio comprende diagnosi preliminare, progettazione su misura, selezione dei materiali, esecuzione dei lavori e collaudo finale.",
        feats=[("Diagnosi e progettazione personalizzata", "Analizziamo lo stato della facciata con termocamere, droni e rilievo 3D, e sviluppiamo progetti che tengono conto di estetica, budget, contesto architettonico e normative."),
               ("Materiali e tecniche innovative", "Intonaci termoisolanti, rivestimenti fotocatalitici autopulenti, facciate ventilate e vetri a controllo solare; piattaforme aeree e sistemi in fune riducono tempi e disagi."),
               ("Estetica e protezione", "Rimuoviamo gli elementi degradati, risaniamo le criticità strutturali e applichiamo finiture resistenti e trattamenti contro muffe e umidità. Quando richiesto integriamo il cappotto termico."),
               ("Gestione completa del progetto", "Dalla richiesta dei permessi edilizi alla direzione lavori, coordiniamo tutte le figure coinvolte rispettando tempi e costi, con garanzia completa su materiali e manodopera.")]),
    "servizi-lattoneria-edile": dict(title="Lattoneria edile", img="lattoneria-edile.jpg",
        desc="Realizziamo grondaie, pluviali, coperture e rivestimenti metallici, sistemi parafulmine: lattoneria artigianale su misura, protezione e deflusso acque garantiti.",
        lead="La lattoneria edile abbraccia una vasta gamma di interventi tecnici e artigianali, fondamentali per la protezione e il corretto drenaggio degli edifici, sempre finalizzati a garantire efficienza, durabilità e sicurezza.",
        body="Affidarsi a La Mole Edilizia su Fune significa contare su un team esperto in opere di lattoneria precise, funzionali e durature, pensate per proteggere e valorizzare ogni tipo di edificio.",
        feats=[("Esperienza su ogni tipo di copertura", "Dalle coperture a falde ai tetti piani delle architetture moderne, adattiamo ogni intervento alle esigenze dell’edificio, assicurando il corretto deflusso delle acque piovane."),
               ("Sistema di raccolta acque", "Progettiamo e installiamo grondaie e pluviali con cura artigianale, evitando ristagni e infiltrazioni."),
               ("Coperture e rivestimenti metallici", "Coperture e facciate in metallo con giunzioni a graffatura semplice o doppia: impermeabili, resistenti e belle da vedere."),
               ("Impianti parafulmine", "Installiamo sistemi parafulmine certificati per proteggere persone ed edificio da eventi atmosferici estremi."),
               ("Un solo partner", "Dalla progettazione alla realizzazione, un servizio chiavi in mano che unisce artigianalità, tecnologia e attenzione al dettaglio.")]),
}
PARENT = {s: c for c in CATS for s in c["items"]}

NAV = [("index.html", "Home"), ("azienda.html", "Azienda"), ("servizi-edilizia-su-fune.html", "Servizi"),
       ("vantaggi.html", "Vantaggi"), ("novita.html", "Novità"), ("contatti.html", "Contatti")]

ABOUT = """<p>Siamo nati da una solida esperienza nel campo dell’edilizia e da una visione chiara: offrire soluzioni moderne, sicure e sostenibili sfruttando le tecniche dell’edilizia su fune.</p>
<p>Nel tempo abbiamo costruito un team altamente specializzato, formato da professionisti che condividono la nostra filosofia: lavorare con efficienza, sicurezza e rispetto per l’ambiente e per il contesto urbano.</p>
<p>Il nostro obiettivo è innovare il settore delle costruzioni con un approccio flessibile e veloce per soddisfare le esigenze di condomini, aziende e privati.</p>"""

MISSION = """<div class="grid two">
<div class="card"><p class="eyebrow">Missione</p><h3>La nostra missione</h3><p>Diventare un punto di riferimento nel settore dell’edilizia su fune, fornendo un servizio di alta qualità, precisione e con alti standard di sicurezza. Puntiamo ad ampliare costantemente la nostra offerta con nuove metodologie, attrezzature e macchinari, restando al passo con l’evoluzione del settore e delle esigenze dei clienti.</p></div>
<div class="card"><p class="eyebrow">Visione</p><h3>La nostra visione</h3><p>Crediamo in un’edilizia moderna, intelligente e responsabile, capace di integrare nuove tecnologie, soluzioni digitali e materiali avanzati, mantenendo al centro sicurezza, efficienza e rispetto per l’ambiente. Vogliamo anticipare i bisogni del futuro e migliorare concretamente la qualità della vita urbana.</p></div>
</div>"""

INTRO_AZIENDA = "Siamo un’eccellenza fondata a Torino e operativa in tutta Italia, specializzati nell’edilizia su corda. Utilizziamo tecniche derivate dall’alpinismo e un team certificato dalla Scuola di Alpinismo Valli di Lanzo per intervenire in contesti complessi senza ricorrere a ponteggi."

VANTAGGI_SHORT = """<p>Il vantaggio risiede nella capacità di intervenire in modo rapido ed efficace senza l’installazione di ponteggi, con un notevole risparmio economico e logistico. Grazie all’edilizia su fune riduciamo significativamente i tempi di esecuzione, limitando i disagi per condomini e passanti.</p>
<p>Ogni operazione viene svolta nel pieno rispetto dei protocolli di sicurezza più avanzati, con attrezzature all’avanguardia e un approccio che preferisce soluzioni sostenibili, con un impatto minimo sul contesto urbano.</p>"""

CERTS = [("bureau-veritas.jpg", "Bureau Veritas", "Certificazioni di qualità e sicurezza nei processi lavorativi."),
         ("csr-plastic-credit.jpg", "CSR Plastic Credit", "Riciclo certificato dei rifiuti plastici."),
         ("istituto-giordano.jpg", "Istituto Giordano", "Validazione delle tecniche e dei sistemi di ancoraggio.")]

REVIEWS = [("Mauro G.", "27/06/2022", "Educati, professionali, veloci."),
           ("Global S.", "07/03/2021", "Una collaborazione eccellente. Sempre disponibili a cercare una soluzione a ogni problema, veloci nell’eseguire i lavori, qualità 100%. Soprattutto la serietà, che oggigiorno è difficile trovare."),
           ("Costantin I.", "13/07/2020", "Ottima esperienza di personale giovane e competente nel settore. Molto attrezzati e attenti per la nostra sicurezza e la loro.")]

ARTICLE = dict(slug="dallalpinismo-alle-vette-urbane-la-storia-delledilizia-su-fune",
    title="Dall’alpinismo alle vette urbane, la storia dell’edilizia su fune", img="storia-edilizia-su-fune.jpg",
    desc="Scopri come l’edilizia su fune è passata dall’alpinismo ai cantieri urbani. Efficienza e sicurezza senza ponteggi.",
    body="""<p>Nel mondo delle costruzioni, le innovazioni più importanti spesso nascono da intuizioni semplici. L’edilizia su fune è un esempio chiaro: una tecnica che ha trasformato il modo di lavorare in quota, portando efficienza, sicurezza e sostenibilità dove prima sembravano impossibili. Ma da dove arriva questa metodologia e perché si è diffusa così tanto?</p>
<p>Negli anni ’50 alcuni pionieri iniziarono a utilizzare le stesse corde e attrezzature dell’alpinismo e della speleologia per eseguire lavori in quota. L’idea era tanto semplice quanto geniale: se quelle tecniche permettevano di affrontare pareti rocciose e grotte profonde, potevano essere adattate anche alle facciate degli edifici e alle coperture più difficili da raggiungere.</p>
<p>Negli anni ’80 l’edilizia su fune si diffuse rapidamente. Negli Stati Uniti fu adottata per la manutenzione dei grattacieli, mentre in Francia fu impiegata per restaurare simboli come la Tour Eiffel. In Inghilterra nacque IRATA, l’associazione internazionale che ancora oggi definisce gli standard di sicurezza e formazione a livello mondiale.</p>
<p>In Italia la corda non era una novità. Già agli inizi del ’900 i sanpietrini usavano funi di canapa per lavorare sulla cupola di San Pietro a Roma. Ma è negli anni ’90 che la tecnica si affermò davvero, soprattutto a Genova, dove i vicoli stretti del centro storico rendevano impossibile montare ponteggi e le corde erano la soluzione più pratica. Anche l’esperienza delle guide alpine e dei vigili del fuoco con le tecniche SAF (Speleo-Alpino-Fluviali) contribuì a far crescere competenze e procedure di sicurezza.</p>
<p>L’edilizia su fune è nata per ridurre tempi, costi e disagi. Dove un ponteggio era costoso, lento o ingombrante, le funi rappresentavano una strada più rapida e meno invasiva. Da esigenza si è presto trasformata in filosofia: un approccio che unisce efficienza, sicurezza certificata e rispetto per l’ambiente.</p>
<p>Oggi il lavoro su fune è una realtà consolidata e regolamentata. In Italia è inquadrato dal D.Lgs. 81/08, mentre a livello internazionale esistono protocolli severi che ne certificano la sicurezza. Ma non si tratta solo di una tecnica di lavoro: è un modo di pensare l’edilizia, con interventi rapidi, discreti, sostenibili e sempre più tecnologici.</p>
<h2>Noi di La Mole Edilizia su Fune</h2>
<p>Siamo nati a Torino, una città che ha sempre saputo unire tradizione e innovazione. Qui abbiamo costruito le nostre basi e da qui operiamo soprattutto in Piemonte e nel Nord Italia, portando la tecnica dell’edilizia su fune nei contesti più complessi, dai condomini cittadini agli edifici storici.</p>
<p>Offriamo servizi che vanno dalla pulizia e manutenzione di facciate, tetti e vetri all’impermeabilizzazione di coperture e terrazzi, fino alla messa in sicurezza di edifici storici o moderni e alla riqualificazione completa di interi immobili. Ogni intervento lo affrontiamo con la stessa filosofia: rapidità, precisione, sicurezza e rispetto per l’ambiente.</p>
<p>Crediamo che l’edilizia su fune non sia solo un’alternativa ai ponteggi, ma un modo per migliorare concretamente la vita urbana. Riduciamo costi, tempi e disagi, senza rinunciare alla qualità e alla sicurezza.</p>
<h2>Conclusione</h2>
<p>Dalle corde degli alpinisti alle città moderne, l’edilizia su fune è diventata la nostra passione e il nostro mestiere. Ogni progetto è per noi una sfida che affrontiamo con competenza e rispetto, perché insieme costruiamo città più sicure e vivibili.</p>""")


# --- Pezzi comuni -----------------------------------------------------------------
def head(title, desc, slug, img):
    url = f"{SITE}/" + ("" if slug == "index" else f"{slug}.html")
    t = escape(title if slug == "index" else f"{title} | La Mole Edilizia su Fune")
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{SITE}/assets/img/{img}">
<meta property="og:url" content="{url}">
<meta name="facebook-domain-verification" content="os95ze0x3jrlgvq7fszmf0luu75hd3">
<link rel="icon" href="assets/img/favicon.jpg">
<link rel="preload" href="assets/fonts/montserrat-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-29DS1SS66B"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-29DS1SS66B');
</script>
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '3593393790961940');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=3593393790961940&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
"""


def header(active):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{n}</a></li>' for h, n in NAV)
    return f"""<div class="topbar">
<span>⚡ Interventi in quota senza ponteggi</span>
<span class="topbar-mid"><b>Torino e tutta Italia</b> Sopralluoghi per condomini, aziende e privati</span>
<a href="tel:{TEL_LINK}">☎ {TEL}</a>
</div>
<header class="site-header pill">
<div class="bar">
<a class="logo" href="index.html" aria-label="La Mole Edilizia su Fune, home"><span class="logo-mark" role="img" aria-label="La Mole Edilizia su Fune"></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav id="nav" aria-label="Principale"><ul>{links}</ul></nav>
<a class="btn btn-pill" href="contatti.html">Richiedi un preventivo ↗</a>
</div>
</header>
<main id="main">
"""


def footer():
    cats = "".join(f'<li><a href="{c["slug"]}.html">{c["title"]}</a></li>' for c in CATS)
    soc = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{n}</a></li>' for n, u in SOCIAL)
    return f"""</main>
<footer class="site-footer">
<div class="wrap grid four">
<div><img src="assets/img/logo-bianco.png" alt="" width="72" height="70"><p>Edilizia su fune a Torino e in tutta Italia. Interventi in quota senza ponteggi.</p></div>
<div><h2>Servizi</h2><ul>{cats}</ul></div>
<div><h2>Contatti</h2><ul><li><a href="tel:{TEL_LINK}">{TEL}</a></li><li><a href="{WA}">{CELL}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{ADDR}</li></ul></div>
<div><h2>Seguici</h2><ul>{soc}</ul></div>
</div>
<div class="wrap legal">
<p>LA MOLE EDILIZIA SU FUNE SRL · P.IVA 12716000018 · Sede operativa: {ADDR}</p>
<p>Tutte le immagini dei servizi sono inserite a scopo illustrativo. <a href="privacy-policy.html">Privacy e cookie</a></p>
</div>
</footer>
<a class="wa-float" href="{WA}" rel="noopener" target="_blank" aria-label="Scrivici su WhatsApp">WhatsApp</a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def hero(title, text, img, eyebrow=""):
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    return f"""<section class="hero" style="background-image:url('assets/img/{img}')">
<div class="wrap"><div class="hero-text">{eb}<h1>{title}</h1>{f"<p>{text}</p>" if text else ""}</div></div>
</section>
"""


def cta():
    return f"""<section class="cta">
<div class="wrap cta-in">
<div><h2>Hai bisogno di interventi in quota rapidi, sicuri e senza ponteggi?</h2>
<p>Con la nostra esperienza e tecniche innovative trasformiamo ogni progetto in un successo concreto, dalla manutenzione al restauro. Mettiamo la nostra competenza al servizio delle tue esigenze.</p></div>
<div class="cta-actions"><a class="btn" href="contatti.html">Contattaci ora</a><a class="btn btn-ghost" href="tel:{TEL_LINK}">Chiama {TEL}</a></div>
</div>
</section>
"""


def tiles(items):
    """items: lista di (href, titolo, immagine)."""
    return '<div class="grid tiles">' + "".join(
        f'<a class="tile" href="{h}"><img src="assets/img/{i}" alt="" loading="lazy" width="600" height="450"><span>{t}</span></a>'
        for h, t, i in items) + "</div>"


def cat_tiles():
    return tiles([(f'{c["slug"]}.html', c["title"], c["img"]) for c in CATS])


def crumbs(*parts):
    li = "".join(f'<li><a href="{h}">{n}</a></li>' if h else f'<li aria-current="page">{n}</li>' for h, n in parts)
    return f'<nav class="crumbs wrap" aria-label="Percorso"><ol><li><a href="index.html">Home</a></li>{li}</ol></nav>'


def certs():
    c = "".join(f'<div class="cert"><img src="assets/img/{i}" alt="Logo {n}" loading="lazy" width="160" height="160"><h3>{n}</h3><p>{d}</p></div>' for i, n, d in CERTS)
    return f"""<section class="section alt"><div class="wrap">
<p class="eyebrow">Certificazioni</p><h2>Le nostre certificazioni</h2>
<p class="lead">Collaboriamo con enti e istituzioni di riferimento per garantire il massimo livello qualitativo e normativo nei nostri interventi.</p>
<div class="grid three">{c}</div></div></section>
"""


def page(slug, title, desc, img, body, active):
    (OUT / f"{slug}.html").write_text(head(title, desc, slug, img) + header(active) + body + footer(), encoding="utf-8")


# --- Pagine -----------------------------------------------------------------------
def build():
    page("index", "La Mole Edilizia su Fune | Edilizia su Fune a Torino",
         "La Mole Edilizia su fune: interventi rapidi senza ponteggi, sicurezza certificata, risparmio ed efficienza sostenibile per condomini, aziende e privati.",
         "slide-1.jpg",
         f"""<section class="hero-home" style="background-image:url('assets/img/slide-1.jpg')">
<div class="hero-home-in">
<p class="badge">★ Valutazione eccellente su Google</p>
<h1>La tua difesa contro<br><em>i rischi nascosti.</em></h1>
<div class="hero-actions"><a class="btn btn-pill" href="contatti.html">Richiedi un preventivo ↗</a><p>Edilizia su fune a Torino e in tutta Italia: interventi rapidi e sicuri, senza ponteggi.</p></div>
<ul class="hero-feats">
<li><span>↕</span>Zero ponteggi<br>interventi diretti dalla fune</li>
<li><span>%</span>Fino al 70%<br>di risparmio sui costi</li>
<li><span>✓</span>Personale certificato<br>tecniche dall’alpinismo</li>
</ul>
</div>
</section>
<section class="section"><div class="wrap split">
<div><p class="eyebrow">Chi siamo</p><h2>Soluzioni moderne, sicure e sostenibili</h2>{ABOUT}<a class="link" href="azienda.html">Scopri l’azienda</a></div>
<img src="assets/img/lazienda.jpg" alt="Tecnico de La Mole Edilizia su Fune al lavoro in quota" loading="lazy" width="1024" height="1024">
</div></section>
<section class="section alt"><div class="wrap">
<p class="eyebrow">Servizi</p><h2>I nostri servizi</h2>
<p class="lead">Un’ampia gamma di servizi pensati per garantire soluzioni efficaci e sicure in ogni contesto.</p>
{cat_tiles()}</div></section>
<section class="section"><div class="wrap">
<p class="eyebrow">Recensioni</p><h2>La soddisfazione dei nostri clienti parla per noi</h2>
<p class="lead">Valutazione <strong>eccellente</strong> in base a 14 recensioni su Google.</p>
<div class="grid three">{"".join(f'<figure class="review"><blockquote>“{t}”</blockquote><figcaption>{n} · {d}</figcaption></figure>' for n, d, t in REVIEWS)}</div>
</div></section>
<section class="section alt"><div class="wrap split">
<img src="assets/img/vantaggi-3.jpg" alt="Intervento su fune senza ponteggi" loading="lazy" width="1024" height="1024">
<div><p class="eyebrow">Vantaggi</p><h2>Perché l’edilizia su fune conviene</h2>{VANTAGGI_SHORT}<a class="link" href="vantaggi.html">Tutti i vantaggi</a></div>
</div></section>
{cta()}""", "index.html")

    page("azienda", "Azienda",
         "Edilizia su fune certificata a Torino e in tutta Italia: interventi rapidi senza ponteggi, team di alpinisti, soluzioni sicure, sostenibili e veloci.",
         "slide-1.jpg",
         hero("Azienda", INTRO_AZIENDA, "slide-1.jpg", "Chi siamo") + crumbs((None, "Azienda")) +
         f"""<section class="section"><div class="wrap split">
<div><h2>Chi siamo</h2>{ABOUT}<p>Valorizziamo la nostra competenza tecnica, l’attenzione ai dettagli e la passione, garantendo rapidità, sicurezza e rispetto per l’ambiente.</p></div>
<img src="assets/img/lazienda.jpg" alt="Squadra de La Mole Edilizia su Fune" loading="lazy" width="1024" height="1024">
</div></section>
<section class="section alt"><div class="wrap">{MISSION}</div></section>
<section class="section"><div class="wrap"><h2>I nostri servizi</h2><p class="lead">Un’ampia gamma di servizi pensati per garantire soluzioni efficaci e sicure in ogni contesto.</p>{cat_tiles()}</div></section>
<section class="banner" style="background-image:url('assets/img/immagine-guida.jpg')"><div class="wrap"><h2>In alto per risolvere, vicini per proteggere.</h2>
<p>Affrontiamo ogni intervento con competenza e precisione, anche nei luoghi più difficili da raggiungere. Grazie all’edilizia su fune garantiamo soluzioni efficaci senza ponteggi, con interventi rapidi, sicuri e discreti. Perché la tranquillità di chi vive gli spazi è la nostra priorità.</p></div></section>
{certs()}
<section class="section"><div class="wrap split">
<img src="assets/img/vantaggi-3.jpg" alt="" loading="lazy" width="1024" height="1024">
<div><h2>Vantaggi</h2>{VANTAGGI_SHORT}<a class="link" href="vantaggi.html">Scopri di più</a></div>
</div></section>
{cta()}""", "azienda.html")

    page("servizi-edilizia-su-fune", "Servizi",
         "Edilizia su fune a Torino: pulizia, manutenzione, impermeabilizzazioni, sicurezza in quota e riqualificazioni senza ponteggi in tutta Italia.",
         "slide-1.jpg",
         hero("Servizi", INTRO_AZIENDA, "slide-1.jpg", "Cosa facciamo") + crumbs((None, "Servizi")) +
         "".join(f"""<section class="section{" alt" if n % 2 else ""}"><div class="wrap">
<h2><a href="{c["slug"]}.html">{c["title"]}</a></h2><p class="lead">{c["intro"]}</p>
{tiles([(f"{s}.html", SERVICES[s]["title"], SERVICES[s]["img"]) for s in c["items"]])}</div></section>""" for n, c in enumerate(CATS)) +
         cta(), "servizi-edilizia-su-fune.html")

    for c in CATS:
        page(c["slug"], c["title"], c["desc"], c["img"],
             hero(c["title"], c["intro"], c["img"], "Servizi") + crumbs(("servizi-edilizia-su-fune.html", "Servizi"), (None, c["title"])) +
             f'<section class="section"><div class="wrap">{tiles([(f"{s}.html", SERVICES[s]["title"], SERVICES[s]["img"]) for s in c["items"]])}</div></section>' +
             cta(), "servizi-edilizia-su-fune.html")

    for slug, s in SERVICES.items():
        c = PARENT[slug]
        feats = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in s["feats"])
        others = [(f"{o}.html", SERVICES[o]["title"], SERVICES[o]["img"]) for o in c["items"] if o != slug]
        page(slug, s["title"], s["desc"], s["img"],
             hero(s["title"], s["lead"], s["img"], c["title"]) +
             crumbs(("servizi-edilizia-su-fune.html", "Servizi"), (f'{c["slug"]}.html', c["title"]), (None, s["title"])) +
             f"""<section class="section"><div class="wrap split">
<div><h2>Il servizio</h2><p>{s["body"]}</p><a class="btn" href="contatti.html">Richiedi un sopralluogo</a></div>
<img src="assets/img/{s["img"]}" alt="{escape(s["title"])}: intervento de La Mole Edilizia su Fune" loading="lazy" width="800" height="600">
</div></section>
<section class="section alt"><div class="wrap"><h2>Perché sceglierci</h2>
<p class="lead">La nostra esperienza e professionalità ci permettono di offrire soluzioni su misura per ogni esigenza.</p>
<div class="grid two">{feats}</div></div></section>
<section class="section"><div class="wrap"><h2>Altri servizi di {c["title"]}</h2>{tiles(others)}</div></section>
{cta()}""", "servizi-edilizia-su-fune.html")

    rows = [("Costi", "Ridotti fino al 70%", "Elevati (ponteggi, gru, ecc.)"),
            ("Tempi", "Rapidi (1-2 giorni per allestimento)", "Lunghi (settimane per montaggio)"),
            ("Impatto visivo", "Minimo", "Elevato"), ("Disturbo", "Minimo per inquilini e passanti", "Significativo"),
            ("Flessibilità", "Elevata (adattabile a ogni struttura)", "Limitata"),
            ("Sicurezza", "Elevata con personale certificato", "Variabile")]
    why = [("Zero ponteggi", "Interventi rapidi senza installare costosi e ingombranti ponteggi."),
           ("Costi contenuti", "Risparmio fino al 70% rispetto alle tecniche tradizionali."),
           ("Interventi rapidi", "Tempi ridotti grazie alla mobilità e flessibilità delle tecniche su fune."),
           ("Personale certificato", "Tecnici specializzati con certificazioni internazionali per lavori in quota."),
           ("Massima sicurezza", "Protocolli avanzati e attrezzature certificate per ogni intervento."),
           ("Approccio ecologico", "Materiali sostenibili e riduzione dell’impatto ambientale.")]
    page("vantaggi", "Vantaggi",
         "Ecco perché l’edilizia su fune conviene: zero ponteggi, costi tagliati fino al 70%, tempi rapidi, meno permessi e impatto minimo, con personale certificato.",
         "vantaggi-2-1.jpg",
         hero("Vantaggi", "L’edilizia su fune consente di effettuare interventi in quota senza ponteggi tradizionali. Ispirata alle tecniche di alpinismo, offre numerosi vantaggi rispetto ai metodi tradizionali.", "vantaggi-2-1.jpg", "Perché la fune") +
         crumbs((None, "Vantaggi")) +
         f"""<section class="section"><div class="wrap split">
<div><h2>Efficienza economica</h2><p>Uno dei principali vantaggi dell’edilizia su fune è il risparmio economico: l’assenza di ponteggi e strutture di supporto riduce significativamente i costi dell’intervento.</p>
<ul class="checks"><li><strong>Nessun costo per ponteggi</strong> Risparmio medio del 40%</li><li><strong>Tempi di intervento ridotti</strong> Meno giorni di lavoro, meno costi</li><li><strong>Nessun permesso speciale</strong> per l’occupazione del suolo pubblico</li><li><strong>Costi assicurativi ridotti</strong> per la minor durata dei lavori</li></ul></div>
<img src="assets/img/vantaggi-3.jpg" alt="" loading="lazy" width="1024" height="1024">
</div></section>
<section class="section alt"><div class="wrap"><h2>Perché sceglierci</h2>
<p class="lead">Ecco perché sempre più clienti si affidano a La Mole Edilizia su Fune per i loro interventi.</p>
<div class="grid three">{"".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in why)}</div></div></section>
<section class="section"><div class="wrap"><h2>Confronto con i metodi tradizionali</h2>
<p class="lead">L’edilizia su fune garantisce efficienza, sicurezza e minimo impatto sull’ambiente circostante grazie a tecniche avanzate e personale altamente specializzato.</p>
<div class="table-wrap"><table><thead><tr><th scope="col">Aspetto</th><th scope="col">Edilizia su fune</th><th scope="col">Metodi tradizionali</th></tr></thead>
<tbody>{"".join(f"<tr><th scope='row'>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows)}</tbody></table></div></div></section>
{cta()}""", "vantaggi.html")

    page("novita", "Novità", "Notizie e approfondimenti sull’edilizia su fune da La Mole Edilizia su Fune, Torino.", "slide-1.jpg",
         hero("Novità", "Approfondimenti e storie dal mondo dell’edilizia su fune.", "slide-1.jpg", "Blog") + crumbs((None, "Novità")) +
         f"""<section class="section"><div class="wrap"><a class="post" href="{ARTICLE["slug"]}.html">
<img src="assets/img/{ARTICLE["img"]}" alt="" loading="lazy" width="800" height="444"><div><h2>{ARTICLE["title"]}</h2><p>{ARTICLE["desc"]}</p><span class="link">Leggi l’articolo</span></div></a></div></section>
{cta()}""", "novita.html")

    page(ARTICLE["slug"], ARTICLE["title"], ARTICLE["desc"], ARTICLE["img"],
         hero(ARTICLE["title"], "", ARTICLE["img"], "Novità") + crumbs(("novita.html", "Novità"), (None, "La storia dell’edilizia su fune")) +
         f'<article class="section"><div class="wrap prose">{ARTICLE["body"]}</div></article>{cta()}', "novita.html")

    opts = "".join(f"<option>{s['title']}</option>" for s in SERVICES.values())
    page("contatti", "Contatti", f"Chiama o scrivi La Mole Edilizia su Fune: {TEL} • {EMAIL} • {ADDR}.", "contatti.jpg",
         hero("Contatti", "Raccontaci il tuo intervento: ti rispondiamo con un sopralluogo e un preventivo.", "contatti.jpg", "Parliamone") + crumbs((None, "Contatti")) +
         f"""<section class="section"><div class="wrap split top">
<form class="form" id="contact-form" data-email="{EMAIL}">
<h2>Richiedi più informazioni</h2>
<div class="grid two"><label>Nome *<input name="nome" required autocomplete="given-name"></label><label>Cognome<input name="cognome" autocomplete="family-name"></label></div>
<div class="grid two"><label>Cellulare *<input name="cellulare" type="tel" required autocomplete="tel"></label><label>Email *<input name="email" type="email" required autocomplete="email"></label></div>
<label>Servizio di interesse *<select name="servizio" required><option value="">Scegli…</option>{opts}<option>Altro</option></select></label>
<label>Messaggio *<textarea name="messaggio" rows="5" required></textarea></label>
<label class="check"><input type="checkbox" required> Ho letto l’<a href="privacy-policy.html">informativa privacy</a> *</label>
<button class="btn" type="submit">Invia richiesta</button>
<p class="note">Il pulsante apre il tuo programma di posta con il messaggio già pronto.</p>
</form>
<div class="contact-box"><h2>Contatti</h2><ul class="contact-list">
<li><span>Telefono</span><a href="tel:{TEL_LINK}">{TEL}</a></li>
<li><span>Cellulare / WhatsApp</span><a href="{WA}">{CELL}</a></li>
<li><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><span>Sede operativa</span>{ADDR}</li></ul>
<h3>Seguici anche su</h3><ul class="social">{"".join(f'<li><a href="{u}" rel="noopener" target="_blank">{n}</a></li>' for n, u in SOCIAL)}</ul>
</div></div></section>""", "contatti.html")

    page("privacy-policy", "Privacy e cookie", "Informativa privacy e cookie di La Mole Edilizia su Fune.", "slide-1.jpg",
         hero("Privacy e cookie", "", "slide-1.jpg") + crumbs((None, "Privacy e cookie")) +
         """<section class="section"><div class="wrap prose">
<p><strong>Testo da confermare con il cliente.</strong> Il vecchio sito usava un’informativa esterna: va fornito il testo legale definitivo prima della pubblicazione.</p>
<p>Questo sito usa Google Analytics (Google LLC) per statistiche sulle visite e Meta Pixel (Meta Platforms) per misurare le campagne pubblicitarie.</p>
</div></section>""", "")

    # sitemap per Google
    urls = ["index"] + [p.stem for p in sorted(OUT.glob("*.html")) if p.stem not in ("index", "privacy-policy")]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"<url><loc>{SITE}/{'' if u == 'index' else u + '.html'}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")


if __name__ == "__main__":
    build()
    pages = sorted(OUT.glob("*.html"))
    # self-check: ogni link interno punta a un file esistente
    import re
    bad = [(p.name, h) for p in pages for h in re.findall(r'(?:href|src)="([^"#:]+)"', p.read_text()) if not (OUT / h).exists()]
    assert not bad, f"Link rotti: {bad}"
    print(f"OK: {len(pages)} pagine, nessun link rotto")
