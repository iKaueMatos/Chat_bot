import os

# Link com as referências de como escrever a mensagem
# https://www.twilio.com/docs/voice/twiml

def processar_resposta(resposta,nome):

    if resposta == '1':
        print(f'{os.linesep} Resposta Robertinho:Com certeza Sr.{nome} python e uma linguagem de programação que so vem crescendo no mercado'
              f' nos ultimos dias e uma da que esta no top das 10 linguagens de programaçãomais utilizadas no mundo  {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Resposta Robertinho: Então Sr.{nome} depende muito da sua capacidade de se dedicar aos'
              f' estudos todos os dias sem nenhuma procastinação dessa maenira você vai esta sempre praticando e estudando cada vez mais e mais sobre programação preechendo alguns requisitos de vagas de empresas multinacionais ou internacionais {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} Resposta Robertinho:{nome} Quando você começar a compreeder que tem como resolver um determinado problema'
              f' com somente alguma linhas de codigo por exemplo 5 ou 10 (Entretanto a logica vai fazer parte disso),ao mesmo tempo analisar todo tipo de problema e identificar uma solução mais simples por meio de bibliotecas ou algo do tipo{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep} Resposta Robertinho:{nome},Um dos melhores locais para aprender python e na #Hast tag e a Alura {os.linesep}')


    else:
        print("Digite apenas os numeros listados na lista:1,2,3 ou 4")

def start():

    # Apresentar o chatbot
    print('Olá seja bem vindo eu me chamo Robertinho e estou aqui para tirar suas duvidas!!')
    #pedir nome
    nome = input("Digite seu nome: ")
    #pedir email:
    email = input("Digite seu email: ")

    while True:
    #Mostar o menu de opções
        resposta = input(f'O que gostaria de saber hoje {os.linesep} [1]- Vale a pena aprender python? {os.linesep} [2] - Quanto tempo'
              f' leva para conseguir um emprego na area{os.linesep} [3] - Quando vou saber se dominei uma linguagem de programação? {os.linesep}[4] - onde e recomendado aprender python? {os.linesep}'
                         f' [0] Para sair {os.linesep} Resposta:')
        if resposta == '0':

            break
#Processar resposta
        processar_resposta(resposta,nome)




if __name__ == '__main__':
    start()



