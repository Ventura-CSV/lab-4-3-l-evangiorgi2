def main():
    
    total = 0
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value: '))
        total = sum(numbers)
    print(numbers)
    print(total)
    

    return total, numbers


if __name__ == '__main__':
    main()
