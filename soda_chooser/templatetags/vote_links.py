from django import template

register = template.Library()

@register.inclusion_tag('inclusions/vote_links.html')
def vote_links(beverage):
	return { 'beverage': beverage }