text="Three blind mice rhyme"
# way 1
print('\n'.join('0b'+format(ord(x),'b')for x in text))
print("----------------------------------------------")
# way 2
print('\n'.join(map(bin,bytearray(text,'utf8'))))