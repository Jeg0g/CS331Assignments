#1
# def isPalindrome(x: int) -> bool:
#     return str(x)==str(x)[::-1]
def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    pow=0
    xtest=x
    while xtest>=10:
        pow+=1
        xtest=xtest//10
    pow+=1
    for i in range(pow//2):
        if x//(10**(pow-(2*i)-1))%10!=x%10:
            return False
        x=x//10
    return True
#testcases
print("Problem 1")
print(f"0: {isPalindrome(0)}")
print(f"-121: {isPalindrome(-121)}")
print(f"121: {isPalindrome(121)}")
print(f"2147447412: {isPalindrome(2147447412)}")
print(f"12345432: {isPalindrome(12345432)}")
print()

#2
def removeDuplicates(nums: list[int]):
    ptr=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[ptr]=nums[i]
            ptr+=1
    return (ptr, nums)
#testcases
print("Problem 2")
print(f"[0, 0, 0]: {removeDuplicates([0, 0, 0])}")
print(f"[1, 1, 2]: {removeDuplicates([1, 1, 2])}")
print(f"[-5, -5, -3, -3, -1, -1]: {removeDuplicates([-5, -5, -3, -3, -1, -1])}")
print(f"[0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 100]: {removeDuplicates([0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 100])}")
print(f"[-10, -10, -10, -10, -10, -10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]: {removeDuplicates([-10, -10, -10, -10, -10, -10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4])}")
print()

#3
def sumOfMultiples(n: int) -> int:
    sum=0
    count=0
    for i in range(3,n,3):
        if count==4:
            count=0
        else:
            sum+=i
            count+=1
    for i in range(5,n,5):
        sum+=i
    return sum
#testcases
print("Problem 3")
print(f"5: {sumOfMultiples(5)}")
print(f"10: {sumOfMultiples(10)}")
print(f"500: {sumOfMultiples(500)}")
print(f"1000: {sumOfMultiples(1000)}")
print(f"333: {sumOfMultiples(333)}")
print()

#4
def numberOfWords(para: str) -> int:
    paralist1=para.split()
    words=0
    for i in paralist1:
        words+=len(i.split("\n"))
    return words
#testcases
print("Problem 4")
print(numberOfWords("""Starting the Fall of 2021, the Academic Resource Center is
moving to in person tutoring for most subject areas. There are some online
tutoring sessions available for some subjects."""))
print(numberOfWords("Academic Calendar\nAcademic Programs- Graduate\nAcademic Programs- Undergraduate"))
print()

def art(s: str) -> str:
    outstr=""
    for i in range(1,len(s)):
        tempstr=s[::-1][:i][::-1]
        temp3=""
        for j in range(len(tempstr)-1):
            temp3+=tempstr[j]+"."
        temp3+=tempstr[len(tempstr)-1]
        temp3+=".."*(len(s)-i)
        temp2=temp3[1:][::-1]+temp3
        outstr+=temp2+"\n"
    revoutstr=outstr[::-1]
    tempstr=s
    temp3=""
    for j in range(len(tempstr)-1):
        temp3+=tempstr[j]+"."
    temp3+=tempstr[len(tempstr)-1]
    temp2=temp3[1:][::-1]+temp3
    outstr+=temp2
    outstr+=revoutstr
    return outstr
#testcases
print("Problem 5")
print(f"@: \n{art('@')}")
print(f"@%: \n{art('@%')}")
print(f"ABC: \n{art('ABC')}")
print(f"#####: \n{art('#####')}")
print(f"abcdefghijklmnop: \n{art('abcdefghijklmnop')}")