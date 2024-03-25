# Agenda
# # resolvemos ultilizando o paradigma esruturado
# self = sirva se a si mesmo
# A classe deve comecçar com a primeira letra maiuscula
# quando o nome da classe for composto cameoquase
# maiusculo para objeto
# minusculo para classe
# class Cliente:
#     def __class__(self):
#         self.nome = None
#         self.cpf = None
#         self.saldo = None
#
# class Produto:
#     def __dir__(self):
#         self.marca = None
#         self.modelo = None
#         self.tipo = None
#         self.preco = None
#         self.cliente = None
#
# cliente1 = Cliente()
# cliente1.nome = "fulano "
# cliente1.cpf = "721.766.777-87"
# cliente1.saldo = "150000"
#
# prod1 = Produto()
# prod1.marca = "fiat"
# prod1.modelo = "uno"
# prod1.tipo = ""
# prod1.preco = ""
# prod1.cliente = cliente1
#
# prod1 = Produto
# prod1.marca = 'fiat'
# prod1.modelo = 'argo'
# prod1.preco = 309587
#
# prod2 = Produto
# print(prod1.marca , prod2.marca)
# x = prod1.cliente.cliente1
# print(x)

#
# class Cliente:
#     def __dir__(self):
#         self.nome = None
#         self.cpf = None
#         self.saldo = None
#
#
# cliente1 = Cliente()
# cliente1.nome = "Levy  "
# cliente1.cpf = "721.766.777-87 "
# cliente1.saldo = "150000\n "
#
# cliente2 = Cliente()
# cliente2.nome = "joão "
# cliente2.cpf = "721.766.777-87 "
# cliente2.saldo = "140000\n "
#
# cliente3 = Cliente()
# cliente3.nome = "wesley "
# cliente3.cpf = "721.766.777-87 "
# cliente3.saldo = "1550000 "
#
# print(cliente1.nome + cliente1.cpf + cliente1.saldo)
# print(cliente2.nome + cliente2.cpf + cliente2.saldo)
# print(cliente3.nome + cliente3.cpf + cliente3.saldo)
#
# # cliente2 = Cliente
# print(cliente2.nome, cliente2.cpf, cliente2.saldo)

# cliente3 = Cliente
# print(cliente3.nome, cliente3.cpf, cliente3.saldo)

# Agenda de contatos
#
# crie uma agenda pessoal
# com N contato usando os conceitos iniciais de P.O.O
# O progama deve ser capaz de adicionar, editar, excluir, e buscar um contato na agenda (Funções)

# def adicionar_contato():
#     class Pessoa:
#         def __dir__(self):
#             self.nome = input('Informe o seu nome:')
#
#             cliente3 = Pessoa()
#             cliente3.nome
#
#
# def editar():
#     print('2')
#
#
# def excluir():
#     print('3')
#
#
# def buscar_contato():
#     print('4')
#
#
# agenda = []
#
# p = input('(1) Adicionar novo contato:\n'
#           '(2) Editar:\n'
#           '(3) Excluir:\n'
#           '(4) Buscar contato:\n')
#
# if p == '1':
#     adicionar_contato()
#
# if p == '2':
#     editar()
#
# if p == '3':
#     excluir()
#
# if p == '4':
#     buscar_contato()
#

# Crie uma agenda pessoal com (N)contatos, até o usuário querer parar usando os conceitos iniciais de POO
# O programa deve ser capaz de:
# Adicionar
# Editar
# EXCLUIR
# BUSCAR UM CONTATO NA AGENDA
# while True:
#         if input('OLÁ, GOSTARIA DE VER O MENU INICIAL DA SUA AGENDA DE CONTATOS? [S/N]?R:').upper() == 'N':
#             break
#
#
# menu = input('-----------------------------------\n'               # 35 -
#             '|1| ADICIONAR UN NOVO CONTATO:\n'
#             '|2| EDITAR LISTA DE CONTATOS:\n'
#             '|3| EXCLUIR UM CONTATO DA LISTA:\n'
#             '|4| BUSCAR UM CONTATO NA LISTA:\n'
#             '-----------------------------------\n')
#
#
# if menu == '1':
#    print('fun 1')
#
#
# if menu == '2':
#    print('fun2')
#
#
# if menu == '3':
#    print('fun3')
#
#
# if menu == '3':
#    print('fun3')

# modelando uma biblioteca computacionalmente  usando POO

# 1° passo: identificar as calsses do universo do universo do problema biblioteca
#
# usuario
# livro
#
# 2° passo: descrever / modelar as classes em Python

class Usuario:          # recomenda - se usar letras maiusculas no inicio do nome da classe
    def __init__(self,  nome, mat, cpf, uname,  email, dtn, tel, passwd="1234", livro=[]): # Metodo construtos de clases - função
        # definir  o molde de objeto que eu quero construir a partir d classe
        self.nome = nome                # um atributo funciona como uma variável (espaço de mémoria que armazena um valor)
        self.matricula = mat
        self.cpf = cpf
        self.username = uname
        self.senha = passwd
        self.email = email
        self.fone = tel
        self.dt_nascimento = dtn
        self.livros_emprestados = livro    #list()

# 3° passo: uma vez definida a clase eu posso instanciar (criar / construir ) um objeto
# (exemplo) dessa clase invocando seu metodo costrutor

user1 = Usuario ("Maria","123424","12376576575","Das dores","fulano@.com","12/01/2008","(63) 991224757")

print(user1.senha)
# user2 = Usuario ()
# user3 = Usuario ()
# user4 = Usuario ()

# Para acessar atributos de objetos em Python ultilizo o seguinte padrão:
# nom_do_objeto.nome_do_atributo.
# user1.nome

print(user1.nome, user1.fone , user1.livros_emprestados)

user1.nome = "levy "
user1.fone = "63 9897966868"
user1.livros_emprestados = ("Don casmuro ")



class Livro:
    pass