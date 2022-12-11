from django.contrib import admin
from .models import Order, Payment, OrderProduct
# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ['user','product','payment','quantity','ordered','product_price','variations']
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','full_name','email','phone','city','order_total','status','is_ordered','created_at']
    list_filter = ['status','is_ordered']
    list_per_page = 20
    search_fields = ['order_number','email','first_name','last_name','phone']
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)