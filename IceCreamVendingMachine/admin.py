from django.contrib import admin
from IceCreamVendingMachine.models import IceCream
from IceCreamVendingMachine.models import Stores
from IceCreamVendingMachine.models import SnowCone
from IceCreamVendingMachine.models import WhereOff
from IceCreamVendingMachine.models import WhereOffAmounts
from IceCreamVendingMachine.models import Users

# Register your models here.
admin.site.register(IceCream)
admin.site.register(Stores)
admin.site.register(SnowCone)
admin.site.register(WhereOff)
admin.site.register(WhereOffAmounts)
admin.site.register(Users)
