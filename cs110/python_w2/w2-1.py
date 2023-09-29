

# convert a decimal to a decimal with 2 digits.
def convertDecimalTo2DigitDecimal(origFloat):
    return float('%.2f' % origFloat );

# convert a string to a decimal with 2 digits.
def convertStringTo2DigitDecimal(origString):
    return convertDecimalTo2DigitDecimal(float(origString));

# a recursive function to force user to input a postive number.
def forcePostiveUserInput(msg):
    result = float(input(msg));
    if result < 0 :
        print(' ~ The value should be postive !!!')
        result = forcePostiveUserInput(msg);
    
    return result;

# a recursive function to force user to input a right tax rate.
def forceTaxRate(msg):
    result = float(input(msg));
    if (result < 0 or result > 100):
        print(' ~ The tax rate should between 0 and 100 !!!');
        result = forceTaxRate(msg);

    return result ;

# a recursive function to force user to input a right payment amount.
def forceLargerNumber(msg, baseNumber):
    result = float(input(msg));
    if (result < baseNumber):
        print(f" ~ Your payment amount ${result} is less than ${baseNumber} !!!")
        result = forceLargerNumber(msg, baseNumber)

    return result 

def main():
    # get user input
    # child_meal_price = float(input("What is the price of a child's meal?"))
    child_meal_price = forcePostiveUserInput("What is the price of a child's meal?")
    audit_meal_price = forcePostiveUserInput("What is the price of a adult's meal?")
    child_count = forcePostiveUserInput('How many children are there?')
    audit_count = forcePostiveUserInput('How many adults are there?')

    # calculate subtotal
    subtotal = child_meal_price * child_count + audit_meal_price * audit_count
    subtotal = convertDecimalTo2DigitDecimal(subtotal);

    print('')
    print(f"Subtotal: ${subtotal}")
    print('')

    # calculate tax_rate
    tax_rate = forceTaxRate("What is the sales tax rate?")

    # calculate sales_tax
    sales_tax = convertDecimalTo2DigitDecimal(subtotal * tax_rate / 100);
    print(f"Sales Tax: ${sales_tax}")

    # calculate total
    total = convertDecimalTo2DigitDecimal(subtotal + sales_tax);
    print(f"Total: ${total}")
    print('')

    # calculate change
    payment = forceLargerNumber('What is the payment amount?', total)
    print(f"Change: ${ convertStringTo2DigitDecimal(payment - total) }")

main()

