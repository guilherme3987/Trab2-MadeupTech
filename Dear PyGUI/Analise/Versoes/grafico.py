import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Dados fornecidos
data_version = [
    ("2024-02-06 21:14:07 -0600", "v1.11.0"),
    ("2023-09-12 22:11:12 -0500", "v1.10.0"),
    ("2023-05-04 20:58:24 -0500", "v1.9.1"),
    ("2023-03-22 20:54:33 -0500", "v1.9.0"),
    ("2022-10-30 20:54:50 -0500", "v1.8.0"),
    ("2022-10-21 22:44:38 -0500", "v1.7.3"),
    ("2022-10-16 21:46:50 -0500", "v1.7.2"),
    ("2022-09-09 08:33:46 -0500", "v1.7"),
    ("2022-04-25 20:52:14 -0500", "v1.6"),
    ("2022-03-30 20:22:17 -0500", "v1.5.0"),
    ("2022-03-01 22:54:04 -0600", "v1.4.0"),
    ("2022-01-20 09:41:22 -0600", "v1.3.1"),
    ("2022-01-15 08:48:08 -0600", "v1.3"),
    ("2021-12-30 23:24:03 -0600", "v1.2"),
    ("2021-12-10 12:18:53 -0600", "v1.1.3"),
    ("2021-12-03 14:27:59 -0600", "v1.1.2"),
    ("2021-11-18 20:08:01 -0600", "v1.1.1"),
    ("2021-11-11 21:22:12 -0600", "v1.1"),
    ("2021-10-15 23:45:11 -0500", "v1.0.1"),
    ("2020-05-28 11:42:40 -0500", None),  # Sem versão associada
    ("2021-10-13 00:22:39 -0500", "v1.0.0"),
    ("2021-08-12 13:12:21 -0500", "v0.8.62"),
    ("2021-04-26 17:56:07 -0500", "v0.6.415"),
    ("2020-11-05 21:36:52 -0600", "v0.5.66"),
    ("2020-09-15 10:13:58 -0500", "v0.3.7"),
    ("2020-09-05 17:42:49 -0500", "v0.2.0"),
    ("2020-09-04 11:21:54 -0500", "v0.1.3"),
    ("2020-05-28 11:42:40 -0500", None),  # Repetido, sem versão associada
]

# Criando listas separadas para datas e versões
dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z") for date, _ in data_version]
versions = [version if version is not None else 'Sem versão' for _, version in data_version]

# Criação do gráfico
plt.figure(figsize=(12, 6))
plt.scatter(dates, versions, color='blue', marker='o')

# Ajustando os eixos
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)

# Adicionando títulos e labels
plt.title('Versões por Data')
plt.xlabel('Data')
plt.ylabel('Versão')

# Exibindo o gráfico
plt.tight_layout()
plt.show()