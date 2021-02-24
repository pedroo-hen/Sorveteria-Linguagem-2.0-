#Curso: Técnico em Informatica.
#Turma: 2º Ano.
#Turno: Matutino.
#Disciplina: Programação Orientada a Objetos.
#Alunos: Brenda Custodio de Souza - Pedro Henrique Silva. 

from time import sleep

class Cliente(object):
    def _init_(self, nome, contato, cpf):
        self.nome = nome
        self.contato = contato
        self.cpf = cpf

print('-' * 55)
print('Seja bem vindo a Sorveteria, escolha uma opção abaixo: ')
print('-' * 55)
print("[1]. Fazer cadastro.")
print("[2]. Fazer pedido.")
print("[3]. Sugerir novo item ao cardápio. ")
print('-' * 55)

resposta = int(input("Opção: "))

if resposta == 3:
  item = input("Insira sua sugestão ao cardápio:")
  print("Aguarde...")
  print("Sua sugestão foi registrada com sucesso!")



if resposta == 1:
  nome = input('Qual é o seu nome? ')

  try:
    contato = int(input("Qual é o seu numero? "))
  except : #nome da exceçao
    print("Numero invalido! Tente novamente.")
    exit()

  try:
    cpf = int(input("Qual é o seu CPF? "))
  except : #nome da exceçao
    print("CPF invalido! Tente novamente.")
    exit()

  print('Certo Srª', nome + ', Agora você pode fazer o seu pedido')

class Sorvete():
   def _init_(self, tipo, quantidade, sabor, acompanhamento, x):
        super(Sorvete, self)._init_(tipo, quantidade, sabor, acompanhamento, x)

        def _init_(self, tipo, quantidade, sabor, acompanhamento, x, valor):
            self.tipo = tipo
            self.quantidade = quantidade
            self.sabor = sabor
            self.acompanhamento = acompanhamento
            self.x = x
            self.valor = valor

print("Suas opções estão abaixo: ")
print('*' * 55)
print('[1] Barca de sorvete')
print("[2] Taça de sorvete")
print("[3] Casquinha")
print('*' * 55)

x = int(input("""Digite o numero do pedido desejado: 
"""))

if x < 0 or x > 3:
  raise Exception("A opção selecionada é invalida.")

class Barca(Sorvete):
    def _init_(self, tipo, quantidade, sabor, acompanhamento, x):
        super(Sorvete, self)._init_(tipo, quantidade, sabor, acompanhamento, x)

    if x == 1:
        print("Você escolheu a Barca, vamos a preparação.")
        print("""___________________________________________________________________________
|    Peso  |          Sabor            |           Acompanhamento         |
|__________|___________________________|__________________________________|
|[1] - 1kg | [1] - Uva                 | [1] - Flocos                     |
|[2] - 2kg | [2] - Creme               | [2] - cereja                     |
|          | [3] - Coco                | [3] - granulado                  |
|          | [4] - Maracujá            | [4] - bala de goma com chocolate |
|          | [5] - Doce de leite       | [5] - chocolate derretido        |
|__________|___________________________|__________________________________|
""")
        print("OBS:Não se esqueça de digitar o numero do ingrediente desejado: ")
        print(" ")
        print('*' * 55)
        print("Vamos as opções: ")
        print("[1] - 1Kg")
        print("[2] - 2Kg")

        quantidade = int(input("Opção: "))

        if quantidade > 2:
          raise Exception("A opção selecionada é invalida.")

        print("Esses são os sabores: ")
        print("[1] - Uva")
        print("[2] - Creme")
        print("[3] - Coco")
        print("[4] - Maracujá")
        print("[5] - Doce de leite")

        Sabor = int(input("Opção: "))

        if Sabor > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Agora os acompanhamentos: ")
        print("[1] - Flocos")
        print("[2] - cereja")
        print("[3] - granulado")
        print("[4] - bala de goma com chocolate")
        print("[5] - chocolate derretido ")
        
        acompanhamento = int(input("Opção: "))

        if acompanhamento > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Processando pedido, por favor aguarde...")
        sleep(3)
        print(' Seu pedido foi realizado com sucesso.')
    
        if 1 == quantidade:
            print('O valor é 30,00 reais. Muito obrigado, volte sempre.')

        elif 2 == quantidade:
            print('O valor é 40,00 reais. Muito obrigado, volte sempre.')

        else:
            print('Voçê nao preencheu os dados corretamente. Faça seu pedido novamente.')
  
        lista = [quantidade, Sabor, acompanhamento]
        print ('''
        Seu pedido foi uma a barca de: ''',lista)
        print("""___________________________________________________________________________
|    Peso  |          Sabor            |           Acompanhamento         |
|__________|___________________________|__________________________________|
|[1] - 1kg | [1] - Uva                 | [1] - Flocos                     |
|[2] - 2kg | [2] - Creme               | [2] - cereja                     |
|          | [3] - Coco                | [3] - granulado                  |
|          | [4] - Maracujá            | [4] - bala de goma com chocolate |
|          | [5] - Doce de leite       | [5] - chocolate derretido        |
|__________|___________________________|__________________________________|
""")



