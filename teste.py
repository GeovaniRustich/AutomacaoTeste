from selenium import webdriver
from selenium.webdriver.common.by import By
from perfil import Perfil
import pyautogui, time
import pyperclip
import pandas as pd
import unidecode, random as r
import fordev


class Perfis(Perfil):
    
    def __init__(self, nome, nasc, cpf, email, telefone):
        super().__init__(nome, nasc, cpf, email, telefone)
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

pyautogui.PAUSE = 1


aluno1 = Perfil.monta_nome(self=Perfil)
aluno2 = Perfil.monta_nome(self=Perfil)
alunoMain = Perfil.monta_nome(self=Perfil)
professor = Perfil.monta_nome(self=Perfil)
responsavel = Perfil.monta_nome(self=Perfil)

print(f'{aluno1=}, {aluno2=}, {alunoMain=}, {professor=}, {responsavel=}')

class CadastrarPerfil:
    # def __init__(self):

        perfil = Perfis(nome='', nasc='', cpf='', email='', telefone='')
        nasc = perfil.monta_dt_nasc()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()

                        # CADASTRO DO PRIMEIRO ALUNO

        pyautogui.press('win')
        pyautogui.write('notepade')
        pyautogui.press('enter')

        pyautogui.write(aluno1)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(cpf)

        #Para o RG
        pyautogui.press('tab')
        rg = fordev.generators.rg()
        pyautogui.write(rg)

        #Data de Nascimento
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=1, interval=0.5)
        # pyautogui.press('down') 
        # pyautogui.press('down')
        # pyautogui.press('enter')

        # #Celular
        # pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)
        pyautogui.press('enter')

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('s')
            
                            # CADASTRO SEGUNDO ALUNO

        nasc = perfil.monta_dt_nasc()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('i')

        pyautogui.write(aluno2)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(cpf)

        #Para o RG
        pyautogui.press('tab')
        pyautogui.write(cpf)

        #Data de Nascimento
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=1, interval=0.5)
        # pyautogui.press('down') 
        # pyautogui.press('down')
        # pyautogui.press('enter')

        #Celular
        # pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)
        pyautogui.press('enter')

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('s')
        
                                # CADASTRO aluno Main

        nasc = perfil.monta_dt_nasc()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()
        
        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('i')

        pyautogui.write(alunoMain)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(cpf)

        #Para o RG
        pyautogui.press('tab')
        pyautogui.write(cpf)

        #Data de Nascimento
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=1, interval=0.5)
        # pyautogui.press('down') 
        # pyautogui.press('down')
        # pyautogui.press('enter')

        #Celular
        # pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)
        pyautogui.press('enter')


        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('s')
        
                                        # CADASTRO RESPONSAVEL

        nasc = perfil.monta_dt_nasc()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('i')

        pyautogui.write(responsavel)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=1, interval=0.5)
        rg = fordev.generators.rg()
        pyautogui.write(rg)

        #Para o RG
        pyautogui.press('tab')
        pyautogui.write(cpf)

        #Data de Nascimento
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=1, interval=0.5)
        # pyautogui.press('down') 
        # pyautogui.press('down')
        # pyautogui.press('enter')

        # #Celular
        # pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)
        pyautogui.press('enter')

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('s')
        
                                # CADASTRO PROFESSOR
        nasc = perfil.monta_dt_nasc()
        cpf = perfil.monta_cpf()
        email = perfil.monta_email()
        telefone = perfil.gerar_telefone()

        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('i')

        pyautogui.write(professor)

        #Email do perfil
        pyautogui.press('tab')
        pyautogui.write(email) 

        #Cpf do perfil
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(cpf)

        #Para o RG
        pyautogui.press('tab')
        pyautogui.write(cpf)

        #Data de Nascimento
        pyautogui.press('tab', presses=1, interval=0.5)
        pyautogui.write(nasc)

        #Sexo
        pyautogui.press('tab', presses=1, interval=0.5)
        # pyautogui.press('down') 
        # pyautogui.press('down')
        # pyautogui.press('enter')

        # #Celular
        # pyautogui.press('tab', presses=16, interval=0.5)
        pyautogui.write(telefone)
        pyautogui.press('enter')


        # with pyautogui.hold('ctrlleft'):
        #     pyautogui.press('s')