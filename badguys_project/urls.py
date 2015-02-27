from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^about$',
        TemplateView.as_view(template_name='about.html'), name="about"),
)

urlpatterns += patterns('badguys.vulnerable.views',

    # Exercise 01 - Injection Attacks
    url(r'^injection$',
        TemplateView.as_view(template_name='vulnerable/injection/index.html'),
        name="injection"),
    url(r'^injection/sql$', 'sql', name="injection-sql"),
    url(r'^injection/file-access$', 'file_access',
        name="injection-file-access"),
    url(r'^user-pic$', 'user_pic', name='user-pic'),
    url(r'^injection/code-execution$', 'code_execution',
        name="injection-code-execution"),

    # Exercise 02 - Broken Authentication & Session Management
    url(r'^broken-auth-and-session-management$',
        TemplateView.as_view(template_name='vulnerable/broken_auth/index.html'),
        name='broken-auth'),

    # Exercise 03 - XSS Attacks
    url(r'^cross-site-scripting$',
        TemplateView.as_view(template_name='vulnerable/xss/index.html'),
        name="xss"),
    url(r'^cross-site-scripting/path-matching/(?P<path>.+)$', 'xss_path',
        name="xss-path"),
    url(r'^cross-site-scripting/form-field$', 'xss_form',
        name="xss-form"),
    url(r'^cross-site-scripting/query-params$', 'xss_query',
        name="xss-query"),

    # Exercise 04 - Insecure Direct Object References
    url(r'^direct-object-references$',
        TemplateView.as_view(template_name='vulnerable/direct_object_references/index.html'),
        name="direct-object-references"),

    url(r'^direct-object-references/users/(?P<userid>\d+)$', 'dor_user_profile',
        name='direct-object-references-profile'),

    # Exercise 05 - Security Misconfiguration
    url(r'^misconfiguration$',
        TemplateView.as_view(template_name='vulnerable/misconfig/index.html'),
        name='misconfig'),

    url(r'^misconfiguration/boom$', 'boom', name='misconfig-boom'),

    # Exercise 06 - Sensitive Data Exposure
    url(r'^data-exposure$',
        TemplateView.as_view(template_name='vulnerable/exposure/index.html'),
        name='exposure'),
    url(r'^data-exposure/login$', 'exposure_login',
        name='exposure-login'),

    # Exercise 07 - Missing Function-Level Access Control

    url(r'^missing-access-control$',
        TemplateView.as_view(template_name='vulnerable/access_control/index.html'),
        name='access-control'),

    url(r'^missing-access-control/happy-page$', 'missing_access_control',
        name='access-control-missing'),

    # Exercise 08 - CSRF Attacks
    url(r'^csrf$',
        TemplateView.as_view(template_name='vulnerable/csrf/index.html'),
        name='csrf'),
    url(r'^csrf/image$', 'csrf_image',
        name='csrf-image'),
    url(r'^csrf/third-party-site$',
        TemplateView.as_view(template_name='vulnerable/csrf/third_party.html'),
        name='csrf-third-party'),
    url(r'^csrf/gift-card$',
        TemplateView.as_view(template_name='vulnerable/csrf/gift_card.html'),
        name='csrf-gift-card'),

    # Exercise 09 - Using Known Vulnerable Components
    url(r'^vulnerable-components$',
        TemplateView.as_view(template_name='vulnerable/components/index.html'),
        name='components'),

    # Exercise 10 - Unvalidated Redirects & Forwards
    url(r'^redirects-and-forwards$',
        TemplateView.as_view(template_name='vulnerable/redirects/index.html'),
        name='redirects'),
    url(r'^redirects-and-forwards/redirects$',
        TemplateView.as_view(template_name='vulnerable/redirects/redirects.html'),
        name='redirects-redirects'),
    url(r'^redirects-and-forwards/redirect$', 'unvalidated_redirect',
        name='redirects-redirect'),
    url(r'^redirects-and-forwards/forwards$',
        TemplateView.as_view(template_name='vulnerable/redirects/forwards.html'),
        name='redirects-forwards'),
    url(r'^redirects-and-forwards/forward$', 'unvalidated_forward', name='redirects-forward')

    # url(r'^$', 'badguys_project.views.home', name='home'),
    # url(r'^badguys_project/', include('badguys_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
