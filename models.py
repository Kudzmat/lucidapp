from app import db
from datetime import datetime


# local order model
class LocalOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(150))
    amount = db.Column(db.Integer)
    markup = db.Column(db.Integer)
    my_rtgs_rate = db.Column(db.Integer)
    changer_rate = db.Column(db.Integer)

    # will be worked out
    markup_usd = db.Column(db.Float)
    total_rtgs_excl = db.Column(db.Float)
    total_rtgs_vat = db.Column(db.Float)
    total_usd_excl = db.Column(db.Float)
    total_usd_vat = db.Column(db.Float)
    profit = db.Column(db.Float)

    # will return profit
    def get_profit(self):
        pass

#order = LocalOrder(date='2022-02-15', amount=5000, markup=15, my_rtgs_rate)
