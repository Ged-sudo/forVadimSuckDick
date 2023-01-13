from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render, redirect

from . import forms
from .models import MenueDonar
from . import calculate_at_now

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ""
        model = MenueDonar
        fields = ['pk', 'menue_choices', 'count', 'date_sale']

class InfoGet(APIView):
    def get(self, request, format = None):
        info_items = MenueDonar.objects.all()
        serializer = InfoSerializer(info_items, many=True)  
        return Response({"Info - ":serializer.data})


def addInfoFromPage(request):
    if request.method == 'POST':
        form = forms.AddInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addNewInfo')
        else:
            return redirect('addNewInfo')
    form = forms.AddInfoForm()
    
    return render(request, 'count_sale/index.html', {'form': form})

def all_item_sell(request):
    item = MenueDonar.objects.all()
    all_marga = calculate_at_now.needed_info
    return render(request, 'count_sale/all_sale.html', {'all_item_sell': item})