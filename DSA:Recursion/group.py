#Given a string expression of numbers and operators, 
# return all possible results from computing all the different possible ways to group numbers and operators



def Compute(expression):
    
    def operate(a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b

   
    def computeHelper(start, end):
        results = []

# Base case
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

print(Compute(expression1))  
print(Compute(expression2))  

 
           