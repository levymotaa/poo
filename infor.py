# primeira class
# class Usuario:
#     def __init__(self, mat, user,password,instituncional):
#         self.matricula = mat
#         self.username = user
#         self.senha = password
#         self.email = instituncional
#
# user1= Usuario ("202311900008","Virginia","3357", "virginia.venega@ifto.edu.br")
#
#
# x = input('Informe sua matricula:')
# y = input('Informe sua senha:')
#
#
# #matricula, usarname e senha. atributo que diferencie ele



class Estudante:
    def __init__(self, user, mat, password ):
        self.username = user
        self.matricula = mat
        self.senha = password




    def __str__(self):
        return f"Nome: {self.username}\nIdade: {self.matricula}\nMatrícula: {self.senha}"

# Exemplo de uso
estudante1 = Estudante("Virginia", 20, "virginia")
estudante2 = Estudante("Vitor", 22, "virginia")
print(estudante1.username)

# user1.nome = "levy "
# user1.fone = "63 9897966868"
# user1.livros_emprestados = ("Don casmuro ")
