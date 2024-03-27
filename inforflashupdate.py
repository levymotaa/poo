class Usuario:
    def __init__(self, name=None, matricula=None, password=None):
        self.nome = name
        self.mat = matricula
        self.senha = password
        self.tipo = '1'
        self.logado = False
        # self.login()
        # self.interfaceadm()

# self.cadastro()

    def login(self):
        print('|Login de usuário|  ')
        u = input('informe o nome de usuário:')
        m = input('Informe a matricula:')
        s = input('Informe a sua senha:')
        if self.senha == s and self.mat == m and self.nome == u:
            self.logado = True#aqui ele ta vendo se o usuário tem cadastro no sistema:
            self.interfaceadm()

    def interfaceadm(self):
        print('|Interface administrativa|  \n'
              '== Selecione uma opção ==')
        menu = input('(1)Adicionar eventos:\n'
                     '(2)Cadastrar usuário:\n')

        # if menu == '2' and self.logado:
        #     self.cadastro()  # aqui eu quero que chame a função cadastro de usuário
        if menu == '1':
            pass      #
        elif menu == '2': #and self.logado:
            self.cadastro()
        # else:
        #     print('está certo')

    def cadastro(self):
        # self.none = input("")
        v = input('DESEJA FAZER O CADASTRO DE QUAL USUÁRIO: \n'
                  '(1) ALUNO:\n'
                  '(2) ADM:\n')
        self.tipo = v
        if v == '1':
            self.nome = input("Informe o nome do aluno:")
            self.mat = input("Crie uma matricula: ")
            self.senha = input("Crie uma senha:")
        if v == '2':
            self.nome = input("Informe o nome do Adm:")
            self.mat = input("Crie uma matricula: ")
            self.senha = input("Crie uma senha:")

alunos, professor = [], []

while True:
    usu = Usuario()     # aqui vai pro método construtor
    # usu.cadastro()      # aqui define que o cadastro será feito dentro da função cadastro
    if usu.tipo == '1':
        alunos.append(usu)
    elif usu.tipo == '2':
        professor.append(usu)
    else:
        pass
    if input("Deseja cadastrar outro usuário S/N: ").upper() != 'S':
        break

for i in alunos:
    print(f"Nome: {i.nome}, Matrícula: {i.mat}, Senha: {i.senha}")

for i in professor:
    print(f"Nome: {i.nome}, Matrícula: {i.mat}, Senha: {i.senha}")


