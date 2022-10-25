#Create a currency.py program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.
# # currency

yuan = float(input('What do you have left in yuan: '))
yen = float(input('What do you have left in yen: '))
won = float(input('What do you have left in won: '))



Dolar = (yuan * 0.14) + (yuan * 0.0067) + (won * 0.0007) 

print(Dolar)


