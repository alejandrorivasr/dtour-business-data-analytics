
import unittest
import pandas as pd
from src.validation import validar_servicios

class TestValidacion(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "fecha": pd.to_datetime(["2025-10-10"]),
            "destino": ["Museo"],
            "estudiantes": [120],
            "camiones": [3],
            "no_realizado": [False],
            "fuente": ["Ejemplo"]
        })

    def test_datos_validos(self):
        self.assertTrue(validar_servicios(self.df))

    def test_cantidad_negativa(self):
        self.df.loc[0, "estudiantes"] = -5

        with self.assertRaises(ValueError):
            validar_servicios(self.df)

    def test_fecha_invalida(self):
        self.df.loc[0, "fecha"] = pd.NaT

        with self.assertRaises(ValueError):
            validar_servicios(self.df)

    def test_columna_faltante(self):
        df = self.df.drop(columns=["camiones"])

        with self.assertRaises(ValueError):
            validar_servicios(df)

    def test_base_vacia(self):
        with self.assertRaises(ValueError):
            validar_servicios(self.df.iloc[0:0])

if __name__ == "__main__":
    unittest.main()
