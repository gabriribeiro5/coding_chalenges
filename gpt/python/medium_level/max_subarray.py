class MaxSubarrayProblem:
    """
    A class to solve the maximum subarray sum problem using Kadane's Algorithm.
    """
    def max_subarray_sum(self, nums: list[int]) -> int:
        # Validate constraints
        if not (1 <= len(nums) <= 10 ** 5):
            raise ValueError("Attribute length is unacceptable")
        if not all(-10 ** 4 <= number <= 10 ** 4 for number in nums):
            raise ValueError("One or more items do not match limits")

        # Initialize variables for Kadane's Algorithm
        current_sum = 0
        global_sum = float('-inf')

        # Calculate the maximum subarray sum
        for number in nums:
            current_sum = max(number, current_sum + number)
            global_sum = max(global_sum, current_sum)

        return global_sum

def test_solution():
    p = MaxSubarrayProblem()
    tests = {
        "TEST A": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "TEST B (All Negative)": [-2, -3, -1],
        "TEST C (Single Element)": [5],
        "TEST D (Large Input)": [1] * (10 ** 5)
    }
    results = {}
    for test_name, nums in tests.items():
        print(f"Running {test_name}: {nums[:10]}... (truncated for large input)")
        results[test_name] = p.max_subarray_sum(nums)
        print(f">>> Result: {results[test_name]}")
    return results

if __name__ == "__main__":
    test_solution()
