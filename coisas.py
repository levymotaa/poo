class Usuario:
    def __init__(self, name, matricula, passoword):
        self.nome = name
        self.mat = matricula
        self.senha = passoword

    def cadastro(self):
        v = input('DESEJA FAZER O CADRASTO DE QUAL USUARIO ?\n'
                  '(1)ALUNO\n'
                  '(2)ADM\n')
        if v == '1':
            usu = Usuario(input("Informe o nome do usuário: "), input("Informe a matrícula: "), input("Informe a senha: "))
user1 = cadastro()


        # aluno = []
        #
        # aluno.append(usu)
        # print("Lista de alunos:")
        #     for a in aluno:
        #  print(f"Nome: {a.nome}, Matrícula: {a.mat}, Senha: {a.senha}")

adm = []




