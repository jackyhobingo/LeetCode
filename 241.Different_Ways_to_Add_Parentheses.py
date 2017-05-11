class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', input)
        int_list = map(int, tokens[::2])
        operator_list = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return [int_list[lo]]
            return [operator_list[i](a, b) 
                    for i in range(lo, hi) 
                    for b in build(i+1, hi)
                    for a in build(lo, i)]
        return build(0, len(int_list) - 1)
