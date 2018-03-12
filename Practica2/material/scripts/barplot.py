import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../investors.csv')

gridspec_kw = dict(height_ratios = [1,5])

print(data)
f, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, sharex=True, gridspec_kw=gridspec_kw)
ax = sns.barplot(x='Nombre', y='Porcentaje de acciones en circulación', data=data, ax=ax1)
ax = sns.barplot(x='Nombre', y='Porcentaje de acciones en circulación', data=data, ax=ax2)

ax1.set_ylim(58, 60)
ax2.set_ylim(0, 6)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)

plt.show()
