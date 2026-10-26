
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]

# Datos completamente sintéticos
historico = pd.DataFrame([
    ["2024-10-15", "Museo", 120, 3, False],
    ["2024-11-20", "Cine", 95, 2, False],
    ["2025-02-12", "Parque", 140, 4, False],
    ["2025-05-08", "Museo", 110, 3, False],
], columns=[
    "Fecha", "Lugar", "Alumnos",
    "Autobuses", "No realizado"
])

odoo = pd.DataFrame([
    ["2025-10-10", "Museo", 105, 3, False],
    ["2025-11-18", "Cine", 80, 2, False],
    ["2026-02-17", "Parque", 125, 3, False],
    ["2026-04-21", "Museo", 0, 0, True],
    ["2026-05-11", "Cine", 115, 3, False],
], columns=[
    "Fecha del paseo", "Destino",
    "Tickets reales", "Unidades",
    "No realizado"
])

# Estandarizar fuentes
historico = historico.rename(columns={
    "Fecha": "fecha",
    "Lugar": "destino",
    "Alumnos": "estudiantes",
    "Autobuses": "camiones",
    "No realizado": "no_realizado"
})

odoo = odoo.rename(columns={
    "Fecha del paseo": "fecha",
    "Destino": "destino",
    "Tickets reales": "estudiantes",
    "Unidades": "camiones",
    "No realizado": "no_realizado"
})

historico["fuente"] = "Historico"
odoo["fuente"] = "Odoo"

# Integración
datos = pd.concat(
    [historico, odoo],
    ignore_index=True
)

datos["fecha"] = pd.to_datetime(datos["fecha"])

from validation import validar_servicios

validar_servicios(datos)

# Validaciones básicas
assert datos["fecha"].notna().all()
assert datos["estudiantes"].ge(0).all()
assert datos["camiones"].ge(0).all()
assert len(datos) == 9

# Excluir registros confirmados como no realizados
validos = datos.loc[
    ~datos["no_realizado"]
].copy()

assert len(validos) == 8

# Ciclo escolar: agosto a julio
validos["ciclo"] = (
    validos["fecha"].dt.year
    - (validos["fecha"].dt.month < 8).astype(int)
)

resumen = (
    validos.groupby("ciclo")
    .agg(
        paseos=("fecha", "size"),
        estudiantes=("estudiantes", "sum"),
        camiones=("camiones", "sum")
    )
)

# Guardar resultados de demostración
SALIDA = BASE / "reports" / "demo"
SALIDA.mkdir(parents=True, exist_ok=True)

resumen.to_csv(SALIDA / "resumen_sintetico.csv")

ax = resumen["estudiantes"].plot.bar(
    figsize=(8, 5),
    title="Synthetic Example | Students by School Year"
)

ax.set_xlabel("School year starting in")
ax.set_ylabel("Students")
ax.tick_params(axis="x", rotation=0)

plt.tight_layout()
plt.savefig(
    SALIDA / "estudiantes_sinteticos.png",
    dpi=180
)
plt.close()

print("Synthetic demo completed successfully.")
print(resumen)
print("Results:", SALIDA)
