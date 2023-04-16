from django.shortcuts import render
import base64

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def home(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        k = request.POST['key']
        m = request.POST['mode']
        m.lower()
        if m == 'e':
            result = encode(k, msg)
        elif m == 'd':
            result = decode(k, msg)
        else:
            result = 'Wrong mode entered. Try again.'
        return render(request, 'home.html', {'result': result})
    else:
        return render(request, 'home.html')
