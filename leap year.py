year=int(input("Enter the year to find leap year or not:"));
result = "leap year" if ((year%4==0 and year%100!=0) or year%400==0) else "Not a leap year:"
print(result);
