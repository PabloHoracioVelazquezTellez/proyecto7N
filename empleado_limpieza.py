# empleado_limpieza.py
from empresa import Empresa
from persona import Persona

class EmpleadoLimpieza(Persona, Empresa):
    def __init__(self):
        Persona.__init__(self)
        Empresa.__init__(self)
        self._numero_empleado = ""
        self._turno =""

    # Getter y Setter
    def get_numero_empleado(self):
        if self._numero_empleado == "":
            return self._numero_empleado
        else:
            return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado

    def get_turno(self):
        if self._turno=="":
            return "error"
        else:
            return self._turno

    def set_turno(self, turno):
        self._turno = turno


    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_empresa = Empresa.mostrar_informacion(self)
        return f"{base_info_persona}, Número de Empleado: {self._numero_empleado}, Turno: {self._turno}, {base_info_empresa}"
