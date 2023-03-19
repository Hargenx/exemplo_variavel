import time
from datetime import date


def tempo():
  x = time.time()
  print(f'Local time: {time.ctime(x)}')
  data_atual = date.today()
  print(data_atual)
  data_formatada = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
  print(data_formatada)
  data_atual2 = data_atual.strftime('%d/%m/%Y')
  print(data_atual2)