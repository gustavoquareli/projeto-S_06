from src import data_manipulation as dm
import sys
from a import teste01
from b import teste02


if __name__ == '__main__':
    print("Iniciando a execução")

    teste01.teste_arquivo_01()
    teste02.teste_arquivo_02()

print("Fim da execução")


sys.path.append('../')
