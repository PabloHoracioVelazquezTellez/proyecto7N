# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._categoria = ""
        self._maxEstudios = ""


    # Getter y Setter
    def get_departamento(self):
        if self._departamento == "":
            return "error"
        else:
            return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_categoria(self):
        if self._categoria == "":
            return "error"
        else:
            return self._categoria

    def set_categoria(self, categoria):
        self._categoria= categoria

    def get_maxEstudios(self):
        if self._maxEstudios=="":
            return "error"
        else:
            return self._maxEstudios

    def set_maxEstudios(self, maxEstudios):
        self._maxEstudios= maxEstudios

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoria {self._categoria}, Maximo Grado de Estudios: {self._maxEstudios}"
