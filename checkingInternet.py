
import PySimpleGUI as sg
import urllib.request
       
class App():
    def __init__(self):
        try:
            self.r = requests.get(r"https://www.google.com/");
        except Exception:
            return "Not";
    def check_internet(self):
        try:
            urllib.request.urlopen("http://google.com", timeout=2)
            #print('Интернет работает');
            #sys.stdout.write('Internet is working');
            return 'Internet is working';
            
        except Exception:
            #print('Не работает интернет. Перезагрузите или обратитесь к провайдеру');
            return 'Internet doesn\'t work. Please, try connection again';
    def check_siteworking(self,value):
        try:
            import requests;
            r = requests.get(value);
            if r.status_code == 200:
                print('Сайт работает');
                return 'Сайт работает';
            elif r.status_code == 404:
                print('Сайт не работает');
                return 'Сайт не работает';
        except Exception:
            pass;

        
class GUI(App):

    def __init__(self):
        sg.theme('DarkPurple4');        
        layout = [  [sg.Text("Click to check your internet working?",font = ["Arial",18])],     
                    [sg.Input()],
                    [sg.Text(size=(40,3),key='-OUTPUT-')],
                    [sg.Button('Check internet'),sg.Button('Check site working'),sg.Button('Quit')] ]

        
        window = sg.Window('Internet check', layout)      # Part 3 - Window Defintion
                                                        

              # Do something with the information gathered
        while True:
            event, values = window.read()

            if event == 'Quit' or event == sg.WINDOW_CLOSED:
                
                break;
            if event == "Check internet":
                r = App.check_internet(self);
                methodname = 'check_internet';
                method=getattr(App,methodname);
                window['-OUTPUT-'].update(method(self),
                                    text_color = 'yellow',
                                    font =["Arial",18]);
                
            if event == "Check site working":
                mName = 'check_siteworking';
                m = getattr(App,mName);
                window['-OUTPUT-'].update(m(self,values[0]),
                                          font =["Arial",18],
                                          text_color='yellow');
                pass;
        
        window.close()     

a = GUI();




