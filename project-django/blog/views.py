from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def Home(request):
    return HttpResponse("<h1>Hello , Django</h1>")




# def Post_list(request):
#     posts = Post.objects.all()
#     # print(posts)
#     result = ""
#     for post in posts:
#         result += post.title + "<br/>"
#         print(result)
#         # print("Post title", post.title)
#     # return HttpResponse("<h1>Post list</h1>")
#     return HttpResponse(result)



def Post_list(request):
    posts = Post.objects.all()
    context = {
        "name": "Shipon",
        "posts": posts,
    }
    return render(request, "post_list.html", context)




def Post_details(request, pk_id):
    # print(pk_id)
    post = Post.objects.get(id=pk_id)
    result = f"{post.title}<br/>{post.content}"
    return HttpResponse(result)
    # return HttpResponse("<h1>Post details</h1>")
