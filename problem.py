def main():
    inputNums = input()
    nums = [eval(num) for num in inputNums[1:-1].split(',')]
    sum = 0
    resultNums = []
    for num in nums:
        sum = sum + num
        resultNums.append(sum)
    print(resultNums)
main()
