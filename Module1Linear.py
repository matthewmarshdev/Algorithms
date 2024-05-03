Tuple = (1, 2, 'trouble', 4, 'linear', 7, 45, 'declare', 'classtest45', 6) 

n = 'Geeks'

def search(Tuple, n): 

	for i in range(len(Tuple)): 
		if Tuple[i] == n: 
			return True
	return False

if search(Tuple, n): 
	print("Found") 
else: 
	print("Not Found") 
