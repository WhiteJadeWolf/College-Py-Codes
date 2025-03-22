"""             Decode the message :--
A message containing the letters from A-Z can be encoded into the numbers using the mapping A-> 1, B-> 2, C-> 3, ..., Z-> 26. 
To decode an encoded message, you need to group the digits and do the reverse mapping. 
You are required to display all the possible decoded messages.

For example: "11106" can be decoded into:
a. "AAJF" with the grouping (1 1 10 6)
b. "KJF" with the grouping (11 10 6) """

def decoder(message, result=""):
    if not message:
        print(result)
        return

    if message[0] != "0":
        decoder(message[1:], result + chr(int(message[:1]) + 64))

    if len(message) > 1 and "10" <= message[:2] <= "26":
        decoder(message[2:], result + chr(int(message[:2]) + 64))

msg = input("Enter encoded message: ")
print("\nPossible decodings :--")
decoder(msg)