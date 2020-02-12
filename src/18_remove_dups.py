def remove_dups(lst):
	hash = {}
	output = []
	for i in lst:
		if not i in hash:
			output.append(i)
			hash[i] = 1
			
		
remove_dups(["john", "taylor", "john"])
	