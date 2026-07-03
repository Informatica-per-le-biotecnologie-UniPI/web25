---
layout: page
title: Esame
permalink: /esame/
---

<script>
	$(document).ready(function(){ $(".menu .item").tab(); });
</script>

L'esame si compone di due moduli, uno di algoritmica e uno di programmazione. I due possono essere sostenuti in appelli separati, ma all'interno di uno stesso anno accademico. Il modulo di algoritmica prevede un compito scritto, quello di programmazione un progetto da fare in gruppi da 2-3 studenti, seguito da discussione orale.


## FAQ

### Voti
- **Dove/Quando vengono pubblicati i voti?** In [questo sheet](https://docs.google.com/spreadsheets/d/1sceV5cGmsFAPHo4SDdtfjNyHVMBFmWezQ56HtSMShAU/edit?usp=sharing) in seguito all'appello.
- **Come viene calcolato il voto?** Media aritmetica dei voti su due moduli. Entrambi devono essere sufficienti.

### Moduli
- **Posso dare i due moduli separatamente?** Si, ma entro lo stesso anno accademico. Se uno studente non sostiene con profitto entrambi i moduli tra l'appello di ottobre (compreso) e l'appello di settembre dell'anno successivo (compreso), dovrà sostenere nuovamente entrambi i moduli.
- **Per dare un modulo devo aver passato l'altro?** No, i due moduli sono indipendenti. Si consiglia comunque di studiare prima il modulo di algoritmica.

### Ricevimenti e orali
- **Dove trovo il Dipartimento di Informatica?** [Edificio C del Polo Fibonacci](https://maps.app.goo.gl/7KCceYCRTwNGPDMq9), secondo piano.
- **Dove trovo la Sala Riunioni Est/Ovest?** Chiedi nella portineria del dipartimento, o consulta [la mappa online](https://di.unipi.it/mappa-dipartimento/).

### Progetto
- **Quando vengono consegnati i testi dei progetti?** Tipicamente dai 7 ai 10 giorni prima dell'appello, con notifica sulla bacheca del sito.
- **Devo iscrivermi all'appello per consegnare il progetto?** Si. In ogni caso, nelle note d'iscrizione indicare che modulo si intende dare. Per gli appelli straordinari, indicare anche su che programma viene dato il corso.
- **Per l'orale devo portare il computer?** Si consiglia di portare il proprio. In caso non si possa, è disponibile un laptop.
- **Come carico il progetto su Github?** Crea un account, e segui le [istruzioni online per creare un repository privato](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository). Dalla pagina del repository seleziona `Upload` (a volte indicato con il tasto `+`) e seleziona i file da caricare.
- **Come invito un collaboratore?** Segui la [documentazione online](https://docs.github.com/articles/inviting-collaborators-to-a-personal-repository).


### Lezioni
- **Sono previsti laboratori aggiuntivi?** No, le lezioni seguono il calendario indicato. Studenti interessati a chiarimenti o approfondimenti possono contattare i docenti e usufruire del ricevimento (riferimenti su Unimap).
- **Devo portare il computer a lezione?** Solo per il modulo di programmazione.
- **Dove trovo i programmi da installare?** Pagina `Materiali`.

- **Dove trovo il gruppo Teams?** [Qui](https://teams.microsoft.com/l/team/19%3AjDZbg-1U0hUSzpYOsEoN00_TuxFkLu-vEt9hR5fyPJk1%40thread.tacv2/conversations?groupId=475fb31f-ea24-41c1-abb0-97226190f015&tenantId=c7456b31-a220-47f5-be52-473828670aa1).

---

# Progetti

I testi di progetto appaiono in precedenza a ogni appello. Una cheat sheet è disponibile [qui](../static_files/cheat.pdf) per aiutare nella sintassi del linguaggio.

<div class="ui top attached tabular menu">
    <a class="item" data-tab="linee"><b>Linee guida</b></a>
    <a class="item" data-tab="gennaio">Gennaio</a>
    <a class="item" data-tab="febbraio">Febbraio</a>
    <a class="item" data-tab="marzo">Marzo</a>
    <a class="item" data-tab="aprile">Aprile</a>
    <a class="item" data-tab="maggio">Maggio</a>
    <a class="item" data-tab="giugno">Giugno</a>
    <a class="item active" data-tab="luglio">Luglio</a>
    <a class="item" data-tab="settembre">Settembre</a>
</div>
<!--  -->
<div class="ui bottom attached tab segment" data-tab="linee" markdown="1">
    
### Progetto

In gruppi di 2-3 persone, gli studenti devono decidere come modellare i concetti richiesti, definendo classi, interfacce, estensioni, campi, e metodi, operando scelte giustificate. Il progetto **deve** includere:

1. Una documentazione
    1. Generale: un `README.md` che indica la struttura del progetto, e.g., che modulo svolge quali funzioni, quali sono le funzioni che offrono quali feature, ecc. Si includa anche una piccola sezione `Quickstart` in cui si dettaglia come eseguire gli esempi di utilizzo richiesti dal testo. Trovi esempi di `README.md` [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/postings/blob/master/README.md) e [qui](https://github.com/Informatica-per-le-biotecnologie-UniPI/traits/blob/feb7/README.md). Clicca su `Raw` per vedere il codice.
    2. In codice: documentazione per funzioni e classi, i.e., commenti e tipizzazione funzioni
2. Uno script eseguibile `main.py` con esempi di utilizzo che mostrino **tutte** le funzionalità richieste dal testo, una per una. Funzionalità non mostrate nel main sono considerate **non implementate**.
3. Uno o più file (non il `main.py`) che implementano la consegna.

Progetti che non seguono la struttura sopra indicata sono considerati insufficienti.


### Consegna

Per la consegna, creare un repository privato su [Github](https://github.com/), e invitare user `msetzu` come collaboratore.


### Valutazione

La valutazione del progetto include, in ordine di importanza:

1. Correttezza del codice: il codice rispetta la consegna
2. Documentazione e leggibilità: il codice è scorrevole di facile lettura
3. Modularità, estensibilità: il codice è ben organizzato in moduli/classi/funzioni, e di facile estensione
4. Completezza del codice: il codice tratta anche i casi limite, e.g., un trascrittore di DNA che lancia eccezione quando il DNA dato ha lunghezza zero


---

# Tips & Tricks

### Nomenclatura, tipizzazione, e commenti
- Usa nomi significativi, ed evita quando possibile sigle e variabili a una lettera, e.g., `x`
- Usa lo *snake case* per variabili e funzioni: separa le parole con `_`, e.g., `starting_codon`
- Usa il *camel case* per le classi: separa le parole con una maiuscola, e.g., `PapillomaVirus`
- Indica i tipi dei parametri delle funzioni, e il loro tipo di ritorno
- Nelle funzioni e nei metodi, indica con un breve commento cosa la funzione implementa, e a cosa servono i vari parametri

### Import
In caso di progetto con diversi file, puoi trattare ogni file come un "modulo" da cui importare funzioni e/o classi. E.g., dato un file `amoeba.py` con contenuto

`amoeba.py`
```python
def foo(a, b):
    ...

class Amoeba:
    ...
```

puoi poi creare, nella stessa cartella, un file con contenuto

```python
from amoeba import Amoeba
from amoeba import foo

x = Amoeba()
y = foo(...)
...
```

**Nota:** L'`import` esegue il file che importa. Se hai del codice esterno alle funzioni/classi, questo viene eseguito ogni volta che fai l'import. Per buona pratica, nei file da cui vuoi importare funzioni/classi non inserire codice ulteriore.

### Documentazione

Quando sei in dubbio, sfrutta la [cheat sheet](https://informatica-per-le-biotecnologie-unipi.github.io/web25//static_files/cheat.pdf) o la documentazione di Python!

- Documentazione [costrutti](https://docs.python.org/3/tutorial/controlflow.html)
- Documentazione [collezioni](https://docs.python.org/3/tutorial/datastructures.html)
- Documentazione [eccezioni](https://docs.python.org/3/tutorial/errors.html)
- Documentazione [funzioni predefinite](https://docs.python.org/3/library/functions.html)

## Scrittura codice
Quando scrivi codice:
1. Identifica che categorie di dati ti servono
2. Identifica che tipo di manipolazioni vuoi farci
3. Traducile in Python con tipi esistenti/nuove classi
4. Struttura, su carta, un piccolo algoritmo per risolvere il problema
	1. Separa quando possibile funzionalità diverse, fino a raggiungere piccoli task relativamente semplici: divide et impera
	2. Identifica relazioni tra i task, e.g., per simulare la trascrizione del DNA devo estrarre triplette, convertire le triplette in aminoacidi, etc.
5. Traduci in Python: decidi cosa implementare come funzione, come metodo, etc.
6. Scrivi un paio di esempi guida per testare il tuo codice, e.g., un paio di piccoli genomi a mano su cui testare se il tuo codice funziona
7. Implementa separatamente tutte le diverse funzioni/algoritmi
8. Testa il tuo codice sugli esempi del punto sopra, partendo dai tuoi task base. Se falliscono, torna indietro, aggiusta, e torna al punto precedente

L'utilizzo di strumenti di AI per la scrittura di codice o documentazione **non è consentito**.

</div>
<!--  -->
<div class="ui bottom attached tab segment" data-tab="gennaio" markdown="1">

*Segui le linee guida nella tab di fianco. Scadenza consegna: 9 gennaio. Per dubbi, chiedere via mail.*

# Contesto

Nell'editing genetico, un genoma base viene modificato, aggiungendo delle sequenze predefinite, dette *insertions*, in determinati punti del genoma stesso, risultando in un *edit* del genoma. Tali inserimenti avvengono subito dopo degli specifici *insertion point*, ossia specifici punti del genoma identificati da una sequenza genetica. Un edit risulta in un unico inserimento: se un genoma presenta `> 1` insertion points, l'edit avviene solo su uno, scelto arbitrariamente. Inoltre, se l'insertion è già presente nel genoma, l'inserimento **non** avviene.

**Esempio.**
```python
genome = "ACCTGCAACTGC"
insertion_point = "CT"
insertion = "GGGTGGG"
```

Questo esempio fornisce i seguenti insert point (indicati da `*`):
```python
"ACCT*GCAACT*GC"
```
L'edit avviene inserendo le insertion in uno solo degli insertion points, e.g.,

- `"ACCTGGGTGGGGCAACTGC"`
- `"ACCTGCAACTGGGTGGGGC"`

Gli inserimenti possono avere successo, oppure no, risultando in genomi non modificati, o modificati erroneamente. In caso di errori si ha una di due casistiche:

1. l'inserimento è vuoto
2. l'inserimento è non vuoto: il primo carattere dell'insertion viene inserito correttamente, ma gli altri possono mutare

Nell'esempio di cui sopra, possibili inserimenti con errori includono

- `ACCTGCAACTGC` inserimento vuoto
- `ACCTGCAACTGGTAAAGC` ultimi tre caratteri incorretti
- `ACCTGCAACTGGTAGGC` penultimo carattere incorretto


Nelle seguenti, assumi un alfabeto genomico standard di basi "ACGT".

---

# Traccia
## Parte A
*Gruppi da 1 a 3 studenti*

**1.**
Scrivere una funzione che, dato un genoma di partenza, un insertion, un insertion point, e un potenziale edit:

1. Calcola se l'edit è corretto o meno
2. Calcola il punto di inserimento, i.e., l'indice in cui è avvenuto l'inserimento. In caso di ambiguità, considera un punto arbitrario
3. In caso di edit incorretto, calcola l'errore: quante basi dell'insertion sono state inserite incorrettamente?


**2.**
Viene fornito un insieme di `k` possibili inserimenti, i.e., `k` inserimenti e `k` insertion points. Scrivi una funzione che, dato un edit, calcola il numero di errori per ognuno dei `k` possibili inserimenti, e li ordina da quello con meno a quello con più successo.

**Esempio.**
```python
genome = "ACCTGCAACTGC"
insertion_points = ["CT", "AC"]
insertion = ["GTG", "TGT"]

edits = [
	"ACCTGCAACT GAG GC",
	"ACCTGCAACT GGG GC",
	"AC TAT TGGCAACTGC", 
	"AC TGT CTGCAACTGC",	
	"ACCTGCAACTGC",
]
```

In questo caso, l'ordine restituito sarebbe

```python
"AC TGT CTGCAACTGC", # errori: 0 su insertion point AC
"ACCTGCAACT GAG GC", # errori: 1 su insertion point CT
"ACCTGCAACT GGG GC", # errori: 1 su insertion point CT
"AC TAT TGGCAACTGC", # errori: 1 su insertion point AC
"ACCTGCAACT GC", # errori: 3 su insertion point CT
```

Nota: gli spazi negli esempi sopra sono stati inseriti per leggibilità. *Non* sono parte dell'edit.

## Parte B
*Gruppi da 2 a 3 studenti*

Il modulo [random](https://docs.python.org/3/library/random.html) fornisce funzioni per l'estrazione/generazione pseudo-casuale di valori. Consultalo per trovare funzioni che fanno al caso per l'implementazione di questa parte.

Scrivi una funzione che genera possibili edit sulla base di un dato genoma di base, insertion, e insertion point. Gli edit dovranno essere generati sulla base di un parametro che indica che tipo di edit generare. In ogni casistica, considera *tutti* i possibili insertion point, non solo il primo che trovi. Nello specifico, possono essere richiesti edit di questo tipo:

- Privo di errori: edit inserito nell'insertion point corretto, e con l'insertion corretta. Considera *tutti* i possibili inserition point nel genoma.
- Con `r` (`r` numero intero) errori: inserito nell'insertion point corretto, ma con `r` mutazioni nell'insertion. Anche qui, considera *tutti* i possibili inserition point nel genoma.
- Senza inserimento: nessuna modifica al genoma originale.

Nella casistica con `r` errori, le basi inserite come errori *non* hanno una probabilità uniforme: la funzione sceglie gli errori su probabilità date, e.g., `"T"` con probabilità `0.5`, `"G"` con probabilità `0.3`, e `A` con probabilità `0.2`.

## Parte C
*Gruppi da 3 studenti*

Il modulo [random](https://docs.python.org/3/library/random.html) fornisce funzioni per l'estrazione/generazione pseudo-casuale di valori. Consultalo per trovare funzioni che fanno al caso per l'implementazione di questa parte.

Crea una funzione che seleziona dei valori per:

- Insertion: valori scelti randomicamente. Lunghezza dell'insertion scelta a campione da una distribuzione di tua scelta.
- Insertion point: valori scelti randomicamente.
- Casistica di edit, come indicata nella parte B. Tipo di edit scelto randomicamente, e in caso di errori, il numero di errori scelto a campione da una distribuzione di tua scelta.

Dati un genoma e un numero di edit desiderati, la funzione genera degli edit sulla base dei valori sopra indicati.


</div>
<!--  -->
<div class="doi ui bottom attached tab segment" data-tab="febbraio" markdown="1">

**Scadenza.** venerdi 6, ore 10:30.

Leggi con **massima attenzione** le linee guida prima di iniziare.

# Contesto

In chemioinformatica, le molecole sono spesso modellate e rappresentate con stringhe che seguono precise regole di *encoding*. L'encoding definisce come una molecola, e.g., l'acetofenone, viene trascritta in una stringa, similmente a quanto accade per le formule molecolari. In questo progetto, lavoreremo sulla verifica di un encoding particolare: *FAME*.

### Atomi
All'interno delle stringhe FAME, gli atomi sono indicati con il loro simbolo atomico standard, rigorosamente in maiuscolo, e.g., `C` per l'atomo di carbonio. FAME rappresenta unicamente molecole con atomi di carbonio (`C`), azoto (`N`), ossigeno (`O`), idrogeno (`H`), fluoro (`F`), o zolfo (`S`), in una qualsiasi combinazione. A ogni atomo associamo una *valenza*, definita come il numero di elettroni aggiuntivi che garantisce stabilità. E.g., il carbonio ha valenza `4` poiché per essere stabile deve avere `4` elettroni in condivisione da altri atomi. Pertanto, stringhe FAME in cui il carbonio non ha legami che gli garantiscono valenza `4` modellano molecole non valide. In FAME, consideriamo unicamente semplici legami covalenti in cui gli atomi sono condivisi.
Nelle stringhe FAME, **due atomi che sono oggetto di un legame**, e.g., idrogeno e ossigeno nell'acqua, **si trovano uno di seguito all'altro**, e sono **inframezzati da** dei simboli che rappresentano il **legame** covalente che intercorre, e.g., legame covalente singolo, doppio, o triplo. 

**Esempi.** Utilizziamo `{LEGAME X}` per indicare un legame covalente su `X` elettroni. 
- $H_2O$ con FAME`H{LEGAME SINGOLO}O{LEGAME SINGOLO}H`
-  $C_2 H_2$ con FAME `H{LEGAME SINGOLO}C{LEGAME TRIPLO}C{LEGAME SINGOLO}H`.
-  $C_2 H_2$ con FAME `H{LEGAME SINGOLO}H{LEGAME SINGOLO}C{LEGAME TRIPLO}C` è un esempio non corretto: implica che il secondo idrogeno ha due legami singoli, uno con il primo idrogeno e uno con il primo carbonio, e che il secondo carbonio ha solo un legame triplo. Pertanto il secondo idrogeno viola la valenza, cosi' come il secondo carbonio.

### Legami
FAME modella i legami covalenti, e ne inserisce un encoding tra gli atomi in legame secondo la seguente tabella.

| Encoding | Legame           | Valenza | Info                                                                                                                   | Esempio                            |
| -------- | ---------------- | ------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `-`      | Legame singolo   | `1`     | Opzionale                                                                                                              | $H_2 O$ con `H-O-H`                |
| `^...&`  | Ramificazione    |         | Le ramificazioni iniziano con un `^` e terminano con un `&`, e gli atomi in cui si ramifica non hanno ulteriori legami | `C^-H&-H`, `O^-H&-H`, `O^-H-H&`    |
| `=`      | Legame doppio    | `2`     |                                                                                                                        | `C^=O=O&`                          |
| `#`      | Legame triplo    | `3`     |                                                                                                                        | `H-C#C-H`                          |
|          | Legame aromatico | `1.5`   | Atomi con lettere minuscole, apertura e chiusura anello con numeri. Ogni blocco tra quadre.                            | `[c-H]1[c-H][c-H][c-H][c-H][c-H]1` |

**Nota.** Assumi che i singoli legami siano sempre validi per difetto, i.e., che in una stringa FAME un atomo con valenza `X` abbia legami con valenza `Y <= X`, e.g., un ossigeno può avere legami singoli o doppi, ma non tripli.

#### Ramificazioni
Le ramificazioni arricchiscono FAME, permettendo di modellare molecole in cui un singolo atomo è oggetto di più legami, e.g., un carbonio con quattro idrogeni. In FAME, le ramificazioni iniziano con un `^`, terminano con un `&`, e riportano `>= 1` legami. Se un atomo ha ramificazioni, queste lo seguono *immediatamente* nella stringa FAME. I.e., in `H-C-O^-H&`, la ramificazione `^-H&` va interpretata come ramificazione dell'ossigeno.

Gli atomi all'interno della ramificazione **non** hanno legami tra loro, né con altri atomi, e.g., se un carbonio ramifica in un ossigeno, l'ossigeno non ha altri legami a sua volta. In caso di ramificazione su più atomi, e.g., un carbonio con quattro idrogeni, gli atomi interessati sono indicati una di seguito all'altro, e.g., `C^-H-H-H&-H` o `C^-H-H-H&` per il metano.

#### Legami aromatici
Nel caso di composti aromatici, in cui gli atomi formano un anello aromatico, ogni atomo nell'anello è legato ad altri due atomi nell'anello. In FAME, gli atomi che fanno parte dell'anello sono indicati i) *in minuscolo*, e ii) tra parentesi quadre, assieme a eventuali legami con atomi esterni all'anello. Assumi che un atomo nell'anello può avere legami e/o ramificazioni. Inoltre, l'atomo di apertura e chiusura anello sono seguiti da indici che riportano il numero dell'anello all'interno della molecola. In caso di legami con ulteriori atomi esterni all'anello, e.g., idrogeni nel benzene:
- L'atomo nell'anello aromatico appare sempre in prima posizione, e.g., `[c-H]` è corretto, mentre `[H-c]` no.
- Un atomo nell'anello può avere *al più* un legame con un atomo al di fuori dell'anello. Se ne ha uno, l'atomo interessato *non* ha ulteriori legami. E.g., il caso `[c^-H&-H]` non è valido (oltre alla valenza non corretta per il carbonio), poiché `c` può avere al massimo un legame con un atomo esterno, i.e., nessuna ramificazione, mentre `[c-H]` è valido poiché `c` ha un solo legame esterno.
- Fa eccezione al punto precedente l'ultimo atomo nell'anello, che può avere legami con atomi esterni che portano ad altri legami, e.g., il bifenile, che ha due anelli `[c-H]1[c-H][c-H][c-H][c-H][c]1`. Questi sono quindi indicati con `[c-H]1[c-H][c-H][c-H][c-H][c]1-[c-H]2[c-H][c-H][c-H][c-H][c]2`

Poiché le molecole possono avere più anelli, il primo e ultimo atomo (o coppia (atomo, ramificazione)) dell'anello sono seguiti dall'indice dell'anello, e.g., nel benzene ($C_6 H_6$) il primo e l'ultimo `[cH]` sono seguiti da `1`, risultando in `[cH]1[cH][cH][cH][cH][cH]1`. Gli indici partono da `1` e sono incrementali. Considera che gli anelli **non sono** mai **innestati**, e ricorda che i legami aromatici hanno valenza di `1.5`, e che in un anello questa sale a `3.0` per natura stessa dell'anello.

---

# Traccia

## Parte A
*Gruppi da 1 a 3 studenti*

Scrivi una funzione che determina, dato un encoding FAME, se questo è valido o meno. Ossia, se i singoli caratteri della stringa siano tutti atomi o legami, se i legami sono possibili, i.e., i legami rispettano le valenze dei singoli atomi, e se ogni singolo atomo rispetta la sua valenza, e.g., ogni carbonio è in legami per un totale di valenza 4. In questa parte, non considerare i legami aromatici.

## Parte B
*Gruppi da 2 a 3 studenti*

Scrivi una funzione che, dati due encoding FAME, determina se le due molecole corrispondenti possono entrare in un legame covalente. Considera come possibili atomi che formano un legame, solo gli atomi nella "testa" e "coda" dell'encoding FAME, ossia il primo atomo di uno FAME, e l'ultimo atomo dell'altro.

**Esempi.**

- In `C^-H&#C`, l'ultimo carbonio ha solo un legame triplo con il primo carbonio, pertanto ha ora valenza `1`. Un semplice `H`, o un `O-H` offre esattamente valenza `1`
- In `C^-H-H&=O` sia testa che coda non possono formare ulteriori legami: non si può legare a nessun altra molecola.

## Parte C
*Gruppi da 3 studenti*

Integra i legami aromatici nella parte A e B.

</div>

<!--  -->

<div class="doi ui bottom attached tab segment" data-tab="marzo">
    

    Si utilizzi il testo progetto dell'appello di Gennaio.


    <b>Scadenza.</b> Martedi 3, ore 09:00.


</div>
    
<!--  -->
<div class="doi ui bottom attached tab segment" data-tab="aprile" markdown="1">


Nell'editing genetico, un genoma base viene modificato, aggiungendo delle sequenze predefinite, dette *insertions*, in determinati punti del genoma stesso, risultando in un *edit* del genoma. Tali inserimenti avvengono subito dopo degli specifici *insertion point*, ossia specifici punti del genoma identificati da una sequenza genetica. Un edit risulta in un unico inserimento: se un genoma presenta `> 1` insertion points, l'edit avviene solo sull'ultimo.

**Esempio.**
```python
genome = "ACCTGCAACTGC"
insertion_point = "CT"
insertion = "GGGTGGG"
```
L'edit avviene inserendo la insertion nell'ultimo insertion points, i.e., `"ACCTGCAACTGGGTGGGGC"`

Nelle seguenti, assumi un alfabeto genomico standard di basi "ACGT".

---

# Parte A
*Gruppi da 1, 2, e 3 studenti*

1. Scrivere una funzione che, dato un genoma di partenza, una insertion, e un insertion point, esegua l'edit del genoma.
2. Scrivere una funzione che, dato un genoma di partenza, `k` insertion, e `k` insertion point, esegua l'edit del genoma su tutte le insertion e insertion point. Se una insertion appare `m <= k` volte tra le `k` insertion, si hanno delle *repliche*:
   - Al primo edit viene inserita una volta
   - Al secondo edit viene inserita due volte
   - ...
   - Al m-esimo edit viene inserita `m` volte

**Esempio.**

```python

genome = "ACCGCAACGC"
insertion_points = ["CG", "GC", "AA", "TT"]
insertions = ["TT", "C", "TT", "GGG"]
```
Il primo inserimento (`"CG", "TT"`) risulta in
```python
"ACCGCAACGTTC"
#         ^ inserito 1 volta
```
Il secondo (`"GC", "C"`) risulta in
```python
"ACCGCCAACGTTC"
#     ^ inserito 1 volta
```
Il terzo (`"AA", "TT"`) risulta in un doppio inserimento di `"TT"`, perché appare per la seconda volta tra le insertion
```python
"ACCGCCAATTTTCGTTC"
#        ^ inserito 2 volte
```
Il quarto (`"TT", "GGG"`) risulta in
```python
"ACCGCCAATTTTCGTTGGGC"
#                ^ inserito 1 volta
```
Nota che gli edit sono consecutivi! Un singolo edit modifica il genoma, e potrebbe quindi creare nuovi insertion point che prima non esistevano.

# Parte B
*Gruppi da 2, e 3 studenti*

1. Scrivi una funzione che "annulli" un edit da un genoma dato, i.e., dato l'insertion point e l'insertion, la vada a rimuovere dal genoma. Assumi la stessa regola di inserimento, i.e., l'edit è avvenuto solo nell'ultimo insertion point valido. Rimuovi l'insertion una sola volta, senza considerare possibili repliche.
2. Scrivi una funzione che "annulli" una sequenza di `k` edit da un genoma dato, i.e., dati `k` insertion point e `k` insertion, le vada a rimuovere dal genoma. Considera repliche:
   - Alla prima occorrenza di una insertion nella lista di rimozione, tenta di rimuoverla una volta
   - Alla seconda occorrenza di una insertion nella lista di rimozione, tenta di rimuoverla due volte
   - ...
   - Alla `m`-esima occorrenza di una insertion nella lista di rimozione, tenta di rimuoverla `m` volte
   Considera possibili richieste non valide: insertion point non validi, o insertion non presenti. In questi casi, la rimozione termina direttamente senza tentare le rimozioni successive.

# Parte C
*Gruppi da 3 studenti*

Scrivi una funzione che dati `k` insertion, e `k` insertion point, li ordina per uno *score*. Lo score è dato da una mappa `BASE -> VALORE` che assegna un valore a ogni base. Lo score di un insertion è la media del `VALORE` di ogni base che la compone.
	
	
</div>
    
<!--  -->
<div class="doi ui bottom attached tab segment" data-tab="maggio">
    <div class="ui placeholder">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
    </div>
</div>
    
<!--  -->
<div class="doi ui bottom attached tab segment" data-tab="giugno" markdown="1">



**Consegna**: 10 giugno, ore 10:15.

Leggi con **massima attenzione** le linee guida prima di iniziare.

# Contesto

In chemioinformatica, le molecole sono spesso modellate e rappresentate con stringhe che seguono precise regole di *encoding*. L'encoding definisce come una molecola, e.g., l'acetofenone, viene trascritta in una stringa, similmente a quanto accade per le formule molecolari. In questo progetto, lavoreremo sulla verifica di un encoding particolare: *FAME*.

### Atomi
All'interno delle stringhe FAME, gli atomi sono indicati con il loro simbolo atomico standard, rigorosamente in maiuscolo, e.g., `C` per l'atomo di carbonio. FAME rappresenta unicamente molecole con atomi di carbonio (`C`), azoto (`N`), ossigeno (`O`), idrogeno (`H`), fluoro (`F`), o zolfo (`S`), in una qualsiasi combinazione. A ogni atomo associamo una *valenza*, definita come il numero di elettroni aggiuntivi che garantisce stabilità. E.g., il carbonio ha valenza `4` poiché per essere stabile deve avere `4` elettroni in condivisione da altri atomi. Pertanto, stringhe FAME in cui il carbonio non ha legami che gli garantiscono valenza `4` modellano molecole non valide. In FAME, consideriamo unicamente semplici legami covalenti in cui gli atomi sono condivisi.
Nelle stringhe FAME, **due atomi che sono oggetto di un legame**, e.g., idrogeno e ossigeno nell'acqua, **si trovano uno di seguito all'altro**, e sono **inframezzati da** dei simboli che rappresentano il **legame** covalente che intercorre, e.g., legame covalente singolo, doppio, o triplo. 

**Esempi.** Utilizziamo `{LEGAME X}` per indicare un legame covalente su `X` elettroni. 
- $H_2O$ con FAME`H{LEGAME SINGOLO}O{LEGAME SINGOLO}H`
-  $C_2 H_2$ con FAME `H{LEGAME SINGOLO}C{LEGAME TRIPLO}C{LEGAME SINGOLO}H`.
-  $C_2 H_2$ con FAME `H{LEGAME SINGOLO}H{LEGAME SINGOLO}C{LEGAME TRIPLO}C` è un esempio non corretto: implica che il secondo idrogeno ha due legami singoli, uno con il primo idrogeno e uno con il primo carbonio, e che il secondo carbonio ha solo un legame triplo. Pertanto il secondo idrogeno viola la valenza, cosi' come il secondo carbonio.

### Legami
FAME modella i legami covalenti, e ne inserisce un encoding tra gli atomi in legame secondo la seguente tabella.

| Encoding | Legame           | Valenza | Info                                                                                                                   | Esempio                            |
| -------- | ---------------- | ------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `-`      | Legame singolo   | `1`     | Opzionale                                                                                                              | $H_2 O$ con `H-O-H`                |
| `^...&`  | Ramificazione    |         | Le ramificazioni iniziano con un `^` e terminano con un `&`, e gli atomi in cui si ramifica non hanno ulteriori legami | `C^-H&-H`, `O^-H&-H`, `O^-H-H&`    |
| `=`      | Legame doppio    | `2`     |                                                                                                                        | `C^=O=O&`                          |
| `#`      | Legame triplo    | `3`     |                                                                                                                        | `H-C#C-H`                          |
|          | Legame aromatico | `1.5`   | Atomi con lettere minuscole, apertura e chiusura anello con numeri. Ogni blocco tra quadre.                            | `[c-H]1[c-H][c-H][c-H][c-H][c-H]1` |

**Nota.** Assumi che i singoli legami siano sempre validi per difetto, i.e., che in una stringa FAME un atomo con valenza `X` abbia legami con valenza `Y <= X`, e.g., un ossigeno può avere legami singoli o doppi, ma non tripli.

#### Ramificazioni
Le ramificazioni arricchiscono FAME, permettendo di modellare molecole in cui un singolo atomo è oggetto di più legami, e.g., un carbonio con quattro idrogeni. In FAME, le ramificazioni iniziano con un `^`, terminano con un `&`, e riportano `>= 1` legami. Se un atomo ha ramificazioni, queste lo seguono *immediatamente* nella stringa FAME. I.e., in `H-C-O^-H&`, la ramificazione `^-H&` va interpretata come ramificazione dell'ossigeno.

Gli atomi all'interno della ramificazione **non** hanno legami tra loro, né con altri atomi, e.g., se un carbonio ramifica in un ossigeno, l'ossigeno non ha altri legami a sua volta. In caso di ramificazione su più atomi, e.g., un carbonio con quattro idrogeni, gli atomi interessati sono indicati una di seguito all'altro, e.g., `C^-H-H-H&-H` o `C^-H-H-H&` per il metano.

#### Legami aromatici
Nel caso di composti aromatici, in cui gli atomi formano un anello aromatico, ogni atomo nell'anello è legato ad altri due atomi nell'anello. In FAME, gli atomi che fanno parte dell'anello sono indicati i) *in minuscolo*, e ii) tra parentesi quadre, assieme a eventuali legami con atomi esterni all'anello. Assumi che un atomo nell'anello può avere legami e/o ramificazioni. Inoltre, l'atomo di apertura e chiusura anello sono seguiti da indici che riportano il numero dell'anello all'interno della molecola. In caso di legami con ulteriori atomi esterni all'anello, e.g., idrogeni nel benzene:
- L'atomo nell'anello aromatico appare sempre in prima posizione, e.g., `[c-H]` è corretto, mentre `[H-c]` no.
- Un atomo nell'anello può avere *al più* un legame con un atomo al di fuori dell'anello. Se ne ha uno, l'atomo interessato *non* ha ulteriori legami. E.g., il caso `[c^-H&-H]` non è valido (oltre alla valenza non corretta per il carbonio), poiché `c` può avere al massimo un legame con un atomo esterno, i.e., nessuna ramificazione, mentre `[c-H]` è valido poiché `c` ha un solo legame esterno.
- Fa eccezione al punto precedente l'ultimo atomo nell'anello, che può avere legami con atomi esterni che portano ad altri legami, e.g., il bifenile, che ha due anelli `[c-H]1[c-H][c-H][c-H][c-H][c]1`. Questi sono quindi indicati con `[c-H]1[c-H][c-H][c-H][c-H][c]1-[c-H]2[c-H][c-H][c-H][c-H][c]2`

Poiché le molecole possono avere più anelli, il primo e ultimo atomo (o coppia (atomo, ramificazione)) dell'anello sono seguiti dall'indice dell'anello, e.g., nel benzene ($C_6 H_6$) il primo e l'ultimo `[cH]` sono seguiti da `1`, risultando in `[cH]1[cH][cH][cH][cH][cH]1`. Gli indici partono da `1` e sono incrementali. Considera che gli anelli **non sono** mai **innestati**, e ricorda che i legami aromatici hanno valenza di `1.5`, e che in un anello questa sale a `3.0` per natura stessa dell'anello.

---

# Traccia

## Parte A
*Gruppi da 1 a 3 studenti*

Scrivi una funzione che determina, dato un encoding FAME, se questo è valido o meno. Ossia, se i singoli caratteri della stringa siano tutti atomi o legami, se i legami sono possibili, i.e., i legami rispettano le valenze dei singoli atomi, e se ogni singolo atomo rispetta la sua valenza, e.g., ogni carbonio è in legami per un totale di valenza 4. In questa parte, non considerare i legami aromatici.

## Parte B
*Gruppi da 2 a 3 studenti*

Scrivi una funzione che, dati due encoding FAME, determina se le due molecole corrispondenti possono entrare in un legame covalente. Considera come possibili atomi che formano un legame, solo gli atomi nella "testa" e "coda" dell'encoding FAME, ossia il primo atomo di uno FAME, e l'ultimo atomo dell'altro.

**Esempi.**

- In `C^-H&#C`, l'ultimo carbonio ha solo un legame triplo con il primo carbonio, pertanto ha ora valenza `1`. Un semplice `H`, o un `O-H` offre esattamente valenza `1`
- In `C^-H-H&=O` sia testa che coda non possono formare ulteriori legami: non si può legare a nessun altra molecola.

## Parte C
*Gruppi da 3 studenti*

Integra i legami aromatici nella parte A e B.	
	
</div>

	
<!--  -->


<div class="doi ui bottom attached tab segment active" data-tab="luglio" markdown="1">
    
**Consegna**: 10 luglio, ore 10:00.
Leggi con **massima attenzione** le linee guida prima di iniziare.

	
	<div class="ui placeholder">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
    </div>

	
</div>

	
<!--  -->
<div class="doi ui bottom attached tab segment" data-tab="settembre">
    <div class="ui placeholder">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
    </div>
</div>
    
