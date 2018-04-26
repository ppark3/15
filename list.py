def minimum(password):
	upper = [x for x in password if x.isupper()]
	lower = [x for x in password if x.islower()]
	digit = [x for x in password if x.isdigit()]
	if not upper or not lower or not digit:
		return False
	else:
		return True
		
print minimum("123") #false
print minimum("kasldjfsdKSALJDFK") #false
print minimum("Pp1") #true

def strength(password):
	upper = [x for x in password if x.isupper()]
	lower = [x for x in password if x.islower()]
	digit = [x for x in password if x.isdigit()]
	alnum = [x for x in password if not x.isalnum()]
	weak = 1
	strong = 1
	if len(upper) > 0:
		weak += 1
	if len(lower) > 0:
		weak += 1
	if len(digit) > 0:
		weak += 1
	if len(alnum) > 0:
		weak += 1
	if len(upper) > 1:
		strong += 1
	if len(lower) > 1:
		strong += 1
	if len(digit) > 1:
		strong += 1
	if len(alnum) > 1:
		strong += 1
	if weak != 5:
		return weak
	else:
		return weak + strong
		
print strength("a")
print strength("afAF12#$")