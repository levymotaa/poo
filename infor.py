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
        self.config --



    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nMatrícula: {self.matricula}"

# Exemplo de uso
estudante1 = Estudante("Virginia", 20, "2022001")
estudante2 = Estudante("Vitor", 22, "2022002")

print(estudante1)
print("\n")

estudante1.estudar("TPS")
print("\n")

print(estudante2)
print("\n")

estudante2.estudar("POO")
