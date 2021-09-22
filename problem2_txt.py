test_cases = float(input("Enter the test cases between 1 and 100 : "))
element = [] #define a empty list
if test_cases >= 1 and test_cases<=100: #applying condition according to first constraints
    for k in range(0,int(test_cases)):
        N = float(input("Enter the Natural Number between 1 and 10 : "))
        if N>=1 and N<=10: #applying condition according to second constraints
            for i in range(0,int(N)):
                flag = float(input("Enter Element between 0 and 15 : "))
                if flag>=0 and flag<=15: #applying condition according to third constraints
                    element.append(flag)
                else:
                    print("You Entered Wrong Input")
        sum_element = 0
        for j in element:
            sum_element = sum_element + j
        print("Sum of array according to ",k+1,"test cases = ",sum_element) 
        element = []
    
