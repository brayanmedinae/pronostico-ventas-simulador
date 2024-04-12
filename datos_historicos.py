import sqlite3
import pandas as pd

class DatosHistoricos:

    def __init__(self) -> None:
        self.df = pd.DataFrame()


    def crear_datos_historicos(self, datos_historicos):
        self.con = sqlite3.connect("datos_historicos.db")
        self.cur = self.con.cursor()
        self.df = pd.read_excel(datos_historicos, engine='openpyxl')
        self.df.to_sql('datos_historicos', self.con, if_exists='replace', index=False)
        self.cur.close()
        self.con.close()


    def reutilizar_datos_historicos(self):
        self.con = sqlite3.connect("datos_historicos.db")
        self.cur = self.con.cursor()
        self.df.from_records(self.cur.execute("SELECT * FROM datos_historicos;"))
        self.cur.close()
        self.con.close()


    def get_datos_para_pronostico(self, columna_fecha, columna_ventas, columna_tipo_producto, tipo_producto):
        self.con = sqlite3.connect("datos_historicos.db")
        self.cur = self.con.cursor()
        query = f"SELECT {columna_fecha}, {columna_ventas} FROM datos_historicos WHERE {columna_tipo_producto} = '{tipo_producto}';"
        df = pd.read_sql_query(query, self.con)
        self.cur.close()
        self.con.close()
        return df


    def get_tipos_productos(self, columna_tipo_producto):
        self.con = sqlite3.connect("datos_historicos.db")
        self.cur = self.con.cursor()
        query = f"SELECT DISTINCT {columna_tipo_producto} FROM datos_historicos;"
        df = pd.read_sql_query(query, self.con)
        self.cur.close()
        self.con.close()
        return df[columna_tipo_producto].tolist()

