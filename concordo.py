def main ():
    resposta = input("Você concorda? ").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "ss":
        print("Eu concordo")
    elif resposta == "não" or resposta == "n":
        print("Eu não concordo")

main()