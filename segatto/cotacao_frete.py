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
    aeroporto = [
        "Congonhas - SP",
        "Guarulhos - SP",
        "Campo de Marte - SP",
        "Pinto Martins - CE",
        "Eduardo Gomes - AM",
    ]
    return aeroporto[opcao-1]

def escolhe_distancia(opcao):
    distancia = [102, 112, 98, 2922, 6294]
    return distancia[opcao-1]

def recebe_embalagem():
    while True:
        mod_msg.msg_embalagem()
        tipo = mod_inputs.recebe_int("Escolha uma embalagem: ")
        if tipo in(1, 2):
            break
        else:
            print("Opção inválida!")
    return tipo
            
def tipo_emb(tipo_embalagem):
    match tipo_embalagem:
        case 1:
            embalagem = "Caixa de Papelão"
        case 2:
            embalagem = "Caixa Container"
    return embalagem

def Calcula_frete(distancia, tipo_embalagem):

    if tipo_embalagem == 1:

        print("\nEmbalagem Caixa de Papelão")

        y = mod_inputs.recebe_float("Digite a altura em metros: ") 
        x = mod_inputs.recebe_float("Digite a largura em metros: ")  
        z = mod_inputs.recebe_float("Digite a profundidade em metros: ")
        w = mod_inputs.recebe_float("Digite o peso em Kg: ")

        f = 0.26

    elif tipo_embalagem == 2:

        print("\nEmbalagem Container")

        y = mod_inputs.recebe_float("Digite a altura em centímetros: ")
        x = mod_inputs.recebe_float("Digite a largura em centímetros: ")
        z = mod_inputs.recebe_float("Digite a profundidade em centímetros: ")
        w = mod_inputs.recebe_float("Digite o peso em Kg: ")
        f = 0.37

    formula = ((y* x * z * w) * (1 + f) * (1+(distancia * 9.8)))

    return round( formula, 2)
 # aqui eu devo criar um opcao que vai tratar se a embalagem vai ser 1 ou 2.   

def main():
    while True:
        opcao = recebe_destino()
        if opcao == 0:
            break

        aeroporto = escolhe_aeroporto(opcao)
        distancia = escolhe_distancia(opcao)
        tipo = recebe_embalagem()
        embalagem = tipo_emb(tipo)
        frete = Calcula_frete(distancia, tipo)

        print("O aeroporto é ", aeroporto)
        print("A distancia é ", distancia, "Km")
        print("A embalagem escolhida é ", embalagem)
        print("O valor do frete é $ ", frete)


if __name__ == "__main__":
    main()