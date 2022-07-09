from django.urls import path

from .views import (
    home,
    contact_project,
    contact_position,
    contact_say,
    cloudkids,
    aboutus,
    career,
    contactus,
    portfolio,
    services,
)
app_name = "webpage"
urlpatterns = [
    path("", view=home, name="home"),
    path("contact_project/", view=contact_project, name="contact_project"),
    path("contact_position/", view=contact_position, name="contact_position"),
    path("contact_say/", view=contact_say, name="contact_say"),
    path("cloudkids", view=cloudkids, name="cloudkids"),
    path("aboutus/", view=aboutus, name="aboutus"),
    path("career/", view=career, name="career"),
    path("contactus/", view=contactus, name="contactus"),
    path("portfolio/", view=portfolio, name="portfolio"),
    path("services/", view=services, name="services"),
]