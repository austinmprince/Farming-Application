from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser, Farmer, Consumer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin





class AddUserForm(forms.ModelForm):
    """
    New User Form. Requires password confirmation.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class UpdateUserForm(forms.ModelForm):
#     """
#     Update User Form. Doesn't allow changing password in the Admin.
#     """
#     password = ReadOnlyPasswordHashField()
#
#
#     class Meta:
#         model = CustomUser
#         fields = (
#             'email', 'password', 'first_name', 'last_name', 'is_active',
#             'is_staff'
#         )
#
#     def clean_password(self):
# # Password can't be changed in the admin
#         return self.initial["password"]

# https://kite.com/blog/python/custom-django-user-model/
class UserAdmin(BaseUserAdmin):
    # form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'id')
    list_filter = ('is_staff', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'is_farmer', 'is_consumer')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (
            None, {'fields': ('username', 'email', 'password')}),
            # ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'is_farmer', 'is_consumer')}),
            ('Personal Info',
            {
                'fields': (
                    'first_name', 'last_name', 'is_consumer', 'is_farmer'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

class ConsumerAdmin(admin.ModelAdmin):
    model = Consumer

    list_display = ['get_username', 'get_first_name', 'get_last_name']

    def get_first_name(self, obj):
        return obj.user.first_name
    def get_last_name(self, obj):
        return obj.user.last_name
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'


# class FarmerAdmin(admin.ModelAdmin):
#     model = Farmer
#     list_display = ['get_username', 'get_first_name', 'get_last_name']
#     def get_first_name(self, obj):
#         return obj.user.first_name
#     def get_last_name(self, obj):
#         return obj.user.last_name
#     def get_username(self, obj):
#         return obj.user.username
#     # def farm_name(self, obj):
#     #     return obj.farm.name
#     # farm_name.short_description = 'Farm Name'
#     get_username.short_description = 'Username'
#     get_first_name.short_description = 'First Name'
#     get_last_name.short_description = 'Last Name'


# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Farmer)
admin.site.register(Consumer, ConsumerAdmin)
# admin.site.register()
