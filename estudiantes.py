# estudiantes.py
from persona import Persona

class Estudiantes(Persona):
    def __init__(self):
        super().__init__()
        self._matricula = ""
        self._carrera=""
        self._semestre=""

    # Getter y Setter
    def get_matricula(self):
        if self._matricula == "":
            return "error"
        else:
            return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_carrera(self):
        if self._carrera == "":
            return "error"
        else:
            return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def set_semestre(self, semestre):
        self._semestre=semestre

    def get_semestre(self):
        if self._semestre =="":
            return "error"
        else:
            return self._semestre

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Matrícula: {self._matricula}, Carrera: {self._carrera}, Semestre: {self._semestre}"


