from django.contrib import admin
from .models import Share, ShareLike
# Register your models here.



class ShareLikeAdmin(admin.TabularInline):
        model = ShareLike

class ShareAdmin(admin.ModelAdmin):
    inlines = [ShareLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model =Share 



admin.site.register(Share, ShareAdmin)
