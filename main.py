class Empleado:
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Antiguedad: {self.antiguedad}")

class Desempeño:
    def __init__(self, puntualidad, trabajoEquipo, productividad, observaciones, promedio, estado):
        self.puntualidad = puntualidad
        self.trabajoEquipo = trabajoEquipo
        self.productividad = productividad
        self.observaciones = observaciones
        self.promedio = promedio
        self.estado = estado
    def mostrar(self):
        print(f"Puntualidad: {self.puntualidad}")
        print(f"Trabajo Equipo: {self.trabajoEquipo}")
        print(f"Productividad: {self.productividad}")
        print(f"Observaciones: {self.observaciones}")
        print(f"Promedio: {self.promedio}")
        print(f"Estado: {self.estado}")
class Contacto:
    def __init__(self, telefono,correo):
        self.telefono = telefono
        self.correo = correo
    def mostrar(self):
        print(f"Telefono: {self.telefono}")
        print(f"Correo: {self.correo}")
