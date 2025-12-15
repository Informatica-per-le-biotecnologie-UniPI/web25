def apply_mask(collection: list, mask: list):
    """Applica la maschera mask a collection, restituendone i valori selezionati."""
    return [collection[mask_filter] for mask_filter in mask if mask_filter]

def apply_negated_mask(collection: list, mask: list):
    """Applica la maschera mask a collection, restituendone i valori *non* selezionati."""
    return [collection[mask_filter] for mask_filter in mask if not mask_filter]

def sum_mask(collection: list, mask: list) -> float:
    """Somma tutti i valori selezionati dalla maschera."""
    return sum(apply_mask(collection, mask))

