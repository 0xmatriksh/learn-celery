from django.shortcuts import redirect, render
from celery.result import AsyncResult

# Create your views here.
from .tasks import add


def home(request):
    # add.delay(4,4)
    # print(type(x))
    print(1)
    ans = 0
    if request.method == 'POST':
        r = add.delay(18,4)
        ans = AsyncResult(r.id).get()  

    context = {
        'ans':ans
    }
    return render(request, 'learn/index.html',context)
