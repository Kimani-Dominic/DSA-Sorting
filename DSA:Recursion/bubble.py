



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
    
    def ComputeHelper(start, end):
        results = []
        if expression[start, end + 1].isdigit():
            return [int(expression[start, end + 1])]
        
        for i in range(start, end + 1):
            if expression [i] in {'+', '-', '*', '/'}:
                leftResults = ComputeHelper(start, i - 1)
                rightResults = ComputeHelper(i + 1, end)
                
                for left in leftResults:
                    for right in rightResults:
                        results.append(operate(left, right, expression[i]))
        return results
    
    return ComputeHelper(0, len(expression) - 1)


                    
            
    
# Example usage:
expression1 = '2-1-1'
expression2 = "2*3-4*5"

print(Compute(expression1))  # Output: [0, 2]
print(Compute(expression2))  # Output: [-34, -14, -10, -10, 10]

 








