from django.http import HttpResponse
from rest_framework.views import APIView

from .models import *


class WordView(APIView):

    def get(self, request):
        """
        Get word from the server to process
        url : GET /word/
        """
        s = Status.objects.get(id=0)
        if len(Word.objects.all()) > 0 and not s.completed:
            item = Word.objects.all()[0].item
            Word.objects.all()[0].delete()
            return HttpResponse(item)

        return HttpResponse("")

    def post(self, request):
        """
        Add word to the server
        url : POST /word/?item=<word>
        """
        default = ""
        word = self.request.query_params.get("item", default)
        if word != default:
            new_word = Word(item=word)
            new_word.save()
            return HttpResponse("success")

        return HttpResponse("failure")


class SubmitPass(APIView):

    def post(self, request):
        """
        Submit a password if found
        url : POST /submit/?item=<password>
        """
        default = ''
        word = self.request.query_params.get('item', default)

        if word != default:
            s = Status.objects.get(id=0)
            s.completed = True
            s.password = word
            s.save()
            return HttpResponse("success")

        return HttpResponse('failure')


class Reset(APIView):

    def post(self, request):
        """
        Remove saved password
        url : POST /reset/
        """
        s = Status.objects.get(id=0)
        s.completed = False
        s.password = ''
        s.save()

        return HttpResponse('success')
