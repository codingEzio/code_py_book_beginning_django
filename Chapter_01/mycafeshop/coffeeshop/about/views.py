from django.shortcuts import render


def contact(request):
    """
    About the param 'request'
        I. Access the content from a web request
        II. Then you can
            -- do something with it
            -- or do queries to a database
        III. in the end, you pass the info to a template
    """
    
    return render(request, 'about/contact.html')