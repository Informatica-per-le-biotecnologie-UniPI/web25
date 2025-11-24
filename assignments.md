---
layout: assignments
title: Esercitazioni
permalink: /esercitazioni/
---

Le esercitazioni accompagnano passo passo l'apprendimento della programmazione.
È **fortemente consigliato** lavorarci durante le esercitazioni in aula, da soli o con il proprio gruppo di studio, e sfruttare ricevimenti in caso di dubbi.

---

Per mostrare un risultato, usa `print()`.

## Valori, tipi, ed espressioni

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

# 4
Una *maschera* (mask) è una sequenza booleana che filtra gli elementi di una sequenza. Se l'`i`-esimo elemento della maschera é vero, allora l'elemento viene selezionato, altrimenti viene scartato.

1. Costruisci una maschera di una lunghezza arbitraria
2. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri selezionati dalla maschera
3. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, stampa tutti i caratteri scartati dalla maschera
4. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri selezionati dalla maschera. Considera scartati tutti gli elementi in eccesso
5. Data una sequenza, e.g., una stringa, di lunghezza inferiore della maschera, stampa tutti i caratteri scartati dalla maschera. Considera scartati tutti gli elementi in eccesso
6. Data una sequenza, e.g., una stringa, della stessa lunghezza della maschera, somma tutti gli elementi selezionati dalla maschera
