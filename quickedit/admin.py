from django.conf import settings
from django.db.models import get_model
from django.contrib import admin
from django.utils.functional import curry
from django.forms.models import modelformset_factory, modelform_factory


FIELDS = getattr(settings, 'QUICK_EDITABLE_FIELDS', {}).copy()
for k,v in FIELDS.items():
    if isinstance(k, basestring):
        FIELDS[get_model(*k.split('.'))] = v
        del FIELDS[k]


class QuickEditAdmin(admin.ModelAdmin):
    change_list_template = 'quickedit/change_list.html'
    quick_editable = ()
    
    def get_changelist_formset(self, request, **kwargs):
        """
        Returns the quickedit formset for the row
        """
        defaults = {
            "formfield_callback": curry(self.formfield_for_dbfield, request=request),
        }
        defaults.update(kwargs)
        return modelformset_factory(self.model, modelform_factory(self.model),
                extra=0,fields=self.quick_editable+self.list_editable, **defaults)
        
for model,modeladmin in admin.site._registry.items():
    if model in FIELDS:
        attrs = {'quick_editable': FIELDS[model]}
        if not modeladmin.list_editable:
            attrs.update(list_editable=(FIELDS[model][0],))
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (modeladmin.__class__, QuickEditAdmin), attrs))