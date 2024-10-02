from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment 
from .forms import PostForm 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm, CommentForm
from django.views.generic import ListView
from django.views import View


 #vistas para listar, crear, actualizar y ver publicaciones, así como para agregar comentarios.

def principal(request):
    return render(request, 'principal.html')


# para la creacion del post : ESTE ES EL QUE SE ESTA UTILIZANDO 
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')


#para poder ver la lista de entradas creadas y manejar los comentarios 
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Plantilla para renderizar la lista de posts
    context_object_name = 'posts'  # Nombre con el que accederemos a la lista de posts en el template
    ordering = ['-created_at']  # Ordenar los posts por fecha de creación (del más reciente al más antiguo)


class AddCommentView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm()
        return render(request, 'add_comment.html', {'form': form, 'post': post})
    
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, id=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_list')  # Redirige a la lista de posts
        return self.get(request, post_id)


# Vista para manejar el envío de comentarios
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Asigna el post al comentario
            comment.save()
            return redirect('post_list')  # Redirige a la lista de posts después de agregar el comentario
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form': form, 'post': post})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})



