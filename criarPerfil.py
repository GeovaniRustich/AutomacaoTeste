import pyautogui, time
from perfil import Perfil
import fordev

nomeCadastros = str(input('Insira o nome a ser colocado nos cadastros: '))

codigoCentroCusto = str(input('Insira o código para cadastro de Centro de Custo e Plano de conta: '))       

emailPrincipal = str(input('Digite seu email: '))

formulaSisAvaliacao = str(input('Qual será a formula ultilizada para o sistema de avaliação (Não pode conter Espaços): '))

pyautogui.PAUSE = 0.7

nomeReduzido = (f'{nomeCadastros[:3]}{nomeCadastros[6:9]}')


aluno1 = Perfil.monta_nome(self=Perfil)
aluno2 = Perfil.monta_nome(self=Perfil)
alunoMain = Perfil.monta_nome(self=Perfil)
professor = Perfil.monta_nome(self=Perfil)
responsavel = Perfil.monta_nome(self=Perfil)

class Perfis(Perfil):
    
    def __init__(self, nome, nasc, cpf, email, telefone):
        super().__init__(nome, nasc, cpf, email, telefone)
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


class AbrirNavegador:

    pyautogui.alert("Nâo mexa no computador, código rodando!")


    pyautogui.press('win')
    pyautogui.write('google')
    pyautogui.press('enter')
    with pyautogui.hold('win'):
        pyautogui.press('up')

    time.sleep(1)

class AbrirJacad:

    usuario = 'root'
    senha = '123123'

    pyautogui.write('192.168.10.104')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=268, y=322)
    time.sleep(0.5)
    pyautogui.doubleClick(x=129, y=1020)
    time.sleep(4)
    pyautogui.press('tab', presses=2, interval=1)
    pyautogui.press('enter')


    #Aguardar JACAD abrir
    time.sleep(12)
    pyautogui.write(usuario)    
    pyautogui.press('tab')
    pyautogui.write(senha) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)
    #clicando no Perfil

    time.sleep(5)
    

# class CadastrarPerfil:
#     # def __init__(self) -> None:

#         pyautogui.click(x=245, y=100)

#         with pyautogui.hold('ctrlleft'):
#           pyautogui.press('n')
#         perfil = Perfis(nome='', nasc='', cpf='', email='', telefone='')
#         nasc = perfil.monta_dt_nasc()
#         cpf = perfil.monta_cpf()
#         email = perfil.monta_email()
#         telefone = perfil.gerar_telefone()

#                         # CADASTRO DO PRIMEIRO ALUNO

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('i')

#         pyautogui.write(aluno1)

#         #Email do perfil
#         pyautogui.press('tab')
#         pyautogui.write(email) 

#         #Cpf do perfil
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.write(cpf)

#         #Para o RG
#         pyautogui.press('tab')
#         rg = fordev.generators.rg()
#         pyautogui.write(rg)

#         #Data de Nascimento
#         pyautogui.press('tab', presses=7, interval=0.5)
#         pyautogui.write(nasc)

#         #Sexo
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.press('down') 
#         pyautogui.press('down')
#         pyautogui.press('enter')

#         #Celular
#         pyautogui.press('tab', presses=16, interval=0.5)
#         pyautogui.write(telefone)

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('s')
#         time.sleep(2)
#                             # CADASTRO SEGUNDO ALUNO

#         nasc = perfil.monta_dt_nasc()
#         cpf = perfil.monta_cpf()
#         email = perfil.monta_email()
#         telefone = perfil.gerar_telefone()

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('i')

#         pyautogui.write(aluno2)

#         #Email do perfil
#         pyautogui.press('tab')
#         pyautogui.write(email) 

#         #Cpf do perfil
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.write(cpf)

#         #Para o RG
#         pyautogui.press('tab')
#         rg = fordev.generators.rg()
#         pyautogui.write(rg)

