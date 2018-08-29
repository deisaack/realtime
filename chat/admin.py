from django.contrib import admin


from .models import Thread, ChatMessage


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage


class ThreadAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline]
    
    class Meta:
        model = Thread 


admin.site.register(Thread, ThreadAdmin)
