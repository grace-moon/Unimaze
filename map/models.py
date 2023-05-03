from django.conf import settings
from django.db import models
from django.utils import timezone


class Map_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.CharField(max_length=50)
    floor = models.CharField(max_length=20, default="", null=True)
    door_num = models.CharField(max_length=50)
    vectary_viewer_key = models.CharField(max_length=50, default="")
    text = models.TextField(default="Door Number를 확인해주세요.")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def get_viewer_url(self):
        # Vectary Viewer API에서 사용할 URL을 생성합니다.
        viewer_url = f"https://app.vectary.com/p/{self.vectary_viewer_key}"
        return viewer_url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.building_name


class Direcrions_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.CharField(max_length=20, default="")
    from_place_num = models.CharField(max_length=20, null=True)
    to_place_num = models.CharField(max_length=20, null=True)
    from_place_name = models.CharField(max_length=20, default="")
    to_place_name = models.CharField(max_length=20, default="")
    img = models.ImageField(upload_to='images/')
    path_name = models.CharField(max_length=20, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.building_name


class THA(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.CharField(max_length=20, default="")
    from_place_num = models.CharField(max_length=20, null=True)
    to_place_num = models.CharField(max_length=20, null=True)
    from_place_name = models.CharField(max_length=20, default="")
    to_place_name = models.CharField(max_length=20, default="")
    img = models.ImageField(upload_to='images/')
    path_name = models.CharField(max_length=20, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.building_name




