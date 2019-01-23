#Page Visits Funnel

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

combo_vis_cart = pd.merge(visits,cart, how='left')
print(combo_vis_cart)
print(len(combo_vis_cart))

combo_cart_check = pd.merge(cart, checkout, how='left')
print(combo_cart_check)

combo_check_purchase = pd.merge(checkout, purchase, how = 'left')



all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data)

print(len(combo_vis_cart[combo_vis_cart.cart_time.isnull()]))

print(len(combo_vis_cart[combo_vis_cart.cart_time.isnull()])/float(len(combo_vis_cart)))

print(len(combo_cart_check[combo_cart_check.checkout_time.isnull()])/float(len(combo_cart_check)))

len_null_purchase = len(combo_check_purchase[combo_check_purchase.purchase_time.isnull()])

len_check = len(combo_check_purchase)

print(len_null_purchase/float(len_check))


all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())


