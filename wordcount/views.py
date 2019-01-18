from django.shortcuts import render

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']

    ip_address = request.META['REMOTE_ADDR']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'wordcount/count.html', {
        'fulltext': full_text, 
        'ip_address': ip_address,
        'word_list': word_list, 
        'total': len(word_list),
        'dictionary' : word_dictionary.items()
    })