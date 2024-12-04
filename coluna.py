def main():
    coluna(numero())

def coluna(colunaa):
    print("🟩\n" * colunaa, end="")


def numero():
    while True:
        coluna = int(input("Quantas colunas você quer?"))
        if coluna > 0:
                return coluna

main()