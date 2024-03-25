
class Usuario:
    def __init__(self, matdirecao, mataluno, matprofessor,matrepresentante, livro=[]):

        self.direcao = matdirecao
        self.aluno = mataluno
        self.professor = matprofessor
        self.represetante = matrepresentante
        self.livros_emprestados = livro

x = input("Informe o nome do usuario:")
q = input("Informe")
d = input("Informe")
f = input("")
g = input("")
h = input("")
j = input("")
m = input("")

usuario_rebeca = Usuario(x, q, d, f, g, h, j,m)




# user1 = Usuario ("Maria","123424","12376576575","Das dores","fulano@.com","12/01/2008","(63) 991224757")
#
# print(user1.email)
# print(user1.senha)


# print(user1.nome, user1.fone, user1.livros_emprestados)
#
# user1.nome = "levy "
# user1.fone = "63 9897966868"
# user1.livros_emprestados = ("Don casmuro ")
