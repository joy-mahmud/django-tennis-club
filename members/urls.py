from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.members_home),
    path('about/',views.members_about),
    path('addMember/',views.add_member),
    path('addMemberByUrl/',views.add_member_by_url),
    path("addMultipleMember/",views.add_multiple_member),
    path('viewAllMembers/',views.view_members),
    path('searchMember/',views.search_member)
]
