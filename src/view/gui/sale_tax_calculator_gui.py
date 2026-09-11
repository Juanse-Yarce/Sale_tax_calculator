from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout



class SaleTaxCalculatorApp(App):
    def build(self):
        return contenedor

    def calcular_cuota(self, sender):
        categoria = str(self.categoria.text)
        valor_compra = float(self.valor_compra.text)
        cantidad = int(self.cantidad.text)

        