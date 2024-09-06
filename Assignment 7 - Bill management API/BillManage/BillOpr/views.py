from utils.utils import even_split, add_tax, add_discount

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from json import loads, JSONDecodeError



'''
++++++  NOTE  +++++++
Postman export is provided that includes below created APIs with their showcase and document!
'''


@csrf_exempt
def split_evenly(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            
            no_of_people = data.get("noOfPeople", 0)
            if (no_of_people <= 0) or (not isinstance(no_of_people, int)):
                return JsonResponse({"ERROR": "noOfPeople should be number that greater than 0!"})
            
            total = data.get("total", 0)
            if (total <= 0) or (not isinstance(total, int | float)):
                return JsonResponse({"ERROR": "Total should be a number that greater than 0!"})

            evenly_splited = even_split(total, no_of_people)

            return JsonResponse({"evenly_splited": evenly_splited})
        
        else:
            return JsonResponse({"ERROR": "Request should be POST."})
        
    except JSONDecodeError:
        return JsonResponse({"ERROR": "JSON format error."})
    
    except TypeError as et:
        return JsonResponse({"ERROR": f"Invalid type. Details: {et}"})
    
    except:
        return JsonResponse({"ERROR": "Server may have several issues."})


@csrf_exempt
def split_unevenly(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            
            peoples = data.get("peoples", 0)
            if (not isinstance(peoples, list)):
                return JsonResponse({"ERROR": 'peoples should be a List/Array, like: [{"peoples": [{"name": "Saad", "money": 1000}]}'})
            
            total = data.get("total", 0)
            if (not total) or (total <= 0):
                return JsonResponse({"ERROR": "Total should be a number that greater than 0!"})

            evenly_splited = even_split(total, len(peoples))
            unevenly_splited = dict()

            for person in peoples:
                unevenly_splited[person["name"]] = evenly_splited - person["money"]

            return JsonResponse({"unevenly_splited": unevenly_splited})
        
        else:
            return JsonResponse({"ERROR": "Request should be POST."})
        
    except JSONDecodeError:
        return JsonResponse({"ERROR": "JSON format error."})
    
    except TypeError as et:
        return JsonResponse({"ERROR": f"Invalid type. Details: {et}"})
    
    except:
        return JsonResponse({"ERROR": "Server may have several issues."})


@csrf_exempt
def add_tip_tax_and_evenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)

            no_of_people = data.get("noOfPeople", 0)
            if (no_of_people <= 0) or (not isinstance(no_of_people, int)):
                return JsonResponse({"ERROR": "noOfPeople should be number that greater than 0!"})
            
            total = data.get("total", 0)
            if (total <= 0) or (not isinstance(total, int | float)):
                return JsonResponse({"ERROR": "Total should be a number that greater than 0!"})

            # Extracting tax rate and tip, if not then 0 will considered
            tax_rate = data.get("tax_rate", 0)
            tip = data.get("tip", 0)

            # Adding tax and tip, when 0 then total will not effected
            total = add_tax(total, tax_rate) + tip

            evenly_splited = even_split(total, no_of_people)

            return JsonResponse({"evenly_splited": evenly_splited})
        
        else:
            return JsonResponse({"ERROR": "Request should be POST."})
        
    except JSONDecodeError:
        return JsonResponse({"ERROR": "JSON format error."})
    
    except TypeError as et:
        return JsonResponse({"ERROR": f"Invalid type. Details: {et}"})
    
    except:
        return JsonResponse({"ERROR": "Server may have several issues."})


@csrf_exempt
def add_discount_and_evenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            
            no_of_people = data.get("noOfPeople", 0)
            if (no_of_people <= 0) or (not isinstance(no_of_people, int)):
                return JsonResponse({"ERROR": "noOfPeople should be number that greater than 0!"})
            
            total = data.get("total", 0)
            if (total <= 0) or (not isinstance(total, int | float)):
                return JsonResponse({"ERROR": "Total should be a number that greater than 0!"})

            # Extracting tax rate and tip, if not then 0 will considered
            discount_rate = data.get("discount_rate", 0)

            # Adding tax and tip, when 0 then total will not effected
            total = add_discount(total, discount_rate)

            evenly_splited = even_split(total, no_of_people)

            return JsonResponse({"evenly_splited": evenly_splited})
        
        else:
            return JsonResponse({"ERROR": "Request should be POST."})
        
    except JSONDecodeError:
        return JsonResponse({"ERROR": "JSON format error."})
    
    except TypeError as et:
        return JsonResponse({"ERROR": f"Invalid type. Details: {et}"})
    
    except:
        return JsonResponse({"ERROR": "Server may have several issues."})


@csrf_exempt
def shared_items_and_unevenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            
            shared_items = data.get("shared_items", 0)
            if (not shared_items):
                return JsonResponse({"ERROR": 'shared_items should be like -> {shared_items: [{"item": "Biryani", "peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000}]}'})
            
            response = {"shared_items": list(), "wrong_items": list()}

            for shared_item in shared_items:
                item_is_wrong = False

                total = shared_item.get("total", 0)
                if not total:
                    total = "Total is not exists!"
                    item_is_wrong = True
                
                peoples = shared_item.get("peoples", 0)
                if not peoples:
                    peoples = "Peoples are not exists!"
                    item_is_wrong = True

                # Checking that both requirement are fulfilled?
                if item_is_wrong:
                    # Adding wrong shared items and also their errors, then skip it
                    response["wrong_items"].append({"item": shared_item, "errors": (total, peoples)})
                    continue
                
                item = shared_item.get("item", None)
                if not item:	# item name is not a big deal
                    item = "N/A"

                evenly_splited = even_split(total, len(peoples))
                
                item_result = {item: list(), "total": total}

                for person in peoples:
                    money = evenly_splited - person["money"]
                    item_result[item].append({"name": person["name"], "money": money})

                response["shared_items"].append(item_result)

            return JsonResponse(response)
        
        else:
            return JsonResponse({"ERROR": "Request should be POST."})
        
    except JSONDecodeError:
        return JsonResponse({"ERROR": "JSON format error."})
    
    except TypeError as et:
        return JsonResponse({"ERROR": f"Invalid type. Details: {et}"})
    
    except:
        return JsonResponse({"ERROR": "Server may have several issues."})

