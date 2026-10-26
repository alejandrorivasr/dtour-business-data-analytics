
import pandas as pd

COLUMNAS = [
    "fecha", "destino", "estudiantes",
    "camiones", "no_realizado", "fuente"
]

def validar_servicios(df):
    faltantes = set(COLUMNAS) - set(df.columns)

    if faltantes:
        raise ValueError(
            f"Columnas faltantes: {sorted(faltantes)}"
        )

    if df.empty:
        raise ValueError("La base está vacía.")

    if not pd.api.types.is_datetime64_any_dtype(
        df["fecha"]
    ) or df["fecha"].isna().any():
        raise ValueError("Existen fechas inválidas.")

    for col in ["estudiantes", "camiones"]:
        valores = pd.to_numeric(
            df[col], errors="coerce"
        )

        if valores.isna().any() or valores.lt(0).any():
            raise ValueError(
                f"Valores inválidos en {col}."
            )

    if not df["no_realizado"].isin(
        [True, False]
    ).all():
        raise ValueError("Estado de realización inválido.")

    return True
