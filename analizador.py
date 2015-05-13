Alfabeto = ['a','b','c','resultado','imprime','=','(',')','_','+','0','1','2','3','4','5','6','7','8','9','10']
PalabrasReservadas=['imprime']
Identificadores=['a','b','c','resultado']
ConstantesNumericas=['0','1','2','3','4','5','6','7','8','9','10']
ConstantesAlfa=['a','b','c','resultado']
Operadores=['=','+']
Delimitadores=['=','(',')','_','+']

linea = raw_input("Ingresa Linea: ")
a = list(linea)
A=0
P=0
I=0
C=0
CA=0
O=0
D=0
var=''

print a
clave=1
TablaSimbolos={}
for i in a:
	TablaSimbolos[clave]=i
	clave=clave+1

	
print TablaSimbolos.keys()

print '-----------------------------------'
for k,v in TablaSimbolos.items():
	print("Clave: {0}, Simbolo=({1})".format(k,v))

print '-----------------------------------'

for i in a:
	if i in Alfabeto:
		if i in PalabrasReservadas:
				print 'Es PalabrasReservadas ' + i
		elif i in Identificadores:
			print 'Es Identificador ' + i
		elif i in ConstantesNumericas:
			print 'Es ConstantesNumericas ' + i
		elif i in ConstantesAlfa:
			print 'Es ConstantesAlfa ' + i
		elif i in Operadores:
			print 'Es Operadores ' + i
		elif i in Delimitadores:
			print 'Es Delimitadores ' + i
	else:
		print 'Error, caracter no definido: ' + i



