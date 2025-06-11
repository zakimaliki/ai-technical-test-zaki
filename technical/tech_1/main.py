def find_discount_position(input_str):
    # Convert input string to list of integers
    prices = list(map(int, input_str.split()))
    start_price = prices[0]

    for i in range(1, len(prices)):
        # Check if current price is lower than previous price and initial price
        if prices[i] < prices[i - 1] and prices[i] < start_price:
            return i
    # Return 0 if no discount found
    return 0

# Test input to try the function
test_input = "3 4 1"
print(find_discount_position(test_input))
