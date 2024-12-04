def main():
    tamanho = int(input("Qual é o tamanho dos blocos: "))
    bloco(tamanho)

def bloco(tamanho):
    bloco = ("🟩" * tamanho)
    print (f"{bloco}\n" * tamanho, end = '')
           
main()