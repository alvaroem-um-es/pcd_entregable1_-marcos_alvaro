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
        self.nombre = nombre
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

    def get_estudiante(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, Asignaturas: {self.mostrar_asignaturas()}"

    def set_estudiante(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def del_estudiante(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
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
    

    def get_investigador(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, ID: {self.id}, Departamento: {self.departamento}, Área de Investigación: {self.area_investigacion}"

    def set_investigador(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
        self.id = id
        self.departamento = departamento
        self.area_investigacion = area_investigacion

    def del_investigador(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
        self.id = None
        self.departamento = None
        self.area_investigacion = None

    def get_area_investigacion(self):
        return self.area_investigacion



class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []
    
    def get_profesor(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, ID: {self.id}, Departamento: {self.departamento}, Asignaturas Impartidas: {self.asignaturas_impartidas}"

    def set_profesor(self, nombre, dni, direccion, sexo, id, departamento, asignaturas_impartidas):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
        self.id = id
        self.departamento = departamento
        self.asignaturas_impartidas = asignaturas_impartidas

    def del_profesor(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
        self.id = None
        self.departamento = None
        self.asignaturas_impartidas = None

    def añadir_asignatura(self, asignatura):
        self.asignaturas_impartidas.append(asignatura)

    def get_asignaturas_impartidas(self):
        return [asignatura.nombre for asignatura in self.asignaturas_impartidas]



class ProfesorTitular(Profesor, Investigador):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        super(ProfesorTitular, self).__init__(nombre, dni, direccion, sexo, id, departamento, area_investigacion)




class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []
    



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

    profe = ProfesorTitular("Paco","09224070N","Av Libertad", Sexo.M, "ID002", departamento_DIIC, "Matemáticas")
    print(profe.get_profesor())  # Obtener información del profesor (heredado de Profesor)
    print(profe.get_investigador()) #heredo de investigador
    profe.añadir_asignatura(Asignatura("Matemáticas"))
    print(profe.get_asignaturas_impartidas())