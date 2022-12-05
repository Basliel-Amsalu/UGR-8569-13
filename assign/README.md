--- how to run the encryptions---
>> in the command line argument enter the file name.py ,the sentence that needs to be encrypted and the encryption type and press enter then the program will enrypt that data and print the encrypted text then it will decrypt the enrypted text and print the decrypted text. basically the encryption method for rsa encryption takes the public keys and the message to be encrypted as an argument and the decryption takes the private keys and the encrypted message to be decrypted, the transposition cipher takes the message to be encrypted as an argument and the decryption takes the encrypted message as an argument, the affine encryption method takes the message to be encrypted and the key as an argument and the decryption method takes the encrypted message and the key as an argument.
----Theorems and concepts----
>>for the affine cipher:
It uses modular arithmetic to transform the integer that each plaintext letter corresponds to into another integer that correspond to a ciphertext letter. E(x) =(a x + b)mod m
m= size of the alphabet.
a,b= key of the cipher.
a must be coprime with m (gcd(a,m)=1).
it uses modular inverse to decypher the encrypted text to the original text. first we find number x such that x*a(mod26) = 1 by using extended euclidean algorithm. g,x,d = egcd(a,m) we only take the x.
>>for the transposition cipher:
In a transposition encryption, the order of the alphabets is re-arranged to obtain the cipher-text.The message is written out in rows of a fixed length, and then read out again column by column, and the columns are chosen in some scrambled order. the number of rows and the permutation of the columns are defined by the keyword.
number of rows = number of characters in the key
the permutation = the alphabetical order of the letters in the key
spaces are filled with _(blank)
finally the text is read from the columns in the order specified by the keyword
then to decipher we work out the column lengths by dividing the message length by the key length. after that reorder the columns by reforming the keyword.
>>for the rsa cipher:
there is the rabin miller method to check if a number is probably prime which uses the fermats theorem 
for every a, 1<= a < n , a**(n-1)%n = 1
then there is method to check if the randomly generated low prime number is prime or not by checking all the numbers in the range of 2 and the number if any of them are divisible by 2 which means it is not prime so it basically is a test to know if a number is not prime. this method falls back to the rabin miller method if uncertain
there is also a key generation method used for generating the public and private keys and coprime method that checks if e is coprime with r gcd(e,r)=1 to find the right vlue for e.
p,q are produced by the random large prime generating method
n= p*q
r=(p-1)*(q-1)
e = 1 < e <=r and e is coprime with r
d= modinverse of e,r
lastly it uses extended euclidean algorithm and modular inverse just like for the affine cipher to find the inverse d for the private key.
--- why the encryption /decryption work ---
>> for affine:
because it uses the modular arthimetic and the key and changes the outlook of how the message is presented the encryption works and because the decryption can return the original message using the modular inverse method and the key presented so the decryption works too
>> for transposition:
because it uses matrix representation of the entered message and analyze each row and column to get the encrypted message based on the number of rows and permutation provided by the key and decrypts it by reordering the columns of the matrix.
>> for rsa:
because it uses randomly generated prime numbers to get the value of the public and the private keys to change each value of the string converted to integer using ord method and encrypt it in numerical values and also to decrypt the numerical value of the encryption to the numerical form of the original text and convert each value into character to get the original message.


---- group members ---
1 Basliel Amsalu UGR/8569/13  SECTION 3
2 Fanual Asfaw UGR/4303/13  SECTION 3
3 Hanna Legesse UGR/4973/13  SECTION 3
4 Meron Abebe UGR/9559/13  SECTION 3

