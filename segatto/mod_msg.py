import pyfiglet

def msg_inicial():
    print("Seja bem vindo ao Sistema\n")
    mensagem = pyfiglet.figlet_format("COTA-FRETE", font="pagga")
    print(mensagem)

def msg_login_ini():
    print("##############################")
    print("<<<<<< LOGAR NO SISTEMA >>>>>>")
    print("##############################\n")

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | CALCULADORA - 1 | CALCULA FRETE - 2 #####\n")

def msg_calc_ini():
    print("#############################")
    print("<<<<<<<< CALCULADORA >>>>>>>>")
    print("#############################\n")

def msg_cotacao():
    print("""
    ==========================================
            COTAÇÃO FRETE
    ==========================================
    """)
    print("Aéroportos disponíveis")
    print("1 - Congonhas - SP")
    print("2 - Guarulhos - SP")
    print("3 - Compo de marte - SP")
    print("4 - Pinto Martins - CE")
    print("5 - Eduardo gomes - AM")

def msg_embalagem():
    print("""
        =====================================
                        EMBALAGEM           
        =====================================
        """)
    
    print(" 1 - Embalagem de papelão")
    print(" 2 - Embalagem Container")

def msg_final_programa():
    print("""
    =================================== SISTEMA ENCERRADO COM SUCESSO===================================

    Obrigado por utilizar nosso sistema!

    Esperamos que as ferramentas de cotação de frete e cálculo de processamento tenham facilitado suas atividades.

    Até a próxima!

    Obrigado pela preferência!
    """)

def msg_menu_principal():
    print("##########################################################")
    print("<<<<<<<<<<<<<<<<<<<< MENU PRINCIPAL >>>>>>>>>>>>>>>>>>>>>>")
    print("##########################################################\n")
    print("##### SAIR - 0 | PAPELÃO- 1 | CONTAINER - 2 #####\n")