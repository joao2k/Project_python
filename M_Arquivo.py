import csv
def ler_CSV(caminho):
    try:
        lista = []
        with open(caminho, encoding="utf-8", errors='ignore') as f:
            linhas = csv.reader(f, delimiter=';')
            for linha in linhas:
                lista.append(linha)
            return lista
        f.close()
    except FileNotFoundError:

        return 'ERRO'


def gerar_alteracao(alterado):
    with open("mudanças.txt", mode='a') as f:
        f.write(alterado + '\n')







