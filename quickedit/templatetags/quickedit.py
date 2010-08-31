from django.contrib.admin.templatetags.admin_list import items_for_result, result_headers
from django.template import Library
from django.forms.models import modelform_factory


register = Library()

def results(cl,r):
    qe = hasattr(cl.model_admin, 'quick_editable')
    if cl.formset:
        if qe:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield {
                    'fields':list(items_for_result(cl, res, form)), 
                    'quickedit':form
                }
        else:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield {
                    'fields': list(items_for_result(cl, res, form)),
                    'quickedit': None
                }
    else:
        if qe:
            for res in cl.result_list:
                yield {
                    'fields':list(items_for_result(cl, res, None)), 
                    'quickedit':cl.model_admin.get_changelist_formset(r).form(instance=res)
                }
        else:
            for res in cl.result_list:
                yield {
                    'fields': list(items_for_result(cl, res, None)),
                    'quickedit': None
                }

def qe_result_list(context, cl):
    return {
        'qe_fields': cl.model_admin.quick_editable,
        'cl': cl,
        'result_headers': list(result_headers(cl)),
        'results': list(results(cl,context['request'])),
    }
qe_result_list = register.inclusion_tag('quickedit/change_list_results.html',
                        takes_context=True)(qe_result_list)
