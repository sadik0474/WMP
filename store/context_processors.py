from .models import Category

def categories(request):
    return {
        'category1': Category.objects.all()
    }