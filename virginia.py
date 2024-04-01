import time


class Usuario:
    def init(self, name=None, matricula=None, password=None):
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
        # self.eventos.append(evento)

    def autenticar(self):
        print('|SEJA BEM VINDO AO INFORFLASH|\n'
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
        if u == 'levy' and m == '11' and s == '2':
            self.interfaceadm()
        elif u == 'ana' and m == '22' and s == '3':
            self.interfacealuno()
        else:
            print('Credenciais inválidas! Tente novamente...')

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
            print('SAINDO!!!')

    def interfacealuno(self):
        print('\n| INTERFACE ALUNO |\n'
              '|SEJA BEM VINDO AO MURAL DE AVISOS\n')
        i = input('(1) VER EVENTOS:\n'
                  '(2) SAIR:\n')
        if i == '1':
            pass  # aqui eu levo para função ver avisos
        else:
            time.sleep(2)
            print('SAINDO...')
 # PAUSA POR 2 SEGUNDOS, FIQUE FELIZ ESPERANDO MAIS 2 PONTO :)  # PAUSA POR MAIS 2 SEGUNDOS # PAUSA POR MAIS DOIS SEGUNDOS, FIQUE FELIZ É O ULTIMO :(

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

        alunos, adm = [], []

        usu = Usuario()
        if usu.tipo == '1':
            aluno.append(usu)
        elif usu.tipo == '2':
            adm.append(usu)
        else:
            pass
        o = input('\n|Selecione uma opção|\n'
                  '(1) Fazer um novo cadastro:\n'
                  '(2) Sair!!!')
        if o == '1':
            self.cadastro()
        else:
            print('Saindo!!!', end='', flush=True)
            time.sleep(2)  # kkkk sou eu de novo, FIQUE FELIZ ESPERANDO MAIS 2 PONTO :)
            print('.', end='', flush=True)
            time.sleep(2)  # MAIS 2 SEGUNDOS KKKKKK \n*v
            self.autenticar()


# Criando instâncias de dois usuários
user1 = Usuario()  # usuário adm

user2 = Usuario()  # usuário aluno

# Lista de usuários
usuarios = [user1, user2]
# Verificando as credenciais e direcionando para a interface apropriada
user1.autenticar()