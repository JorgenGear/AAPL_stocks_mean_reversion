#hw4 stock market trading
#code to read lines from AAPL.txt
file = open("/home/ubuntu/environment/hw4/AAPL.txt")
lines = file.readlines()

#compiling data into a list
prices = []
for line in lines:
    prices.append(round(float(line),2))

#titling output
print("AAPL Mean Reversion Strategy Output: 2022 Data")
print()

#defining variables
current_price = 0
buy = 0
first_buy = 0
total_profit = 0

#for loop to calculate selling times vs buying times based on 5 day average
for price in prices:
    if current_price >= 5:
        #calculating the 5 day average
        five_day_average = (prices[current_price-1] + prices[current_price-2] + prices[current_price-3] + prices[current_price-4] + prices[current_price-5]) / 5
        #if statement to determine whether or not to buy
        if price < five_day_average * .96 and buy == 0:
            buy = price
            print("buying at: ", price)
            #updating the first_buy variable
            if first_buy == 0:
                first_buy = price
            else:
                pass
        #if statement to determine whether or not to sell
        elif price > five_day_average * 1.04 and buy != 0:
            #calculating trade profit for individual buys and total amount
            trade_profit = price - buy
            total_profit += trade_profit
            print("selling at: ", price)
            print("trade profit: ", round(trade_profit,2))
            buy = 0
        else:
            pass
    #adding to current_price to move loop through list
    current_price += 1
print()

print("Total profit: ", "$", + round(total_profit,2))
print("First buy: ", "$", first_buy)
final_profit_percentage = (total_profit / first_buy) * 100
print("Percentage Returns: ", round(final_profit_percentage,2), "%")
