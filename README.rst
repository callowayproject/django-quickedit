Quick Edit Documentation
==============================

:Authors:
   Corey Oordt
   Justin Quick <justquick@gmail.com>,
:Version: 0.1


::

    pip install django-quickedit==0.1.0

Django Quick Edit is a way to quickly edit fields in a model directly from the
admin change_list view. It hijacks the functionality of ``list_editable`` fields
but allows for data entry in a drop down form instead of inline. This concept
was borrowed from Wordpress and adapted into the Django admin interface.
Here is an example screenshot to show functionality

.. image:: http://github.com/washingtontimes/django-quickedit/raw/master/screenshot.png

Configuration
--------------

To enable fields to show up in the drop down form, specify the model and fields in your ``settings.py``::

    QUICK_EDITABLE_FIELDS = {
        # 'app_label.model_name': fields
        'comments.comment': ('ip_address','user_name','comment','is_public','is_removed')
    }
    
Also you must specify ``list_editable`` to turn on the form action so you can actually save data.
If the ``ModelAdmin`` does not have it defined (like Django's ``CommentsAdmin``) then the first field
in your listing will be added so it will be something like: ``CommentsAdmin.list_editable = ('ip_address',)``