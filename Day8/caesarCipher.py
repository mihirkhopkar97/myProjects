alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  result = ""
  for letter in text:
    if(letter in alphabet):
      position = alphabet.index(letter)
      if(direction=='encode'):
        new_position = (position + shift)%26
      else:
        new_position = position - shift
      result += alphabet[new_position]
    else:
      result+=letter
  print(f"The result text is {result}")


from art import logo
print(logo)

while(True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)
  run_again = input("restart the cipher program?(Yes/No)")
  if(run_again.lower()=='no'):
    break