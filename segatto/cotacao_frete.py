import mod_msg
import mod_inputs

def recebe_destino():
    while True:
        mod_msg.msg_cotacao()
        opcao = mod_inputs.recebe_int("Escolha uma opção! ")
        if opcao in(0, 1, 2, 3, 4, 5):
            break
        else: 
            print("Opção inválida")
    return opcao
    
def escolhe_aeroporto(opcao):
    aeroporto = ["Congonhas - SP", "Guarulhos - SP", "Campo de Marte - SP", "Pinto Martins - CE", "Eduardo Gomes - AM"]
    return aeroporto[opcao-1]

def escolhe_distancia(opcao):
    distancia = [102, 112, 98, 2922, 6294]
    return distancia[opcao-1]

def recebe_embalagem():
    while True:
        mod_msg.msg_embalagem()
        tipo = mod_inputs.recebe_int("Escolha uma embalagem")
        if tipo in(0, 1, 2):
            break
        else:
            print("Opção inválida!")
        return tipo
            
def escolhe_embalagem(opcao):
    embalagem =["Embalagem de Papelão", "Embalagem Container"]
    return embalagem[opcao-1]

 # aqui eu devo criar um opcao que vai tratar se a embalagem vai ser 1 ou 2.   

def main():
    while True:
        opcao = recebe_destino()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)

            embalagem_opcao = recebe_embalagem()
            embalagem = escolhe_embalagem(embalagem_opcao)

            print("O aeroporto é ", aeroporto)
            print("A distancia é ", distancia)
            print("A embalagem escolhida é ", embalagem)

        else:
            break


if __name__ == "__main__":
    main()

def escolhe_formula():

    aembalagem = recebe_embalagem()
    if aembalagem == "Enbalagem papelão":

        print("\nEmbalagem Caixa de Papelão")

        y = mod_inputs.recebe_float("Digite a altura em metros: ")
        x = mod_inputs.recebe_float("Digite a largura em metros: ")
        z = mod_inputs.recebe_float("Digite a profundidade em metros: ")
        w = mod_inputs.recebe_float("Digite o peso em Kg: ")

        f = 0.26

    elif aembalagem == "container":

        print("\nEmbalagem Container")

        y = mod_inputs.recebe_float("Digite a altura em centímetros: ")
        x = mod_inputs.recebe_float("Digite a largura em centímetros: ")
        z = mod_inputs.recebe_float("Digite a profundidade em centímetros: ")
        w = mod_inputs.recebe_float("Digite o peso em Kg: ")

        f = 0.37

    return y, x, z, w, f