#         #Data de Nascimento
#         pyautogui.press('tab', presses=7, interval=0.5)
#         pyautogui.write(nasc)

#         #Sexo
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.press('down') 
#         pyautogui.press('down')
#         pyautogui.press('enter')

#         #Celular
#         pyautogui.press('tab', presses=16, interval=0.5)
#         pyautogui.write(telefone)

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('s')
#         time.sleep(2)
#                                 # CADASTRO aluno Main

#         nasc = perfil.monta_dt_nasc()
#         cpf = perfil.monta_cpf()
#         email = perfil.monta_email()
#         telefone = perfil.gerar_telefone()
        
#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('i')

#         pyautogui.write(alunoMain)

#         #Email do perfil
#         pyautogui.press('tab')
#         pyautogui.write(emailPrincipal) 

#         #Cpf do perfil
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.write(cpf)

#         #Para o RG
#         pyautogui.press('tab')
#         rg = fordev.generators.rg()
#         pyautogui.write(rg)

#         #Data de Nascimento
#         pyautogui.press('tab', presses=7, interval=0.5)
#         pyautogui.write(nasc)

#         #Sexo
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.press('down') 
#         pyautogui.press('down')
#         pyautogui.press('enter')

#         #Celular
#         pyautogui.press('tab', presses=16, interval=0.5)
#         pyautogui.write(telefone)

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('s')
#         time.sleep(2) 
#                                         # CADASTRO RESPONSAVEL

#         nasc = perfil.monta_dt_nasc()
#         cpf = perfil.monta_cpf()
#         email = perfil.monta_email()
#         telefone = perfil.gerar_telefone()

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('i')

#         pyautogui.write(responsavel)

#         #Email do perfil
#         pyautogui.press('tab')
#         pyautogui.write(email) 

#         #Cpf do perfil
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.write(cpf)

#         #Para o RG
#         pyautogui.press('tab')
#         rg = fordev.generators.rg()
#         pyautogui.write(rg)

#         #Data de Nascimento
#         pyautogui.press('tab', presses=7, interval=0.5)
#         pyautogui.write(nasc)

#         #Sexo
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.press('down') 
#         pyautogui.press('down')
#         pyautogui.press('enter')

#         #Celular
#         pyautogui.press('tab', presses=16, interval=0.5)
#         pyautogui.write(telefone)

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('s')
#         time.sleep(2)
#                                 # CADASTRO PROFESSOR
#         nasc = perfil.monta_dt_nasc()
#         cpf = perfil.monta_cpf()
#         email = perfil.monta_email()
#         telefone = perfil.gerar_telefone()

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('i')

#         pyautogui.write(professor)

#         #Email do perfil
#         pyautogui.press('tab')
#         pyautogui.write(email) 

#         #Cpf do perfil
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.write(cpf)

#         #Para o RG
#         pyautogui.press('tab')
#         rg = fordev.generators.rg()
#         pyautogui.write(rg)

#         #Data de Nascimento
#         pyautogui.press('tab', presses=7, interval=0.5)
#         pyautogui.write(nasc)

#         #Sexo
#         pyautogui.press('tab', presses=2, interval=0.5)
#         pyautogui.press('down') 
#         pyautogui.press('down')
#         pyautogui.press('enter')

#         #Celular
#         pyautogui.press('tab', presses=16, interval=0.5)
#         pyautogui.write(telefone)

#         with pyautogui.hold('ctrlleft'):
#             pyautogui.press('s')
#         time.sleep(2)



class CursoBase:

    nomeReduzido = (f'{nomeCadastros[:3]}{nomeCadastros[6:9]}')

    #Abre a tela do Curso Base
    # pyautogui.click(x=1540, y=120)
    pyautogui.click(x=100, y=40)
    pyautogui.click(x=140, y=165)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')

    # Escreve nomes de impressão 1,2 e 3
    for i in range(0,3):
        pyautogui.write(nomeCadastros)
        pyautogui.press('tab')

    # Escreve nome reduzido
    pyautogui.write(nomeReduzido)

    # Grau Acadêmico
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.3)
    pyautogui.press('space')

    # Grau Acadêmico a constar no Diploma
    pyautogui.click(x=624, y=705)
    pyautogui.write('Bacharel')
    pyautogui.press('tab')
    pyautogui.write('Bacharela')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    time.sleep(2)
    pyautogui.click(x=1459, y=181)

