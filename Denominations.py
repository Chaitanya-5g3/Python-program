amount=int(input())
five_hundred_notes=amount//500
remaining_balance1=amount%500
one_hundred_notes=remaining_balance1//100
remaining_balance2=remaining_balance1%100
fifty_rupees_notes=remaining_balance2//50
remaining_balance3=remaining_balance2%50
ten_rupees_notes=remaining_balance3//10
remaining_balance4=remaining_balance3%10
print("five hundred notes",five_hundred_notes)
print(" One hundred rupees",one_hundred_notes)
print("fifty rupees notes:", fifty_rupees_notes)
print("ten rupees notes", ten_rupees_notes)
