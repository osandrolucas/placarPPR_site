from django.shortcuts import render

def post_list(request):
    return render(request, 'placarPPR/post_list.html', {})
