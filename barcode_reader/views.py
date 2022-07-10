from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import UploadImageForm
from .models import Product
from .utils import read_barcode, search_youtube
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

def index(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            barcode = read_barcode(form.instance.image.path)
            os.remove(form.instance.image.path)
            return redirect(reverse('suggestion', args=(barcode,)))
    else:
        form = UploadImageForm()
    return render(request, 'barcode_reader/index.html', {'form': form})

def suggestion(request, barcode):
    product = get_object_or_404(Product, barcode=barcode)
    video_url = search_youtube(product.chi_name)
    return render(request, 'barcode_reader/suggestion.html', {'product': product, 'video_url': video_url})
