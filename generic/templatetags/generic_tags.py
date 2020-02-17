from django import template
import datetime

register = template.Library()

@register.filter
def get_obj_attr(obj, attr):
	attr_value = getattr(obj, attr)

	if isinstance(attr_value, datetime.date):
		return attr_value.strftime("%d/%m/%Y")
	elif attr_value == None:
		return ""
	else:
		return attr_value