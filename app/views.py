from django.conf import settings
from django.shortcuts import render
import json
from django.core.serializers import serialize
from .models import Place
from django.http import JsonResponse

def index(request):
    return render(request, 'app/index.html', {
        'debug_mode': settings.DEBUG
    })


def places_geojson(request):
    places = Place.objects.prefetch_related('images').all()
    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(place.lng), float(place.lat)]
            },
            "properties": {
                "title": place.title,
                "placeId": str(place.id),
                "detailsUrl": f"/api/place/{place.id}"
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return JsonResponse(geojson)


def place_detail_json(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Place.DoesNotExist:
        return JsonResponse({'error': 'Place not found'}, status=404)

    image_urls = [
        request.build_absolute_uri(img.image.url)
        for img in place.images.all()
        if img.image
    ]

    return JsonResponse({
        "title": place.title,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "imgs": image_urls,
    })