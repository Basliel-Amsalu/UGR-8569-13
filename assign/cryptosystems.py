import math
import random
import sys
class Affine:
    def __init__(self) -> None:
        pass
    # extended euclidean algorithm
    def egcd(self,a, b):
        x,y, u,v = 0,1, 1,0
        while a != 0:
            q, r = b//a, b%a
            m, n = x-u*q, y-v*q
            b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
        return gcd, x, y
    #modular inverse
    def modinv(self,a, m):
        gcd, x, y = self.egcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m
    # affine cipher encryption function
    def encrypt(self,text, key):
        return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                    + ord('A')) for t in text.upper().replace(' ', '') ])
    # affine cipher decryption function
    def decrypt(self,cipher, key):
        return ''.join([ chr((( self.modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                        % 26) + ord('A')) for c in cipher ])

class Transposition:
    def __init__(self):
        self.key = "cypher"
    
    # Encryption
    def encrypt(self,msg):
        cipher = ""
    
        # track key indices
        k_indx = 0
    
        msg_len = float(len(msg))
        msg_lst = list(msg)
        key_lst = sorted(list(self.key))
    
        # calculate column of the matrix
        col = len(self.key)
        
        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))
        # the empty cell of the matix 
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)
    
        # create Matrix and insert message and 
        # padding characters row-wise 
        matrix = [msg_lst[i: i + col] 
                for i in range(0, len(msg_lst), col)]
    
        # read matrix column-wise using key
        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
            cipher += ''.join([row[curr_idx] 
                            for row in matrix])
            k_indx += 1
    
        return cipher
    
    # Decryption
    def decrypt(self,cipher):
        msg = ""
    
        # track key indices
        k_indx = 0
    
        # track msg indices
        msg_indx = 0
        msg_len = float(len(cipher))
        msg_lst = list(cipher)
    
        # calculate column of the matrix
        col = len(self.key)
        
        # calculate maximum row of the matrix
        row = int(math.ceil(msg_len / col))
    
        # convert key into list and sort alphabetically so we can access each character by its alphabetical position.
        key_lst = sorted(list(self.key))
    
        # create empty matrix to store deciphered message
        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]
    
        # Arrange the matrix column wise according to permutation order by adding into new matrix
        for _ in range(col):
            curr_idx = self.key.index(key_lst[k_indx])
    
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx]
                msg_indx += 1
            k_indx += 1
    
        # convert decrypted msg matrix into a string
        try:
            msg = ''.join(sum(dec_cipher, []))
        except TypeError:
            raise TypeError("This program cannot",
                            "handle repeating words.")
    
        null_count = msg.count('_')
    
        if null_count > 0:
            return msg[: -null_count]
    
        return msg 
class Rsa:
    def __init__(self) -> None:
        pass
    #rabin miller method to verify primality 
    #uses the fermats theorem
    def rm(self,n,d):
        a = random.randint(2,(n-2)-2)
        t= pow(a,int(d),n)
        if t == 1 or t== n-1:
            return True
        while d!= n-1:
            t = pow(t,2,n)
            d*=2
            if t==1:
                return False
            elif t==n-1:
                return True
        return False

    #checking if the number is prime or not
    #falls back to the rabin miller method when uncertain
    def isprime(self,num):
        if num<2:
            return False
        #list of prime numbers below 1000
        #so we can use them to check primality for very big numbers
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        if num in lowPrimes:
            return True
        for prime in lowPrimes:
            if num%prime == 0:
                return False
        c = num-1
        while c%2 == 0:
            c/=2
        for i in range(128):
            if not self.rm(num,c):
                return False
        return True
    #generating the keys p,q,e,d,,n,r
    def generatekeys(self,keysize = 1024):
        e = d = n =0
        p = self.generatelargeprime(keysize)
        q = self.generatelargeprime(keysize)
        n = p*q
        r = (p-1)*(q-1)
        while True:
            e = random.randrange(2**(keysize-1),2**keysize-1)
            if (self.iscoprime(e,r)):
                break
        d = self.modinv(e,r)
        return e,d,n
    # method to generate random large prime numbers as the name implies for the value of p,q
    # it is quite safer for the encryption to use randomly generated large prime numers
    def generatelargeprime(self,keysize):
        while True:
            num = random.randrange(2**(keysize-1),2**keysize-1)
            if (self.isprime(num)):
                return num
    #checks the coprimality of the given arguments using their gcd
    #used to check the coprimality of e,r
    def iscoprime(self,p,q):
        return self.gcd(p,q) == 1
    #computes gcd using euclidean algorithm
    def gcd(self,p,q):
        while q:
            p,q = q,p%q
        return p
    # extended euclidean algorithm
    # for back tracking
    def egcd(self,a,b):
        s = 0; so = 1
        t = 1; to = 0
        r = b; ro = a
        while r!= 0:
            q = ro//r
            ro,r = r,ro-q*r
            so,s = s,so-q*s
            to,t = t,to-q*t
        return ro, so, to   
    #modular inverse of the arguments
    #used to find d
    def modinv(self,a,b): 
        gcd,x,y = self.egcd(a,b)
        if x<0:
            x+=b 
        return x
    #the encryption algorithm
    def encrypt(self,e,n,msg):
        cipher = ""
        for c in msg:
            m= ord(c)
            cipher += str(pow(m,e,n))+" " 
        return cipher
    #the decryption algorithm
    def decrypt(self,d,n,cipher):
        msg = ""
        ciph = cipher.split()
        for cip in ciph:
            if cip:
                c = int(cip)
                msg+=chr(pow(c,d,n))
        return msg
#the main function to run all the encryption/decryption systems
def main():
    #command line argument lengthe
    n = len(sys.argv)
    #the message to be encrypted from the command line
    message =  ""
    for i in range(1,n-1):
        message += sys.argv[i]+" "
    #the encryption type chosen
    encryption_type = sys.argv[-1]
    if n >= 3:
        if encryption_type == "Rsa":
            cryp= Rsa()
            keysize = 32
            e,d,n = cryp.generatekeys(keysize)
            msg = message 
            enc = cryp.encrypt(e,n,msg)
            print("Encrypted Message: {}".format(enc))
            print("decrypted message: {}".format(cryp.decrypt(d,n,enc)))
        elif encryption_type == "Transposition":
            msg = message
            cryp = Transposition()
            cipher = cryp.encrypt(msg)
            print("Encrypted Message: {}".format(cipher))
            print("Decrypted Message: {}".format(cryp.decrypt(cipher)))
        elif encryption_type == "Affine":
            cryp = Affine()
            text = message
            key = [17, 20]
            affine_encrypted_text = cryp.encrypt(text, key)
            print('Encrypted Text: {}'.format( affine_encrypted_text ))
            print('Decrypted Text: {}'.format( cryp.decrypt(affine_encrypted_text, key) ))
        else:
            print("invalid encryption type")
    else:
        print("number of arguments you entered is not correct")

if __name__ == '__main__':
    main()