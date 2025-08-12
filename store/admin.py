from django.contrib import admin 
from django.contrib.contenttypes.admin import GenericTabularInline
from . import models
from django.urls import reverse
from django.db.models import QuerySet
from tags.models import TaggedItem



class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<65' , 'LOW')
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<65':
            return queryset.filter(inventory__lt = 65)

#-------------------------------------------------------------

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'membership']
    list_editable = ['membership' ,]
    ordering = ['first_name' , 'last_name']
    list_per_page = 5
    search_fields = ['first_name__istartswith' , 'last_name__istartswith']

#--------------------------------------------------------------

class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [TagInLine]
    prepopulated_fields = {
        'slug' : ['title']
    }
    exclude = ['collection']
    actions = ['clear_inventory']
    list_display = ['title' , 'unit_price' , 'inventory_status' , ]
    list_editable = ['unit_price']
    list_filter = ['last_update', InventoryFilter]
    ordering = ['title']
    list_per_page = 10




    @admin.display(ordering = 'inventory')
    def inventory_status(self , product):
        if product.inventory < 75:
            return 'LOW'
        return 'OK'
    
    @admin.action(description= 'Clear Inventory')
    def clear_inventory(self , request , queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request , 
            f'{updated_count} products were succeefully updated.'
            
        )
    
    

