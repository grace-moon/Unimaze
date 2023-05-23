from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Q


#유니메이즈 관련 포스팅, mazetip, aboutus 등등
class Unimaze_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200, default="")
    text = models.TextField(default="tag를 입력하세요. 각 층에 해당하는 교수님, 업무, 교직원 등등, 모든 걸 다 작성해주세요.")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#학교 내부 연락망
class Univ_Contacts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=20, null=True, blank=True)
    major = models.CharField(max_length=40, null=True,  blank=True)
    name = models.CharField(max_length=20, null=True,  blank=True)
    position = models.CharField(max_length=20, null=True,  blank=True)
    task = models.CharField(max_length=200, null=True,  blank=True)
    contact = models.CharField(max_length=20, default='042-280',  blank=True)
    second_contact = models.CharField(max_length=20, null=True,  blank=True)
    third_contact = models.CharField(max_length=20, null=True,  blank=True)
    location = models.CharField(max_length=200,null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        if self.name:
            return self.name
        elif self.department:
            return self.department
        else:
            return self.contact

class Unimaze_map(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.CharField(max_length=100, default="")
    vectary_viewer_key = models.CharField(max_length=50, default="")
    text = models.TextField(default="tag를 입력하세요. 각 층에 해당하는 교수님, 업무, 교직원 등등, 모든 걸 다 작성해주세요.")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def get_viewer_url(self):
        # Vectary Viewer API에서 사용할 URL을 생성합니다.
        viewer_url = f"{self.vectary_viewer_key}"
        return viewer_url


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.floor