class Copo(Sorvete):
    def _init_(self, tipo, quantidade, sabor, acompanhamento, x):
        super(Sorvete, self)._init_(tipo, quantidade, sabor, acompanhamento, x)

    if x == 2:
        print("Você escolheu a Taça, vamos a preparação.")
        print("""_____________________________________________________________________________
| Quantidade |          Sabor            |           Acompanhamento         |
|____________|___________________________|__________________________________|
|[1] - 300ml | [1] - Chocolate           | [1] - Flocos                     |
|[2] - 500ml | [2] - Morango             | [2] - cereja                     |
|            | [3] - Balnilia            | [3] - granulado                  |
|            | [4] - Maracuja            | [4] - bala de goma com chocolate |
|            | [5] - Ceu azul            | [5] - chocolate derretido        |
|____________|___________________________|__________________________________|
""")

        print("OBS:Não se esqueça de digitar o numero do ingrediente desejado: ")

        print(" ")
        print('*' * 55)
        print("Vamos as opções: ")
        print("[1] - 300ml")
        print("[2] - 500ml")

        quantidade = int(input("Opção: "))

        if quantidade > 2:
          raise Exception("A opção selecionada é invalida.")

        print("Esses são os sabores: ")
        print("[1] - Chocolate")
        print("[2] - Morango")
        print("[3] - Balnilia")
        print("[4] - Maracuja")
        print("[5] - Ceu azul")

        sabor = int(input("Opção: "))

        if sabor > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Agora os acompanhamentos: ")
        print("[1] - Flocos")
        print("[2] - cereja")
        print("[3] - granulado")
        print("[4] - bala de goma com chocolate")
        print("[5] - chocolate derretido ")

        acompanhamento = int(input("Opção: "))

        if acompanhamento > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Processando pedido, por favor aguarde...")
        sleep(3)
        print(' Seu pedido foi realizado com sucesso.')

        if 1 == quantidade:
            print('O valor é 10,00 reais. Muito obrigado, volte sempre.')

        elif 2 == quantidade:
            print('O valor é 15,00 reais. Muito obrigado, volte sempre.')

        else:
            print('Voçê nao preencheu os dados corretamente. Faça seu pedido novamente.')
  
        lista = [quantidade, sabor, acompanhamento]
        print ('''
        Seu pedido foi um Copo de Sorvete de: ''',lista)
        print("""_____________________________________________________________________________
| Quantidade |          Sabor            |           Acompanhamento         |
|____________|___________________________|__________________________________|
|[1] - 300ml | [1] - Chocolate           | [1] - Flocos                     |
|[2] - 500ml | [2] - Morango             | [2] - cereja                     |
|            | [3] - Balnilia            | [3] - granulado                  |
|            | [4] - Maracujá            | [4] - bala de goma com chocolate |
|            | [5] - Ceu azul            | [5] - chocolate derretido        |
|____________|___________________________|__________________________________|
""")

class Casquinha(Sorvete):
    def _init_(self, tipo, quantidade, sabor, acompanhamento, x):
        super(Sorvete, self)._init_(tipo, quantidade, sabor, acompanhamento, x)

    if x == 3:
        print("Você escolheu a Casquinha, vamos a preparação.")
        print("""_______________________________________________________________________________
|  Quantidade  |          Sabor            |           Acompanhamento         |
|______________|___________________________|__________________________________|
|[1] - 1 bola  | [1] - Chocolate           | [1] - Flocos                     |
|[2] - 2 bolas | [2] - Morango             | [2] - cereja                     |
|              | [3] - Balnilia            | [3] - granulado                  |
|              | [4] - Misto               | [4] - bala de goma com chocolate |
|              | [5] - caramelo            | [5] - chocolate derretido        |
|______________|___________________________|__________________________________|
""")
        print("OBS:Não se esqueça de digitar o numero do ingrediente desejado: ")
        print(" ")
        print('*' * 55)
        print("Vamos as opções: ")
        print("[1] - 1 bola")
        print("[2] - 2 bolas")

        quantidade = int(input("Opção: "))

        if quantidade > 2:
          raise Exception("A opção selecionada é invalida.")

        print("Esses são os sabores: ")
        print("[1] - Chocolate")
        print("[2] - Morango")
        print("[3] - Balnilia")
        print("[4] - Misto")
        print("[5] - caramelo")

        sabor = int(input("Opção: "))

        if sabor > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Agora os acompanhamentos: ")
        print("[1] - Flocos")
        print("[2] - cereja")
        print("[3] - granulado")
        print("[4] - bala de goma com chocolate")
        print("[5] - chocolate derretido ")

        acompanhamento = int(input("Opção: "))

        if acompanhamento > 5:
          raise Exception("A opção selecionada é invalida.")

        print("Processando pedido, por favor aguarde...")
        sleep(3)
        print(' Seu pedido foi realizado com sucesso.')

        if 1 == quantidade:
            print('O valor é 2,50 reais. Muito obrigado, volte sempre.')

        elif 2 == quantidade:
            print('O valor é 3,50  reais. Muito obrigado, volte sempre.')

        else:
            print('Voçê nao preencheu os dados corretamente. Faça seu pedido novamente.')

  
        lista = [quantidade, sabor, acompanhamento]
        print ('''
        Seu pedido foi uma Casquinha com: ''',lista)
        print("""_______________________________________________________________________________
|  Quantidade  |          Sabor            |           Acompanhamento         |
|______________|___________________________|__________________________________|
|[1] - 1 bola  | [1] - Balnilia            | [1] - Flocos                     |
|[2] - 2 bolas | [2] - Morango             | [2] - cereja                     |
|              | [3] - Uva                 | [3] - granulado                  |
|              | [4] - Maracujá            | [4] - bala de goma com chocolate |
|              | [5] - Leite Condensado    | [5] - chocolate derretido        |
|______________|___________________________|__________________________________|
""")