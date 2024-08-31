from django.contrib import admin

# Register your models here.
from .models import Produit
#admin.site.register(Produit)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display=('nom','prix','description','image')