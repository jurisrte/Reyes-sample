Monthly_salary = float(input("Input your monthly salary: "))
Loan_amount = float(input("Input your loan amount: "))

if Monthly_salary >= 30000:
    if Loan_amount <= Monthly_salary * 10:
        print("You are eligible for a loan")
        months = int(input("How many months to pay?: "))

        total_loan = Loan_amount * 0.10
        month_payment = total_loan / months

        print(f"Your loan amount with 10% interest is: {total_loan:.2f}")
        print(f"Your monthly payment {months} months will be: {month_payment:.2f}")

    else:
        print("You are not eligble for a loan: Too high loan request")
else:
    print("You are not eligble for a loan: Low salary")
