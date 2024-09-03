Lista = ['67.836,43','36.678,66','29.229,88','27.165,48','19.849,53']
total = 0

for item in Lista:
    Valor_por_estado = float(item.replace('.', '').replace(',', '.'))
    total += Valor_por_estado
for item in Lista:
    Valor_por_estado = float(item.replace('.', '').replace(',', '.'))
    porcentagem = (Valor_por_estado / total) * 100
    print(f"Valor: R${Valor_por_estado:,.2f} - Porcentagem do total: {porcentagem:.2f}%")