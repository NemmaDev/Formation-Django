from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Produit
from django.views import View
from .forms import ProduitForm
from django.contrib import messages

# Create your views here.
def index(request , *args, **Kwargs):
    liste_produits=Produit.objects.all()
    context ={
        "produits":liste_produits,
        'nom':'Produits de la Boutique Nemma'
    }
    return render(request, 'index.html',context)

# class createProduct(View):
#     def get(self, request,*args, **kwargs):
#         return render(request, 'produit/create_produit.html')
    
#     def post(self,request,*args,**kwargs):
#         try:
#             nom=request.POST.get('nom')
#             description=request.POST.get('description')
#             prix=request.POST.get('prix')
#             image=request.FILES.get('image')

#             produit= Produit.objects.create(nom=nom, description=description,prix=prix,image=image)
#             #produit.save()

#             if produit:

#                 return HttpResponse('Produit enregistré avec succès')
#         except Exception as e:
#             return HttpResponse('Error lors de l\' enregistré du produit')

class createProduct(View):
    def get(self, request,*args, **kwargs):
        form=ProduitForm()
        return render(request, 'produit/create_produit.html',{'form':form})
    
    def post(self,request,*args, **kwargs):

        form= ProduitForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,'Produit enregistré avec succès')
            return redirect('produits:index')
        else:
            messages.error(request,'Error lors de l\' enregistré du produit')
            return render(request, 'produit/create_produit.html',{'form':form})