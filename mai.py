class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def visualizar_site(self):
        print(f"{self.nome} está visualizando o site.")


class Administracao(Usuario):
    def __init__(self, nome):
        super().__init__(nome)

    def modificar_informacoes(self, evento):
        print(f"{self.nome} modificou as informações do evento: {evento}")


contas_administradores = {}
contas_usuarios = {}


def cadastrar_administrador():
    nome_usuario = input("Digite um nome de usuário para criar uma conta de administrador: ")
    if nome_usuario in contas_administradores or nome_usuario in contas_usuarios:
        print("Nome de usuário já existe. Por favor, escolha outro.")
        return
    senha = input("Digite uma senha para sua conta de administrador: ")
    contas_administradores[nome_usuario] = senha
    print("Conta de administrador criada com sucesso!")


def cadastrar_usuario():
    nome_usuario = input("Digite um nome de usuário para criar uma conta de usuário: ")
    if nome_usuario in contas_administradores or nome_usuario in contas_usuarios:
        print("Nome de usuário já existe. Por favor, escolha outro.")
        return
    senha = input("Digite uma senha para sua conta de usuário: ")
    contas_usuarios[nome_usuario] = senha
    print("Conta de usuário criada com sucesso!")


def login_administrador():
    nome_usuario = input("Digite seu nome de usuário de administrador: ")
    senha = input("Digite sua senha de administrador: ")
    if nome_usuario in contas_administradores and contas_administradores[nome_usuario] == senha:
        print("Login bem-sucedido! Você é um administrador.")
        return Administracao(nome_usuario)
    else:
        print("Nome de usuário ou senha de administrador incorretos.")
        return None


def login_usuario():
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if nome_usuario in contas_usuarios and contas_usuarios[nome_usuario] == senha:
        print("Login bem-sucedido! Você é um usuário comum.")
        return Usuario(nome_usuario)
    else:
        print("Nome de usuário ou senha incorretos.")
        return None


def esqueceu_senha():
    nome_usuario = input("Digite seu nome de usuário: ")
    if nome_usuario in contas_administradores:
        print("Não é possível recuperar a senha de uma conta de administrador.")
    elif nome_usuario in contas_usuarios:
        nova_senha = input("Digite uma nova senha: ")
        contas_usuarios[nome_usuario] = nova_senha
        print("Senha alterada com sucesso!")
    else:
        print("Nome de usuário não encontrado.")


# Exemplo de uso
if __name__ == "__main__":
    while True:
        opcao = input("DESEJA FAZER O CADRASTO DE QUAL USUARIO:\n1. Criar conta de administrador\n2. Criar conta de usuário\n3. Fazer login como administrador\n4. Fazer login como usuário\n5. Esqueceu a senha\n6. Sair\n")
        if opcao == "1":
            cadastrar_administrador()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            usuario = login_administrador()
            if usuario:
                usuario.modificar_informacoes("Festa de encerramento")
                break
        elif opcao == "4":
            usuario = login_usuario()
            if usuario:
                usuario.visualizar_site()
                break
        elif opcao == "5":
            esqueceu_senha()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

