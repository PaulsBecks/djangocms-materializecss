from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from djangocms_materializecss.models import Card, CollectionItem, Column, Footer, ImageCard, Navbar, Parallax, Slide, Slider, SocialMediaBar
from django.utils.translation import ugettext_lazy as _

#https://cdn-images-1.medium.com/max/1600/1*9Zt6Pxc1Y4tvuNO04CGX_Q.jpeg


@plugin_pool.register_plugin
class CardPlugin(CMSPluginBase):
    model = Card
    render_template = "djangocms_materializecss/card.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(CardPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class CollectionPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "djangocms_materializecss/collection.html"
    cache = False
    allow_children = True
    child_classes = ['CollectionItemPlugin']

    def render(self, context, instance, placeholder):
        context = super(CollectionPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class CollectionItemPlugin(CMSPluginBase):
    model = CollectionItem
    render_template = "djangocms_materializecss/collection_item.html"
    cache = False
    parent_classes = ['CollectionPlugin']

    def render(self, context, instance, placeholder):
        context = super(CollectionItemPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ColumnsPlugin(CMSPluginBase):
    model = Column
    render_template = "djangocms_materializecss/column.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(ColumnsPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ContainerPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "djangocms_materializecss/container.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(ContainerPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class DividerPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "djangocms_materializecss/divider.html"
    cache = False
    allow_children = False

@plugin_pool.register_plugin
class FooterPlugin(CMSPluginBase):
    model = Footer
    render_template = "djangocms_materializecss/simple_footer.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(FooterPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ImageCardPlugin(CMSPluginBase):
    model = ImageCard
    render_template = "djangocms_materializecss/img_card.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(ImageCardPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class NavbarPlugin(CMSPluginBase):
    model = Navbar
    render_template = "djangocms_materializecss/simple_navbar.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(NavbarPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ParallaxPlugin(CMSPluginBase):
    model = Parallax
    render_template = "djangocms_materializecss/parallax.html"
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        context = super(ParallaxPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class SliderPlugin(CMSPluginBase):
    model = Slider
    render_template = "djangocms_materializecss/slider.html"
    cache = False
    allow_children = True
    child_classes = ['SlidePlugin']

    def render(self, context, instance, placeholder):
        context = super(SliderPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class SlidePlugin(CMSPluginBase):
    model = Slide
    render_template = "djangocms_materializecss/slide.html"
    cache = False
    parent_classes = ['SliderPlugin']

    def render(self, context, instance, placeholder):
        context = super(SlidePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class SocialMediaBarPlugin(CMSPluginBase):
    model = SocialMediaBar
    render_template = "djangocms_materializecss/social_media.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SocialMediaBarPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class TabsPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "djangocms_materializecss/tabs.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TabsPlugin, self).render(context, instance, placeholder)
        return context
