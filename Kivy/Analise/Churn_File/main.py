import matplotlib.pyplot as plt

# Dados fornecidos
arquivos = [
    "kivy/uix/textinput.py", "setup.py", "kivy/core/window/__init__.py", 
    "kivy/data/style.kv", "kivy/uix/widget.py", "kivy/__init__.py", 
    "kivy/uix/scrollview.py", "kivy/lang.py", "kivy/properties.pyx", 
    "kivy/core/text/__init__.py", "kivy/uix/label.py", "kivy/app.py", 
    ".travis.yml", "kivy/uix/listview.py", "kivy/config.py", 
    "kivy/core/window/window_sdl2.py", "kivy/core/image/__init__.py", 
    "kivy/graphics/texture.pyx", "kivy/uix/screenmanager.py"
]

churn = [
    401, 388, 333, 280, 228, 221, 216, 210, 206, 185, 
    178, 163, 163, 158, 157, 144, 140, 138, 134
]

# Criando o gráfico de barras
plt.figure(figsize=(10, 7))
plt.barh(arquivos, churn, color='skyblue')
plt.xlabel("Churn")
plt.ylabel("Arquivos")
plt.title("Arquivos com Mais Churn")
plt.tight_layout()

# Exibindo o gráfico
plt.show()
