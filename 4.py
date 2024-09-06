faturamento = [{'regiao':'SP', 'ganho':'67836,43'},{'regiao':'RJ','ganho':'36678,66'},{'regiao':'MG' ,'ganho':'29229,88' },{'regiao':'ES' ,'ganho':'27165,48' },{'regiao':'Outros' ,'ganho':'19849,53' }]
total = 0
for i in range(len(faturamento)):
        ganho = float(faturamento[i]['ganho'].replace(',','.'))
        total = total + ganho
for y in range(len(faturamento)):
        ganho = float(faturamento[y]['ganho'].replace(',','.'))
        porcentagem = (ganho*100)/total
        print(f'{faturamento[y]['regiao']} : {porcentagem}%')


