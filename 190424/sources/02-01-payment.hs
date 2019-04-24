data PaymentMethod = BankCard String | Cash | Qiwi String
a = BankCard "1234 5678 9012 3456"
b = Cash
c = Qiwi "+7 812 000 00 00"

to_string (BankCard num) = "BankCard " ++ num
to_string Cash           = "Cash"
to_string (Qiwi phone)   = "Qiwi " ++ phone
