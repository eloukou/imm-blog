from django import template
register = template.Library()
from ..models import Answer
@register.simple_tag
def deletematurity():
    for answer in Answer.objects.all():
        answer.maturity = 0
        answer.save()
    return None
    
