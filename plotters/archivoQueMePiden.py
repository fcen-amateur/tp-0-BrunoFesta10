import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Oceania"],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida en Oceanía",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países de Oceanía a lo largo del tiempo",
        autor="La cátedra",
        figura=figura,
    )

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
