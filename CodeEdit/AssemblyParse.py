def to_array(assembly_file, list):
	
	f = open(assembly_file, "r");
	x = f.readlines()
	f.close()
	for i in x:
		list.append(i.replace("\t","").replace("\n",""))
		
def refine(list1,list2):
	check = False;
	keyword=["movl","addl","call"]
	for x in list1:
		if x == "call___main":
			check = True;
		for i in keyword:
			if check == True and i in x:
				value =x.replace(i,"")
				list2.append([i,value[:value.find(",")],value[value.find(",")+2:]])
			
				


test = []
to_array("code.s",test)
print(test)
test2 = []
refine(test,test2)
print(test2)