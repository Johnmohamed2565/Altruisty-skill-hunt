def max_profit(prices):
    
    min_price = float('inf')  
    max_profit = 0           
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


n = int(input("Enter the number of days: ")) #Getting no.of days
prices = [int(input(f"Enter the price for day {i+1}: ")) for i in range(n)]
print(max_profit(prices))
