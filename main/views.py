from django.shortcuts import render, redirect, get_object_or_404    # redirect, get_object_or_404도 필요해서 써준다.
from .models import Bookmark    # models.py의 Bookmark도 가져오고
from .forms import BookmarkForm # forms.py의 BookmarkForm도 가져온다
# Create your views here.

def show(request):  # 요청(request)이 들어오면,
    bookmarks = Bookmark.objects.all()   # bookmarks는 Bookmark가 가진 애를 다 가져와라.

    return render(request, 'show.html', {'bookmarks':bookmarks})


def new(request):
    if request.method == 'POST': # request가 POST 방식으로 들어오면, (요청이 발생하면)
        form = BookmarkForm(request.POST)
        if form.is_valid():  # 내가 form을 알맞게 적었다면,
            bookmark = Bookmark()   # bookmark를 새로 하나 만들어주고 (def edit에선 없앤다)
            bookmark.site_name = form.cleaned_data['site_name'] # site_name은 form에서 받은 걸 쓴다
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save() # 저장해주기
            return redirect('main:show')    # main으로 다시 보내주기
    
    else:   # 요청이 안들어오면,
        form = BookmarkForm()      # 아무일도 안 일어난다.
    return render(request, 'new.html', {'form':form})   # 계속 new.html에 머물러 있는다.


def edit(request, pk):  # 요청도 받고, pk도 받고
    bookmark = get_object_or_404(Bookmark, pk=pk)   # 처음에 특정한 객체(pk)를 가져오게 한다.

    if request.method == 'POST': 
        form = BookmarkForm(request.POST, instance = bookmark)
        if form.is_vaild():
            bookmark.site_name = form.cleaned_data['site_name'] 
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save() 
            return redirect('main:show')    
    
    else:   
        form = BookmarkForm(instance=bookmark)  # edit이니까 기존에 썼던 인자를 bookmark에서 가져온다.
    return render(request, 'new.html', {'bookmark':bookmark,'form':form})   # edit이니까 기존에 썼던 인자를 bookmark에서 가져온다.


def delete(request,pk):
    bookmark = get_object_or_404(Bookmark,pk=pk)

    if request.method == 'POST':    # 삭제 버튼이 눌리면,
        bookmark.delete()   # 삭제된다.
        return redirect('main:show') # main 페이지 새로고침 해라!