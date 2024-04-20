import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md


class Pronostico:

    def __init__(self, datos_historicos, columna_fecha, columna_ventas, periods, freq) -> None:
        self.COLUMNA_FECHAS = columna_fecha
        self.COLUMNA_VENTAS = columna_ventas
        self.COLUMNA_SEGUNDOS = 'matplotlib_dates'
        self.datos_historicos = datos_historicos
        self.datos_historicos[self.COLUMNA_SEGUNDOS] = md.date2num(self.datos_historicos[columna_fecha])
        self.datos_historicos[self.COLUMNA_FECHAS] = pd.to_datetime(self.datos_historicos[columna_fecha])
        self.datos_historicos['_year'] = self.datos_historicos[columna_fecha].dt.year
        self.datos_historicos['_month'] = self.datos_historicos[columna_fecha].dt.month
        if freq == 'YE':
            self.grouped_data = self.datos_historicos.groupby('_year')[self.COLUMNA_VENTAS].sum().astype(int).reset_index()
            self.grouped_data[self.COLUMNA_SEGUNDOS] = md.date2num(pd.to_datetime(self.grouped_data['_year'], format='%Y'))
            self.grouped_data[self.COLUMNA_FECHAS] = pd.to_datetime(self.grouped_data['_year'], format='%Y')
        else:
            self.grouped_data = self.datos_historicos.groupby(['_year', '_month'])[self.COLUMNA_VENTAS].sum().astype(int).reset_index()
            self.grouped_data[self.COLUMNA_SEGUNDOS] = md.date2num(pd.to_datetime(self.grouped_data['_year'].astype(str) + '-' + self.grouped_data['_month'].astype(str), format='%Y-%m'))
            self.grouped_data[self.COLUMNA_FECHAS] = pd.to_datetime(self.grouped_data['_year'].astype(str) + '-' + self.grouped_data['_month'].astype(str), format='%Y-%m')
        self.m = 0
        self.b = 0
        self.periods = periods
        self.freq = freq
        self.datos_historicos = self.grouped_data


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


    def draw(self):
        fechas = self.datos_historicos[self.COLUMNA_FECHAS]
        recta_modelo = self.m*self.datos_historicos[self.COLUMNA_SEGUNDOS] + self.b
        ventas = self.datos_historicos[self.COLUMNA_VENTAS]

        plt.plot_date(fechas, ventas, 'bo', xdate=True, ydate=False)
        plt.plot_date(fechas, recta_modelo, 'r-', xdate=True, ydate=False)

        p = self.prededir(fechas[len(fechas)-1])
        plt.plot_date(p[self.COLUMNA_FECHAS], p[self.COLUMNA_VENTAS], 'g-', xdate=True, ydate=False)

        plt.legend(['Datos históricos', 'Recta modelo', 'Predicción'])
        plt.xlabel('Fecha')
        plt.ylabel('Ventas')

        plt.show()


    def prededir(self, fecha_inicial):
        df = pd.DataFrame()
        df[self.COLUMNA_FECHAS] = pd.date_range(fecha_inicial, periods=self.periods, freq=self.freq)
        df[self.COLUMNA_SEGUNDOS] = md.date2num(df[self.COLUMNA_FECHAS])
        df[self.COLUMNA_VENTAS] = self.m*df[self.COLUMNA_SEGUNDOS] + self.b
        return df


    def table(self):
        table = pd.DataFrame()
        table[self.COLUMNA_FECHAS] = self.datos_historicos[self.COLUMNA_FECHAS]
        table[self.COLUMNA_VENTAS] = self.datos_historicos[self.COLUMNA_VENTAS]
        table[self.COLUMNA_SEGUNDOS] = self.datos_historicos[self.COLUMNA_SEGUNDOS]
        table['year'] = table[self.COLUMNA_FECHAS].dt.year
        table['month'] = table[self.COLUMNA_FECHAS].dt.month

        prediccion = self.prededir(table[self.COLUMNA_FECHAS].iloc[-1]).iloc[1:]
        prediccion['year'] = prediccion[self.COLUMNA_FECHAS].dt.year
        prediccion['month'] = prediccion[self.COLUMNA_FECHAS].dt.month

        table = table._append(prediccion, ignore_index=True)

        if self.freq == 'YE':
            sale_in_years = table.groupby('year')[self.COLUMNA_VENTAS].sum().astype(int)
            result = pd.DataFrame()
            result[self.COLUMNA_VENTAS] = sale_in_years
        else:
            sale_in_months = table.groupby(['year', 'month'])[self.COLUMNA_VENTAS].sum().astype(int)
            result = pd.DataFrame()
            result[self.COLUMNA_VENTAS] = sale_in_months


        result.reset_index(inplace=True)

        result_in_list = [result.columns.tolist()]
        for index, row in result.iterrows():
            result_in_list.append(row.tolist())

        return result_in_list
        


