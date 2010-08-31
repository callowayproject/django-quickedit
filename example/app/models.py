from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Blog(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    tease = models.TextField()
    description = models.TextField()
    public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title

    def save(self, *a, **kw):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super(Blog, self).save(*a, **kw)

    class Meta:
        ordering = ('title',)
        get_latest_by = 'creation_date'


class Entry(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    pub_time = models.TimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date='pub_date')
    tease = models.TextField()
    body = models.TextField()
    public = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog)
    
    class Meta:
        unique_together = ('slug','pub_date')
        verbose_name_plural = _('Entries')
        get_latest_by = 'update_date'
        ordering = ('-pub_date', '-pub_time',)
 
    def __unicode__(self):
        return self.title
    
    def save(self, *a, **kw):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super(Entry, self).save(*a, **kw)

