from rest_framework.response import Response
from .models import Note
from. serializers import NoteSerializer



def NoteLists(request):
    notes = Note.objects.all().order_by('-update')
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

def CreateNote(request):
    data =request.data
    note = Note.objects.create(
        body =data['body']
    )
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

def GetNoteDetails(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

def UpdateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance = note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

def DeleteNote(request, pk):
    note= Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')

