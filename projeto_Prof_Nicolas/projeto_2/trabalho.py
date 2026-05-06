import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.models import HoverTool

sin = "sin(t)"
cos = "cos(t)"
t = np.linspace(0, 10,400)   
y1 = np.sin(t)
y2 = np.cos(t)
df = pd.DataFrame({
    sin: y1,
    cos: y2
})

print("Data:")
print(df)

corr_matrix = df.corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

#criar heatmap da matriz de correlação usando seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".3f")
plt.title("Correlation Matrix Heatmap (Seaborn)")
plt.show()

#criar gráfico de linha usando plotly
fig = px.line(
    df,
    x=t,
    y=[sin, cos],
    markers=True,
    title="seno e coseno no Plotly"
)
fig.show()

#criar gráfico de linha usando bokeh
p = figure(
    title="seno e coseno no Bokeh",
    x_axis_label="t",
    y_axis_label="value",
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

line1 = p.line(t, y1, legend_label=sin, line_width=2)
circle1 = p.scatter(t, y1, size=8, legend_label=sin)

line2 = p.line(t, y2, legend_label=cos, line_width=2)
circle2 = p.scatter(t, y2, size=8, legend_label=cos)

#ao passar o rato apaarece o t e o valor correspondente
hover = HoverTool(tooltips=[
    ("t", "$x"),
    ("value", "$y")
])
p.add_tools(hover)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

show(p)