class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):

            
        str_list = map(str, nums)
        for i in range(len(str_list)):
            for j in range(len(str_list) - 1):
                if int(str_list[j] + str_list[j+1]) < int(str_list[j+1]+ str_list[j]):
                    str_list[j+1], str_list[j] = str_list[j], str_list[j+1]
        r = "".join(str_list)
        for i in range(len(r)):
            if r[i] != "0":
                return r[i:]        
        return "0"
