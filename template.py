from parser import parse

def helper(test):
	# solution code here
	return test

# schema here
schema = [(),[]]

num_tests,tests = parse(schema)
for case,test in enumerate(tests):
	sol = helper(test)
	print 'Case #{}: {}'.format(case+1, sol)
