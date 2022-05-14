graduated = ["ALI", "BADR", 'CEDRA', "EMAN", "EMAN0"]
user_in = input("enter the name of the student: ")
user_in = user_in.upper()
if user_in in graduated:
    print("student "+user_in+" graduated")
else:
    print("student "+user_in+" not graduated")