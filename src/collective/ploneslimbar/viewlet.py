from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase

SITES_TO_PUBLISH = [{'title': 'plone.de', 'url': 'http://plone.de'},
                    {'title': 'plone.fr', 'url': 'http://plone.fr'},
                    {'title': 'plone.it', 'url': 'http://plone.it'},
                    {'title': 'plone.jp', 'url': 'http://plone.jp'},
                    {'title': 'plone.org.br', 'url': 'http://plone.org.br'},
                    {'title': 'plone.org.pl', 'url': 'http://plone.org.pl/'},
                    ]


class SlimbarViewlet(ViewletBase):
    index = ViewPageTemplateFile('slimbar.pt')

    def update(self):
        current_domain = self.request.BASE1
        self.sites_to_publish = [el for el in SITES_TO_PUBLISH if 
                                        el['title'] not in current_domain]
