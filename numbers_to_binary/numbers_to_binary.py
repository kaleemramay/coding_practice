import sys

number = int(sys.argv[1])
print(number)

#Counting number of bits in a number
def counting_bits(number):
    max_bit_value = 1
    bits = 1
    while max_bit_value < number:
        bits +=1
        max_bit_value = (2 ** bits ) - 1
    return bits

bits_in_number = counting_bits(number)
output = "There are {bits} bits in number {number}".format(number=number,bits=bits_in_number)
print(output)

def num_to_bin(number,bits):
    binary_value = ""
    while bits > 0:
        if number >= (2 ** (bits - 1)):
            binary_value += "1"
            bits    -= 1
            number  -= 2**bits
        else: 
            binary_value += "0"
            bits -= 1
    return binary_value

binary_value = num_to_bin(number, bits_in_number)

print("binary value of {number} is {binary_value}".format(number=number,binary_value=binary_value))
