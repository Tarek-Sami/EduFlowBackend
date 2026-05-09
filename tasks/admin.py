from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "headline",
        "priority",
        "status",
        "progress",
        "made_by",
        "deadline",
    )
    list_filter = ("status", "priority", "deadline")
    search_fields = ("headline", "description", "made_by")
    ordering = ("-created_at",)