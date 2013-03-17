# coding:utf8

dictNFA = {
	'q1': {	'e': ['q2', 'q11'],	'0': [''],	'1': [''], 'acep': False,	'start': True	},
	'q2': {	'e': ['q3', 'q5'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q3': {	'e': [''],	'0': [''],	'1': ['q4'], 'acep': False,	'start': False	},
	'q4': {	'e': ['q5', 'q3'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q5': {	'e': [''],	'0': ['q6'],	'1': [''], 'acep': False,	'start': False	},
	'q6': {	'e': ['q7', 'q9'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q7': {	'e': [''],	'0': [''],	'1': ['q8'], 'acep': False,	'start': False	},
	'q8': {	'e': ['q9', 'q7'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q9': {	'e': [''],	'0': ['q10'],	'1': [''], 'acep': False,	'start': False	},
	'q10': {	'e': ['q11', 'q2'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q11': {	'e': ['q12', 'q14'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q12': {	'e': [''],	'0': [''],	'1': ['q13'], 'acep': False,	'start': False	},
	'q13': {	'e': ['q14', 'q12'],	'0': [''],	'1': [''], 'acep': False,	'start': False	},
	'q14': {	'e': [''],	'0': [''],	'1': [''], 'acep': True,	'start': False	},
}

dictDFA = {
	# '1': {	'0': '', '1': ''	},
	# '2': {	'0': '', '1': ''	},
	# '3': {	'0': '', '1': ''	},
	# '4': {	'0': '', '1': ''	},
	# '5': {	'0': '', '1': ''	},
}

# 友情帮助

# NFA to DFA
# NFAtoDFA第er阶段
qA = ['q1', 'q3', 'q2', 'q5', 'q14', 'q11', 'q12']
qB = ['q9', 'q7', 'q6']
qC = ['q3', 'q5', 'q4', 'q14', 'q13', 'q12']
qD = ['q3', 'q2', 'q5', 'q14', 'q11', 'q10', 'q12']
qE = ['q9', 'q8', 'q7']

# 这个是这个阶段要到达的最后答案，结构如下：
dictDFAend = {
	str(qA): { '0': 0, '1': 1, 'start': False, 'acep': False },
	str(qB): { '0': 0, '1': 1, 'start': False, 'acep': False },
	str(qC): { '0': 0, '1': 1, 'start': False, 'acep': False },
	str(qD): { '0': 0, '1': 1, 'start': False, 'acep': False },
	str(qE): { '0': 0, '1': 1, 'start': False, 'acep': False },
}

# 这个阶段输出的最后答案是，如下：（已完成)
dictDFAendend = {
	"['q9', 'q8', 'q7']": {'1': ['q9', 'q8', 'q7'], '0': ['q3', 'q2', 'q5', 'q14', 'q11', 'q10', 'q12'], 'acep': False, 'start': False}, 
	"['q9', 'q7', 'q6']": {'1': ['q9', 'q8', 'q7'], '0': ['q3', 'q2', 'q5', 'q14', 'q11', 'q10', 'q12'], 'acep': False, 'start': False}, 
	"['q3', 'q2', 'q5', 'q14', 'q11', 'q10', 'q12']": {'1': ['q3', 'q5', 'q4', 'q14', 'q13', 'q12'], '0': ['q9', 'q7', 'q6'], 'acep': True, 'start': False}, 
	"['q3', 'q5', 'q4', 'q14', 'q13', 'q12']": {'1': ['q3', 'q5', 'q4', 'q14', 'q13', 'q12'], '0': ['q9', 'q7', 'q6'], 'acep': True, 'start': False}, 
	"['q1', 'q3', 'q2', 'q5', 'q14', 'q11', 'q12']": {'1': ['q3', 'q5', 'q4', 'q14', 'q13', 'q12'], '0': ['q9', 'q7', 'q6'], 'acep': True, 'start': True}
}

# minimum DFA
# 这个是这个阶段要到达的最后答案
minDFAend = {
	'q1': { '0': 'q2', '1': 'q1', 'start': True, 'acep': False },
	'q2': { '0': 'q1', '1': 'q2', 'start': False, 'acep': True },
}

# print dictNFA
# print dictNFA['q1']
# print dictNFA['q1']['e']
# print dictNFA['q1']['e'][0]

# ==============================================程序从这里开始========================================
# write by Lincoln
# NFA to DFA
def NFAtoDFA():
	print "This is NFAtoDFA function:"
	global tmpI
	tmpI = []
	tmp0 = []
	tmp1 = []
	tmp2 = []
	tmp3 = []
	tmp4 = []

	# NFAtoDFA第一阶段
	def loopE(xNFA, xe, tmpII): # 输出e（不消耗）的值	
		if dictNFA[xNFA]['start']:
			if xe == u'e':
				# print xNFA
				tmpII.append(xNFA)

		loopB(xNFA, xe, tmpII)
		tmpII = list(set(tmpII))
		return tmpII

	def loopB(xNFA, xe, tmpInI):	# xNFA是I列表，xe是消耗（a或b或不消耗），tmpInI是最后生成的列表
		for x in xrange(0, len(dictNFA[xNFA][xe])):
			firstDict = dictNFA[xNFA][xe][x]
			if dictNFA[xNFA][xe][x]:
				# print dictNFA[xNFA][xe][x]
				pass
			try:
				loopB(firstDict, xe, tmpInI)
				loopB(firstDict, 'e', tmpInI)
				tmpInI.append(dictNFA[xNFA][xe][x])				
			except:
				break		
		tmpInI = list(set(tmpInI))
		return tmpInI

	def loopNFAtoDFA(tmpIII):	#tmpIII统一输入
		tmpIIIa = []
		tmpIIIb = []
		for x in xrange(0, len(tmpIII)):
			tmpIIIa = loopB(tmpIII[x], '0', tmpIIIa)
			tmpIIIb = loopB(tmpIII[x], '1', tmpIIIb)
		dictDFA.update({ str(tmpIII): { '0': tmpIIIa, '1': tmpIIIb, 'start': False, 'acep': False } })
		def seachStartOrAccept(startOrAccept):	#这个是用来查账它开始start或者结束accept（accept就是两个圈）
			for x in xrange(0, len(dictNFA.keys())):
				if dictNFA.values()[x][startOrAccept]:
					return dictNFA.keys()[x]
		# print seachStartOrAccept('start')
		# print seachStartOrAccept('acep')
		# print 'hehe'
		if seachStartOrAccept('start') in tmpIII:
			dictDFA[str(tmpIII)]['start'] = True
		if seachStartOrAccept('acep') in tmpIII:
			dictDFA[str(tmpIII)]['acep'] = True
		# print str(tmpIIIa) not in dictDFA.keys()
		# print str(tmpIIIb) not in dictDFA.keys()
		if str(tmpIIIa) not in dictDFA.keys():
			loopNFAtoDFA(tmpIIIa)
		if str(tmpIIIb) not in dictDFA.keys():	
			loopNFAtoDFA(tmpIIIb)

	tmp0 = loopE('q1', 'e', tmp0)	# tmpI是原始数组， tmp0第一个数组，就是I

	loopNFAtoDFA(tmp0)	# 开始执行NFA to DFA

	print '-'*50
	print '-'*50

	print 'This part is the tuple of DFA(as q1, q2, q3, q4, q5)'
	print dictDFA.keys()
	print 'x'*50
	print 'NFA to DFA result(finish):'
	print dictDFA 	# 这个是这个阶段最后答案
	print 'x'*50

# NFAtoDFA print is 1 2 3 5 11 12 14

# Minimun DFA
def minDFA():
	print "This is minDFA function:"

	# minDFA第一阶段
	minDFA = {
		'q1': { '0': 'q2', '1': 'q1', 'start': True, 'acep': False },
		'q2': { '0': 'q1', '1': 'q2', 'start': False, 'acep': True },
	}
	print minDFA

	pass


print 'programme running'
print 'NFA input is:'
print dictNFA
print '='*80
NFAtoDFA()

print '-'*80
print 'you know it(try to do)'
minDFA()
print '='*80
print 'programme end'

# ==============================================程序在这里结束========================================