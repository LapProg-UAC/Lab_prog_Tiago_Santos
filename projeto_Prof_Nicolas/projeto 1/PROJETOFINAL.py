import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

# -------------------------
# 1. LER DADOS
# -------------------------
pinguins = pd.read_csv("pinguins_palmer.csv")
co2 = pd.read_csv("co2_maunaloa.csv")

# -------------------------
# 2. GRAFICO 1: PINGUINS (Scatter)
# -------------------------
fig1 = px.scatter(
    pinguins,
    x="barbatana",
    y="massa",
    color="especie",
    title="Pinguins"
)
fig1.write_image("grafico1.png")

# -------------------------
# 3. GRAFICO 2: CO2 (Linha ao longo do tempo)
# -------------------------
# Agrupar por ano e calcular média
co2_grouped = co2.groupby("ano")["ppm"].mean().reset_index()

fig2 = px.line(
    co2_grouped,
    x="ano",
    y="ppm",
    title="CO2 ao longo do tempo"
)
fig2.write_image("grafico2.png")

# -------------------------
# 4. GRAFICO 3: Estimativa massa vs CO2
# -------------------------
anos = np.arange(2010, 2021)
# Crescimento barbatanas: 14 mm por ano, base 180mm em 2010
flipper = 180 + 14 * (anos - 2010)
# Massa proporcional (exemplo simples)
massa = flipper * 10

# CO2 correspondente aos anos
co2_anos = co2_grouped[co2_grouped["ano"].isin(anos)]
min_len = min(len(massa), len(co2_anos))
massa = massa[:min_len]
co2_vals = co2_anos["ppm"].values[:min_len]

# Correlação
correlacao = np.corrcoef(massa, co2_vals)[0, 1]

fig3 = px.scatter(
    x=massa,
    y=co2_vals,
    labels={"x": "Massa estimada", "y": "CO2"},
    title=f"Correlação massa vs CO2: {correlacao:.2f}"
)
fig3.write_image("grafico3.png")

# -------------------------
# 5. JUNTAR IMAGENS LADO A LADO
# -------------------------
img1 = Image.open("grafico1.png")
img2 = Image.open("grafico2.png")
img3 = Image.open("grafico3.png")

# Redimensionar para mesma altura
altura = min(img1.height, img2.height, img3.height)
img1 = img1.resize((int(img1.width * altura / img1.height), altura))
img2 = img2.resize((int(img2.width * altura / img2.height), altura))
img3 = img3.resize((int(img3.width * altura / img3.height), altura))

# Criar imagem final
largura_total = img1.width + img2.width + img3.width
final = Image.new("RGB", (largura_total, altura))

# Colar lado a lado
x_offset = 0
for img in [img1, img2, img3]:
    final.paste(img, (x_offset, 0))
    x_offset += img.width

final.save("resultado_final.png")
print("Imagem final criada: resultado_final.png")
