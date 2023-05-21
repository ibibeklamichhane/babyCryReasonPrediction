import os
# from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from django.shortcuts import render

from django.http import HttpResponse

from .MetaData import getmetadata
from .predict import predict_gen
# Create your views here.


def index(request):
    return render(request,'predictor/home.html')



def predict(request):
    # path="/home/bishal/bishal/major_project/classificationSystem/babyCryClassificationSystem/predictor/uploaded_file"
   if request.method == 'POST':
        # Get the uploaded file
        audio_file = request.FILES['audio_file']
        print(audio_file)
        print(request.FILES)
        
        # Save the file to a temporary location
        tmp_file = os.path.join(settings.MEDIA_ROOT, 'tmp', audio_file.name)
        with open(tmp_file, 'wb+') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        # Call your classification function here with the path to the saved file
        # classification_result = classify(tmp_file)
        meta = getmetadata(tmp_file)
            
        genre = predict_gen(meta)
        print(genre)

        # Delete the temporary file
        os.remove(tmp_file)

        # Render the result
        context = {'genre':genre}
        #return render(request,'predictor/home.html',context)
        return render(request,'predictor/result.html',context)
        #return JsonResponse({context})
   ##


        