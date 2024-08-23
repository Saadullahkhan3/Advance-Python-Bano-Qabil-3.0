from utils.utils import is_int, is_float
from utils.math_opr import _avg, _product

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from json import loads, JSONDecodeError



@csrf_exempt
def total(request):
    try:
        data = loads(request.body)
        nums = data.get('nums', [])
        
        if not nums:
            return JsonResponse({"error": "There are should be numbers in base 10 (int/float/double) and also in iterable like List/Array"})
        
        if not all(map(is_int, nums) or map(is_float, nums)):
            return JsonResponse({"error": "All items should be numbers that all are should in base 10 (int/float/double)"})

        response = {"total": sum(nums)}
        return JsonResponse(response)
    
    except RuntimeError as run_e:
        return JsonResponse({"runtime_error": f"Error: {run_e}"})
    
    except JSONDecodeError:
        return JsonResponse({"Json error": "Request JSON is invalid"})
    

@csrf_exempt
def avg(request):
    try:
        data = loads(request.body)
        nums = data.get('nums', [])

        if not nums:
            return JsonResponse({"error": "There are should be numbers in base 10 (int/float/double) and also in iterable like List/Array"})
        
        if not all(map(is_int, nums) or map(is_float, nums)):
            return JsonResponse({"error": "All items should be numbers that all are should in base 10 (int/float/double)"})
        
        response = {"avg": _avg(nums)}
        return JsonResponse(response)
    
    except RuntimeError as run_e:
        return JsonResponse({"runtime_error": f"Error: {run_e}"})
    
    except JSONDecodeError:
        return JsonResponse({"Json error": "Request JSON is invalid"})


@csrf_exempt
def product(request):
    try:
        data = loads(request.body)
        nums = data.get('nums', [])

        if not nums:
            return JsonResponse({"error": "There are should be numbers in base 10 (int/float/double) and also in iterable like List/Array"})    

        if not all(map(is_int, nums) or map(is_float, nums)):
            return JsonResponse({"error": "All items should be numbers that all are should in base 10 (int/float/double)"})
        
        response = {"product": _product(nums)}
        return JsonResponse(response)
        
    except RuntimeError as run_e:
        return JsonResponse({"runtime_error": f"Error: {run_e}"})
    
    except JSONDecodeError:
        return JsonResponse({"Json error": "Request JSON is invalid"})
    

