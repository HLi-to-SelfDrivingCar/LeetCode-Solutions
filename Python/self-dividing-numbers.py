# Time:  O(nlogr) = O(n)
# Space: O(logr) = O(1)

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDividingNumber(num):
            n = num
            while n > 0:
                n, r = divmod(n, 10)
                if r == 0 or (num%r) != 0:
                    return False
            return True
        
        return [num for num in xrange(left, right+1) if isDividingNumber(num)]


# Time:  O(nlogr) = O(n)
# Space: O(logr) = O(1)
class Solution2(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [num for num in xrange(left, right+1) \
                if not any(map(lambda x: x == 0 or num % x != 0, map(int, list(str(num)))))]

