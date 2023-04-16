import base64
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        msg = request.POST.get("msg")
        key = request.POST.get("key")
        mode = request.POST.get("mode")
        if mode == "e":
            msg_bytes = msg.encode("utf-8")
            key_bytes = key.encode("utf-8")
            result_bytes = base64.b64encode(msg_bytes + key_bytes)
            result = result_bytes.decode("utf-8")
        elif mode == "d":
            msg_bytes = base64.b64decode(msg.encode("utf-8"))
            key_bytes = key.encode("utf-8")
            result_bytes = msg_bytes[:-len(key_bytes)]
            result = result_bytes.decode("utf-8")
        else:
            result = "Wrong mode entered. Try again."
    else:
        result = ""
    return render(request, "index.html", {"result": result})
