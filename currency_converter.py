
def usd_to_euro(usd):
    return str(usd * .90) + " EUR"

def euro_to_usd(euro):
    return str(euro * 1.11) + " USD"

def usd_to_many(usd):
    # convert usd to eur, gbp, inr, aud, cad, zar, nzd, jpy, cny
    usd_conversions = []
    for value in usd:
        usd_conversions.append(str(int(value * .90)) + " EUR")
        usd_conversions.append(str(int(value * .70)) + " GBP")
        usd_conversions.append(str(int(value * 68.46)) + " INR")
        #usd_conversions.append(str(value * ))
    return usd_conversions

print(usd_to_many([5, 19]))