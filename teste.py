class Usuario:
    def __init__(self, name=None, matricula=None, password=None):
        self.nome = name
        self.mat = matricula
        self.senha = password
        self.tipo = '1'
        # self.cadastro()

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
    usu.cadastro()      # aqui define que o cadastro será feito dentro da função cadastro
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

