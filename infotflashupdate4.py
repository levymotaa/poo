import time


class Usuario:
    def __init__(self, name=None, matricula=None, password=None):
        self.nome = name
        self.mat = matricula
        self.senha = password
        self.tipo = '1'
        self.logado = False
        self.eventos = []

    def AdicionarEvento(self):
        print('INTERFACE ADICIONE UM EVENTO')
        disciplina = input('Informe a disciplina:')
        tipo = input('Informe o tipo de evento:')
        data = input('Informe a data do evento:')
        descricao = input('Informe a descrição:')
        diasdeprova = input('Dia da proxima avaliação:')
        evento = {'disciplina': disciplina, 'tipo': tipo, 'data': data, 'descricao': descricao,
                  'diasdeprova': diasdeprova}

    def autenticar(self):
        print('\n|SEJA BEM VINDO AO INFORFLASH|\n'
              'INFORME NOS CAMPOS ABAIXO AS INFORMAÇÕES NECESSÁRIAS PARA REALIZAR O LOGIN')
        u = input('Informe o nome de usuário:')
        m = input('Informe a matrícula:')
        s = input('Informe a senha:')


        # if user1.nome == u and user1.mat == m and user1.senha == s:
        #     user1.logado = True
        #     self.interfaceadm()
        #
        # elif user2.nome == u and user2.mat == m and user2.senha == s:
        #     user2.logado = True
        #     self.interfacealuno()
        # else:
        #     print('Credenciais inválidas! Tente novamente', end='', flush=True)
        #     time.sleep(2)  # hello, FIQUE FELIZ ESPERANDO MAIS 2 PONTO :)
        #     print('.', end='', flush=True)
        #     time.sleep(2)  # MAIS 2 SEGUNDOS, calma cara
        #     print('.', end='', flush=True)
        #     time.sleep(2)  # MAIS 2 SEGUNDOS KKKKKK \n*v
        #     print('.\n', end='', flush=True)
        #     self.autenticar()
    def interfaceadm(self):
        print('\n| INTERFACE ADMINISTRATIVA |\n'
              '|== Selecione uma opção == |\n')

        menu = input('(1) Adicionar eventos:\n'
                     '(2) Cadastrar usuário:\n'
                     '(3) Sair!!!')
        if menu == '1':
            self.AdicionarEvento()  # aqui vai para a função AdicionarEventos
        elif menu == '2':
            self.cadastro()
        else:
            print('SAINDO',end='', flush=True)
            time.sleep(2)  # sou eu dnv kkkkkkkk
            print('!', end='', flush=True)
            time.sleep(2)  # MAIS 2 SEGUNDOS, eae esta apressado ?
            print('!', end='', flush=True)
            time.sleep(2)  # MAIS 2 SEGUNDOS KKKKKK \n*v
            print('!', end='', flush=True)

    def interfacealuno(self):
        print('\n| INTERFACE ALUNO |\n'
              '|SEJA BEM VINDO AO MURAL DE AVISOS\n')
        i = input('(1) VER EVENTOS:\n'
                  '(2) SAIR:\n')
        if i == '1':
            pass  # aqui eu levo para função ver avisos
        else:
            print('SAINDO', end='', flush=True)
            time.sleep(2)  #  FIQUE FELIZ ESPERANDO MAIS 2 PONTO :)
            print('.', end='', flush=True)
            time.sleep(2)  # Peraaaaa e so mais dois segundo :(
            print('.', end='', flush=True)
            time.sleep(2) #opsss, so mais um pouco
            print('.\n', end='', flush=True)

    def cadastro(self):
        print('\n| INTERFACE DE CADASTRO |\n')
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

        o = input('\n|Selecione uma opção|\n'
                  '(1) Fazer um novo cadastro:\n'
                  '(2) Sair!!!')
        if o == '1':
            self.cadastro()
        else:
            print('Saindo', end='', flush=True)
            time.sleep(2)  # kkkk sou eu de novo, FIQUE FELIZ ESPERANDO MAIS 2 PONTO :)
            print('!', end='', flush=True)
            time.sleep(2) # MAIS 2 SEGUNDOS KKKKKK \n*v
            print('!', end='', flush=True)
            time.sleep(2)  # MAIS 2 SEGUNDOS KKKKKK \n*v
            print('!', end='', flush=True)


# Criando instâncias de dois usuários
user1 = Usuario('levy', '11', "2")  # usuário adm
user2 = Usuario('ana', '22', '3')
# Lista de usuários
usuariospd = [user1, user2]

# Verificando as credenciais e direcionando para a interface apropriada
user1.autenticar()
