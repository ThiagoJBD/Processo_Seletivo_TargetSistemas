def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
          sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def presente(num):
  sequencia = fibonacci(num)
  if num in sequencia:
    return True
  else:
    return False

def main():
    numero = int(input("Digite um número para iniciar:\n"))
    
    if presente(numero):
      print("O número está presente na sequência de Fibonacci")
    else:
      print("O número não está presente na sequência de Fibonacci")
      
if __name__ == "__main__" :
  main()
