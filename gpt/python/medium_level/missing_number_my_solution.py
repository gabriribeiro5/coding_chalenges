class MissingNumberProblem:
    """
    Problem details:
        You are given an array of integers from 1 to n (inclusive), with one number missing.
        Find the missing number.

    Example:
        given an array [3, 7, 1, 2, 8, 4, 5], the missing number is 6.

    Constraints:
        The array will have n - 1 integers.
        The number n will be provided (i.e., the length of the complete array).
        The array is unsorted.
    
    Your task:
        Implement a Python function to solve this problem.
        Aim for optimal time and space complexity.
        Feel free to ask for hints if you get stuck!
    """
    def find_missing_number(self, nums: list[int], array_lenght: int) -> int:
        # sort array
        sorted_nums = sorted(nums)
        expected_value = min(nums)
        lenght_count = 0
        
        missing_number = expected_value

        while lenght_count < array_lenght:
            for i in sorted_nums:
                lenght_count += 1
                if i == expected_value:
                    expected_value += 1
                else:
                    missing_number = expected_value

        missing_number: int

        return missing_number

def test_solution():
    problem = MissingNumberProblem()
    tests = {
        "TEST A": [3, 7, 1, 2, 8, 4, 5]
    }
    results = {}
    for test_name, nums in tests.items():
        print(f"Running {test_name}: {nums[:10]}... (truncated for large input)")
        results[test_name] = problem.find_missing_number(nums, 8)
        print(f">>> Result: {results[test_name]}")
    return results

if __name__ == "__main__":
    test_solution()
