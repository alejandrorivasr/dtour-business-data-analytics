
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]

DATOS = BASE / "data" / "aggregated"
SALIDA = BASE / "reports" / "reproduced"
SALIDA.mkdir(parents=True, exist_ok=True)

mensual = pd.read_csv(DATOS / "monthly_operations.csv")
destinos = pd.read_csv(DATOS / "destination_operations.csv")

ciclos = ["2024-2025", "2025-2026"]
meses = [10, 11, 12, 1, 2, 3, 4, 5, 6]
etiquetas = ["Oct", "Nov", "Dec", "Jan", "Feb",
             "Mar", "Apr", "May", "Jun"]

# Validar los datos públicos antes de graficar
assert len(mensual) == 18
assert not mensual.duplicated(["ciclo_escolar", "mes"]).any()

totales = mensual.groupby("ciclo_escolar")[
    ["paseos", "estudiantes"]
].sum()

assert totales.loc["2024-2025", "paseos"] == 386
assert totales.loc["2025-2026", "paseos"] == 325

assert totales.loc["2024-2025", "estudiantes"] == 51017
assert totales.loc["2025-2026", "estudiantes"] == 42051

assert destinos["paseos"].sum() == mensual["paseos"].sum()

# 1 y 2. Gráficas mensuales
for columna, titulo, archivo in [
    ("paseos", "Educational trips by school year",
     "trips_by_school_year.png"),
    ("estudiantes", "Student participations by school year",
     "students_by_school_year.png")
]:

    tabla = mensual.pivot(
        index="mes",
        columns="ciclo_escolar",
        values=columna
    ).reindex(index=meses, columns=ciclos)

    assert tabla.notna().all().all()

    x = np.arange(len(meses))
    ancho = 0.36

    fig, ax = plt.subplots(figsize=(11, 5))

    for i, ciclo in enumerate(ciclos):
        ax.bar(
            x + (i - 0.5) * ancho,
            tabla[ciclo],
            ancho,
            label=ciclo
        )

    ax.set_xticks(x, etiquetas)
    ax.set_ylabel(
        "Trips" if columna == "paseos"
        else "Student participations"
    )
    ax.set_title(titulo)
    ax.legend()
    ax.grid(axis="y", alpha=0.2)

    plt.tight_layout()
    plt.savefig(SALIDA / archivo, dpi=180)
    plt.close()

# 3. Cambio de paseos por destino
tabla = destinos.pivot_table(
    index="destino_publico",
    columns="ciclo_escolar",
    values="paseos",
    aggfunc="sum",
    fill_value=0
).reindex(columns=ciclos, fill_value=0)

tabla["cambio"] = tabla[ciclos[1]] - tabla[ciclos[0]]

tabla["magnitud"] = tabla["cambio"].abs()

top = (
    tabla.nlargest(10, "magnitud")
    .sort_values("cambio")
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(top.index, top["cambio"])
ax.axvline(0, color="black", linewidth=1)

ax.set_title("Change in trips by destination")
ax.set_xlabel("2025-2026 minus 2024-2025")
ax.grid(axis="x", alpha=0.2)

plt.tight_layout()
plt.savefig(
    SALIDA / "destination_changes.png",
    dpi=180
)
plt.close()

print("REAL AGGREGATED DATA ANALYSIS")
print(totales)
print("\nThree charts generated successfully.")
print("Output folder:", SALIDA)
