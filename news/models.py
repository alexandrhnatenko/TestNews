from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)

    @staticmethod
    def reset_votes():
        """
        Function to reset votes
        :return: None
        """
        Post.objects.update(votes=0)


class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="comments",
                             on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
