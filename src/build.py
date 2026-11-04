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
        desc="Allontanamento piccioni e volatili da tetti, cornicioni e facciate con reti e dissuasori discreti, installati su fune senza ponteggi. Torino e tutta Italia.",
        problem="Piccioni e storni su cornicioni, balconi e sottotetti sporcano, rovinano le facciate e portano malattie. Li allontaniamo in modo discreto e senza fare male agli animali.",
        how=[("Sopralluogo", "Vediamo dove si posano e nidificano i volatili e scegliamo la soluzione giusta per quell’edificio."),
             ("Reti e dissuasori", "Installiamo reti resistenti al sole e dissuasori poco visibili, in acciaio inox o materiali riciclati, che non feriscono gli animali."),
             ("Pulizia e installazione dalla fune", "Puliamo le zone sporche e montiamo i sistemi calandoci dall’alto: niente ponteggio, niente cestello in strada.")],
        get=["Edificio protetto senza rovinarne l’aspetto", "Foto del lavoro fatto", "Controllo successivo e ritocchi se servono"]),
    "servizi-lavaggio-vetri": dict(title="Lavaggio Vetri", img="lavaggio-vetri.jpg",
        desc="Lavaggio vetri e vetrate in altezza con tecnici su fune: pulizia senza aloni di facciate continue e superfici difficili da raggiungere, senza ponteggi.",
        problem="Vetrate alte e facciate in vetro difficili da raggiungere si coprono di smog, calcare e sporco. Le puliamo calandoci dall’alto, senza fermare le attività di chi sta sotto.",
        how=[("Metodo adatto al vetro", "Usiamo acqua e detergenti biodegradabili, con il metodo giusto per ogni tipo di vetro: temperato, stratificato o antiriflesso."),
             ("Accesso su fune o piattaforma", "Raggiungiamo ogni punto con corde e dispositivi anticaduta, o con piattaforme aeree quando conviene."),
             ("Controllo finale", "A fine lavoro verifichiamo insieme il risultato.")],
        get=["Vetri puliti e senza aloni", "Nessun ponteggio davanti all’edificio", "Possibilità di pulizie programmate"]),
    "servizi-pulizia-canali-gronda-e-tetti": dict(title="Pulizia Canali Gronda e Tetti", img="pulizia-tetti.jpg",
        desc="Pulizia di grondaie, pluviali e tetti con accesso su fune: rimozione di foglie, muschio e detriti per evitare allagamenti e infiltrazioni.",
        problem="Grondaie e pluviali intasati da foglie e detriti fanno traboccare l’acqua, che finisce su facciate, balconi e solai. Il risultato sono infiltrazioni e danni.",
        how=[("Ispezione", "Controlliamo grondaie, pluviali e tetto, anche con videocamere nei tratti chiusi."),
             ("Pulizia completa", "Togliamo foglie, terra, muschio e detriti e liberiamo i pluviali, lavorando dalla fune nei punti difficili."),
             ("Verifica dello scarico", "Controlliamo che l’acqua scorra bene fino a terra e segnaliamo eventuali parti rotte."),
             ("Rifiuti smaltiti correttamente", "Portiamo via tutto e lo avviamo al riciclo.")],
        get=["Grondaie e pluviali liberi", "Foto prima e dopo", "Consigli su ogni quanto ripetere la pulizia"]),
    "servizi-sicurezza-e-check-up-tetti": dict(title="Sicurezza e Check-up Tetti", img="check-up-tetti.jpg",
        desc="Check-up del tetto senza ponteggi: ispezione su fune e con drone, relazione con foto e piano di manutenzione per coperture civili e industriali.",
        problem="Un tegola spostata o una piccola crepa sul tetto oggi diventano domani un’infiltrazione o un pericolo per chi passa sotto. Il check-up li trova prima.",
        how=[("Ispezione dall’alto", "Usiamo il drone per avere una visione completa e scendiamo su fune per controllare da vicino i punti critici."),
             ("Messa in sicurezza", "Se troviamo elementi pericolanti li sistemiamo o li mettiamo in sicurezza subito."),
             ("Relazione", "Ti consegniamo un documento con foto, problemi trovati, livello di urgenza e un piano di manutenzione.")],
        get=["Fotografia chiara dello stato del tetto", "Priorità degli interventi", "Piano di manutenzione"]),
    "servizi-impermeabilizzazione-tetti-cornicioni-e-terrazzi": dict(title="Impermeabilizzazione Tetti, Cornicioni e Terrazzi", img="impermeabilizzazione-tetti.jpg",
        desc="Impermeabilizzazione di tetti, cornicioni e terrazzi senza ponteggi: guaine e trattamenti resistenti al caldo e al gelo contro le infiltrazioni.",
        problem="Quando tetti, cornicioni e terrazzi non tengono più l’acqua, compaiono macchie, muffa e intonaco che si stacca. Rifacciamo l’impermeabilizzazione anche dove arrivare è difficile.",
        how=[("Ricerca del punto debole", "Individuiamo da dove entra l’acqua prima di intervenire."),
             ("Preparazione", "Puliamo e ripariamo la superficie, togliendo le parti rovinate."),
             ("Nuova impermeabilizzazione", "Applichiamo guaine o membrane liquide adatte a quella superficie, resistenti al sole, al gelo e agli sbalzi di temperatura."),
             ("Lavoro su fune", "Su cornicioni e parti alte lavoriamo calandoci dall’alto, senza ponteggio.")],
        get=["Superfici che non fanno più passare l’acqua", "Garanzia sul lavoro (durata da concordare)", "Foto dell’intervento"]),
    "servizi-isolamento-termico": dict(title="Isolamento Termico", img="isolamento-termico.jpg",
        desc="Isolamento termico e cappotto anche su fune: meno dispersioni di calore, più comfort e bollette più leggere, con posa certificata UNI 11716.",
        problem="Una casa che d’inverno disperde calore e d’estate si scalda troppo costa di più in bolletta ed è meno confortevole. Un buon isolamento risolve il problema.",
        how=[("Analisi", "Valutiamo l’edificio e dove si perde calore, anche con la termocamera."),
             ("Materiali adatti", "Scegliamo pannelli e materiali isolanti in base alla struttura e al tipo di facciata."),
             ("Posa anche senza ponteggio", "Dove possibile lavoriamo su fune, con sistemi fissati meccanicamente che evitano demolizioni."),
             ("Posa certificata", "Rilasciamo l’attestato di corretta posa del cappotto secondo la norma UNI 11716:2018.")],
        get=["Meno dispersioni e più comfort", "Attestato di corretta posa", "Controllo con termocamera su richiesta"]),
    "servizi-isolamento-e-rifacimento-tetti": dict(title="Isolamento e Rifacimento Tetti", img="isolamento-e-rifacimento-tetti.jpg",
        desc="Rifacimento e isolamento tetti per case, condomini e aziende: nuova copertura, isolamento termico e acustico, supporto per gli incentivi fiscali.",
        problem="Un tetto vecchio fa entrare acqua, disperde calore e prima o poi va rifatto. Lo rinnoviamo completamente, isolandolo per farti risparmiare energia.",
        how=[("Diagnosi e progetto", "Valutiamo lo stato del tetto e proponiamo la soluzione più adatta all’edificio e al budget."),
             ("Rimozione e riparazione", "Togliamo la vecchia copertura e sistemiamo le strutture rovinate."),
             ("Isolamento e impermeabilizzazione", "Posiamo isolanti termici e acustici, guaine e ventilazione."),
             ("Nuova copertura", "Tegole, coppi, pannelli metallici o fotovoltaico integrato, a scelta.")],
        get=["Tetto nuovo e isolato", "Supporto per le pratiche degli incentivi fiscali", "Garanzia su materiali e manodopera"]),
    "servizi-installazione-e-revisione-linee-vita": dict(title="Installazione e Revisione Linee Vita", img="linee-vita.jpg",
        desc="Installazione e revisione linee vita a norma UNI 11900 su tetti e coperture: ancoraggi certificati, ispezioni periodiche e documentazione CE.",
        problem="Chi sale sul tetto per manutenzioni deve potersi agganciare in sicurezza: la linea vita è obbligatoria e va controllata periodicamente.",
        how=[("Progetto", "Studiamo la copertura e decidiamo dove posizionare ancoraggi e cavi."),
             ("Installazione", "Montiamo ancoraggi, binari e cavi in acciaio certificati, compatibili con i dispositivi più diffusi."),
             ("Revisione periodica", "Ispezioniamo le linee esistenti e sostituiamo i pezzi usurati.")],
        get=["Linea vita a norma UNI 11900", "Documentazione e certificazioni CE", "Promemoria per le revisioni"]),
    "servizi-messa-in-sicurezza": dict(title="Messa in sicurezza", img="messa-in-sicurezza.jpg",
        desc="Messa in sicurezza urgente di facciate, cornicioni e balconi con tecnica su fune: rimozione parti pericolanti, consolidamento e documentazione.",
        problem="Intonaco che si stacca, cornicioni crepati, frontalini dei balconi che cadono: sono un pericolo immediato per chi passa sotto. Interveniamo in fretta, senza aspettare il ponteggio.",
        how=[("Intervento rapido", "Raggiungiamo la facciata su fune e rimuoviamo subito le parti pericolanti."),
             ("Consolidamento", "Fissiamo le zone a rischio con reti in fibra o resine, così il rifacimento si può programmare con calma."),
             ("Documentazione", "Rilasciamo la documentazione tecnica sull’intervento e sulle condizioni di sicurezza.")],
        get=["Pericolo eliminato in tempi brevi", "Relazione per amministratore e Comune", "Indicazioni per il rifacimento"]),
    "servizi-ricerca-e-riparazione-infiltrazioni": dict(title="Ricerca e Riparazione Infiltrazioni", img="infiltrazioni-da-tetto.jpg",
        desc="Ricerca infiltrazioni d’acqua con termocamera e strumenti non invasivi, e riparazione mirata senza demolire, su tetti, facciate e muri.",
        problem="Una macchia sul soffitto o una muffa che torna sempre: spesso l’acqua entra da un punto lontano da dove si vede. Troviamo l’origine e la ripariamo.",
        how=[("Ricerca strumentale", "Usiamo termocamera e misuratori di umidità per trovare il punto esatto da cui entra l’acqua, senza rompere nulla."),
             ("Riparazione mirata", "Sigilliamo crepe e fessure con prodotti specifici, raggiungendo i punti alti su fune."),
             ("Verifica", "A lavoro finito controlliamo che non ci sia più umidità.")],
        get=["Causa trovata, non solo il sintomo", "Riparazione senza demolizioni", "Verifica finale dell’umidità"]),
    "servizi-rifacimento-facciate": dict(title="Rifacimento Facciate", img="rifacimento-facciate.jpg",
        desc="Rifacimento e restauro facciate di condomini, aziende ed edifici storici: diagnosi, intonaci, pitture, cappotto termico e gestione delle pratiche.",
        problem="Una facciata rovinata peggiora l’aspetto e il valore dell’edificio e col tempo lascia passare acqua e umidità. La rifacciamo dalla diagnosi al collaudo.",
        how=[("Diagnosi", "Analizziamo la facciata anche con drone e termocamera per capire cosa va sistemato."),
             ("Progetto e pratiche", "Prepariamo il progetto e ci occupiamo dei permessi edilizi necessari."),
             ("Lavori", "Rimuoviamo le parti rovinate, rifacciamo intonaci e finiture e, se richiesto, aggiungiamo il cappotto termico. Su fune o piattaforma, a seconda dell’edificio."),
             ("Collaudo", "Verifichiamo il risultato finale.")],
        get=["Un solo referente per tutto il lavoro", "Facciata protetta da acqua e muffa", "Garanzia su materiali e manodopera"]),
    "servizi-lattoneria-edile": dict(title="Lattoneria edile", img="lattoneria-edile.jpg",
        desc="Lattoneria edile su misura: grondaie, pluviali, scossaline, coperture metalliche e impianti parafulmine, installati anche su fune.",
        problem="Grondaie rotte, scossaline staccate e pluviali bucati fanno finire l’acqua dove non deve. Realizziamo e sostituiamo tutte le opere in lamiera dell’edificio.",
        how=[("Grondaie e pluviali", "Progettiamo e installiamo sistemi di raccolta dell’acqua su misura, per tetti a falde e piani."),
             ("Coperture e rivestimenti metallici", "Realizziamo coperture e facciate in metallo con giunzioni a graffatura."),
             ("Impianti parafulmine", "Installiamo sistemi parafulmine certificati."),
             ("Dalla fune", "Montiamo tutto senza ponteggio, anche nei punti più alti.")],
        get=["Lavoro su misura, chiavi in mano", "Acqua piovana che scorre dove deve", "Un solo partner dalla misura al montaggio"]),
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

