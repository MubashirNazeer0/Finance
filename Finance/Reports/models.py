from django.db import models

# Create your models here.
class Clients(models.Model):
    Name=models.CharField(max_length=100)
    Cnic=models.CharField(max_length=100)
    Contact=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name

class Investors(models.Model):
    Name=models.CharField(max_length=100)
    Cnic=models.CharField(max_length=100)
    Contact=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name

class UpcommingClientInvestments(models.Model):
    client=models.ForeignKey(Clients, on_delete=models.CASCADE)
    dateTo=models.DateField()
    dateFrom=models.DateField()
    Amount=models.CharField(max_length=100)
    Profit=models.CharField(max_length=100)

    def __str__(self):
        return self.client.Name
    
class UpcommingInvestorInvestments(models.Model):
    investor=models.ForeignKey(Investors, on_delete=models.CASCADE)
    dateTo=models.DateField()
    dateFrom=models.DateField()
    Amount=models.CharField(max_length=100)
    Profit=models.CharField(max_length=100)
   
    def __str__(self):
        return self.investor.Name
# Proxy model for ClientInvestments
class InvestorInvestmentsProxy(UpcommingInvestorInvestments):
    class Meta:
        proxy = True
        verbose_name = "All Investor Investment"
        verbose_name_plural = "All Investor Investments"    
    
# Proxy model for ClientInvestments
class ClientInvestmentsProxy(UpcommingClientInvestments):
    class Meta:
        proxy = True
        verbose_name = "All Client Investment"
        verbose_name_plural = "All Client Investments"