import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def is_valid(A, B):
    if A is None or B is None:
        return False, 'Data should contain two numbers named A and B.'
    if type(A) not in (int, float) or type(B) not in (int, float):
        return False, 'Both A and B should be numbers.'
    return True, None


def make_response(data, status_code):
    response = JsonResponse(data)
    response.status_code = status_code
    return response


@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A + B})
        else:
            return make_response({'error': 'No data provided!'}, 400)
    return make_response({'error': 'Method not allowed.'}, 405)


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A - B})
        else:
            return make_response({'error': 'No data provided!'}, 400)
    return make_response({'error': 'Method not allowed.'}, 405)


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            return JsonResponse({'answer': A * B})
        else:
            return make_response({'error': 'No data provided!'}, 400)
    return make_response({'error': 'Method not allowed.'}, 405)


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            A = data.get('A', None)
            B = data.get('B', None)
            valid, error = is_valid(A, B)
            if not valid:
                return make_response({'error': error}, 400)
            if B == 0:
                return make_response({'error': 'Division by zero!'}, 400)
            return JsonResponse({'answer': A / B})
        else:
            return make_response({'error': 'No data provided!'}, 400)
    return make_response({'error': 'Method not allowed.'}, 405)
