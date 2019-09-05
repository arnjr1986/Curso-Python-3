#Valor em metros, convertido em cm e mm

medida = float(input('Medida em metros: '))
cm = medida * 100
mm = medida *1000

print('A medida de {}m corresponde à {}cm e {}mm.'.format(medida,cm,mm))

print('\nExtra')
km = medida/1000
hm = medida/100
dam = medida/10
dec = medida*10

print('A medida de {}m correspone à {}km, {}hm, {}dam, {}dec'.format(medida,km,hm,dam,dec))
