# -------------------------------------------------------------- #
#  Copyright (c) UMU Corporation. All rights reserved.
# ######################## PROGRAMACIÓN ORIENTADA A OBJETOS ####################### #
# ########################  ENTREGABLE 1  ####################### #


#### IMPLEMENTACIÓN CÓDIGO PARA GESTOR DE UNIVERSIDADES ####

# -------------------------------------------------------------- #

#### CLASES PARA LAS EXCEPCIONES Y ENUMERACIONES DEL CÓDIGO ####


from enum import Enum
from abc import ABCMeta, abstractmethod


class AsignaturaCreditosError(Exception):
    pass

class AsignaturaDepartamentoError(Exception):
    pass

class ProfesorAsignaturaError(Exception):
    pass

class EstudianteAsignaturaError(Exception):
    pass

class DniFormatoError(Exception):
    pass

class Sexo(Enum):
    M = 'Masculino'
    V = 'Femenino'

class Departamento(Enum):
    DIIC = 'DIIC'
    DITEC = 'DITEC'
    DIS = 'DIS'

# -------------------------------------------------------------- #

#### CLASES PARA LOS OBJETOS PERTENECIENTES AL ENUNCIADO CON SUS MÉTODOS CORRESPONDIENTES ####

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        if not self._es_formato_dni_valido(dni):
            raise DniFormatoError("El formato del DNI no es válido.")
        
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def _es_formato_dni_valido(self, dni):
        return len(dni) == 8 and dni.isdigit() #Verificamos que el DNI tiene el formato correcto (por ejemplo 8 dígitos)


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
        try:
            if isinstance(asignatura, str): 
                asignatura = Asignatura(asignatura)

            elif isinstance(asignatura, dict):
                asignatura = Asignatura(asignatura['nombre'], asignatura['codigo'], asignatura['creditos'], asignatura['departamento'])

            self.asignaturas.append(asignatura)

        except EstudianteAsignaturaError as e:
            print(f"Error al matricular estudiante: {str(e)}")

    def desmatricular(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)

    def mostrar_asignaturas(self):
        return [asignatura.nombre for asignatura in self.asignaturas]


class Asignatura:
    def __init__(self, nombre, codigo=None, creditos=None, departamento=None): 
        if creditos is not None and not isinstance(creditos, int):
            raise AsignaturaCreditosError("Los créditos de la asignatura deben ser un número entero.")
        
        if creditos is not None and creditos > 6:
            raise AsignaturaCreditosError("Demasiados créditos")

        if departamento is not None and departamento not in Departamento:
            raise AsignaturaDepartamentoError("El departamento de la asignatura no es válido.")
        
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
        try:
            if isinstance(asignatura, str): 
                asignatura = Asignatura(asignatura, departamento=self.departamento) #Creamos una instancia con el mismo departamento que el profesor 

            elif isinstance(asignatura, dict):
                asignatura = Asignatura(asignatura['nombre'], asignatura['codigo'], asignatura['creditos'], asignatura['departamento'])

            if asignatura.departamento != self.departamento: 
                raise ProfesorAsignaturaError("El profesor no pertenece al mismo departamento que la asignatura.")
        
            self.asignaturas_impartidas.append(asignatura)
        
        except (AsignaturaCreditosError, AsignaturaDepartamentoError, ProfesorAsignaturaError) as e:
            print(f"Error al añadir asignatura: {str(e)}")

    def get_asignaturas_impartidas(self):
        return [asignatura.nombre for asignatura in self.asignaturas_impartidas]


class ProfesorTitular(Investigador, Profesor):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        Investigador.__init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion)
        Profesor.__init__(self, nombre, dni, direccion, sexo, id, departamento)


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []


# -------------------------------------------------------------- #

#### INSTANCIAMIENTO DE LAS CLASES Y COMPROBACIÓN DE ERRORES ####


if __name__ == "__main__":
    #Creamos instancias de Departamento
    departamento_DIIC = Departamento.DIIC
    departamento_DITEC = Departamento.DITEC

    #Creamos instancias de Profesores
    profe1 = ProfesorTitular("Paco", "09224070", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    profe2 = ProfesorAsociado("Ana", "12345679", "Calle Principal", Sexo.V, "ID002", departamento_DITEC)

    #Añadimos las asignaturas a los profesores
    profe1.añadir_asignatura("Matemáticas")
    profe1.añadir_asignatura(Asignatura("Física", "FIS101", 6, departamento_DIIC))
    profe2.añadir_asignatura({"nombre": "Lengua", "codigo": "INF101", "creditos": 3, "departamento": departamento_DITEC})

    #Mostramos las asignaturas impartidas por cada profesor
    print("Asignaturas impartidas por", profe1.nombre + ":")
    print(profe1.get_asignaturas_impartidas())

    print("\nAsignaturas impartidas por", profe2.nombre + ":")
    print(profe2.get_asignaturas_impartidas())

    #Cambiamos el departamento de un profesor
    profe1.cambio_departamento(departamento_DITEC)
    print("\nNuevo departamento de", profe1.nombre + ":", profe1.devolver_departamento())

    #Creamos la instancia de un estudiante
    estudiante1 = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)

    #Matriculamos asignaturas al estudiante
    estudiante1.matricular(Asignatura("Historia", "HIS101", 5, departamento_DITEC))
    estudiante1.matricular('Lengua')
    estudiante1.matricular({"nombre": "Fisica", "codigo": "INF101", "creditos": 5, "departamento": departamento_DITEC})

    #Mostramos la información del estudiante 
    print("\nInformación de", estudiante1.nombre + ":")
    print(estudiante1.get_estudiante())

    #Manejo de excepciones:
    try:
        asignatura_invalida = Asignatura("Física", creditos="cinco")  #Esto lanzará una excepción AsignaturaCreditosError
    except AsignaturaCreditosError as e:
        print(f"Error al crear la asignatura: {str(e)}")

    try:
        asignatura_invalida2 = Asignatura(Asignatura("Física", "FIS101", 8, departamento_DIIC))  #Esto lanzará una excepción AsignaturaCreditosError, muchos créditos
    except AsignaturaCreditosError as e:
        print(f"Error al crear la asignatura: {str(e)}")

    profesor = Profesor("Ana", "12345679", "Calle Principal", Sexo.V, "ID002", departamento_DITEC) 
    try:
        profesor.añadir_asignatura(Asignatura("Física", "FIS101", 6, departamento_DIIC))  #Esto lanzará una excepción ProfesorAsignaturaError
    except ProfesorAsignaturaError as e:
        print(f"Error al añadir asignatura: {str(e)}")

    estudiante = Estudiante("Maria", "98765432", "Calle Secundaria", Sexo.V)
    try:
        persona = Persona("Juan", "123456789", "Calle Principal", Sexo.M)  #Esto lanzará una excepción DniFormatoError
    except DniFormatoError as e:
        print(f"Error al crear la persona: {str(e)}")

    try:
        estudiante.matricular(Asignatura("Historia", "HIS101", 9, departamento_DITEC))  #Esto lanzará una excepción AsignaturaCreditosError
    except AsignaturaCreditosError as e:
        print(f"Error al matricular estudiante: {str(e)}")

 