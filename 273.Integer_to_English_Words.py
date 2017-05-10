class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict_ = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        dict_2 = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }

        num_list = []
        while num > 0:
            num_list.append(num % 1000)
            num /= 1000
        
        ans_str_list = []
        
        for n, thousand in zip(num_list, [None, "Thousand", "Million", "Billion"]):
            
            if n and thousand:
                ans_str_list.append(thousand)

            hundred = n / 100
            ten = n % 100
            if 0 < ten < 20:
                ans_str_list.append(dict_[ten])
            elif ten:
                if ten % 10:
                    ans_str_list.append(dict_[ten % 10])
                if ten / 10:
                    ans_str_list.append(dict_2[ten / 10])
            if hundred:
                ans_str_list.append("Hundred")
                ans_str_list.append(dict_[hundred])

        return " ".join(ans_str_list[::-1]) or "Zero"
