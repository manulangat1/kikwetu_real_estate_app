from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedModel 
from apps.profiles.models import Profile
# Create your models here.
class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")
class Rating(TimeStampedModel):
    rater = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL , null=True , verbose_name=_("User providing the rating"))
    agent = models.ForeignKey(Profile, on_delete=models.SET_NULL , null=True , verbose_name=_("agent_receiving the rating"), related_name="agent_review")
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices, default=Range.RATING_1)
    comment = models.TextField(verbose_name=_("Comment"), max_length=500, blank=True)

    class Meta: 
        unique_together = ('rater', 'agent')
    def __str__(self):
         return f"{self.agent} rated at {self.rater}"