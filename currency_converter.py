
def usd_to_euro(usd):
    if str(usd).isnumeric():
        return str(usd * .90) + " EUR"
    else:
        print("You must enter a USD value to convert...")
def euro_to_usd(euro):
    if str(euro).isnumeric():
        return str(euro * 1.11) + " USD"
    else:
        print("You must enter a EURO value to convert...")
def usd_to_many(usd):
    # convert usd to eur, gbp, inr, aud, cad, zar, nzd, jpy, cny
    usd_conversions = []
    for value in usd:
        if str(value).isnumeric():
            usd_conversions.append(str(value) + " USD converts to")
            usd_conversions.append(str(int(value * .90)) + " EUR")
            usd_conversions.append(str(int(value * .70)) + " GBP")
            usd_conversions.append(str(int(value * 68.46)) + " INR")
        else:
            print("You must enter a USD value to convert...")
            break
        #usd_conversions.append(str(value * ))
    return usd_conversions

