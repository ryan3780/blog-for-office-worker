from django.db import models

# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    little_title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
    Article,
    related_name = "article_comments", # Class Article에서 class Comment에 접근하기 위한 방법(related_name)
    on_delete = models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "{}에 댓글: {}".format(self.article.title, self.content)
