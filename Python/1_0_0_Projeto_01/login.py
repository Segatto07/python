import mod_msg
import mod_inputs

USUARIO = "Gabriel"
SENHA = "951753"

def valida_usuario(user):
    while True:
        usuario = mod_inputs.racebe_str(" Informe o seu usuário: ")
        if len(usuario) >= 5:
            if USUARIO == usuario:
                break
            else:
                print("Usuário incorreto. Tente novamente! \n")
        else:
            print("O usuário deve ter pelo menos 5 caracteres!")

    return  user

def valida_senha(senha1):
    while True:
        senha = mod_inputs.receber_senha("Digite sua senha! ")
        if senha1 == senha:
            break
        else:
            print("Senha incorreta! ")
    return senha1

def main():
    mod_msg.msg_login_ini()
    usuario_validado = valida_usuario(USUARIO) 
    senha_validada = valida_senha(SENHA) 

    print("Seu usuário é: ", usuario_validado)
    print("Sua senha é: ", senha_validada)