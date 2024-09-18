import matplotlib.pyplot as plt

# Listas de nomes e quantidades
nomes = [
    "docs/CHANGELOG.txt",
    "CMakeLists.txt",
    "DearPyGui/dearpygui/demo.py",
    "DearPyGui/dearpygui/core.pyi",
    "DearPyGui/src/core/AppItems/mvAppItem.h",
    "docs/README.md",
    "DearPyGui/src/core/AppItems/mvAppItem.cpp",
    "DearPyGui/cmake/dpg_sources.cmake",
    "DearPyGui/dearpygui/dearpygui.py",
    "DearSandbox/sandbox.py",
    "DearPyGui/src/Core/mvMarvel.cpp",
    "DearPyGui/src/core/AppItems/plots/mvPlot.cpp",
    "DearPyGui/src/core/mvApp.cpp",
    "MarvelSandbox/App.py",
    "DearPyGui/src/core/AppItems/mvItemRegistry.cpp",
    "DearPyGui/src/core/AppItems/containers/mvWindowAppItem.cpp",
    "docs/CHANGELOG.md",
    "DearPyGui/src/core/AppItems/nodes/mvNodeEditor.cpp",
    "DearSandbox/Demo.py"
]

quantidades = [
    318,
    267,
    232,
    202,
    191,
    183,
    180,
    154,
    145,
    144,
    129,
    128,
    125,
    122,
    122,
    121,
    107,
    96,
    91
]

# Criar gráfico de barras
plt.figure(figsize=(12, 6))
plt.barh(nomes, quantidades, color='skyblue')
plt.xlabel('Quantidade de Churn')
plt.title('Arquivos com Mais Churn')
plt.gca().invert_yaxis()  # Inverter a ordem dos arquivos para melhor visualização
plt.show()
