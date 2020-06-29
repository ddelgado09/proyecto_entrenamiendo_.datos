'''
veggie cut
091 329 
autor: David A Herrera A
documentacion:
	este codigo hace parse segun las reglas
	primera parte es `Re: PREGUNTA-TITULO\n\n`
	segunda parte es `de\xa0NOMBRE-ESTUDIANTE\xa0- `
	tercera parte es `DIA, # de MES de AÑO, HH:MM\n\n\xa0\n\n`
	cuarta parte es `TEXTO-OPINION`
	quinta parte es n\nCalificacion maxima:\xa0-\n\nMostrar mensaje anterior\xa0|\xa0Editar\xa0|\xa0Borrar\xa0|\xa0Responder\n\n
'''
from ..clases import pazFormatter as pf
import re
target = open('log.txt', 'w')
target.truncate()

""" def parseall():
	path = ['word2014-II.docx','word2015-I.docx','word2015-II.docx','word2016-I.docx','word2016-II.docx']
	for p in path:
		parse(p)
	target.close() """

def parse(path):
	'''
	Lee el texto del archivo sin enlaces, acentos, ni puntuación
	Separado por estudiante, eliminando quinta parte
	'''	
	tx = pf.get_text(path)
	#limpieza
	tx = tx.replace('Final del formulario','')
	tx = tx.replace('Principio del formulario','')
	tx = tx.replace('Calificacion maxima','')	
	tx = re.sub('Mostrar.*?Responder', '\xa0Responder', tx)
	#separacion
	txls = re.split('\xa0Responder', tx, flags=re.DOTALL)
	report('========================***************************======================')
	report('========================***************************======================')
	report('========================***************************======================')
	report('========================***************************======================')
	report(path)
	
	'''
	Extraer cada parte de arriba
	'''
	spl = '\xa0'	
	students = {}
	for tx in txls:
		items = tx.split(spl)
		items = list(filter(lambda x: x != '\n\n', items))		#elimina multiples '\n\n'
		items = list(filter(lambda x: x != spl, items))		#elimina multiples '\n\n'
		info = []
		for i in items:
			info.append(' '.join(i.split()))	#elimina todo espacio redundante
		if len(info) < 3:
			break
		#title = get_title(map(lambda e: " ".join(e.split()), info[0])
		title = get_title(info[0])
		student_name = get_name(info[1])
		timestamp = get_time(info[2])
		opinion = get_opinion(info[3:])
		#if student_name not in students:
		students[(title,student_name,timestamp)] = ''.join(opinion)
		report(title)
		report(student_name)
		report(timestamp)
		report('========**************============')
		report('\n'.join(opinion))
		report('========**************============')
	return students

def end():
	target.close()

def report(str):
	target.write(str)
	target.write("\n")
	
def get_opinion(o):
	return o
		
def get_time(t):
	tm = t.split()
	t = list(filter(lambda x: x != 'de', tm))	#elimina multiples 'de'
	h_m = t[-1][:-2] + ':' + t[-1][-2:]
	t[-1] = h_m
	#separar hora
	return ' '.join(t)
		
def get_name(n):
	nl = n.split()
	'''
	si el nombre es duplicado, aparece igual al prinicipio y la mitad + 1
	'''
	mitad = int( len(nl) / 2 )
	if nl[0] == nl[mitad]:
		return ' '.join(nl[:mitad])
	else:
		return ' '.join(nl)

def get_title(t):
	'''
	\s* significa posibles espacios
	(.*?) guarda todo menos el Re y de,
	ejemplo: '  Re Pensamientos sobre la paz  de  '
	'''
	mo = re.match( r'^(Re)?(.*?)de$', t)
	if mo:
		return mo.group(2).strip()
	else:
		return t
	#for path in ['word2014-II.docx']:#,'word2015-I.docx','word2015-II.docx','word2016-I.docx','word2016-II.docx']
'''
if __name__ == "__main__": 
	main()
'''