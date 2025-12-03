---
layout: assignments
title: Esercitazioni
permalink: /esercitazioni/
---

Le esercitazioni accompagnano passo passo l'apprendimento della programmazione.
È **fortemente consigliato** lavorarci durante le esercitazioni in aula, da soli o con il proprio gruppo di studio, e sfruttare ricevimenti in caso di dubbi.

---

Per mostrare un risultato, usa `print()`.

# 1
Dato un genoma di lunghezza arbitraria...
1. Estrai il codone (tre caratteri) iniziale
2. Estrai il codone (tre caratteri) finale

# 2
L'espressione
```python
var = 10
f"{var}"
```
viene detta `f-string` (stringa formattata), e valuta a `"10"`: in una stringa preceduta da `f`, le espressioni tra `{ }` vengono valutate, e se son stringhe (o possono essere valutate come tali), inserite nella stringa.

1. Dati i) un codone iniziale, ii) un codone finale, e iii) una sequenza intermedia, crea una f-string che le concateni
2. Dati i) un codone iniziale, ii) un codone finale, e iii) una sequenza intermedia, crea una stringa che le concateni, ma senza usare una f-string
3. Scrivi un'espressione che verifichi che le stringhe date dal punto `1.` e `2.` siano uguali

# 3
4. L'espressione `"ACGT'` contiene un errore?
5. L'espressione `'"ACGT"'` contiene un errore?
6. L'espressione `'"ACGT"'` contiene un errore?
7. L'espressione `'"0" + 1` contiene un errore?
8. L'espressione `'"0" + "1"` contiene un errore?
9. L'espressione `'"0" + "1" == 1` contiene un errore?

# 4
Data una collezione di numeri...
1. Trova i valori massimi
2. Trova i valori minimi
3. Ripeti `1.`, ma se ritrovi lo stesso valore massimo, stampalo ogni volta che lo trovi
4. Ripeti `2.`, ma se ritrovi lo stesso valore minimo, stampalo ogni volta che lo trovi
5. Ripeti `1.`, in questo caso la collezione è una lista: accedi agli elementi usando l'operatore `[]`
6. Verifica che un elemento dato sia nella collezione
7. Verifica che due elementi dati siano entrambi nella collezione
8. Verifica che uno di due elementi dati sia nella collezione, e l'altro no
9. E un'altra collezione di numeri, verifica che tutti gli elementi della seconda siano nella prima
10. E un'altra collezione di numeri della stessa lunghezza, conta il numero di caratteri uguali (posizione per posizione)

# 5
Una *maschera* (mask) è una sequenza booleana che filtra gli elementi di una sequenza. Se l'`i`-esimo elemento della maschera é vero, allora l'elemento viene selezionato, altrimenti viene scartato.

1. Costruisci una maschera di una lunghezza arbitraria
2. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri selezionati dalla maschera
3. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri scartati dalla maschera
4. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri selezionati dalla maschera. Considera scartati tutti gli elementi in eccesso
5. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri scartati dalla maschera. Considera scartati tutti gli elementi in eccesso
6. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, somma tutti gli elementi selezionati dalla maschera

# 6
Sono date `n` stringhe (seleziona `n` a piacere) di una data lunghezza `m`.
1. Per ogni posizione `i` in `[0, m - 1]`, stampa tutti i caratteri che appaiono in posizione `i`
2. Per ogni posizione `i` in `[0, m - 1]`, stampa il carattere più frequente in posizione `i`
3. Con `n == 2`, verifica che le due stringhe siano palindrome

---

# Dna to Protein

Scrivere un programma che, data una stringa di DNA, la traduce nella catena di amminoacidi corrispondente. Il programma
1. Traduce il DNA in RNA
2. Traduce l'RNA in una sequenza di amminoacidi

Per semplicità, considera solo un sottoinsieme di amminoacidi. Considera inoltre di dover incorporare alcuni vincoli:

- Il DNA deve avere una lunghezza appropriata
- Esistono un codone iniziale e uno finale che non codificano amminoacidi


---

# Motifs

Data una stringa di DNA, un *motif* rappresenta una sottosequenza frequente, ossia che appare spesso nel DNA. Scrivi un programma che, data una lunghezza, cerca tutti i motif candidati, ne calcola la frequenza, e li restituisce ordinati per frequenza.

