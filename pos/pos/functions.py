
from datetime import datetime

from django.shortcuts import redirect

from .models import OrderItem
from .values import CurrentCart, Items, Receipts


# POS ACTIONS WILL INCLUDE INCREMENT, DECREMENT AND ADD(OR EDIT)
# body represents the request.POST
def handlePOSActions(body):
    item_id = body.get('item_id')
    quantity = body.get('quantity')
    if not quantity:
        quantity = 0 
    else:
        quantity = int(quantity)
    action = body.get('action')

    #https://www.geeksforgeeks.org/python-list-comprehension/ #Conditional statements in list comprehension
    item = next((item for item in Items if item.itemId == int(item_id)), None)

    if item is None:
        return redirect('/error')
    
    if action == 'increment':
        quantity += 1
        
        if item.totalQuantity() == 0 or item.totalQuantity() < quantity:
            return redirect('/')
        
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity
    elif action == 'decrement':
        quantity -= 1
        if quantity < 0:
            return redirect('/')
        
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity
    elif action == 'add':
        if item.totalQuantity() < quantity or quantity < 0:
            return redirect('/')
     
        item.quantityInStock = item.totalQuantity() - quantity
        item.quantity = quantity

    cart_item = next((cartItem for cartItem in CurrentCart if cartItem.item.itemId == int(item_id)), None)
    if cart_item:
        cart_item.quantity = quantity
    else:
        cart_item = OrderItem(item, quantity)
        CurrentCart.append(cart_item)

    # cleaning the cart if 0 na yung quantity
    for cartItem in CurrentCart:
        if cartItem.quantity == 0:
            CurrentCart.remove(cartItem)


def getMonthNumber(month: str=None):
    if not month:
        return datetime.now().month

    months = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

    return months[month]

def processDataDashboard(monthNum: int=datetime.now().month):

    dashboardmonth = [receipt for receipt in Receipts if receipt.date.month == monthNum]
    monthtax = sum([receipt.totalTax for receipt in dashboardmonth])
    monthsub = sum([receipt.totalSub for receipt in dashboardmonth])
    monthtotal  = sum([receipt.total_cost for receipt in dashboardmonth])
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # limit date of the month to now
    currentMonth = datetime.now().month
    months = [month for month in months if months.index(month) + 1 <= currentMonth]

    data = []

    for month in months:
        month_Num = months.index(month) + 1

        getthisMonth = [receipt for receipt in Receipts if receipt.date.month == month_Num]
        getTotalRevenue = sum([receipt.total_cost for receipt in getthisMonth])
        getTotalTax = sum([receipt.totalTax for receipt in getthisMonth])

        data.append({
            "month": month,
            "totalRevenue": getTotalRevenue,
            'totalTax' : getTotalTax
        })

    return {
        "dashboardmonth" : {
            "month": months[monthNum - 1],
            "totalTax": monthtax,
            "totalSub": monthsub,
            "total": monthtotal
        },
        "data" : data
    }


