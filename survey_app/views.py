from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    
    print(request.POST)
    context = {
        'fname': request.POST['first_name'].title(),
        'lname': request.POST['last_name'].title(),
        'city': request.POST['city'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
    }
    
    if 'black_belt' in request.POST:
        context['black_belt'] = request.POST['black_belt']
    if 'github_account' in request.POST:
        context['github_account'] = request.POST['github_account']
    if 'fav_color' in request.POST:
        context['fav_color'] = request.POST['fav_color']
        
    return render(request, 'result.html', context)