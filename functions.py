def revenue(amount_usd, markup):
    new_markup = (markup / 100) + 1
    rev = amount_usd * new_markup
    return round(rev, 2)


# will return rtgs total excl vat & with vat
def rtgs_amount(usd_amount, rate):
    total_excl = usd_amount * rate
    total_vat = total_excl * 1.145
    return round(total_excl, 2), round(total_vat, 2)


# will return usd total excl vat & with vat
def usd_total(rtgs_excl, rate):
    usd_excl = rtgs_excl / rate
    usd_vat = usd_excl * 1.145
    return round(usd_excl, 2), round(usd_vat, 2)


# will return profit
def get_profit(usd_vat, usd_excl):
    profit = usd_vat - usd_excl
    return round(profit, 2)


print(get_profit(6840.26, 5974.03))
