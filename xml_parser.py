from Tkinter import *

#xml_string = "<breakfast_menu><food><name>Belgian Waffles</name><price>$5.95</price><description>Our famous Belgian Waffles with plenty of real maple syrup</description><calories>650</calories></food><food><name>French Toast</name><price>$4.50</price><description>Thick slices made from our homemade sourdough bread</description><calories>600</calories></food><food><name>Homestyle Breakfast</name><price>$6.95</price><description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description><calories>950</calories></food></breakfast_menu>"
xml_file = open("my_xml.txt","r+")
xml_string = xml_file.read();
xml_file.close()
cur_pos = 0;
level=0

class node(object):
    
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def res(self,level=0):
    	
    	count = 1
    	global text
    	for val in self.children:
    		strg = ""
    		if not val == None:
    			for i in range(0,level):
    				strg = strg+"	"
    			line = ""
    			line = strg+"parent = "+self.value+"\n"
    			text.insert(INSERT, line)
    			line = strg+"child number= "+str(count)+"\n"
    			text.insert(INSERT, line)
    			line = strg+"child name= "+str(val.value)+"\n"
    			text.insert(INSERT, line)
    			line = "\n"
    			text.insert(INSERT, line)

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
		





def onclick():
   pass



a = xml_parser("root")
root = Tk()
text = Text(root,width=200,height=60)
a.res()
text.insert(END, "Parsing complete")
text.pack()
root.mainloop()






