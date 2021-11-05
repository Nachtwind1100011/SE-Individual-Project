from Crypto.Cipher import ChaCha20
from dhooks import Webhook, File
import requests


def keyEstablish():
    p = 73173011257352935459318495537738755732638377779696984095503297474994032021828155164079756088822919458062032560190846290567666190993822164069073456710381913728973236033243042162414290692238839434152241
    q = 14319539760942308333108318088781155100416173656375406662387866628381930077595802477422210140379139558083840890192531874658876658688348746044633699146148956137537637244150494896253255385179

    print("Would you like to create a key? Otherwise the safe predefined default key will be used.")
    keySet = input("type yes/Y to enter key generation process: ")

    if keySet == "yes" or keySet == "Y":

        print("enter a random number between 1 and " + str(q))
        a = int(input())
        A = pow(2, a, p)
        print("Send the following full integer to your correspondent: " + str(A))
        B = int(input("Enter the large integer your correspondent has sent in return: "))
        key = str(pow(B, a, p))
        print(str(key))
        key = bytes(key.encode())
        key = key[:32]
        return key

    else:
        key = str(
            "33294589197348058923167874396276398243480898329400139821043550898076163970032249866693974278879008728260524084557620909841996279602489401050209449313996940253240976443510154779291933615005820938851050")
        key = bytes(key.encode())
        key = key[:32]
        return key


class CC20:
    filename = "test.bin"
    hook = Webhook("https://discord.com/api/webhooks/838280445740843060/IghteonqZm7-ekMK9HMdazzL0BWSTuJaOqf9jYVzq-5lBF71uW17iDBpvydsbtHTdxij")
    key = keyEstablish()

    nonce = b'11111111'
    mode = ""

    while mode != "done":

        message = ""
        mode = input("select mode (en to encrypt, de to decrypt, \"done\" to exit): ")
        if mode == "done":
            exit()
        if mode == "en":
            cipher = ChaCha20.new(key=bytes(key), nonce=nonce)
            f = open("output.bin", 'wb')
            while message != "exit":
                message = input("message to be encoded (after you are finished, type \"exit\" on a new line): ")
                if message != "exit":
                    message = bytes((message + "\n").encode())
                    ciphertext = cipher.encrypt(message)
                    f.write(ciphertext)
                    f.flush()
            tbs = File("output.bin")
            hook.send(file=tbs)
            f.close()

        elif mode == "de":

            dcipher = ChaCha20.new(key=bytes(key), nonce=nonce)
            with open("url.txt") as f:
                url = f.read()

            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
            f = open(filename, 'rb')
            plaintext = dcipher.decrypt(f.read())
            print(plaintext.decode())
            f.close()

        else:
            print("invalid mode")

# b'x|\xb5\x85\x81\xeb\x93\x13?#c$\x06'
