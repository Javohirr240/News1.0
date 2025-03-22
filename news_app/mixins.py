from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse


class CustomMixins(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """403 xatolikni o‘rniga tushunarli xabar chiqarish"""
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()  # Login sahifasiga yo‘naltirish
        return HttpResponse("Siz SuperUser'ga tegishli buyuruqlarni bajarishga urindigiz. Afsuski sizning statusingiz oddiy")