def total_amount(bill_amount,tip_percentage):
    total_amount=bill_amount*(1+0.01*tip_percentage)
    total_amount=round(total_amount,2)
    print(f"please pay $ {total_amount}")
total_amount(150,20)
