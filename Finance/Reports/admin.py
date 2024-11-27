from django.contrib import admin
from .models import Clients, Investors, UpcommingClientInvestments, UpcommingInvestorInvestments
# # Register your models here.

# admin.site.register(Clients)
# admin.site.register(Investors)
# admin.site.register(ClientInvestments)
# admin.site.register(InvestorInvestments)

































































































































































































































































































































































































from django.utils import timezone
import pytz
from django.contrib import admin
from .models import Clients, Investors, UpcommingClientInvestments, UpcommingInvestorInvestments, ClientInvestmentsProxy, InvestorInvestmentsProxy

from django.contrib import admin
from django.contrib.auth.models import User, Group

# Unregister the default User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.
admin.site.site_title = "Fianance"
admin.site.site_header = "Finance Management"
admin.site.index_title = "Finance Management"
class ClientsAdmin(admin.ModelAdmin):
    list_display = [ 'Name', 'Cnic', 'Contact', 'Address']

class InvestorsAdmin(admin.ModelAdmin):
    list_display = [ 'Name', 'Cnic', 'Contact', 'Address']
    
class ClientInvestmentsUpcomingAdmin(admin.ModelAdmin):
    list_display = ['client', 'dateFrom', 'dateTo', 'Amount', 'Profit']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        asia_timezone = pytz.timezone('Asia/Karachi')
        now = timezone.now().astimezone(asia_timezone)
        
        return queryset.filter(dateFrom__gte=now).order_by('dateFrom')

class InvestorInvestmentsUpcomingAdmin(admin.ModelAdmin):
    list_display = ['investor', 'dateFrom', 'dateTo', 'Amount', 'Profit']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        asia_timezone = pytz.timezone('Asia/Karachi')
        now = timezone.now().astimezone(asia_timezone)
        
        return queryset.filter(dateFrom__gte=now).order_by('dateFrom')


class ClientInvestmentsAllAdmin(admin.ModelAdmin):
    list_display = ['client', 'dateFrom', 'dateTo', 'Amount', 'Profit']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        return queryset.order_by('dateFrom')

class InvestorInvestmentsAllAdmin(admin.ModelAdmin):
    list_display = ['investor', 'dateFrom', 'dateTo', 'Amount', 'Profit']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        return queryset.order_by('dateFrom')


admin.site.register(UpcommingClientInvestments, ClientInvestmentsUpcomingAdmin)  # For upcoming data
admin.site.register(UpcommingInvestorInvestments, InvestorInvestmentsUpcomingAdmin)  # For upcoming data

admin.site.register(ClientInvestmentsProxy, ClientInvestmentsAllAdmin)  # For all data sorted
admin.site.register(InvestorInvestmentsProxy, InvestorInvestmentsAllAdmin)  # For all data sorted


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Investors, InvestorsAdmin)