import email, imaplib, base64, os
from time import sleep, strftime

class Mail():
    def __init__(self):
        self.m = imaplib.IMAP4_SSL('imap.gmail.com')
        self.m.login("Ccprojecthermes@gmail.com", "Hermes123321#")
        self.m.select('INBOX')

    def construction(self, q):
        array = [None] * 17
        completed = b''
        while True:
            if not q.empty():
                f = q.get()
                array[int(f[1])-1] = f[0]
            else:
                pass
            if not None in array:
                print(array)
                for num in array:
                    base64.b64decode(num)
                    completed += num.encode()

                with open("final.jpeg", "wb") as f:
                    f.write(completed)
            else:
                for pos, num in enumerate(array):
                    if num is None:
                        print("Position",str(int(pos)+1), "is empty.")
                    else:
                        print("Position",str(int(pos)+1), "is full")
                sleep(.5)
                os.system('clear')

    def start(self, d, q):
        coords = [None]*2
        while True:
            #typ, data = self.m.search(None, '(ON {0} SUBJECT "SBD Msg From Unit: 300434063827480" UNSEEN)'.format(strftime("%d-%b-%Y")))
            typ, data = self.m.search(None, '(ON 8-Aug-2018 SUBJECT "SBD Msg From Unit: 300434063827480" UNSEEN)')
            for num in data[0].split():
                typ, message = self.m.fetch(num, '(RFC822)')
                body = message[0][1]
                mail = email.message_from_bytes(body)
                x = 0
                for part in mail.walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    if x%2:
                        q.put(part.get_payload(decode=True).decode().split("["))
                    else:
                        a = str(part.get_payload(decode=True)).replace("\\r\\n","").split("Unit Location: ")
                        b = a[1].split()
                        c = b[5].split("CEPradius")
                        coords[0] = float(b[2])
                        coords[1] = float(c[0])
                        d.put(coords)
                    x += 1
                self.m.store(num, '+FLAGS', '\Seen')

    def logout(self):
        print("Logging Out")
        self.m.close()
        self.m.logout()
