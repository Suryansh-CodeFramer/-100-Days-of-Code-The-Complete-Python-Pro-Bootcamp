
alpha=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def encryption():


    passin=input("enter your password").upper()
    shift=int(input("enter your shift number"))
    print("encoding your password")
    passlist=list(passin)
    encrypted_password=""

    for ch in passlist:
        if ch in alpha:
            indexOfIinAlpha=alpha.index(ch)
            encrypted_password=encrypted_password + alpha[(indexOfIinAlpha+shift)%26]

    print(encrypted_password)
    print(passin)




def decryption():
    print("decoding your password")
    dpassin=input("enter your password").upper()
    decrypted_password=""
    decpls=list(dpassin)
    dshift=int(input("enter your dshift number"))
    for ch in decpls:

        if ch in alpha:
            indexOfIinAlpha=alpha.index(ch)
            decrypted_password=decrypted_password+alpha[(indexOfIinAlpha-dshift)%26]

    print(decrypted_password)
    print(dpassin)



def choice():
    ch=input("enter your choice \n 1 to encrypt \n2 to decrypt \n3 to continue \n4 to exit")
    if ch=="1":
        encryption()
    elif ch=="2":
        decryption()
    elif ch=="3":
        choice()
    elif ch=="4":
        return False

    else:
        print("enter valid choice")



t=True
while t:
    t=choice()


