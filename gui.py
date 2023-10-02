import PySimpleGUI as sg

def mainGUI():
    sg.theme('DarkAmber')   # Dark themes are superior
    # All the stuff inside your window.
    layout = [
                [sg.Text('Эта программа смотрит весь фильм покадрово и находит кадры, наиболее близкие к образцу')],
                [sg.Text('Ссылка на фильм'), sg.InputText(key="-VIDEO-", enable_events=True, disabled=True), sg.FileBrowse(file_types=(("Файлы видео", "*.avi *.mkv *.mov *.mp4 *.webm"),))],
                [sg.Text('Ссылка на кадр'), sg.InputText(key="-IMG-", enable_events=True, disabled=True), sg.FileBrowse(file_types=(("Изображения", "*.jpg *.jpeg *.png"),))],
                [sg.Button('Запуск', key="-GO-", disabled=True), sg.Button('Отмена')]
                ]

    # Create the Window
    window = sg.Window('АвтоОля', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(event, values["-VIDEO-"], values["-IMG-"])
        if event == sg.WIN_CLOSED or event == 'Отмена': # if user closes window or clicks cancel
            break
        elif event == "-GO-":
            print(f'Обрабатываемый файл фильма: {values["-VIDEO-"]}, а образец кадра: {values["-IMG-"]}')
            window.close()
            return values["-VIDEO-"], values["-IMG-"]
        elif values["-VIDEO-"] and values["-IMG-"]:
            window['-GO-'].update(disabled=False)
