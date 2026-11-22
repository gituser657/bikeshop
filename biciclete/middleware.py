
# lab 1, cerinta 8, implementare middleware pentru getIP
# functia get_IP definita la ex 4 in views.py este mutata in noul fisier 
# middleware.py care va centraliza astfel de functii in implementarile 
# viitoare. 
# middleware.py va fi link-uit in settings.py

def get_ip(request):                       
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    return request.META.get('REMOTE_ADDR')



class GetIPmiddleware:
    def __init__(self, get_response ):
        self.get_response = get_response
    
    def __call__(self, request):
        request.ip_client = get_ip(request)
        response = self.get_response(request)
        return(response)