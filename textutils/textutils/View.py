#I have created this file - prabhat
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'prabhat','place':'jupyter'}
    return render(request,'index.html',params)
    # return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')
    k = ""
    f=0


    if removepunc=="on":
     punctuations='''!()-[]{}:;'"\,<>./?@#$$%^&*_~'''
     analyzed=""

     for char in djtext:
        if char not in punctuations:
            analyzed+=char
     k+="Remove_punctuations| "
     djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        djtext=analyzed
        k+="Capitalize| "
    if extraspaceremove=="on":
        analyzed=""
        for i,j in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                analyzed+=j
        k+="Remove_extraspace| "
        djtext=analyzed
    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
        k+="Removed_newline| "




    if charcount=="on":
        if removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on":
            analyzed = ""
        analyzed=analyzed+"\n(count: "+str(len(djtext))+")"
        k+="Character count| "


    if removepunc!="on" and fullcaps!="on" and newlineremove!="on" and extraspaceremove!="on" and charcount!="on":
         f=1
         analyzed=djtext
         params={'purpose':'No change','analyzed_text':analyzed}
    #analyze the text
    if f==0:
        params={'purpose':k,'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    if f==1:
        return render(request,'analyze.html',params)






