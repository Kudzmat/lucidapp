from app import app, db
from flask import request, render_template, flash, redirect, url_for
from forms import LocalOrderForm
from functions import revenue, rtgs_amount, usd_total, get_profit
from models import LocalOrder


# home page
@app.route('/')
def index():
    name = 'Kudzayi'
    return render_template('home.html', name=name)


# local order page
@app.route('/local', methods=['GET', 'POST'])
def local_order():
    order = LocalOrderForm()

    if order.validate_on_submit():
        date = order.date.data
        amount = order.amount.data
        markup = order.markup.data
        my_rtgs_rate = order.my_rtgs_rate.data
        changer_rate = order.changer_rate.data

        # getting marked up amount
        markup_usd = revenue(amount, markup)

        # getting rtgs values
        total_rtgs_excl, total_rtgs_vat = rtgs_amount(markup_usd, my_rtgs_rate)

        # getting usd values
        total_usd_excl, total_usd_vat = usd_total(total_rtgs_excl, changer_rate)

        # getting profit
        profit = get_profit(total_usd_vat, total_usd_excl)

        new_local = LocalOrder(date=date,
                               amount=amount,
                               markup=markup,
                               my_rtgs_rate=my_rtgs_rate,
                               changer_rate=changer_rate,
                               markup_usd=markup_usd,
                               total_rtgs_excl=total_rtgs_excl,
                               total_rtgs_vat=total_rtgs_vat,
                               total_usd_excl=total_usd_excl,
                               total_usd_vat=total_usd_vat,
                               profit=profit)
        db.session.add(new_local)
        db.session.commit()
    return render_template('local.html', form=order)
