from django.contrib.admin.templatetags.admin_list import items_for_result, result_headers
from django.template import Library
from django.forms.models import modelform_factory


register = Library()

def results(cl):
    qe = hasattr(cl.model_admin, 'quick_editable')
    if cl.formset:
        if qe:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield {
                    'fields':list(items_for_result(cl, res, form)), 
                    'quickedit':form
                }#'quickedit':form(instance=res)}
        else:
            for res, form in zip(cl.result_list, cl.formset.forms):
                yield list(items_for_result(cl, res, form))
    else:
        if qe:
            for res in cl.result_list:
                yield {
                    'fields':list(items_for_result(cl, res, None)), 
                    'quickedit':form
                }#'quickedit':form(instance=res)}
        else:
            for res in cl.result_list:
                yield list(items_for_result(cl, res, None))

def qe_result_list(context, cl):
    static_url = context.has_key('STATIC_URL') and 'STATIC_URL' or 'MEDIA_URL'
    return {
        'cl': cl,
        'result_headers': list(result_headers(cl)),
        'results': list(results(cl)),
        'STATIC_URL': context[static_url]
    }
qe_result_list = register.inclusion_tag('quickedit/change_list_results.html',
                        takes_context=True)(qe_result_list)
