from django.contrib import admin
from .models import Reactive, LabEquipment, Edition, Literature, Analysis, Synthesis, Stage


class HiddenField(admin.ModelAdmin):
    def get_model_perms(self, request):
    	return {}

class ReactiveAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'formula', 'cas', 'mm']


class LiteratureAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']


class AnalysisAdmin(admin.ModelAdmin):
	list_display = ['__unicode__']


class StageInline(admin.StackedInline):
	model = Stage
	extra = 1


class SynthesisAdmin(admin.ModelAdmin):
	inlines = [StageInline,]


admin.site.register(Reactive, ReactiveAdmin)
admin.site.register(LabEquipment)
admin.site.register(Edition, HiddenField)
admin.site.register(Literature)
admin.site.register(Analysis, HiddenField)
admin.site.register(Synthesis, SynthesisAdmin)
admin.site.register(Stage, HiddenField)
