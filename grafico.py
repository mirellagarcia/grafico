#Grafico
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter 

#Criar dados para o eixo X
np.random.seed(19680800)

X = np.linspace(0.5, 7, 150)
X

# Criar dados para a função Y1
Y1 = 4+np.cos(X)
Y1

# Criar dados para a função Y2
Y2 = 3.1+np.cos(3.1+X/0.5)/2
Y2

# Criar dados para a função Y3
Y3 = np.random.uniform(Y1, Y2, len(X))
Y3

# Função para rotular ticks
def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x

# Função para criar círculos
def circle(x, y, radius=0.15):
    from matplotlib.patches import Circle
    from matplotlib.patheffects import withStroke
    circle = Circle((x, y), radius, clip_on=False, zorder=10, linewidth=1,
                    edgecolor='black', facecolor=(0, 0, 0, .0125),
                    path_effects=[withStroke(linewidth=5, foreground='w')])
    ax.add_artist(circle)

# Função para criar rótulos
def text(x, y, text):
    ax.text(x, y, text, backgroundcolor="white",
            ha='center', va='top', weight='bold', color='blue')

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, aspect=1)

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))
ax.yaxis.set_minor_formatter(FuncFormatter(minor_tick))


ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0, labelsize=8)
ax.tick_params(which='minor', length=5, labelsize=8, labelcolor='0.5')

ax.grid(linestyle="--", linewidth=0.5, color='0', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Limite superior", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Limite inferior")
ax.plot(X, Y3, linewidth=0, 
        marker='P', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Mirella Eloize Morais Garcia", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Título do eixo X")
ax.set_ylabel("Título do eixo Y")

ax.legend()

# Marca Menor
circle(1, 1)
text(1, 0.75, "2101065")

color = 'blue'
ax.annotate('bordas', xy=(4.0, 0.35), xycoords='data',
            xytext=(3.3, 0.5), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

ax.annotate('', xy=(3.15, 0.0), xycoords='data',
            xytext=(3.45, 0.45), textcoords='data',
            weight='bold', color=color,
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color=color))

#Colocar texto
ax.text(4.0, -0.4, "Made with http://matplotlib.org",
        fontsize=10, ha="right", color='0.5')

#plt.show()
#Salvar o arquivo
from google.colab import files
plt.savefig("Hands_On_Matplotlib.png")
files.download("Hands_On_Matplotlib.png")
