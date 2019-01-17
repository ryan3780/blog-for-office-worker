from django.shortcuts import render
# 자동으로 새로고침 역할을 하기 위해 import한 모듈이다.
from django.http import HttpResponseRedirect
from .models import Article, Comment, HashTag
# Create your views here.
def index(request) :
    # GET 방식으로 정보를 요청하는 방법
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()

    if not category and not hashtag :
        article_list = Article.objects.all()
    elif category :
        article_list = Article.objects.filter(category = category)
    else : # hashtag__name 꼭 __를 붙여야 한다.
        article_list = Article.objects.filter(hashtag__name = hashtag)

    # article_list = Article.objects.all()
    # set ==> 중복을 허용하지 않는 집합
    # category_list = set([])
    # for article in article_list :
    #     class에서 정의한 것을 get_변수_display() 함수를 이용하면 choices에 있는 이름이 나온다.
    #     category_list.add(article.get_category_display())

    # 위에랑 같은 처리 방법
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])
# GET 방식인지 확인 하는 방법
    # print(request.GET)

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id) :
    # GET & POST
    # Article Class에서 id를 받아온다. id 는 article_id가 넘겨준 정보를 가지고 있다.
    article = Article.objects.get(id = article_id)

    # comment_list = Comment.objects.filter(article__id = article_id)
    # comment_list = article.article_comments.all()
    # article_list = Article.objects.filter(hashtag__name = hashtag)
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        "hashtag_list" : hashtag_list,
        # "article_list" : article_list,
        # "comment_list" : comment_list, # class Article에서 class Comment에 접근하여 가져온 정보
    }

    if request.method == "GET" :
        pass
    elif request.method == "POST" :
        # POST 방식이며, get()안에는 input 태그의 name을 써준다.
        username = request.POST.get("username")
        content = request.POST.get("content")
        # 정보가 넘어 오는지 확인 하는 방법 print 찍어라
        # print(username)
        # print(content)
        Comment.objects.create(
            article = article,
            username = username,
            content = content,
        )
        # 새로 고침을 해주는 방법 (예시 : 127.0.0.1:8000"/{}/" 아티클 id가 들어 가는 것)
        return HttpResponseRedirect("/{}/".format(article_id))


    return render(request, "detail.html", ctx)

# def about(request) :
#     pass
