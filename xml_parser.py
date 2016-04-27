xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"

cur_pos = 0;


class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def res(self):
    	print self.value,self.children




def check_for_open():
	global cur_pos
	start=cur_pos+1
	signal = 0
	#name = "lol"
	if(xml_string[cur_pos]=='<'):
		signal=1
		if not xml_string[cur_pos+1]=='/':
			cur_pos+=2
			while not (xml_string[cur_pos]=='>'):
				cur_pos+=1;
		else:
			result = [0,'']
			#print 'ok'
			return result

	else:
		result = [0,'']
		#print result
		return result

	if(signal==1):
		name = xml_string[start:cur_pos]

	result = [signal,name]
	#print result
	return result



def check_for_close():
	global cur_pos
	start = cur_pos+2
	signal = 0
	name = ""

	if(xml_string[cur_pos]=='<'):
		
		if(xml_string[cur_pos+1]=='/'):
			cur_pos+=1;
			signal = 1;
			while not (xml_string[cur_pos]=='>'):
				cur_pos+=1;
		else:
			result = [signal,'']
			return result


	if(signal == 1):
		name = xml_string[start:cur_pos]

	result= [signal,name]

	print result

	return result




	


def xml_parser(name):
	global cur_pos
	children = []
	
	while not xml_string[cur_pos]=='<' :
		cur_pos+=1

	print "kk",cur_pos
	a = check_for_open()
	#cur_pos+=1
	#print 'ff',cur_pos
	#while not xml_string[cur_pos]=='<' :
	#	cur_pos+=1
	#print cur_pos,"yy"

	b = check_for_close()
	print "->",a
	print cur_pos
	print "-->",b

	if a[0]==1:
		cur_pos+=1
		print cur_pos
		print 'wrong'
		if cur_pos < len(xml_string):
			children.append(xml_parser(a[1]))

		else:
			result = node(name,children)
			
			return result

	if b[0]==1:
		result = node(name,children)
		return result
		


#cur_pos=14
#check_for_close()
xml_parser("root")

