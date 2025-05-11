
import matplotlib.pyplot as plt
from statsmodels.datasets import grunfeld
import random

data = grunfeld.load()
firms = data.data['firm']
year = data.data['year']
invest = data.data['invest']

firmi = list(set(firms))
izbraniy = random.sample(firmi, 3)

for firm in izbraniy:
    firm_years = []
    firm_invest = []
    for i in range(len(firms)):
        if firms[i] == firm:
            firm_years.append(year[i])
            firm_invest.append(invest[i])

    plt.plot(firm_years, firm_invest, '-', label=f'Фирма {firm}')

plt.title('Динамика инвестиций по фирмам')
plt.xlabel('Год')
plt.ylabel('Сумма инвестиций')
plt.legend()
plt.show()