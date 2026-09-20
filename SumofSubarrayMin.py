class Solution(object):

    def getNSL(self, arr, n):

        result = [-1]*n
        st = []

        for i in range(n):

            if not st:

                result[i] = -1


            else:
                while st and arr[st[-1]] >= arr[i]:
                    st.pop()

                result[i] = -1 if not st else st[-1]

            st.append(i)

        return result

    def getNSR(self,arr, n):

        result = [n]*n
        st = []

        for i in range(n-1, -1,-1):

            if not st :

                result[i] = n


            else:
                while st and arr[st[-1]] > arr[i]:
                    st.pop()

                result[i] = n if not st else st[-1]
            st.append(i)

        return result



    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        NSL= self.getNSL(arr, n)
        NSR = self.getNSR(arr,n)

        sum = 0
        MOD = 10**9+7

        for i in range(n):

            ls = i - NSL[i]
            rs = NSR[i] - i

            total_ways = ls * rs

            totalsum = total_ways * arr[i]

            sum = (sum + totalsum) % MOD

        return sum

        





    