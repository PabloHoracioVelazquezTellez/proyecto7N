# administrativos.py
from persona import Persona

class Administrativos(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._area =""

    # Getter y Setter
    def get_cargo(self):
        if self._cargo == "":
            return "error"
        else:
            return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_area(self):
        if self._area == "":
            return "error"
        else:
            return self._area

    def set_area(self, area):
        self._area = area

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Cargo: {self._cargo}, Area: {self._area}"
