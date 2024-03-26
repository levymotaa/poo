class Usuario:
    def __init__(self, name, matricula, passoword):
        self.nome = name
        self.mat = matricula
        self.senha = passoword

    def cadastro(self):
        v = input('DESEJA FAZER O CADRASTO DE QUAL USUARIO'
                  '(1)ALUNO'
                  '(2)ADM')
        if v == '1':
            x = input("Informe o nome do usuario")
            y = input("Informe a matricula ")
            z = input("Informe a senha do usuário ")
            return Usuario(x, y, z)
        else:
            return None


usu = Usuario(input("Informe o nome do usuário: "), input("Informe a matrícula: "), input("Informe a senha: "))

usu.cadastro()