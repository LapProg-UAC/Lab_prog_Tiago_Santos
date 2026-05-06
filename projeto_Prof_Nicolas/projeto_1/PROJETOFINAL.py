from matplotlib.figure import Figure
import pandas as pd
from PIL import Image
import plotly.express as px

def upload_data():
    """
    Uploads the datasets for penguins and CO2 levels.
    Returns:
        pinguins (DataFrame): Dataset of penguins.
        co2 (DataFrame): Dataset of CO2 levels.
    """
    pinguins = pd.read_csv("projeto_Prof_Nicolas/projeto_1/pinguins_palmer.csv")
    co2 = pd.read_csv("projeto_Prof_Nicolas/projeto_1/co2_maunaloa.csv")
    return pinguins, co2

pinguins, co2 = upload_data()

def plot_penguins(pinguins: pd.DataFrame) -> Figure:
    """
    Plots a scatter graph of penguin flipper length vs body mass, colored by species.
    param:
        pinguins (DataFrame): Dataset of penguins.
        return:
            fig (Figure): Scatter plot of penguins.
    """
    fig = px.scatter(
        pinguins,
        x="barbatana",
        y="massa",
        color="especie",
        title="Pinguins"
    )
    fig.write_image("projeto_Prof_Nicolas/projeto_1/grafico1.png")
    return fig

def plot_co2(co2: pd.DataFrame) -> Figure:
    """
    Plots a line graph of CO2 levels over time.
    param:
        co2 (DataFrame): Dataset of CO2 levels.
    return:
        fig (Figure): Line plot of CO2 levels over time.
    """
    co2_grouped = co2.groupby("ano")["ppm"].mean().reset_index()
    fig2 = px.line(
        co2_grouped,
        x="ano",
        y="ppm",
        title="CO2 ao longo do tempo"
    )
    fig2.write_image("projeto_Prof_Nicolas/projeto_1/grafico2.png")
    return fig2

def plot_massa_co2(pinguins: pd.DataFrame, co2: pd.DataFrame) -> Figure:
    """
    Plots a scatter graph of estimated penguin mass vs CO2 levels, and calculates the correlation.
    param:
        pinguins (DataFrame): Dataset of penguins.
        co2 (DataFrame): Dataset of CO2 levels.
    return:
        fig (Figure): Scatter plot of estimated mass vs CO2 levels with correlation in the title.
    """
    co2_grouped = co2.groupby("ano")["ppm"].mean().reset_index()
    co2_grouped["massa_estimada"] = pinguins["massa"]
    print(co2_grouped)
    fig3 = px.scatter(
        co2_grouped,
        x="ppm",
        y="massa_estimada",
        title=f"Estimativa Massa vs CO2 (Correlação: {co2_grouped['ppm'].corr(co2_grouped['massa_estimada']):.2f})"
    )
    fig3.write_image("projeto_Prof_Nicolas/projeto_1/grafico3.png")
    return fig3

def combine_images() -> Figure:
    """
    Combines the three generated graphs into a single image.
    return:
        final (Figure): Combined image.
    """

    img1 = Image.open("projeto_Prof_Nicolas/projeto_1/grafico1.png")
    img2 = Image.open("projeto_Prof_Nicolas/projeto_1/grafico2.png")
    img3 = Image.open("projeto_Prof_Nicolas/projeto_1/grafico3.png")

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
    final.save("projeto_Prof_Nicolas/projeto_1/resultado_final.png")
    print("Imagem final criada: resultado_final.png")
    return final

def main():
    pinguins, co2 = upload_data()
    plot_penguins(pinguins)
    plot_co2(co2)
    plot_massa_co2(pinguins, co2)
    combine_images()

if __name__ == "__main__":
    main()