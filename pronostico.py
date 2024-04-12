import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md


class Pronostico:

    def __init__(self, datos_historicos, columna_fecha, columna_ventas) -> None:
        self.COLUMNA_FECHAS = columna_fecha
        self.COLUMNA_VENTAS = columna_ventas
        self.COLUMNA_SEGUNDOS = 'segundos'
        self.df = pd.read_excel(datos_historicos)
        self.df[self.COLUMNA_SEGUNDOS] = md.date2num(self.df[columna_fecha])
        print(self.df.head())
        self.m = 0
        self.b = 0


    def metodo_minimos_cuadrados(self):
        x = self.df[self.COLUMNA_SEGUNDOS]
        y = self.df[self.COLUMNA_VENTAS]
        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x*y)
        sum_x2 = sum(x**2)
        self.m = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - sum_x**2)
        self.b = (sum_y - self.m*sum_x)/n
        print(f"La ecuación de la recta de regresión es: y = {self.m}x + {self.b}")
        self.df['prediccion'] = self.m*self.df[self.COLUMNA_SEGUNDOS] + self.b
        self.df.to_csv('datos.csv')



    def draw(self):
        fechas = self.df[self.COLUMNA_FECHAS]
        prediccion = self.df['prediccion']
        ventas = self.df[self.COLUMNA_VENTAS]

        plt.plot_date(fechas, ventas, 'bo', xdate=True, ydate=False)
        plt.plot_date(fechas, prediccion, 'r-', xdate=True, ydate=False)

        p = self.prededir(fechas[len(fechas)-1], 5, 'YE')
        plt.plot_date(p['fechas'], p['prediccion'], 'g-', xdate=True, ydate=False)

        plt.show()

    def prededir(self, fecha_inicial, periods, freq):
        df = pd.DataFrame()
        df['fechas'] = pd.date_range(fecha_inicial, periods=periods, freq=freq)
        df = pd.concat([pd.DataFrame({'fechas': [fecha_inicial]}), df], ignore_index=True)
        df['segundos'] = md.date2num(df['fechas'])
        df['prediccion'] = self.m*df['segundos'] + self.b
        return df

