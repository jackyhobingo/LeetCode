class Solution(object):
    
    
    def to_str(self, now_list, now, now_list_len, maxWidth):
        
        space_num = maxWidth - now
        every_space = space_num
        last_space = 0
        if now_list_len > 1:
            every_space = space_num // (now_list_len - 1)
            last_space = space_num % (now_list_len - 1)
        result_str = ""
        last = ""
        if len(now_list) > 1:
            last = now_list.pop()
        for w in now_list:
            temp_space = every_space
            if last_space > 0:
                last_space -= 1
                temp_space += 1
            result_str = result_str + w + temp_space * " " 
        if last:
            result_str = result_str + last
        return result_str
         
        
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if words == [""] or maxWidth == 0:
            return [" " * maxWidth]
        result = []
        
        now = 0
        now_list = []
        now_list_len = 0
        for word in words:
            next_sum = now + len(word)

            if next_sum + now_list_len > maxWidth:
                result_str = self.to_str(now_list, now, now_list_len, maxWidth)
                result.append(result_str)
                
                now = 0
                now_list_len = 0
                now_list = []
                next_sum = len(word)

            now = next_sum
            now_list_len += 1 
            now_list.append(word)
            
        if now_list_len:
            last_str = " ".join(now_list)
            last_str = last_str + (maxWidth - len(last_str)) * " "
            result.append(last_str)
        
        return result
        
