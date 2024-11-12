from classes.asset import Asset

# We will collect the clients input

name = input("What asset are you looking to analyize?: ")
ticker = input("Provide us with the ticker symbol of that asset: ")
print("How long do you want us to look back?")
time = input("Choose one of these options: 1_D, 5_D, 3_M, 6_M, YTD, 1_Y, 5_Y, MAX -> ")

asset = Asset(name, ticker, time)
