import json

with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento = dados['faturamento']
faturamento_filtrado = [valor for valor in faturamento if valor > 0]
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
dias_acima_da_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print('Menor faturamento: R$ ' + str(menor_faturamento))
print('Maior faturamento: R$ ' +  str(maior_faturamento))
print('Número de dias com faturamento acima da média: ' + str(dias_acima_da_media))
