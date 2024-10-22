import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = sns.load_dataset('tips')

plt.figure(figsize=(8,5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2")

plt.xlabel('Periodo (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Periodo (Almoco ou Jantar)')
plt.show()

# Gasto Medio por Periodo
sns.barplot(x='time', y='total_bill', data=df)

plt.xlabel('Periodo (Time)')
plt.ylabel('Media de Gastos')
plt.title('Media de Gastos por Periodo (Almoco ou Jantar)')
plt.show()


# Gorjeta Media por Periodo
sns.barplot(x='time', y='total_bill', data=df, palette="Set3")

plt.xlabel('Periodo (Time)')
plt.ylabel('Media da Gorjeta')
plt.title('Media da gorjeta por Periodo (Almoco ou Jantar)')
plt.show()