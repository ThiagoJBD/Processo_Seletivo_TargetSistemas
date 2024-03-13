def inverte_string(texto):
  lista_texto = list(texto)
  i = 0
  j = len(lista_texto) -1
  while i < j:
    aux = lista_texto[i]
    lista_texto[i] = lista_texto[j]
    lista_texto[j] = aux
    i += 1
    j -= 1
  return ''.join(lista_texto)

def main():
  texto = input("Digite um texto: \n")
  print(inverte_string(texto))
  
if __name__ == "__main__":
  main()
