from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

CATEGORY_TYPE_CHOICES = (
    ('ELEMENTARY', _('Elementary School')),
    ('HIGH', _('High School')),
)
CATEGORY_SUBTYPE_CHOICES = (
    ('1', _('1st year')),
    ('2', _('2nd year')),
    ('3', _('3rd year')),
    ('4', _('4th year')),
    ('5', _('5th year')),
    ('6', _('6th year')),
    ('7', _('7th year')),
    ('8', _('8th year')),
)

class Video(models.Model):
    name = models.CharField(_("Name"), max_length=512)
    description = models.TextField(_("Description"), blank=True, null=True)
    ratings = models.IntegerField(_("Ratings"), default=0)
    category_type = models.CharField(_("Scholar Seniority"), choices=CATEGORY_TYPE_CHOICES, default='ELEMENTARY', max_length=12)
    category_subtype = models.CharField(_("Class"), choices=CATEGORY_SUBTYPE_CHOICES, default='0', max_length=1)
    video = models.FileField(null=True,
                             upload_to=settings.MEDIA_ROOT,
                             validators=[
                                FileExtensionValidator(
                                    allowed_extensions=['MOV','avi','mp4','webm','mkv', 'png'])
                             ])
    
    
    created_at = models.DateTimeField(_("Created at"), auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey("accounts.User", verbose_name=_("Created by"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")
    
    def get_absolute_url(self):
        return reverse("videos:detail", kwargs={"pk": self.pk})
