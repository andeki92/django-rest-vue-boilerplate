from django.views.generic import TemplateView


class LandingPage(TemplateView):
    ''' Create a landing page using the supplied template name '''
    template_name = "landing-page.html"
