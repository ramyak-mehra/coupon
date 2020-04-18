from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Coupan
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q



def home(request):

    return render(request, 'coupan/home.html', {'coupans': Coupan.objects.all()})


class CoupanListView(ListView):
    model = Coupan
    template_name = 'coupan/home.html'
    context_object_name = 'coupans'
    ordering = ['-publish_date']
    paginate_by = 3

    def get_queryset(self):
        coupans = Coupan.objects.all()
        query = self.request.GET.get('search')
        if query:
            coupans = coupans.filter(
                Q(title__icontains=query)|
                Q(owner__username__icontains=query)|
                Q(description__icontains=query)
            ).distinct()
            return coupans
        else:
            return coupans
class UserCoupanListView(ListView):
    model = Coupan
    template_name = 'coupan/user_coupan.html'
    context_object_name = 'coupans'
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return Coupan.objects.filter(owner=user).order_by('-publish_date')



class CoupanDetailView(DetailView):
    model = Coupan


class CoupanCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Coupan
    fields = ['title', 'description', 'end_date', 'code']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if user.profile.user_category == 'Company':
            return True
        else:
            False


class CoupanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Coupan
    fields = ['title', 'description', 'end_date', 'code']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coupan = self.get_object()
        user = self.request.user
        owner = coupan.owner
        if user == owner and user.profile.user_category == 'Company':
            return True
        else:
            False


class CoupanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Coupan
    success_url = '/'

    def test_func(self):
        coupan = self.get_object()
        user = self.request.user
        owner = coupan.owner
        if user == owner and user.profile.user_category == 'Company':
            return True
        else:
            False
