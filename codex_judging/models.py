from django.db import models

class Submission(models.Model):
    user = models.CharField(max_length=100)  # 제출한 사용자
    code = models.TextField()  # 제출된 코드
    language = models.CharField(max_length=50)  # 사용한 언어 (Python, C++, Java 등)
    status = models.CharField(max_length=20, default="Pending")  # 채점 상태
    created_at = models.DateTimeField(auto_now_add=True)  # 제출 시간

    def __str__(self):
        return f"{self.user} - {self.language} - {self.status}"
