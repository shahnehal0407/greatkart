from django.contrib import admin
from .models import Payment,Order,OrderProduct
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model=OrderProduct
    extra = 0
    readonly_fields = ('payment','user','product','quantity','product_price','ordered')









class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','full_name','order_total', 'phone','email','status','is_ordered']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','phone','Email']
    list_per_page = 20
    inlines = [OrderProductInline]




admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)

