import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from bokeh.io import output_notebook

t = np.linspace(0, 10,400)   
y1 = np.sin(t)
y2 = np.cos(t)

df = pd.DataFrame({
    "sin(t)": y1,
    "cos(t)": y2
})

print("Data:")
print(df)

corr_matrix = df.corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".3f")
plt.title("Correlation Matrix Heatmap (Seaborn)")
plt.show()

fig = px.line(
    df,
    x=t,
    y=["sin(t)", "cos(t)"],
    markers=True,
    title="seno e coseno no Plotly"
)
fig.show()

p = figure(
    title="seno e coseno no Bokeh",
    x_axis_label="t",
    y_axis_label="value",
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

line1 = p.line(t, y1, legend_label="sin(t)", line_width=2)
circle1 = p.scatter(t, y1, size=8, legend_label="sin(t)")

line2 = p.line(t, y2, legend_label="cos(t)", line_width=2)
circle2 = p.scatter(t, y2, size=8, legend_label="cos(t)")

hover = HoverTool(tooltips=[
    ("t", "$x"),
    ("value", "$y")
])
p.add_tools(hover)

p.legend.location = "top_left"
p.legend.click_policy = "hide"

show(p)