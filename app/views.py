from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import ObjectDoesNotExist
from mysql.connector.cursor import SQL_COMMENT
from .models import User
import mysql.connector

import pymysql.cursors
from operator import itemgetter
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    return html(request, "index")
def welcome(req):
    return render(req,'welcome.html')
def login(req):
    if req.method == "POST":
        con = mysql.connector.connect(host="localhost", user="root", password="lucas3195",database="Health_platform", auth_plugin='mysql_native_password')
        cursor = con.cursor(buffered=True)
        con2 = mysql.connector.connect(host="localhost", user="root", password="lucas3195",database="Health_platform", auth_plugin='mysql_native_password')
        cursor2 = con2.cursor(buffered=True)

        sql_command = "SELECT email FROM app_user"
        sql_command2 = "SELECT password FROM app_user"
        cursor.execute(sql_command)
        cursor2.execute(sql_command2)

        e = []
        p = []
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        # print(e)
        # print(p)
        res = list(map(itemgetter(0),e))
        res2 = list(map(itemgetter(0),p))
        print(res)
        print(res2)
        if req.method == "POST":
            email = req.POST['email']
            password = req.POST['password']
            i=0
            k=len(res)
            while i < k:
                if res[i] == email and res2[i] == password:
                    Email = {'email':email}
                    return render(req,'welcome.html', Email)
                    break
                i += 1
            else:
                messages.error(req, "請檢查帳號密碼")
                return redirect('login')
    return render(req,'login.html')
def register(req):
    if req.method == "POST":
        user = User()

        user.name = req.POST['name']
        user.birth = req.POST['birth']
        user.email = req.POST['email']
        user.password = req.POST['password']
        user.repassword = req.POST['repassword']
        user.height = req.POST['height']
        user.weight = req.POST['weight']
        user.neck_line = req.POST['neck_line']

        if user.password != user.repassword:
            messages.error(req, '密碼輸入不一致')
            return redirect('register')
        elif user.fname == "" or user.password == "":
            messages.info(req, '請填入基本資料')
            return redirect('register')
        else:
            user.save()
    return render(req,'register.html')

def first_page(req):
    return render(req,'first_page.html')
def ess(req):
    if req.method == "GET":
        print(req.GET)
    return render(req,'ess.html')
def pretest(req):
    return render(req,'pretest.html')
def VoiceRecognition(req):
    ess_total = req.GET
    return render(req,'import_csv.html', ess_total)
def KeyPoint(req):
    return render(req,'key_point.html')
def KeyPointResult(req):
    return render(req,'key_point_result.html')

def index(req):
    
    ess_total = req.GET
    print(ess_total)
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
    context = {
               "collapse": "",
               "labels": json.dumps(labels),
               "spo2_data": json.dumps(spo2_data),
               "audio_labels": json.dumps(audio_labels),
               "audio_data": json.dumps(audio_data),
               "ess_total": ess_total,
           }
    

    return render(req,'index.html', ess_total)

def index_2(req):
    ess_total = req.GET
    print(ess_total)
    return render(req,'index_2.html', ess_total)

@csrf_exempt  
def index_3(req):
    ess_total = req.GET
    return render(req,'index_3.html', ess_total)

def importCsv(req):
    return render(req,'import_csv.html')