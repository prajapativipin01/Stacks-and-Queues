class Solution:

    def getNSL(self,nums,n):

        result = [-1]*n
        st = []

        for i in range(n):

            # case: if the stack is empty then push the index -1
            if not st:

                result[i] = -1

            else:

                while st and nums[st[-1]] > nums[i]:

                    st.pop()  # if the current element is less than the stack ke top se to pop kr do use stack se
                result[i] = -1 if not st else st[-1]

            st.append(i)

        return result


    def getNSR(self, nums, n): 

        result = [n]*n
        st = []

        for i in range(n-1, -1,-1):

            if not st:
                result[i] = n # is stack khali ho to max index push 

            else:

                while st and nums[st[-1]] >= nums[i]:

                    st.pop()

                result[i]  = n if not st else st[-1]

            st.append(i)

        return result


    def getNGL(self,nums, n):

        result = [-1]*n
        st = []

        for i in range(n):

            if not st:
                result[i] = -1

            else:

                while st and nums[st[-1]] < nums[i]:
                    st.pop()

                result[i] = -1 if not st else st[-1]

            st.append(i)

        return result

    def getNGR(self, nums,n):

        result = [n]*n
        st = []

        for i in range(n-1,-1,-1):

            if not st:

                result[i] = n

            else:

                while st and nums[st[-1]] <= nums[i]: 

                    st.pop()

                result[i]  = n if not st else st[-1]

            st.append(i)

        return result

    def summax(self, nums):
        n = len(nums)
        sum = 0

       
        NGL = self.getNGL(nums, n)
        NGR = self.getNGR(nums, n)

        for i in range(n):

            ls = i - NGL[i]
            rs = NGR[i] - i

            total_ways = ls * rs

            total_sum = total_ways * nums[i]

            sum = (sum + total_sum)  

        return sum

    def summin(self,arr):

        n = len(arr)  
        sum = 0

        
        NSL = self.getNSL(arr, n)
        NSR = self.getNSR(arr, n)

        for i in range(n):

            ls = i - NSL[i]
            rs = NSR[i] - i

            total_ways = ls * rs

            total_sum = total_ways * arr[i]

            sum = (sum + total_sum)  

        return sum

    def subArrayRanges(self, nums: list[int]) -> int:

        return self.summax(nums) - self.summin(nums)
