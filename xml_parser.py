xml_string = "<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>"

cur_pos = 0;


class node(object):
    def __init__(self, value, children = [],attr=[]):
        self.value = value
        self.children = children


def check_for_open(cur_pos):
	
	start=cur_pos+1
	signal = 0
	name = ""
	if(xml_string[cur_pos]=='<'):
		signal=1
		while not (xml_string[cur_pos]=='>'):
			cur_pos+=1;

	if(signal==1):
		name = xml_string[start:cur_pos]

	result = (signal,name)
	
	return result



def check_for_close(cur_pos):
	start = cur_pos+1
	signal = 0
	name = ""

	if(xml_string[cur_pos]=='<'):
		if(xml_string[cur_pos]=='/'):
			signal = 1;
		while not (xml_string[cur_pos]=='>'):
			cur_pos+=1;

	if(signal == 1):
		name = xml_string[start:cur_pos]

	result= (signal,name)

	print result



	



def xml_parser():
	children = []
	name = ""



check_for_open(cur_pos)
check_for_close(cur_pos)


