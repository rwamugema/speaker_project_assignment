from django.shortcuts import render
from django.http import HttpResponse

def list_all_speakers(request):
    data = Speakers.objects.all().values()
    template = loader.get_template('all_speakers.html')

    return HttpResponse (template.render({speakers: data}, request ))

def create_a_new_speaker(request):

    return render(request, 'speaker_create.html' )

def view_single_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    view_item = [speaker for speaker in data if speaker['id'] == speaker_id]

    return render(request, 'view_speaker.html',{'speaker': view_item}) 

def update_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    update_item = [speaker for speaker in data if speaker['id'] == speaker_id]

    return render(request, 'update_speaker.html',{'speaker': update_item })       

def delete_speaker(request, speaker_id):
    data = Speakers.objects.all().values()
    delete_item = [item for item in data if item['id'] ==speaker_id ]

    return render(request, 'delete_speaker.html',{'speaker': delete_item })    