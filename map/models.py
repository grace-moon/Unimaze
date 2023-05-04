from django.conf import settings
from django.db import models
from django.utils import timezone

#유니메이즈 관련 포스팅, mazetip, aboutus 등등
class Unimaze_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200, default="")
    text = models.TextField(default="Door Number를 확인해주세요.")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#길찾기 등등 캔버스 사용.
class Direcrions_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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

#학교 내부 연락망
class Univ_Contacts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=20)
    name = models.IntegerField(default="", null=True)
    task = models.CharField(max_length=200, null=True)
    contact = models.IntegerField(default="042", null=True )
    location = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


#건물 3D 맵
#30주년 기념관
class TTA(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#융합과학관
class FS(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#혜화문화관
class HC(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#인문사회관
class HS(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor



#산학협력관
class IAC(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#제 4생활관
class TFD(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#문무관
class MM(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#제 2생활관
class  TSD(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#입학홍보관
class AD(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#한의학관
class OM(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#공학실험관
class EE(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#지산도서관
class JL(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor



#기초과학관
class BS(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor


#공학관
class EN(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#학생회관
class SH(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor


#응용과학관
class AS(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#창학관
class CH(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#The 4th Edu-Park
class EP(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#국제생활관(제3생활관)
class TTD(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#맥센터(메인홀)
class MAC_M(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor


#맥센터(렉처홀)
class MAC_L(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor

#제 5생활관
class HRC(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=20)
    building_num = models.IntegerField(default="", null=True)
    floor = models.IntegerField(default="", null=True)
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
        return self.floor



