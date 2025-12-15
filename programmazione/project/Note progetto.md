# Concetti
## Ratto
- Genoma
- Fertilita'
- Riproduzione

**Genoma.**
Vincoli: 
- basi canoniche
- lunghezza > 30, multiplo di 3
**Riproduzione.**
- k figli, dati da
	- fattori ambientali #todo
	- fertilita' genitori
- genoma di base randomico, poi con dei tratti in aggiunta, e poi aggiungo mutazioni randomiche 

| Concetto     | Implementazione                                                                                    |
| ------------ | -------------------------------------------------------------------------------------------------- |
| Ratto        | Classe                                                                                             |
| Genoma       | str                                                                                                |
| Fertilita'   | float                                                                                              |
| Tratti       | Tratto                                                                                             |
| Riproduzione | Funzione/Metodo: parametri fattori ambientali, fertilita' genitori, tipo di ritorno lista di ratti |

## Tratto
- lunghezza, e.g., 1
- punto di inizio, e.g., 1
- valori, e.g., "A" = "blu", "C" = "verde", ...
- indice di dominanza
- scelta del tratto tra due tratti dati: se entrambi sono distrutti, allora distrutto, altrimenti scelta proporzionale

| Concetto            | Implementazione                                                 |
| ------------------- | --------------------------------------------------------------- |
| Tratto              | Classe                                                          |
| lunghezza           | int                                                             |
| punto di inizio     | int                                                             |
| valori              | dizionario                                                      |
| indici di dominanza | dizionario                                                      |
| scelta tratto       | metodo/funzione: parametri tratti dati, tipo di ritorno: tratto |


