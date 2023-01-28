import PySimpleGUI as sg

layout = [
        [sg.InputText(key='-INPUT-', size=(30,1)),sg.Button('C', size=(7,1))],
        [sg.Button('7', size=(7,2)),sg.Button('8', size=(7,2)),sg.Button('9', size=(7,2)),sg.Button('*', size=(7,2))],
        [sg.Button('4', size=(7,2)),sg.Button('5', size=(7,2)),sg.Button('6', size=(7,2)),sg.Button('+', size=(7,2))],
        [sg.Button('1', size=(7,2)),sg.Button('2', size=(7,2)),sg.Button('3', size=(7,2)),sg.Button('-', size=(7,2))],
        [sg.Button('÷', size=(7,2)),sg.Button('0', size=(7,2)),sg.Button('.', size=(7,2)),sg.Button('=', size=(7,2))]
    ]

janela = sg.Window('Calculadora', layout, sg.theme('Default1'))
        
def main():
    while True:
        
        event, values = janela.read()
        if event in ( '0','1','2','3','4','5','6','7','8','9','+','-','*','÷','.'):
            janela['-INPUT-'].update(values['-INPUT-']+event)
        
        elif event == sg.WIN_CLOSED:
            break
        
        elif event == 'C':
            janela['-INPUT-'].update('')
        
        elif event == '=':
            lista = []
            for d in values['-INPUT-']:
                lista.append(d)
           
            if '÷' in lista:
                lista.insert(lista.index('÷'),'/')
                lista.remove('÷')
                values['-INPUT-'] = "".join(lista)     
                resul = eval(values['-INPUT-'])
                janela['-INPUT-'].update(resul)
            else:
                try:
                    resul = eval(values['-INPUT-'])
                    janela['-INPUT-'].update(resul)
                except:
                    janela['-INPUT-'].update("ERRO")
                
if __name__ == "__main__":
    main()