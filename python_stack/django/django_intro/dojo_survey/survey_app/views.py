from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    return render(request, 'form.html')

# def process(request):
#     if request.method == 'POST':
#         context={
#             'name': request.POST['name'],
#             'ice': request.POST['ice-cream'],
#             'top': request.POST['topping']
#         }
#         return redirect('/results')
#         # return render(request,'results.html', context)
#     return render(request,'results.html')

def process(request):
    if request.method == 'POST':
        name = request.POST ['name']
        topping = request.POST ['topping']
        ice_cream = request.POST ['ice_cream']
        request.session ['name'] = name
        request.session ['ice_cream'] = ice_cream
        request.session ['topping'] = topping

        return redirect('/results')
        # return render(request,'results.html', context)
    return render(request,'results.html')

def results(request):
    print('got here from redirect')
    return render(request,'results.html')
