import seaborn.objects as so
from gapminder import gapminder

def plot():
    figura2 = (
        so.Plot(
            gapminder[gapminder["pop"]<1000000],
            x="lifeExp",
            y="gdpPercap",
            color="year",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida respecto a los ingresos en paises pequeños",
            x="Expectativa de Vida",
            y="Ingresos Per Capita",
            color="Año",
        )
              )
    return dict(
        descripcion="Expectativa de vida respecto a los ingresos en paises pequeños",
        autor="Bruno Festa",
        figura2=figura2,
    )