FAQ = [("Serve il ponteggio?", "No. Lavoriamo calandoci dall’alto con corde e imbragature. In alcuni casi usiamo piattaforme aeree, ma mai ponteggi."),
       ("Serve un permesso per occupare il suolo pubblico?", "Di norma no, perché non montiamo strutture sul marciapiede. Lo verifichiamo comunque al sopralluogo, caso per caso."),
       ("È sicuro?", "Sì. I nostri tecnici sono formati con la Scuola di Alpinismo Valli di Lanzo e lavorano secondo il D.Lgs. 81/08, con attrezzature certificate."),
       ("Quanto costa?", "Dipende dall’intervento: per questo facciamo prima un sopralluogo e poi un preventivo dettagliato. Senza ponteggio i costi sono in genere più bassi."),
       ("Ci saranno disagi per chi abita nel palazzo?", "Pochi: niente impalcature davanti alle finestre e cantieri molto più brevi. Le zone sotto l’intervento vengono delimitate solo mentre lavoriamo."),
       ("In che zone lavorate?", "Siamo a Grugliasco (Torino) e lavoriamo soprattutto in Piemonte e Nord Italia, ma interveniamo in tutta Italia.")]
FAQ_HTML = "".join(f"<details class=\"faq\"><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

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


def cta(title="Hai bisogno di un intervento in quota, senza ponteggi?"):
    return f"""<section class="cta">
<div class="wrap cta-in">
<div><h2>{title}</h2>
<p>Raccontaci il problema: facciamo un sopralluogo e ti mandiamo un preventivo chiaro, senza impegno.</p></div>
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
<h1>Lavori su tetti e facciate<br><em>senza ponteggi.</em></h1>
<div class="hero-actions"><a class="btn btn-pill" href="contatti.html">Richiedi un sopralluogo ↗</a><p>Infiltrazioni, facciate, grondaie, linee vita: interveniamo calandoci con le corde, come gli alpinisti. Torino e tutta Italia.</p></div>
<ul class="hero-feats">
<li><span>↕</span>Niente ponteggio<br>meno costi, meno disagi</li>
<li><span>⏱</span>Cantiere rapido<br>pronti a lavorare in 1-2 giorni</li>
<li><span>✓</span>Tecnici formati<br>Scuola di Alpinismo Valli di Lanzo</li>
</ul>
</div>
</section>
<section class="section"><div class="wrap">
<p class="eyebrow">Da dove partire</p><h2>Che problema hai?</h2>
<p class="lead">Scegli quello che vedi sul tuo edificio: ti mostriamo come lo risolviamo.</p>
<div class="problems"><a class="problem" href="servizi-ricerca-e-riparazione-infiltrazioni.html"><span aria-hidden="true">💧</span>Macchie di umidità o acqua che entra</a><a class="problem" href="servizi-messa-in-sicurezza.html"><span aria-hidden="true">🧱</span>Intonaco o cornicioni che si staccano</a><a class="problem" href="servizi-pulizia-canali-gronda-e-tetti.html"><span aria-hidden="true">🍂</span>Grondaie intasate o che traboccano</a><a class="problem" href="servizi-allontanamento-volatili.html"><span aria-hidden="true">🕊</span>Piccioni su tetti e balconi</a><a class="problem" href="servizi-sicurezza-e-check-up-tetti.html"><span aria-hidden="true">🏠</span>Tetto vecchio da controllare o rifare</a><a class="problem" href="servizi-rifacimento-facciate.html"><span aria-hidden="true">🎨</span>Facciata rovinata da rinnovare</a><a class="problem" href="servizi-installazione-e-revisione-linee-vita.html"><span aria-hidden="true">🔗</span>Linea vita da installare o revisionare</a><a class="problem" href="servizi-lavaggio-vetri.html"><span aria-hidden="true">🪟</span>Vetrate alte da pulire</a></div>
<p class="note">Non trovi il tuo caso? <a href="servizi-edilizia-su-fune.html">Guarda tutti i 12 servizi</a> o <a href="contatti.html">scrivici</a>.</p>
</div></section>
<section class="section alt"><div class="wrap split">
<div><p class="eyebrow">Cos’è l’edilizia su fune</p><h2>Come gli alpinisti, ma sul tuo palazzo</h2>
<p>Invece di montare un ponteggio, i nostri tecnici si calano dall’alto con corde e imbragature, usando le tecniche dell’alpinismo. Arrivano su qualsiasi punto di tetti e facciate e lavorano come farebbero da un’impalcatura.</p>
<p>Per te significa: niente settimane di montaggio, niente struttura davanti alle finestre, meno costi e, di norma, nessun permesso per occupare il marciapiede. Il tutto in sicurezza, nel rispetto del D.Lgs. 81/08.</p>
<a class="link" href="vantaggi.html">Confronto con il ponteggio</a></div>
<img src="assets/img/vantaggi-3.jpg" alt="Tecnico su fune al lavoro su una facciata" loading="lazy" width="1024" height="1024">
</div></section>
<section class="section"><div class="wrap">
<p class="eyebrow">Per chi lavoriamo</p><h2>Condomini, aziende e privati</h2>
<div class="grid three">
<div class="card"><h3>Amministratori di condominio</h3><p>Sopralluogo, preventivo chiaro da portare in assemblea, relazione con foto a fine lavoro. Nessun ponteggio che blocca cortili e ingressi.</p></div>
<div class="card"><h3>Aziende e capannoni</h3><p>Coperture industriali, linee vita, vetrate e facciate, con interventi pianificati per non fermare l’attività.</p></div>
<div class="card"><h3>Privati</h3><p>Dalla grondaia che perde alla facciata da rifare: interventi anche piccoli, senza i costi di un cantiere tradizionale.</p></div>
</div></div></section>
<section class="section alt"><div class="wrap">
<p class="eyebrow">Come lavoriamo</p><h2>Dalla chiamata al lavoro finito</h2>
<ol class="steps">
<li><strong>Ci contatti</strong>Per telefono, WhatsApp o modulo. Ci racconti il problema, anche con una foto.</li>
<li><strong>Sopralluogo</strong>Veniamo a vedere l’edificio e capiamo cosa serve davvero.</li>
<li><strong>Preventivo</strong>Ricevi un preventivo chiaro, con lavori e tempi.</li>
<li><strong>Intervento e relazione</strong>Lavoriamo su fune e a fine lavoro ti consegniamo le foto di quanto fatto.</li>
</ol></div></section>
<section class="section"><div class="wrap">
<p class="eyebrow">Servizi</p><h2>Tutti i nostri servizi</h2>
<p class="lead">Quattro aree, dodici servizi, tutti eseguiti senza ponteggio.</p>
{cat_tiles()}</div></section>
<section class="section"><div class="wrap">
<p class="eyebrow">Recensioni</p><h2>La soddisfazione dei nostri clienti parla per noi</h2>
<p class="lead">Valutazione <strong>eccellente</strong> in base a 14 recensioni su Google.</p>
<div class="grid three">{"".join(f'<figure class="review"><blockquote>“{t}”</blockquote><figcaption>{n} · {d}</figcaption></figure>' for n, d, t in REVIEWS)}</div>
</div></section>
<section class="section alt"><div class="wrap prose">
<p class="eyebrow">Domande frequenti</p><h2>Le domande che ci fanno più spesso</h2>
{FAQ_HTML}
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
        steps = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in s["how"])
        gets = "".join(f"<li>{g}</li>" for g in s["get"])
        others = [(f"{o}.html", SERVICES[o]["title"], SERVICES[o]["img"]) for o in c["items"] if o != slug]
        page(slug, s["title"], s["desc"], s["img"],
             hero(s["title"], s["problem"], s["img"], c["title"]) +
             crumbs(("servizi-edilizia-su-fune.html", "Servizi"), (f'{c["slug"]}.html', c["title"]), (None, s["title"])) +
             f"""<section class="section"><div class="wrap split">
<div><h2>Cosa ricevi</h2><ul class="checks">{gets}</ul><p class="note">Lavoriamo su fune con tecnici formati all’alpinismo: niente ponteggio, meno tempi e meno disagi.</p><a class="btn" href="contatti.html">Richiedi un sopralluogo</a></div>
<img src="assets/img/{s["img"]}" alt="{escape(s["title"])}: intervento de La Mole Edilizia su Fune" loading="lazy" width="800" height="600">
</div></section>
<section class="section alt"><div class="wrap"><h2>Come interveniamo</h2>
<div class="grid two">{steps}</div></div></section>
<section class="section"><div class="wrap"><h2>Altri servizi di {c["title"]}</h2>{tiles(others)}</div></section>
{cta(f"Ti serve un intervento di {s['title'].lower()}?")}""", "servizi-edilizia-su-fune.html")

    rows = [("Costi", "Ridotti: nessuna struttura da noleggiare", "Elevati (ponteggi, gru, ecc.)"),
            ("Tempi", "Rapidi (1-2 giorni per allestimento)", "Lunghi (settimane per montaggio)"),
            ("Impatto visivo", "Minimo", "Elevato"), ("Disturbo", "Minimo per inquilini e passanti", "Significativo"),
            ("Flessibilità", "Elevata (adattabile a ogni struttura)", "Limitata"),
            ("Sicurezza", "Elevata con personale certificato", "Variabile")]
    why = [("Zero ponteggi", "Interventi rapidi senza installare costosi e ingombranti ponteggi."),
           ("Costi contenuti", "Senza ponteggio si risparmiano montaggio, noleggio e smontaggio."),
           ("Interventi rapidi", "Tempi ridotti grazie alla mobilità e flessibilità delle tecniche su fune."),
           ("Personale certificato", "Tecnici specializzati con certificazioni internazionali per lavori in quota."),
           ("Massima sicurezza", "Protocolli avanzati e attrezzature certificate per ogni intervento."),
           ("Approccio ecologico", "Materiali sostenibili e riduzione dell’impatto ambientale.")]
    page("vantaggi", "Vantaggi",
         "Ecco perché l’edilizia su fune conviene: zero ponteggi, costi ridotti, tempi rapidi, meno permessi e impatto minimo, con personale certificato.",
         "vantaggi-2-1.jpg",
         hero("Vantaggi", "L’edilizia su fune consente di effettuare interventi in quota senza ponteggi tradizionali. Ispirata alle tecniche di alpinismo, offre numerosi vantaggi rispetto ai metodi tradizionali.", "vantaggi-2-1.jpg", "Perché la fune") +
         crumbs((None, "Vantaggi")) +
         f"""<section class="section"><div class="wrap split">
<div><h2>Efficienza economica</h2><p>Uno dei principali vantaggi dell’edilizia su fune è il risparmio economico: l’assenza di ponteggi e strutture di supporto riduce significativamente i costi dell’intervento.</p>
<ul class="checks"><li><strong>Nessun costo per ponteggi</strong> Si paga il lavoro, non la struttura</li><li><strong>Tempi di intervento ridotti</strong> Meno giorni di lavoro, meno costi</li><li><strong>Nessun permesso speciale</strong> per l’occupazione del suolo pubblico</li><li><strong>Costi assicurativi ridotti</strong> per la minor durata dei lavori</li></ul></div>
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
