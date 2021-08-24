import os

def app():
  listadeexecucao = [
    "python src/Testes/testesemotimizacao.py > Anexo/relatorio-Recursivo-sem-otimização.txt",
    "python src/Testes/testeadsemmotimizacao.py > Anexo/relatorio-Algoritmo-Dinamico-sem-otimização.txt",
    "python src/Testes/testesemotimizacao.py > Anexo/relatorio-Recursivo-com-otimização.txt",
    "python src/Testes/testeadsemmotimizacao.py > Anexo/relatorio-Algoritmo-Dinamico-com-otimização.txt"
  ]

  for ex in listadeexecucao:
    os.system(ex)

if __name__ == '__main__':
  app()