class CentroDeCusto:

    # Abrir tela de Centro de Custo
    pyautogui.click(x=187, y=46)
    pyautogui.click(x=256, y=704)
    pyautogui.click(x=533, y=308)
    time.sleep(1.5)
    # Cadastra o Centro de Custo
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(codigoCentroCusto)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    time.sleep(2)

    pyautogui.click(x=1338 ,y=316)


class criarPeriodo:
    time.sleep(1)
    pyautogui.click(x=106, y=40)
    pyautogui.click(x=161, y=272)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')
    
    pyautogui.click(x=675, y=338)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('01012023')
    pyautogui.press('tab')
    pyautogui.write('31122023')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.write('2023')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    time.sleep(2)
class subPeriodo:

    #Cadastro do 1° Semestre    
    pyautogui.click(x=709, y=303) #Clicando no menu academico
    pyautogui.click(x=555, y=424)
    
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('1° Semestre')
    pyautogui.press('tab')
    pyautogui.write('01012023')
    pyautogui.press('tab')
    pyautogui.write('01062023')
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.5)
    pyautogui.press('tab')
    pyautogui.write('105')
    pyautogui.press ('tab', presses=2, interval=0.5)

    for i in range(0, 3):
       pyautogui.press('space')
       pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
      pyautogui.press('s')
    time.sleep(2)

    #Cadastro do 2° Semestre
    pyautogui.click(x=709, y=303)
    pyautogui.click(x=555, y=424)
    
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('2° Semestre')
    pyautogui.press('tab')
    pyautogui.write('02062023')
    pyautogui.press('tab')
    pyautogui.write('01122023')
    pyautogui.press('tab')
    pyautogui.press('down', presses=3, interval=0.5 )
    pyautogui.press('tab')
    pyautogui.write('105')
    pyautogui.press ('tab', presses=2, interval=0.5)

    for i in range(0, 3):
       pyautogui.press('space')
       pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
      pyautogui.press('s')
    time.sleep(2)

    pyautogui.click(x=1375 ,y=193)

class CriarSistemaAvaliacao:
    pyautogui.click(x=34, y=45)
    pyautogui.moveTo(x=220, y=163)
    pyautogui.click(x=389, y=570)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')
    
    pyautogui.write(nomeCadastros) 
    pyautogui.press('tab')
    pyautogui.write(formulaSisAvaliacao)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('tab')

    pyautogui.write(formulaSisAvaliacao)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    pyautogui.click(x=639, y=775)
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)

    pyautogui.write('N1')
    pyautogui.press('tab')
    pyautogui.write('N1')

    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    time.sleep(2)

    pyautogui.click(x=639, y=775)
    pyautogui.press('tab')
    pyautogui.write('1')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)

    pyautogui.write('N2')
    pyautogui.press('tab')
    pyautogui.write('N2')

    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    time.sleep(2)

    #Adicionando o sitema de avaliação no Periodo Letivo

    pyautogui.click(x=1328, y=184)

    pyautogui.click(x=917, y=281)

    pyautogui.click(x=523, y=420)

    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    

class Curso:
    pyautogui.click(x=186, y=96)
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')
    
    pyautogui.click(x=759, y=316)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('0')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=8, interval=0.4)
    pyautogui.write('SUS')
    pyautogui.press('tab', presses=3, interval=0.5)
    for i in range(0, 12):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('1')
    pyautogui.press('tab')
    pyautogui.write('8')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('7')
    pyautogui.press('enter')    
    pyautogui.press('tab')
    pyautogui.write('3')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('75')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write('6')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('6')
    pyautogui.press('enter')
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
            

