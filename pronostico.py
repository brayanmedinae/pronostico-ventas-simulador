import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md


class Pronostico:

    def __init__(self, datos_historicos, columna_fecha, columna_ventas, periods, freq) -> None:
        self.COLUMNA_FECHAS = columna_fecha
        self.COLUMNA_VENTAS = columna_ventas
        self.COLUMNA_SEGUNDOS = 'segundos'
        self.datos_historicos = datos_historicos
        self.datos_historicos[self.COLUMNA_SEGUNDOS] = md.date2num(self.datos_historicos[columna_fecha])
        self.datos_historicos[self.COLUMNA_FECHAS] = pd.to_datetime(self.datos_historicos[columna_fecha])
        self.m = 0
        self.b = 0
        self.periods = periods
        self.freq = freq


    def metodo_minimos_cuadrados(self):
        x = self.datos_historicos[self.COLUMNA_SEGUNDOS]
        y = self.datos_historicos[self.COLUMNA_VENTAS]
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x*y)
        sum_x2 = sum(x**2)
        self.m = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
        self.b = (sum_y - self.m*sum_x)/n
        print(f"La ecuación de la recta de regresión es: y = {self.m}x + {self.b}")


    def draw(self):
        fechas = self.datos_historicos[self.COLUMNA_FECHAS]
        recta_modelo = self.m*self.datos_historicos[self.COLUMNA_SEGUNDOS] + self.b
        ventas = self.datos_historicos[self.COLUMNA_VENTAS]

        plt.plot_date(fechas, ventas, 'bo', xdate=True, ydate=False)
        plt.plot_date(fechas, recta_modelo, 'r-', xdate=True, ydate=False)

        p = self.prededir(fechas[len(fechas)-1])
        plt.plot_date(p['fechas'], p['prediccion'], 'g-', xdate=True, ydate=False)

        plt.show()


    def prededir(self, fecha_inicial):
        df = pd.DataFrame()
        df['fechas'] = pd.date_range(fecha_inicial, periods=self.periods, freq=self.freq)
        df = pd.concat([pd.DataFrame({'fechas': [fecha_inicial]}), df], ignore_index=True)
        df['segundos'] = md.date2num(df['fechas'])
        df['prediccion'] = self.m*df['segundos'] + self.b
        return df

