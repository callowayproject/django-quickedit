from django.contrib import admin
from django.utils.functional import curry
from django.forms.models import modelformset_factory, modelform_factory


class QuickEditAdmin(admin.ModelAdmin):
    change_list_template = 'quickedit/change_list.html'
    
    def get_changelist_formset(self, request, **kwargs):
        """
        Returns the quickedit formset for the row
        """
        defaults = {
            "formfield_callback": curry(self.formfield_for_dbfield, request=request),
        }
        defaults.update(kwargs)
        return modelformset_factory(self.model, modelform_factory(self.model),
                extra=0, fields=self.quick_editable, **defaults)

    