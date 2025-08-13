import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --------------------
# Parâmetros da simulação
# --------------------
GRID_SIZE = 30
DENSIDADE_INICIAL = 0.3
INTERVALO_MS = 300
FRAMES = 100
OBSTACULOS = [(5,5), (10,15), (20,20), (15,8)]  # posições fixas de árvores/estruturas

# Inicializa a grade: 0 = vazio, 1 = pessoa, 2 = obstáculo
grade = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[1-DENSIDADE_INICIAL, DENSIDADE_INICIAL])
for x, y in OBSTACULOS:
    grade[x, y] = 2  # obstáculo

# Mapa de cores: branco = vazio, vermelho = pessoa, verde = obstáculo
cmap = ListedColormap(['white', 'red', 'green'])

def atualizar(frame_num, img, grade):
    nova_grade = grade.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grade[i, j] == 2:
                continue

            vizinhos = np.sum(grade[max(i-1,0):min(i+2,GRID_SIZE), max(j-1,0):min(j+2,GRID_SIZE)] == 1) - (grade[i,j]==1)
            
            if grade[i, j] == 1:
                if vizinhos < 2 or vizinhos > 3:
                    nova_grade[i, j] = 0
            else:
                if vizinhos == 3:
                    nova_grade[i, j] = 1

    img.set_data(nova_grade)
    grade[:] = nova_grade[:]
    return img

fig, ax = plt.subplots()
img = ax.imshow(grade, interpolation='nearest', cmap=cmap)
ax.set_title("Fluxo de Pessoas na Praça Pública com Obstáculos")
ax.axis("off")

ani = animation.FuncAnimation(fig, atualizar, fargs=(img, grade), frames=FRAMES, interval=INTERVALO_MS, save_count=50)

# Salvar como GIF
ani.save("fluxo_pessoas_praca_obstaculos.gif", writer='pillow')
print("GIF salvo como fluxo_pessoas_praca_obstaculos.gif")
plt.show()