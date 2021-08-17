from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist
import json

def index(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    return html(request, "index")


def html(request, filename):
    # labels = ["Jan", "Feb", "Mar", "Apr"]
    # data = [100,80,150,200]

    labels = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5]
    spo2_data = [
        94.0,95.0,95.0,98.0,97.0,97.0,97.0,96.0,98.0,97.0,
        97.0,95.0,97.0,96.0,97.0,99.0,97.0
    ]
    audio_labels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    audio_data =  [-5.8691,5.204,-32.0421,56.5586,-91.2613,-4.4865,15.6937,4.5946,
                   1.5676,16.1982,17.2072,13.6757,-15.5856,-13.0631,0.5586,9.6396,]
    # audio_data = [
    #               -5.8691,5.204,-32.0421,56.5586,-91.2613,-4.4865,15.6937,4.5946,
    #               1.5676,16.1982,17.2072,13.6757,-15.5856,-13.0631,0.5586,9.6396,
    #               -5.4955,40.9189, -0.4505,39.9099,10.1441,5.6036,76.2342,25.2793,
    #               -13.0631,-1.4595,-33.7477,-22.6486,13.1712,-8.5225,8.1261,-6.5045,
    #               -19.1171,-3.982,-8.018,23.7658,15.1892,2.5766,-14.0721,29.3153,              
    #               -5.4955,16.1982,-19.1171,-37.2793,-2.4685,8.6306,2.5766,33.8559,-4.991,
    #               28.8108,1.0631,15.6937,9.6396,-52.9189,18.2162,-32.7387,-5.4955,-1.4595,
    #               12.6667,17.7117,0.0541,4.5946,8.1261,15.6937,-29.2072,-10.5405,4.0901,              
    #               3.0811,27.8018,-4.4865,23.7658,2.0721,-11.5495,-16.0901,13.6757,9.1351,                 
    #               23.2613,-9.5315,6.1081,-0.955,-16.0901,-1.4595,-27.1892,2.0721,-47.8739,
    #              -11.5495,1.0631,6.1081,53.5315,1.0631,2.0721,8.6306,-9.027,6.6126,20.7387,
    #              -18.6126,-16.0901,-7.009,33.3514,26.2883,-11.045,-10.5405,6.6126,2.5766
    # ]
    # audio_labels = [] 
    context = {"filename": filename,
               "collapse": "",
               "labels": json.dumps(labels),
               "spo2_data": json.dumps(spo2_data),
               "audio_labels": json.dumps(audio_labels),
               "audio_data": json.dumps(audio_data),
           }
    if request.user.is_anonymous and filename != "login":
        return redirect("/login.html")
    if filename == "logout":
        logout(request)
        return redirect("/")
    if filename == "login" and request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

        print("login")
        print(username, password)
    print(filename, request.method)
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)

