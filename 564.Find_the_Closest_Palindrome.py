class Solution(object):
    
    def isPalindromic(self, n):
        len_str = len(n)
        for i in range(len_str):
            if n[i] != n[len_str - i - 1]:
                break
        else:
            return True
        return False
    
    def isNineNineEdge(self, n):
        # if 99, 999, 9999....
        return 10**len(n) - 1 == int(n)
        
    def isUpNineNineEdge(self, n):
        """ 
            if 101, 1001, 10001 ...
            or 100, 1000, 10000
        """
        return abs(10**(len(n)-1) - int(n)) < 2

    
    def find_bigger_Palindromic(self, nearest_list, len_n):
    
        return self.find_next_Palindromic(nearest_list, len_n, True)
    
    def find_smaller_Palindromic(self, nearest_list, len_n):
    
        return self.find_next_Palindromic(nearest_list, len_n, False)
    
    def find_next_Palindromic(self, nearest_list, len_n, isBigger):
        changed_value, middle_bound, change = '9', '0', -1
        if isBigger:
            changed_value, middle_bound, change = '0', '9', +1
        
        middle = len_n / 2
        nearest = nearest_list[:]
        
        
        while nearest[middle] == middle_bound and middle < len_n:
            nearest[middle], nearest[len_n - middle - 1] = changed_value, changed_value
            middle += 1
        
        middle_value = str(int(nearest_list[middle]) + change)
        nearest[middle], nearest[len_n - middle - 1] = middle_value, middle_value
        return ''.join(nearest)
    



    
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        len_n = len(n)
        number = int(n)
        if number == 0:
            return '1'
        elif number <= 10:
            return str(number - 1)
        if self.isNineNineEdge(n):
            return str(10**(len_n)+1)
        if self.isUpNineNineEdge(n):
            return str(10**(len_n-1)-1)
            
        
        nearest_list = ['0' for i in range(len_n)]

        for i in range((len_n + 1) / 2):
            nearest_list[i] = n[i]
            nearest_list[len_n - i - 1] = n[i]

        nearest_one = ''.join(nearest_list)
        nearest_bigger_one = None
        nearest_smaller_one = None
        if int(nearest_one) > number:
            nearest_bigger_one = nearest_one
        if int(nearest_one) < number:
            nearest_smaller_one = nearest_one

        if nearest_bigger_one == None:
            nearest_bigger_one = self.find_bigger_Palindromic(nearest_list, len_n)
        if nearest_smaller_one == None:
            nearest_smaller_one = self.find_smaller_Palindromic(nearest_list, len_n)

        if int(nearest_bigger_one) - number < number - int(nearest_smaller_one):
            return nearest_bigger_one
        else:
            return nearest_smaller_one
