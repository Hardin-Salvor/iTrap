from kivy.app import App
# from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
# from kivy.lang import Builder

Window.size = (390, 844)


def get_resultsdil(d):
    res2o25 = str(round(220000 / d * 1.11))
    resppa5 = str(round(52500 / d * 1.11))
    resozgal5 = str(round(128 / d, 2))
    resml5 = str(round((128 / d * 29.57) / 3.785, 2))

    return {
        'res2o25': res2o25, 'resppa5':
        resppa5, 'resozgal5': resozgal5, 'resml5': resml5
            }


def get_resdoso25(H5):
    rdilpaa5 = str(round(220000 / ((52500 / H5) * 1.11) * 1.11))
    resdil5 = str(round(52500 / H5 * 1.11))
    resdil5oz = str(round(128 / ((52500 / H5) * 1.11), 2))
    resdil5ml = str(round((128 / ((52500 / H5) * 1.11) * 29.57) / 3.785, 2))

    return {'resdil5': resdil5, 'rdilpaa5': rdilpaa5, 'resdil5oz': resdil5oz, 'resdil5ml': resdil5ml}


def get_resfloz5(f5):
    resfldil5 = str(round(128 / f5))
    resflh2o5 = str(round(220000 / (128 / f5) * 1.11))
    resflpaa5 = str(round(52500 / (128 / f5) * 1.11))
    resflml5 = str(round((f5 * 29.57) / 3.785, 2))

    return {'resfldil5': resfldil5, 'resflh2o5': resflh2o5, 'resflpaa5': resflpaa5, 'resflml5': resflml5}


# ------------------------------ de aqui es para perox 15

def get_resultsdil15(d):
    res2o215 = str(round(220000 / d * 1.11))
    resppa15 = str(round(52500 / d * 1.11))
    resozgal15 = str(round(128 / d, 2))
    resml15 = str(round((128 / d * 29.57) / 3.785, 2))

    return {'res2o215': res2o215, 'resppa15':
        resppa15, 'resozgal15': resozgal15, 'resml15': resml15}


def get_resdoso215(H5):
    rdilpaa15 = str(round(220000 / ((52500 / H5) * 1.11) * 1.11))
    resdil15 = str(round(52500 / H5 * 1.11))
    resdil15oz = str(round(128 / ((52500 / H5) * 1.11), 2))
    resdil15ml = str(round((128 / ((52500 / H5) * 1.11) * 29.57) / 3.785, 2))

    return {'resdil15': resdil15, 'rdilpaa15': rdilpaa15, 'resdil15oz': resdil15oz, 'resdil15ml': resdil15ml}


def get_resfloz15(f15):
    resfldil15 = str(round(128 / f15))
    resflh2o15 = str(round(220000 / (128 / f15) * 1.11))
    resflpaa15 = str(round(52500 / (128 / f15) * 1.11))
    resflml15 = str(round((f15 * 29.57) / 3.785, 2))

    return {'resfldil15': resfldil15, 'resflh2o15': resflh2o15, 'resflpaa15': resflpaa15, 'resflml15': resflml15}


class Menu(Screen):
    pass


class Games(Screen):
    def calcdil5(self):
        try:
            dilution5 = int(self.text_input1.text)
        except:
            dilution5 = 0

        ingredient = get_resultsdil(dilution5)

        self.res2o25.text = ingredient.get('res2o25')
        self.resppa5.text = ingredient.get('resppa5')
        self.resozgal5.text = ingredient.get('resozgal5')
        self.resml5.text = ingredient.get('resml5')

    def calchdoso25(self):
        try:
            paa5 = int(self.text_input2.text)
        except:
            paa5 = 0

        ingredient2 = get_resdoso25(paa5)

        self.resdil5.text = ingredient2.get('resdil5')
        self.resdil5oz.text = ingredient2.get('resdil5oz')
        self.rdilpaa5.text = ingredient2.get('rdilpaa5')
        self.resdil5ml.text = ingredient2.get('resdil5ml')

    def calcfloz5(self):
        try:
            floz5 = float(self.text_input3.text)
        except:
            floz5 = 0

        ingredient3 = get_resfloz5(floz5)

        self.resfldil5.text = ingredient3.get('resfldil5')
        self.resflh2o5.text = ingredient3.get('resflh2o5')
        self.resflpaa5.text = ingredient3.get('resflpaa5')
        self.resflml5.text = ingredient3.get('resflml5')

    def clear(self):

        self.ids.text_input1.text = ''
        self.ids.res2o25.text = "0"
        self.ids.resppa5.text = "0"
        self.ids.resozgal5.text = "0"
        self.ids.resml5.text = "0"

        self.ids.text_input2.text = ''
        self.ids.resdil5.text = '0'
        self.ids.resdil5oz.text = '0'
        self.ids.rdilpaa5.text = '0'
        self.ids.resdil5ml.text = '0'

        self.ids.text_input3.text = ''
        self.ids.resfldil5.text = '0'
        self.ids.resflh2o5.text = '0'
        self.ids.resflpaa5.text = '0'
        self.ids.resflml5.text = '0'


class Rules(Screen):

    def calcdil15(self):
        try:
            dilution15 = int(self.text_input15.text)
        except:
            dilution15 = 0

        ingredient = get_resultsdil15(dilution15)

        self.res2o215.text = ingredient.get('res2o215')
        self.resppa15.text = ingredient.get('resppa15')
        self.resozgal15.text = ingredient.get('resozgal15')
        self.resml15.text = ingredient.get('resml15')

    def calchdoso215(self):
        try:
            paa15 = int(self.text_input12.text)
        except:
            paa15 = 0

        ingredient12 = get_resdoso215(paa15)

        self.resdil15.text = ingredient12.get('resdil15')
        self.resdil15oz.text = ingredient12.get('resdil15oz')
        self.rdilpaa15.text = ingredient12.get('rdilpaa15')
        self.resdil15ml.text = ingredient12.get('resdil15ml')

    def calcfloz15(self):
        try:
            floz15 = float(self.text_input13.text)
        except:
            floz15 = 0

        ingredient13 = get_resfloz15(floz15)

        self.resfldil15.text = ingredient13.get('resfldil15')
        self.resflh2o15.text = ingredient13.get('resflh2o15')
        self.resflpaa15.text = ingredient13.get('resflpaa15')
        self.resflml15.text = ingredient13.get('resflml15')

    def clear2(self):

        self.ids.text_input15.text = ''
        self.ids.res2o215.text = '0'
        self.ids.resppa15.text = '0'
        self.ids.resozgal15.text = '0'
        self.ids.resml15.text = '0'

        self.ids.text_input12.text = ''
        self.ids.resdil15.text = '0'
        self.ids.resdil15oz.text = '0'
        self.ids.rdilpaa15.text = '0'
        self.ids.resdil15ml.text = '0'

        self.ids.text_input13.text = ''
        self.ids.resfldil15.text = '0'
        self.ids.resflh2o15.text = '0'
        self.ids.resflpaa15.text = '0'
        self.ids.resflml15.text = '0'


class MainApp(App):
    def build(self):
        return ScreenManager()


MainApp().run()
