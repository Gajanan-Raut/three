def three_middleware(get_response):
    print("Code for initialization and configuration")

    def three_function(request):
        print("Code to be executed before view is called")
        response=get_response(request)
        print("Code to be executed after view is called")
        return response
    
    return three_function