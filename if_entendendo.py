def funcao_if():
  categoria = int(input("Digite a categoria do produto: "))
  if categoria == 1:
    preco = 10
  elif categoria == 2:
    preco = 20
  elif categoria == 3:
    preco = 30
  elif categoria == 4:
    preco = 40
  else:
    preco = 50
  print(f"Preco = {preco}")