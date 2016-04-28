xml_string = "<note><to>Tove</to><from>Jani</from><heading><test><deep>Reminder</deep></test></heading><body>Don't forget me this weekend!</body></note>"

cur_pos = 0;
level=0

class node(object):
    
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def res(self,level=0):
    	
    	count = 1
    	
    	for val in self.children:
    		strg = ""
    		if not val == None:
    			for i in range(0,level):
    				strg = strg+"	"

    			print strg,"parent = ",self.value
    			print strg,"child number= ",count
    			print strg,"child name=", val.value
    			print "\n"
    			count+=1;
    		
    		val.res(level+1)
    			





def check_for_open():
	global cur_pos

	if cur_pos>= len(xml_string):
		return [0,'']

	start=cur_pos+1
	signal = 0
	
	if(xml_string[cur_pos]=='<'):
		signal=1
		if not xml_string[cur_pos+1]=='/':
			cur_pos+=2
			while not (xml_string[cur_pos]=='>'):
				cur_pos+=1;
		else:
			result = [0,'']
			
			return result

	else:
		result = [0,'']
		
		return result

	if(signal==1):
		name = xml_string[start:cur_pos]

	result = [signal,name]
	return result



def check_for_close():
	global cur_pos
	if cur_pos>= len(xml_string):
		return [0,'']

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

	return result




	


def xml_parser(name):
	global cur_pos
	children = []
	
	while(cur_pos<len(xml_string)):
		while cur_pos<len(xml_string) and not xml_string[cur_pos]=='<' :
			if cur_pos < len(xml_string):
				cur_pos+=1
			else:
				return null


		
		a = check_for_open()
		if(cur_pos <len(xml_string)):
			if a[0]==0:
				b = check_for_close()
				if b[0]==1:
					result = node(name,children)
					return result
			else:
				cur_pos+=1
				if cur_pos < len(xml_string):
					children.append(xml_parser(a[1]))

				else:
					result = node(name,children)
					return result

		else:
			result =node (name,children)
			return result
		


a = xml_parser("root")
a.res()




