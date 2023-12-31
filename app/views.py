from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import controller

'''
    ---------------------------------- Website view client ----------------------------------
'''
def index(request):
    return render(request, 'home/ezzepay.html')

@csrf_exempt  
def ezzepay_register_login(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.ezzepay_register_login(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
def sucessfull(request):
    return render(request, 'home/sucessfull.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.signin(data, request)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
def logout(request):
    if request.user.is_authenticated:
        response = controller.signout(request)
        print(response)
        if response['status']:
            return redirect('/')
    else:
        return redirect('/')

@csrf_exempt
def get_client(request):
    if request.user.is_authenticated:
        '''response = controller.get_clients()
        return render(request, 'home/manager/client.html', {
            'clients': response
        })'''
        response = controller.method_not_allowed()
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def add_client(request):
    if request.method == 'POST':
        return render(request, 'home/manager/add.html')
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def add_new_client(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.add_new_client(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def view_client(request):
    data = request.body.decode('utf-8')
    response = controller.view_client(data)
    return render(request, 'home/manager/edit.html', {
        'client': response
    })

@csrf_exempt
def update_client(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.update_client(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
    return JsonResponse(response)

@csrf_exempt
def delete_client(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.delete_client(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
    return JsonResponse(response)


'''
    ---------------------------------- API Greyhounds ----------------------------------
'''    
@csrf_exempt
def greyhounds_profile_get(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.is_greyhound_already_registered(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)    

@csrf_exempt
def greyhounds_profile_filter(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.filters_greyhounds(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)    

@csrf_exempt
def greyhounds_new(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.create_new_greyhound(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
   

@csrf_exempt
def races_day_filter(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.filter_races_day(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def races_day_new(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.create_races_day(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def races_day_remove(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.remove_races_day(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def races_new(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.create_race(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def races_filter(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.filter_races(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def race_update(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.update_result_race(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def race_calculates(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.calculate_races(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def save_odds(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.save_odds(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def race_delete(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.remove_race(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    


@csrf_exempt
def delete_info_history(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.delete_info_history(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def new_info_history(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.new_info_history(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def filter_info_history(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.filter_info_history(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    

@csrf_exempt
def delete_odds(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.delete_odds(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)

@csrf_exempt
def new_odds(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.new_odds(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def filter_odds(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.filter_odds(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def identification_odd(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.identification_odd(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
    
@csrf_exempt
def hacked_profile(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        response = controller.hacked(data)
        return JsonResponse(response)
    else:
        response = controller.method_not_allowed()
        return JsonResponse(response)
