from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

class ReviewView(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.Movie_id = pk
            form.Parent_id=form.Name
            form.save()
        return redirect("/")








# def get_name(request):
#     if request.method == "POST":
#         form = TextName(request.POST)
#         if form.is_valid():
#             return redirect("main")
#     else:
#         form = TextName()
#
#     return render(request, 'movies/test_for_forms.html', {"form":form})
#
#
# class ActorsAdd(CreateView):
#     form_class = Comment
#     template_name = "movies/test_for_forms"
#     success_url = redirect("main")


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(Draft=False)
    context_object_name = "movies_list"
    allow_empty = False
    ordering = ["Category"]

    # template_name = "movies/Movie_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/Movie_list.html", {"movies_list": movies})
    # queryset = Movie.objects.get(Url=slug)


# class ReviewFormView(CreateView):
#     form_class = ReviewForm
#     fields = ["Text", "Name", "Email"]
#     template_name = "movie/Movie_detail"

# def get_context_data(self, **kwargs):
#     context =

class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movies_detail'
    slug_field = 'Url'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["frames"] = FrameOfMovies.objects.filter(Movie=movies_detail.Movie)

    # template_name = "movies/Movie_detail.html"
    # queryset = Movie.objects.filter(Url= )
    # def get(self, request, slug):
    #     movies = Movie.objects.get(Url=slug)
    #     return render(request, "movies/Movie_detail.html", {"movies_detail":movies})


# class AddReview(View):
#     def post(self, request, pk):
#         print(request.POST)
#
#         return redirect("/")


# class MoviesView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/Movie_list.html", {"movies_list": movies})
#
# class MovieDetailView(View):
#     def get(self, request, slug):
#         movies = Movie.objects.get(Url=slug)
#         return render(request, "movies/Movie_detail.html", {"movies_detail":movies})


#
# def index(request):
#     movies = Movie.objects.all()
#
#     context ={
#         "movies":movies
#     }
#
#     return render(request, "movies/Movie_detail.html", context=context)
