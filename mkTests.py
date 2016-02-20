import subprocess

COMPILER = r"..\bin_demo\Compiler.exe"
VM = r"..\bin_demo\VirtualMachine.exe"

def run(test):
	testtext = "\n".join(test.test)
	testfile = open(test.name + ".el", "w")
	testfile.write(testtext)
	testfile.close()

	subprocess.check_output([COMPILER, test.name + ".el", test.name + ".elc"])
	output = subprocess.check_output([VM, test.name + ".elc"])
	return output


class Test(object):
	name = None
	description = None
	output = None
	throws = None
	test = []

	def __init__(self, name, description, output, throws, test):
		self.name = name
		self.description = description
		self.output = output
		self.test = test
		self.throws = throws

text = open("BehaviouralSpecification").readlines()

cTest = None
cDesc = None
cOutput = ""
cThrows = None
test = []

tests = []

for line in text:
	line = line.strip()
	if line.startswith("#Test "):
		cTest = line[6:]
	elif line.startswith("#Description "):
		cDesc = line[13:]
	elif line.startswith("#Output "):
		cOutput = line[8:]
	elif line.startswith("#Throws "):
		cThrows = line[8:]
	elif line == "":
		tests.append(Test(cTest, cDesc, cOutput, cThrows, test))
		cTest = None
		cDesc = None
		cOutput = ""
		cThrows = None
		test = []
	else:
		test.append(line)

passes = 0;
fails = 0;

failures = []
for test in tests:
	print "name ", test.name
	print "description ", test.description
	try:
		result = run(test)
		if result.strip() == test.output:
			print "passes!"
			passes += 1
		else:
			fails += 1
			print "fails: ", result, "!=", test.output
			failures.append(test)
	except subprocess.CalledProcessError as e:
		if test.throws != None and test.throws in e.output:
			print "passes! (Ex)"
			passes += 1
		else:
			fails += 1
			print "fails! (Ex)"
			failures.append(test)
	print "============"

print "Passed tests: ", passes
print "Failed tests: ", fails
for fail in failures:
	print "    ", fail.name