from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        # 작성자가 누군지 연결
        form.instance.writer = self.request.user
        # 게시글이 뭔지 연결. 템플릿에서 추가적인 정보 넘겨줘야 함
        form.instance.article_id = self.request.POST.get('article_pk')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'get')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})