class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coins = {'large dollar':1, 'half dollar':0.5,'quarter': 0.25, 'nickel': 0.05}
        total = 0
        for coin in coins:
            try:
                amount = int(input(f'Insert {coin}: '))
                total += amount * coins[coin]
            except ValueError:
                print(f'invalid input: {coin} try ordering again')
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##        
        if coins < cost:
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f'Here is ${change} in change')
            return True