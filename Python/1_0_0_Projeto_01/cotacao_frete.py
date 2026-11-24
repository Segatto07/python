import mod_msg
import mod_inputs


def recebe_destino():
    while True:
        mod_msg.msg_cotacao()
        destino = mod_inputs.recebe_int("Digite uma opção!")
        if destino == 0:
            break
        elif destino == 1:         
            aeroporto = "Congonhas-SP"
            distancia = "102 KM"

        elif destino == 2:
            aeroporto = "Guarulhos-SP"
            distancia = "112 KM"

        elif destino == 3:
            aeroporto = "Campo de Marte-SP"
            distancia = "98 KM"

        elif destino == 4:
            aeroporto = "Pinto Martins-CE"
            distancia = "2922 KM"

        elif destino == 5:
            aeroporto = "Eduardo Gomes-AM"
            distancia = "6294 KM"

        else:
            print("Opção inválida\n")
    return destino

def escolhe_aeroporto(opcao):
    aeroporto = ["Congonhas - SP", "Guarulhos - SP", "Campo de Marte - SP", "Pinto Martins - CE", "Eduardo Gomes - AM"]
    return aeroporto[opcao-1]

def escolhe_distancia(opcao):
    distancia = ["102, 112, 98, 2922, 6294"]
    return distancia[opcao-1]

def main():
    while True:
        opcao = recebe_destino()
        if opcao != 0:
            aeroporto = escolhe_aeroporto(opcao)
            distancia = escolhe_distancia(opcao)

        else:
            break
 # aqui eu devo criar um opcao que vai tratar se a embalagem vai ser 1 ou 2.   
def recebe_embalagem():
    while True:
        mod_msg.msg_embalagem()
        embalagem = mod_inputs.recebe_str("selecione o tipo de embalagem! ")
        match mod_inputs.recebe_str:
            case 1:
                opcao = "Embalagem de papelão"
            case 2:
                "Embalagem container"
            case _:
                print("Opção inválida!\n")
                break
    return embalagem
# recebo a opcao da embalagem tratada e dps definar a embalagem
def escolher_embalagem():
    aembalagem = ["Embalagem de papelão", "Embalagem Container"]
    return aembalagem[opcao]

def 
