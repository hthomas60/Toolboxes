import unittest

class TestListMethods(unittest.TestCase):
	def test_sort_remove_neg(self):
		self.assertEqual(sort_remove_neg([2,5,2,7,-2,-5,-7]),[2,2,5,7])

	def test_all_pos(self):
		self.assertEqual(all_pos([2,5,2,7,-2,-5,-7]),False)
		self.assertEqual(all_pos([2,5,2,7]),True)



def sort_remove_neg(a):
	"""
	removes the negitive values from a list of
	numbers and sorts the rest
	"""
	a.sort()
	ans = []
	for i in range(len(a)):
		print(i)
		if a[i] >= 0:
			ans.append(a[i])
	return ans

def all_pos(a):
	"""
	Returns true if a list has all positive values
	"""
	ans = []
	for i in range(len(a)):
		
		if a[i] < 0:
			return False
	return True


#print(sort_remove_neg([2,5,2,7,-2,-5,-7]))

if __name__ == '__main__':
    unittest.main()