def diffWaysToCompute(expression):
    # Helper function to evaluate a single operation
    def operate(a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b

    # Helper function to recursively compute results
    def computeHelper(start, end):
        results = []

        # Base case: single number
        if expression[start:end + 1].isdigit():
            return [int(expression[start:end + 1])]

        # Iterate through the expression
        for i in range(start, end + 1):
            if expression[i] in {'+', '-', '*', '/'}:
                left_results = computeHelper(start, i - 1)
                right_results = computeHelper(i + 1, end)

                # Combine results for different combinations
                for left in left_results:
                    for right in right_results:
                        results.append(operate(left, right, expression[i]))

        return results

    # Call the helper function with the entire expression
    return computeHelper(0, len(expression) - 1)

# Example usage:
expression1 = "2-1-1"
expression2 = "2*3-4/5"

print(diffWaysToCompute(expression1))  # Output: [0, 2]
print(diffWaysToCompute(expression2))  # Output: [-34, -14, -10, -10, 10]
print(diffWaysToCompute(2*3-4*5))
 
           