class DisciplinaCurso:
    pyautogui.click(x=415, y=831)
    pyautogui.write('1 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.click(x=415, y=831)
    pyautogui.write('2 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.click(x=415, y=831)
    pyautogui.write('3 Periodo')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Normal 1')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disc.Norm 1')
    pyautogui.press('tab', presses=9, interval=0.5)
      
    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Normal 2')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disc.Norm 2')
    pyautogui.press('tab', presses=9, interval=0.5)
      
    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    
    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Opt. 1')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disciplina.Opt 1')
    pyautogui.press('tab', presses=9, interval=0.5)
 


    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')
        
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=473, y=654)
    pyautogui.click(x=672, y=827)
    pyautogui.press('tab', presses=4, interval=0.5)
    pyautogui.write('Disciplina Opt.2')
    pyautogui.press('tab', presses=3, interval=0.5)
    pyautogui.write('Disciplina.Opt.2')
    pyautogui.press('tab', presses=9, interval=0.5)

    for i in range(0, 11):
        time.sleep(0.5)
        pyautogui.press('tab')
        pyautogui.write('100')
        
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.press('space')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')
    
    pyautogui.click(x=934, y=703)

    with pyautogui.hold('shift'):
        pyautogui.click(x=934, y=703)
    
    with pyautogui.hold('shift'):
        pyautogui.click(x=952, y=724)
    
    pyautogui.click(x=900, y=836)

    pyautogui.click(x=892, y=751)

    
    pyautogui.write('Optativas')
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=1)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('200')
    pyautogui.press('tab')   
    pyautogui.press('space')
    pyautogui.click(x=821, y=407)
    pyautogui.press('enter')



class Turma:
    pyautogui.alert('aaaa')
    pyautogui.click(x=135, y=93)

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('n')
    
    pyautogui.click(x=837, y=280)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)
    pyautogui.press('tab', presses=2, interval=0.5)
    pyautogui.write(nomeCadastros)
    pyautogui.press('tab')
    pyautogui.write(nomeReduzido)


    #precisamos finalizar esse cadastro pois há muitos dados na unidade física


class Requerimento:
    #Vai cadastrar um novo requerimento
    pyautogui.click(x=469, y=45)
    time.sleep(1)
    pyautogui.click(x=528, y=96)
    time.sleep(1)
    pyautogui.click(x=800, y=119)
    time.sleep(1)



    with pyautogui.hold('ctrlleft'):
        pyautogui.press('i')

    pyautogui.write(nomeCadastros)
    pyautogui.press('tab', presses=2, interval=0.3)
    pyautogui.write('teste057')
    pyautogui.press('enter')

    time.sleep(2)


    pyautogui.press('tab')
    pyautogui.press('down', presses=3, interval=0.3)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')
    pyautogui.write('6000')
    pyautogui.press('tab', presses=2, interval=0.3)
    pyautogui.press('down', presses=3, interval=0.3)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('10')
    pyautogui.press('tab')
    pyautogui.write('3')
    pyautogui.press('tab')
    pyautogui.press('space')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    # Realiza solicitação do requerimento via Desktop
    pyautogui.click(x=1249, y=230)
    pyautogui.click(x=81, y=177)
    time.sleep(2)

    pyautogui.click(x=735, y=999)

    pyautogui.press('tab', presses=3, interval=0.1)

    #Preciso pegar o nome do aluno em uma variavel, por exemplo: pyautogui.write(variavel)
    #por hora utilizamos o método de copiar e colar o ultimo nome de aluno que faz a copia na classe aluno 
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('v')
    
    pyautogui.press('enter')

    time.sleep(2)
    
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.2)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('tab')

    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')

    pyautogui.press('tab', presses=2, interval=0.1)
    pyautogui.press('enter')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')