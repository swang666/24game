from itertools import permutations
from operator import truediv, add, sub, mul
class Solution:
    def judgePoint24(self, cards):
        allcards = permutations(cards, 4)
        ops = (truediv, add, sub, mul)
        ops_dic = {truediv: '/', add: '+', sub: '-', mul: '*'}

        def solve(card):
            # 2 case
            # 1
            A, B = card[0], card[1:]
            opsBs = permutations(ops, 2)
            for opsB in opsBs:
                val = opsB[1](opsB[0](B[0], B[1]), B[2])
                for op in ops:
                    if val == 0 and op == truediv:
                        continue
                    if 23.999 <= op(A, val) <= 24.001:
                        sol = str(A) + ops_dic[op] + '((' + str(B[0]) + ops_dic[opsB[0]] + str(B[1]) + ')' + ops_dic[opsB[1]] + str(B[2]) + ')'
                        return sol, True
                temp = opsB[1](B[1], B[2])
                if temp == 0 and opsB[0] == truediv:
                    continue
                val = opsB[0](B[0], temp)
                for op in ops:
                    if val == 0 and op == truediv:
                        continue

                    if 23.999 <= op(A, val) <= 24.001:
                        sol = str(A) + ops_dic[op] + '(' + str(B[0]) + ops_dic[opsB[0]] + '(' + str(B[1]) + ops_dic[opsB[1]] + str(B[2]) + '))'
                        return sol, True
            # 2
            A, B = card[:2], card[2:]
            for opA in ops:
                for opB in ops:
                    for opC in ops:
                        valA = opA(A[0],A[1])
                        valB = opB(B[0],B[1])
                        if valB == 0 and opC == truediv:
                            continue
                        val = opC(valA,valB)
                        if 23.999 <= val <= 24.001:
                            sol = '(' + str(A[0]) + ops_dic[opA] + str(A[1]) + ')' + ops_dic[opC] + '(' + str(B[0]) + ops_dic[opB] + str(B[1]) + ')'
                            return sol, True
            return "No solution found", False
        
        #solve([8,3,8,3])
        for card in allcards:
            sol, found = solve(card)
            if found:
                return sol
        return "No solution found"

if __name__ == "__main__":
    Solver = Solution()
    print(Solver.judgePoint24([8,3,8,3]))
            