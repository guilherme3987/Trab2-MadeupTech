import matplotlib.pyplot as plt

# Lista de nomes de arquivos
file_names = [
    "docs/CHANGELOG.txt",
    "CMakeLists.txt",
    "DearPyGui/dearpygui/demo.py",
    "DearPyGui/dearpygui/core.pyi",
    "DearPyGui/src/core/AppItems/mvAppItem.h",
    "docs/README.md",
    "DearPyGui/src/core/AppItems/mvAppItem.cpp",
    "DearPyGui/cmake/dpg_sources.cmake",
    "DearPyGui/dearpygui/dearpygui.py"
]

# Lista de contagens de alterações
file_counts = [
    318,
    267,
    232,
    202,
    191,
    183,
    180,
    154,
    145
]

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(file_names, file_counts, color='skyblue')
plt.xlabel('Atividade (número de alterações)')
plt.ylabel('Arquivos')
plt.title('Arquivos mais ativos no diretório')
plt.gca().invert_yaxis()  # Inverter o eixo y para mostrar o maior no topo
plt.tight_layout()

# Exibir o gráfico
plt.show()
