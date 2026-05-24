
import pandas as pd
import matplotlib.pyplot as plt
# Cargar datos
df = pd.read_csv('datos/ventas.csv')
df['sales_date'] = pd.to_datetime(df['sales_date'])
# Calcular indicadores
ventas_totales = df['amount'].sum()
producto_mas_vendido = df.groupby('product')['quantity'].sum().idxmax()
print(f'Ventas Totales: ${ventas_totales}')
print(f'Producto más vendido: {producto_mas_vendido}')
# Generar gráfico
df.groupby('sales_date')['amount'].sum().plot(kind='line', marker='o')
plt.title('Evolución de Ventas 2024')
plt.xlabel('Fecha')
plt.ylabel('Monto ($)')
plt.savefig('resultados/grafico_ventas.png')
