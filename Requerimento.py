import pyautogui, time
nomeCadastros = str(input('Insira o nome a ser colocado nos cadastros: '))
pyautogui.PAUSE = 0.5
time.sleep(2)

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
    pyautogui.press('tab', presses=1, interval=0.3)
    pyautogui.press('down' , presses=2, interval=0.3)
    pyautogui.press('tab', presses=2, interval=0.3)
    pyautogui.write('teste89')
    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.press('tab')
    pyautogui.write('6000')
    pyautogui.press('tab')
    pyautogui.press('down', presses=3, interval=0.3)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.press('tab')
    pyautogui.press('space')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')

    pyautogui.click(x=1284, y=204)

    # Realiza solicitação do requerimento via Desktop
    pyautogui.click(x=1249, y=230)
    pyautogui.click(x=81, y=177)
    time.sleep(2)

    pyautogui.click(x=735, y=999)

    pyautogui.press('tab', presses=3, interval=0.1)

    #Preciso pegar o nome do aluno em uma variavel pyautogui.write(variavel)
    #por hora utilizamos o método de copiar e colar o ultimo nome de aluno que faz a copia na classe aluno 
    with pyautogui.hold('ctrlleft'):
        pyautogui.press('v')
    
    pyautogui.press('enter')

    time.sleep(3)
    
    pyautogui.press('tab')
    pyautogui.press('down', presses=2, interval=0.2)
    pyautogui.press('enter')
    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.write(nomeCadastros)
    # pyautogui.press('enter')
    # time.sleep(1)
    # pyautogui.press('tab')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('tab')
    
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')

    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.write(nomeCadastros)
    pyautogui.press('enter')

    pyautogui.press('tab', presses=2, interval=0.1)
    pyautogui.press('enter')

    with pyautogui.hold('ctrlleft'):
        pyautogui.press('s')