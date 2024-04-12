from pronostico import Pronostico
from datos_historicos import DatosHistoricos


filename = "datos-historicos.xlsx"

columna_fecha = "ORDERDATE"
columna_ventas = "SALES"
columna_tipo_producto = "PRODUCTLINE"
tipo_producto = "Ships"
periodos_pronostico = 2
frecuencia_pronostico = 'YE'

db = DatosHistoricos()
db.crear_datos_historicos(filename)
# db.reutilizar_datos_historicos()

tipos_productos = db.get_tipos_productos(columna_tipo_producto)
print(tipos_productos)

datos_historicos = db.get_datos_para_pronostico(columna_fecha, columna_ventas, columna_tipo_producto, tipo_producto)

p = Pronostico(datos_historicos, columna_fecha, columna_ventas, periodos_pronostico, frecuencia_pronostico)

p.metodo_minimos_cuadrados()


p.draw()