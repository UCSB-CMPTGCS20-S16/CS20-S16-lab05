# lab05Tests.py    Tests for lab05, UCSB CS8/CS20, P. Conrad, 04/15/2014

import unittest            
from lab05Funcs import *   

class TestLab05Functions(unittest.TestCase): 


    # tests for isList  

    def test_isList1(self):
        self.assertEqual( isList(3),   False)

    def test_isList2(self):
        self.assertEqual( isList([3]),   True)

    def test_isList3(self):
        self.assertEqual( isList([5,10,15,20]),   True)

    def test_isList4(self):
        self.assertEqual( isList("foo"),   False)

    def test_isList5(self):
        self.assertEqual( isList(["John","Paul","Ringo","George"]),   True)

    def test_isList6(self):
        self.assertEqual( isList([]),   True)
    
    # tests for largestInt

    def test_largestInt_1(self):
       self.assertEqual( largestInt([]), False)

    def test_largestInt_2(self):
       self.assertEqual( largestInt('foo'), False)

    def test_largestInt_3(self):
       self.assertEqual( largestInt([3,5,4.5,6]),    False)

    def test_largestInt_4(self):
       self.assertEqual( largestInt([4]),    4)

    def test_largestInt_5(self):
       self.assertEqual( largestInt([-9,4,7,8,2]),    8)

    # tests for indexOfLargestInt

    def test_indexOfLargestInt_1(self):
       self.assertEqual(  indexOfLargestInt([]),    False)

    def test_indexOfLargestInt_2(self):
       self.assertEqual(  indexOfLargestInt('foo'),    False)

    def test_indexOfLargestInt_3(self):
       self.assertEqual(  indexOfLargestInt([3,5,4.5,6]),    False)

    def test_indexOfLargestInt_4(self):
       self.assertEqual(  indexOfLargestInt([40]),    0)

    def test_indexOfLargestInt_5(self):
       self.assertEqual(  indexOfLargestInt([-90,40,70,80,20]),    3)

    def test_indexOfLargestInt_6(self):
       self.assertEqual(  indexOfLargestInt([10,30,50,20,50]),    2)



    # tests for indexOfSmallestInt

 
    def test_indexOfSmallestInt_1(self):
       self.assertEqual( indexOfSmallestInt([]), False )

    def test_indexOfSmallestInt_2(self):
       self.assertEqual( indexOfSmallestInt('foo'), False )

    def test_indexOfSmallestInt_3(self):
       self.assertEqual( indexOfSmallestInt([3,5,4.5,6]), False )

    def test_indexOfSmallestInt_4(self):
       self.assertEqual( indexOfSmallestInt([40]), 0 )

    def test_indexOfSmallestInt_5(self):
       self.assertEqual( indexOfSmallestInt([20,-90,40,70,80]), 1 )

    def test_indexOfSmallestInt_6(self):
       self.assertEqual( indexOfSmallestInt([50,30,10,30,50,10]), 2 )

    def test_indexOfSmallestInt_7(self):
       self.assertEqual( indexOfSmallestInt([50,30,10,30,50,-10]), 5 )
    

    # tests for longestString

    def test_longestString_1(self):
       self.assertEqual(  longestString([]),    False)

    def test_longestString_2(self):
       self.assertEqual(  longestString('foo'), False )

    def test_longestString_3(self):
       self.assertEqual(  longestString(['foo']), 'foo' )

    def test_longestString_4(self):
       self.assertEqual(  longestString(['bear','cat','dog','mouse']), 'mouse' )

    def test_longestString_5(self):
       self.assertEqual(  longestString(['cat','wolf','bear','dog']), 'wolf' )



    # tests for indexOfShortestString


    def test_indexOfShortestString_1(self):
       self.assertEqual(  indexOfShortestString([]), False )

    def test_indexOfShortestString_2(self):
       self.assertEqual(  indexOfShortestString('foo'), False )

    def test_indexOfShortestString_3(self):
       self.assertEqual(  indexOfShortestString(['foo']), 0 )

    def test_indexOfShortestString_4(self):
       self.assertEqual(  indexOfShortestString(['bear','cat','dog','mouse']), 1 )

    # @@@ ADD SIX TEST CASES HERE FOR smallestInt
    # @@@ (a) a test case for an empty list
    # @@@ (b) a test case for something that is not a list
    # @@@ (c) a test case with only one thing in the list
    # @@@ (d) a test case where the smallest int is the first item
    # @@@ (e) a test case where the smallest int is the last item
    # @@@ (f) a test case where smallest is neither the first nor last item



    # End of tests for lab05




def runTestsWithPrefix(testFile,prefix):
    """
    run only tests from testFile with a certain prefix
    Example: runTestsWithPrefix("lab03Tests.py","test_isPrimaryColor")
    """
    loader = unittest.TestLoader()
    loader.testMethodPrefix = prefix
    suite = loader.discover('.', pattern = testFile) 
    unittest.TextTestRunner(verbosity=2).run(suite)


# When you run this file, it runs either ALL the tests, or
# just some tests.  It depends on which line you comment out (or not)

if __name__ == '__main__':

    # To run ALL tests, uncomment the "unittest.main(exit=False)" line
    unittest.main(exit=False)  

    # Uncomment "runTestsWithPrefix" line to run just SOME tests
    #    First parameter is name of file with tests
    #    Second parameter is prefix starting with test_ 
    #      such as test_FtoC  or test_isString

    # runTestsWithPrefix("lab05Tests.py","test_ithOfNPointsOnCircleX") 
