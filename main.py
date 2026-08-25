import os
import json
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

# Configuração de Janela para Computador
if platform != 'android':
    Window.size = (360, 640)

# CRIAMOS A TELA AQUI PARA O TESTE NÃO DEPENDER DA PASTA 'screens'
class InicialScreen(MDScreen):
    pass

ROOT_KV = '''
MDNavigationLayout:
    MDScreenManager:
        id: screen_manager

        InicialScreen:
            name: 'inicial'
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: "AlgoFin"
                    md_bg_color: app.theme_cls.primary_color
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text: "Sucesso! O App abriu no Android!"
                    halign: "center"
                Widget:

    MDNavigationDrawer:
        id: nav_drawer
        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title: "AlgoFin"
                title_color: app.theme_cls.primary_color
                text: "Educação Financeira e Computação"
                spacing: "8dp"
                padding: "12dp", 0, 0, "36dp"
                
            MDNavigationDrawerItem:
                icon: "home"
                text: "Início"
                on_release: screen_manager.current = 'inicial'; nav_drawer.set_state("close")
'''

class AlgoFinApp(MDApp):
    user_name = StringProperty("Utilizador")
    escola = StringProperty("Escola")
    turma = StringProperty("Turma")
    moedas = NumericProperty(0) 
    nivel_modulo1 = NumericProperty(1)
    nivel_modulo2 = NumericProperty(1)
    nivel_modulo3 = NumericProperty(1)

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.load_data()
        return Builder.load_string(ROOT_KV)

    # --- CORREÇÃO OBRIGATÓRIA PARA ANDROID SALVAR ARQUIVOS ---
    def get_json_path(self):
        return os.path.join(self.user_data_dir, "user_data.json")

    def load_data(self):
        caminho = self.get_json_path()
        if os.path.exists(caminho):
            try:
                with open(caminho, "r", encoding='utf-8') as f:
                    dados = json.load(f)
                    self.user_name = dados.get("nome", "Utilizador")
                    self.moedas = dados.get("moedas", 0) 
                    self.escola = dados.get("escola", "Escola")
                    self.turma = dados.get("turma", "Turma")
                    self.nivel_modulo1 = dados.get("nivel_modulo1", 1) 
                    self.nivel_modulo2 = dados.get("nivel_modulo2", 1)
                    self.nivel_modulo3 = dados.get("nivel_modulo3", 1)
            except Exception:
                pass

    def save_data(self):
        dados = {
            "nome": self.user_name,
            "escola": self.escola,
            "moedas": self.moedas,
            "turma": self.turma,
            "nivel_modulo1": self.nivel_modulo1,
            "nivel_modulo2": self.nivel_modulo2,
            "nivel_modulo3": self.nivel_modulo3
        }
        caminho = self.get_json_path()
        try:
            with open(caminho, "w", encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

if __name__ == '__main__':
    AlgoFinApp().run()
