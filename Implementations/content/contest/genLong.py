# filenames = 
# '../data-structures/STL (5)/IndexedSet.h', '../number-theory (11.1)/Modular Arithmetic/ModInt.h'

def write_to(name, filenames):
	with open(name, 'w') as outfile:
		res = []
		active = False
		def ad(line):
			nonlocal active
			if line.startswith('#include "'):
				return
			if line.startswith("#include <bits/stdc++.h>"):
				res.append("""#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <complex>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <vector>
#include <climits>
""")
				return
			if line.startswith('/**'): 
				active = True
			if active and '*/' in line:
				active = False 
				return
			# line = line.replace('/// ','')
			line = line.replace('/**','')
			line = line.replace('*/','')
			if active:
				return
			if line.endswith("//\n"):
				line = line[:-3]+"\n"
			res.append(line)
			if not res[-1].endswith('\n'):
				res[-1] += '\n'
			while len(res) > 1 and len(res[-1]) <= 1 and len(res[-2]) <= 1:
				res.pop()
			# if len(res) > 1:
				# print("REC",res[-2],res[-1],len(res[-2]),len(res[-1]))

		extra = []
		for fname in filenames:
			with open(fname) as infile:
				v = []
				for line in infile:
					v.append(line)
				print("IMPORTING",fname)
				if fname == 'Template.cpp':
					foundMain = False
					for i in range(len(v)):
						line = v[i]
						if "// IGNORE" in line:
							continue
						if "int main()" in line:
							foundMain = True
						if not foundMain:
							ad(line)
						else:
							extra.append(line)
				else:
					for line in v:
						# print("OOPS",line)
						ad(line)
			ad('\n')
		for line in extra:
			ad(line)
		ind = res[-1].find("cin.tie(0)->")
		res[-1] = res[-1][:ind-1]+"\n\t// read read read\n\tsetIO();\n\t\n"

		res.append('	// you should actually read the stuff at the bottom\n')
		res.append('}\n\n')
		res.append("""/* stuff you should look for
	* int overflow, array bounds
	* special cases (n=1?)
	* do smth instead of nothing and stay organized
	* WRITE STUFF DOWN
	* DON'T GET STUCK ON ONE APPROACH
*/""")
		for line in res:
			outfile.write(line)

write_to('TemplateLong.cpp',['Template.cpp', 'CppIO.h'])
write_to('TemplateLong_Old.cpp',['Template.cpp', 'CppIO_Old.h'])