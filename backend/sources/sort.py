
def mergesort_notas(lista_notas):
    
    if len(lista_notas) <= 1:
        return lista_notas

    mid = len(lista_notas) // 2
    left = mergesort_notas(lista_notas[:mid])
    right = mergesort_notas(lista_notas[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if float(left[i]['valor_nota']) > float(right[j]['valor_nota']):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged