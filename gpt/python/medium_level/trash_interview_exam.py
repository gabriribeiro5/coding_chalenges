class problem1():
    def max_subarray_sum(nums: list[int]) -> int:
        # check constraints
        if (1) <= nums.length <= (10 ** 5) and (-10 ** 4) <= nums[i] <= (10 ** 4):
            pass
        else:
            return "nums does not match the constraints"
        
        # define variables
        current_sum = nums[0]
        global_sum = 0
        
        # solve task
        current_sum = sum(value for value in nums if current_sum < (current_sum + value))

        if current_sum > global_sum:
            global_sum += current_sum

        return global_sum
    
if __name__ == "__main__":
    p = problem1()
    result = p.max_subarray_sum()
    print(result)