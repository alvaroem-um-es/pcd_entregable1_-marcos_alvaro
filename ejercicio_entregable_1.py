from enum import Enum
from abc import ABCMeta, abstractmethod

class Sexo(Enum):
    M = 'Masculino'
    V = 'Femenino'

class Departamento(Enum):
    DIIC = 'DIIC'
    DITEC = 'DITEC'
    DIS = 'DIS'



class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nomnbre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo



class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.id = id
        self.departamento = departamento

    def devolver_departamento(self):
        return self.departamento

    def cambio_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

    def devolver_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.departamento}"

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = []

    def matricular(self, asignatura):
        self.asignaturas.append(asignatura)

    def desmatricular(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)

    def mostrar_asignaturas(self):
        return [asignatura.nombre for asignatura in self.asignaturas]

class Asignatura:
    def __init__(self, nombre, codigo, creditos, departamento):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.departamento = departamento

    def devolver_datos(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}, Departamento: {self.departamento}"

class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.area_investigacion = area_investigacion

    def get_area_investigacion(self):
        return self.area_investigacion

class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []

    def añadir_asignatura(self, asignatura):
        self.asignaturas_impartidas.append(asignatura)

    def get_asignaturas_impartidas(self):
        return [asignatura.nombre for asignatura in self.asignaturas_impartidas]

class ProfesorTitular(Profesor):
    pass

class ProfesorAsociado(Profesor):
    pass

# Ejemplo de uso
if __name__ == "__main__":
    departamento_DIIC = Departamento.DIIC
    investigador = Investigador("Juan", "12345678A", "Calle Principal", Sexo.M, "ID001", departamento_DIIC, "Inteligencia Artificial")

    print("Nombre del investigador:", investigador.nombre)
    print("Área de investigación:", investigador.get_area_investigacion())
    print("Departamento actual:", investigador.devolver_departamento())

    nuevo_departamento = Departamento.DITEC
    investigador.cambio_departamento(nuevo_departamento)
    print("Nuevo departamento:", investigador.devolver_departamento())

