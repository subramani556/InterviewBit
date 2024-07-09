class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
		l=[]
		for i in range(len(A)):
			l.append(A[i])
		A.sort();
		initIndex = 0;
		finalIndex = len(l)-1;
		ans = True;
		for i in range(len(l)):
			if(l[i] != A[i]):
				initIndex = i;
				break
		for j in range(len(l)-1, -1,-1):
			if(l[j] != A[j]):
				finalIndex = j;
				break
				
		for k in range(len(A)):
			if(l[k] != A[k]):
				ans = False;
		if(ans):
			return [-1];
		else:
			return [initIndex,finalIndex]