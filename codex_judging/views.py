from django.http import JsonResponse
from codex_judging.models import Submission
from codex_judging.tasks import add

def submit_code(request):
    if request.method == "POST":
        user = request.POST.get("user")
        code = request.POST.get("code")
        language = request.POST.get("language", "Python")

        submission = Submission.objects.create(user=user, code=code, language=language)

        # Celery 비동기 실행
        add(submission.id)

        return JsonResponse({"message": "Code submitted successfully!", "submission_id": submission.id})

    return JsonResponse({"error": "Invalid request"}, status=400)