---

# Posting lists
Una posting list associa, ad ogni elemento, le posizioni in cui appare in una sequenza. Creare una funzione che crea la posting list di una data stringa.

Esempio.
```
ACGAGGTAC
```
Ha una posting list
```
A: [0, 3, 7]
C: [1, 8]
G: [2, 4, 5]
T: [6]
```


Si crei una funzione per verificare se una stringa `a*b` appare nella sequenza.
`a*b` indica una stringa in cui appare `a`, seguita da un numero arbitrario di caratteri, seguita da `b`.
Si sfrutti la costruzione della posting list.

Esempio.


| `a` | `b` | Appare? |
| --- | --- | ------- |
| `A` | `C` | Si      |
| `A` | `T` | Si      |
| `T` | `C` | Si      |
| `T` | `X` | No      |
| `T` | `G` | No      |


## Posting list 1
Si crei una funzione per verificare se una stringa `a*b*c` appare nella sequenza.

## Posting list 2
Si crei una funzione per verificare se una stringa `(a)+` appare nella sequenza. `(a)+` indica una stringa in cui la stringa `a` appare *almeno* una volta.

## Posting list 3
Si crei una funzione per verificare se una stringa `(a){m,n}` appare nella sequenza. `(a){m,n}` indica una stringa in cui la stringa `a` appare tra `m` e `n` volte. I parametri sono opzionali.

---

# Automata

Un linguaggio regolare implementa un automa, un oggetto matematico che descrive un sistema a stati in cui il sistema è in uno di diversi possibili stati `Si`. Di questi, uno è detto stato iniziale (da cui parte il sistema), e un insieme è detto stato finale (in cui il sistema termina). Il sistema funziona come un *riconoscitore di linguaggi*: elemento per elemento, il sistema consuma una stringa data, e se alla fine si trova in uno stato finale, il sistema *riconosce* il linguaggio, e in caso contrario, no.

Il sistema descrive un insieme di regole di transizione che, partendo dallo stato iniziale, lo fanno passare da uno stato `Si` a uno `Sj`. Ogni passaggio è dato da uno stato di origine, un simbolo, e uno stato di destinazione.

**Esempio.** 

![automaton](https://upload.wikimedia.org/wikipedia/commons/9/9d/DFAexample.svg)

*Un automa con due stati `S1` e `S2`, e le transizioni, definite come archi. Lo stato iniziale viene indicato dalla freccia, e quelli finali da un doppio cerchio.*

Stati del sistema.
```
S = {S1, S2}
```

Transizioni del sistema.

| Sorgente | Simbolo | Destinazione |
| -------- | ------- | ------------ |
| `S1`     | `0`     | `S2`         |
| `S1`     | `1`     | `S1`         |
| `S2`     | `0`     | `S1`         |
| `S2`     | `1`     | `S2`         |

Alcune stringhe accettate (prova partendo da `S1` a seguire gli archi dettati dai simboli: finirai in uno stato finale!)
```
- (stringa vuota)
1
11
111
1111
...
00
0000
000000
010
0110
01110
011110
...
```

**Traccia.** Data una stringa $s$ e un automa $a$, una traccia $T_s^a$ indica la sequenza di stati di $a$ utili a verificare $s$.
E.g., per $s = 0110$ nell'esempio precedente, $T^a_{s} = S_{1}, S_{2}, S_{2}, S_{1}$.

## Automaton 0: Trace

Arricchisci le classi definite nel blocco precedente, aggiungendo un calcolo traccia dove possibile, e.g., nella verifica di una stringa.

## Automaton 1: Non-deterministic automata
Una famiglia di automi è detta *non-deterministica* se nel suo insieme di transizioni esistono due transizioni $S_{i} \xrightarrow{\sigma} S_{j}, S_{i} \xrightarrow{\sigma} S_{k}$ con $S_{j} \neq S_{k}$.
Ossia, se esiste uno stato sorgente in cui possiamo raggiungere due stati destinazione diversi con uno stesso simbolo: un bivio senza indicazioni e che porta a destinazioni diverse.

Implementa la verifica di una stringa su automi non deterministici.
Se ritieni necessario, estendi il tuo sistema di classi.