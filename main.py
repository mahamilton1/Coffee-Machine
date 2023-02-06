from coffee import MENU, resources

# menu shows ingredients on how to make each
# report shows how much of ingredients is remaining
menu = MENU
report = resources
report["money"] = 0
i = "ingredients"
w = "water"
m = "milk"
c = "coffee"
t = "cost"
n = "money"
# drink choice == 'report' -> shows the amounts left in machine
# drink choice == 'off' -> stops the program


def machine():
    if drink != "report":
        def refill():
            report[w] = 300
            report[m] = 200
            report[c] = 100
            return report
        refill()

        def cash():
            print("Please insert coins.")
            qtr = int(input("How many quarters?: ")) * 0.25
            dm = int(input("How many dimes?: ")) * 0.10
            nkl = int(input("How many nickles?: ")) * 0.05
            pny = int(input("How many pennies?: ")) * 0.01
            total = qtr + dm + nkl + pny
            return total
        paid = cash()

        def change():
            cost = menu[drink][t]
            remain = paid - cost
            if remain < 0:
                cost = 0
            report[n] += round(cost, 2)
            return report, remain
        back = round(change()[1], 2)

        if back > 0:
            def water():
                cost = menu[drink][i][w]
                water_left = report[w]
                remain = water_left - cost
                if remain < 0:
                    print("Sorry there's not enough water.")
                    remain = water_left
                report[w] = remain
                return report[w]
            report[w] = water()

            def coffee():
                cost = menu[drink][i][c]
                coff_left = report[c]
                remain = coff_left - cost
                if remain < 0:
                    print("Sorry there's not enough coffee.")
                    remain = coff_left
                report[c] = remain
                return report[c]
            report[c] = coffee()

            def milk():
                milk_left = report[m]
                if drink == "espresso":
                    cost = 0
                else:
                    cost = menu[drink][i][m]
                remain = milk_left - cost
                if remain < 0:
                    print("Sorry there's not enough milk.")
                    remain = milk_left
                report[m] = remain
                return report[m]
            report[m] = milk()

        return back, report


more = True
while more:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'report':
        for val in report:
            ing = val.title()
            amt = report[val]
            if val == 'coffee':
                print(f"{ing}: {amt}g")
            elif val == 'money':
                print(f"{ing}: ${amt}")
            else:
                print(f"{ing}: {amt}ml")
    elif drink == 'off':
        more = False
    elif drink in ("espresso", "latte", "cappuccino"):
        returned = machine()[0]
        if returned < 0:
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Your change back is ${returned}.")
    else:
        print("Sorry, please choose one of the listed options")
    if drink != 'off':
        thirsty = input("Do you want more? Type 'y' or 'n': ")
        print("")
        if thirsty == 'n':
            more = False
