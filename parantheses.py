def generate_parentheses(n):
    def backtrack(s="", left=0, right=0):
        if len(s) == 2 * n:
            valid_parentheses.append(s)
            return
        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    valid_parentheses = []
    backtrack()
    return valid_parentheses


# Specify the number of pairs of parentheses
n = 10

# Generate all valid combinations of parentheses
valid_combinations = generate_parentheses(n)

# Print the valid combinations
print(valid_combinations)