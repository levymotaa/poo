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
        self.eventos.append(evento)

    def autenticar(self):
        print('\n|SEJA BEM VINDO AO INFORFLASH|\n')     #fazer alguns ajustes
        login = input('Escolha uma opção:\n'
                      '(1)Fazer login de usuário\n'
                      '(2)Sair\n')
        if login == '1':
            print('INFORME NOS CAMPOS ABAIXO AS INFORMAÇÕES NECESSÁRIAS PARA REALIZAR O LOGIN')
            u = input('Informe o nome de usuário:')
            m = input('Informe a matrícula:')
            s = input('Informe a senha:')
            if userAdm.nome == u and userAdm.mat == m and userAdm.senha == s:
                userAdm.logado = True
                print('Login feito com sucesso!!!')
                self.interfaceadm()

            elif userAluno.nome == u and userAluno == m and userAluno.senha == s:
                userAluno.logado = True
                print('Login feito com sucesso!!!')
                self.interfacealuno()

            else:
                print('Credenciais inválidas! Tente novamente', end='', flush=True)
                time.sleep(2)
                print('.', end='', flush=True)
                time.sleep(2)
                print('.', end='', flush=True)
                time.sleep(2)
                print('.\n', end='', flush=True)
                self.autenticar()
        elif login == '2':
            print('SAINDO', end='',flush=True)
            time.sleep(2)
            print('.', end='', flush=True)
            time.sleep(2)
            print('.', end='', flush=True)
            time.sleep(2)
            print('.\n', end='', flush=True)
        else:
            pass

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
            print('SAINDO', end='', flush=True)
            time.sleep(2)
            print('!', end='', flush=True)
            time.sleep(2)
            print('!', end='', flush=True)
            time.sleep(2)
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
            time.sleep(2)
            print('.', end='', flush=True)
            time.sleep(2)
            print('.', end='', flush=True)
            time.sleep(2)
            print('.\n', end='', flush=True)

    def cadastro(self):
        print('\n| INTERFACE DE CADASTRO |\n')
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
            time.sleep(2)
            print('!', end='', flush=True)
            time.sleep(2)
            print('!', end='', flush=True)
            time.sleep(2)
            print('!', end='', flush=True)


# Criando instâncias de dois usuários
userAdm = Usuario('levy', '11', "2")  # usuário adm
userAluno = Usuario('ana', '22', '3')


# Verificando as credenciais e direcionando para a interface apropriada
userAdm.autenticar()
