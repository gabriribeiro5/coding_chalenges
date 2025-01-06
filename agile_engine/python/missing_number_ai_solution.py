class SomeProblem:
    def solution_method(self, nums: list[int], array_length: int) -> int:
        expected_sum = (array_length * (array_length + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

def test_solution():
    problem = SomeProblem()
    tests = {
        "TEST A": [3, 7, 1, 2, 8, 4, 5]
    }
    results = {}
    for test_name, nums in tests.items():
        print(f"Running {test_name}: {nums[:10]}... (truncated for large input)")
        results[test_name] = problem.solution_method(nums, len(nums)+1)
        print(f">>> Result: {results[test_name]}")
    return results

if __name__ == "__main__":
    test_solution()
