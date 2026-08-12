port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}

port = 'alface'

if port in port2eng:
    eng = port2eng[port]
    print(f'{port} em inglês é {eng}')
else:
    print(f'A palavra {port} não existe no dicionário')
