class Converter:

    def __init__(self, number:int):
        self.number = number

    def toBinary(self) -> str:
        binary = []
        divisor = 2
        begin = True
        number = self.number
        while begin and number >= 1:

            if number % divisor == 0:
                binary.append("0")
                number = number // 2

            elif number % divisor == 1:
                binary.append("1")
                number = number // 2

            while number < 1:
                binary.reverse()
                binary_str = "".join(binary)
                begin = False
                break

        return binary_str

    def toDecimal(self) -> str:
        decimal = 0
        power = 0
        binary_array = list(str(self.number))
        for power_idx in range(len(binary_array)-1, -1, -1):

            if binary_array[power_idx] == "1":
                decimal += 2**power

            power += 1

        return str(decimal)


if __name__ == '__main__':
    correct_input = False
    while not correct_input:
        convert = input("1 for convert to binary, 0 to convert to decimal: ")
        if convert == "1" or convert == "0":
            correct_input = True
        else:
            print("Incorrect input")

    x = int(input("Number you would like to convert: "))
    conversion = Converter(x)

    if convert == "0":
        print(conversion.toDecimal())
    elif convert == "1":
        print(conversion.toBinary())
