try:
    a=int(input("Enter 1st no: "))
    b=int(input("Enter 2nd no: "))

    print("what kind of operation do you want to perform:\nPress + for addition\nPress - for subtraction\nPress / for division\npress * for multiplication")
    
    opr=input("Enter which operation you need to perform")
    
    match opr:
      case "+":
        print (f"The sum of a and b is : {a+b}")
      case "-":
        print (f"The subtarction of a from b is : {a-b}")
      case "*":
        print (f"The multiplication of a and b is : {a*b}")
      case "/":
        print (f"The division of a by b is : {a/b}")
      case default:
        print("Entered operation does not match with the provided options of operations")

except Exception as e:
    print("User entered invalid value of a or b")