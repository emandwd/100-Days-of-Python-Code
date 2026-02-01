##################### Extra Hard Starting Project ######################
import datetime as dt
import csv
import random
import smtplib


now = dt.datetime.now()
month = now.month
day = now.day

with open("birthdays.csv") as birthday :
    reader = csv.DictReader(birthday)
    for row in reader :

        month_birthday = int(row["month"])
        day_birthday = int(row["day"])
        if month_birthday == month and day_birthday == day :
            name_birthday = row["name"]
            email_birthday = row["email"]

            letter_number = random.randint(1,3)
            filename = f"letter_templates/letter_{letter_number}.txt"

            with open(filename,"r") as file :
                content = file.read()
                edited_content = content.replace("[NAME]", name_birthday)
                print(edited_content)


            # 4. Send the letter generated in step 3 to that person's email address.

            MY_EMAIL = "MY_EMAIL"
            MY_PASSWORD = "MY_PASS"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr = MY_EMAIL,
                    to_addrs = email_birthday,
                    msg = f"Subject: HAPPY BIRTHDAY!! \n\n {edited_content}"
                )


