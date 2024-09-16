import matplotlib.pyplot as plt

# Dados dos arquivos mais ativos
arquivos_ativos = [
    "kivy/uix/textinput.py", "setup.py", "kivy/core/window/__init__.py", 
    "kivy/data/style.kv", "kivy/uix/widget.py", "kivy/__init__.py", 
    "kivy/uix/scrollview.py", "kivy/lang.py", "kivy/properties.pyx"
]

atividade = [401, 388, 333, 280, 228, 221, 216, 210, 206]

# Criando o gráfico de barras para os arquivos mais ativos
plt.figure(figsize=(8, 6))
plt.barh(arquivos_ativos, atividade, color='lightcoral')
plt.xlabel("Atividade")
plt.ylabel("Arquivos")
plt.title("Arquivos Mais Ativos")
plt.tight_layout()

# Exibindo o gráfico
plt.show()
