from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre
    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass
    def __str__(self):
        return f"Empleado: {self.nombre}"
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual
    def calcular_salario_mensual(self) -> float:
        return self.salario_anual / 12
    def __str__(self):
        return f"{super().__str__()}, Salario Anual: {self.salario_anual:.2f}"
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_por_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario_mensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return (f"{super().__str__()}, Horas trabajadas: {self.horas_trabajadas}, "
                f"Tarifa por hora: {self.tarifa_por_hora:.2f}")
        
empleados = []
for i in range(3):
    nombre = input(f"Ingrese el nombre del empleado a tiempo completo {i+1}: ")
    salario_anual = float(input("Ingrese el salario anual: "))
    empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))
for i in range(2):
    nombre = input(f"Ingrese el nombre del empleado a tiempo horario {i+1}: ")
    horas = float(input("Ingrese las horas trabajadas en el mes: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))
    empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))
print("\n--- Lista de Empleados ---")
for emp in empleados:
    print(f"{emp.nombre} -> Salario mensual: {emp.calcular_salario_mensual():.2f}")
