from django.shortcuts import render
from django.http import HttpResponse
import pickle
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def admission_client(request):
    return render(request,'index.html')
def predict(request):
    
    age=int(request.GET['age'])
    tot_bilirubin=int(request.GET['tot_bilirubin'])
    direct_bilirubin=int(request.GET['direct_bilirubin'])
    tot_proteins=int(request.GET['tot_proteins'])
    albumin=int(request.GET['albumin'])
    ag_ratio=int(request.GET['ag_ratio'])
    sgot=int(request.GET['sgot'])
    alkphos=int(request.GET['alkphos'])  
    model=pickle.load(open("/home/abhijan/rf.sav","rb"))
    chances=model.predict([[age,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgot,alkphos]])
    return render(request,"result.html",{'res':chances[0]*100})
