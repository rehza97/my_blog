from .models import Category
import random
def get_all_categories(request):
    categories = Category.objects.all()
    rndm_categories =  random.sample(list(categories), 5)
    context = {
        'categories' : categories,
        'rndm_categories' : rndm_categories
    }
    return context