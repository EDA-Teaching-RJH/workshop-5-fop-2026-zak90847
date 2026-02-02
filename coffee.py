def main():
    amount_due = 75
    accepted_coins = [50, 20, 10, 5]
    while amount_due > 0:
        print(f"Amount Due: {amount_due}p")
        coin = int(input("Insert coin: "))
        if coin in accepted_coins: amount_due -= coin
        if coin not in accepted_coins:
            print("Invalid coin amount please try again.")
        elif coin > amount_due:
            change = abs(amount_due)
    print("Change Owed: {change}p")
if __name__ ==  "__main__":
    main()