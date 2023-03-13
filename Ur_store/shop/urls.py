from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("Language/",views.Language,name="Language"),
    path("contact/",views.contact,name="ContactUs"),
    path("buyagain/",views.buyagain,name="BuyAgain"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.productView,name="ProductView"),
    path("checkout/",views.checkout,name="Checkout")
]
