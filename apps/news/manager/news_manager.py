from django.db import models
from parler.managers import TranslatableManager


class NewsQuerySet(models.QuerySet):
    def filter_by_category(self, category_id):
        return self.prefetch_related('category').filter(category__id=category_id).distinct()


class NewsImagesQuerySet(models.QuerySet):

    def filter_by_news(self, news_id):
        return self.select_related('news').filter(news=news_id).distinct()


class CommentQuerySet(models.QuerySet):

    def filter_by_news(self, news_id):
        return self.select_related('news').filter(news=news_id).distinct()


class StaffQuerySet(models.QuerySet):

    def filter_by_category(self, category_id):
        return self.prefetch_related('category').filter(category__id=category_id).distinct()


class CommentInfoQuerySet(models.QuerySet):

    def filter_by_category(self, category_id):
        return self.prefetch_related('category').filter(category__id=category_id).distinct()

class NewsManager(TranslatableManager):
    def get_queryset(self):
        return NewsQuerySet(self.model, using=self._db)

    def filter_by_category(self, category_id):
        return self.get_queryset().filter_by_category(category_id)


class NewsImagesManager(TranslatableManager):
    def get_queryset(self):
        return NewsImagesQuerySet(self.model, using=self._db)

    def filter_by_news(self, news_id):
        return self.get_queryset().filter_by_news(news_id)


class CommentManager(TranslatableManager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

    def filter_by_news(self, news_id):
        return self.get_queryset().filter_by_news(news_id)


class StaffManager(TranslatableManager):
    def get_queryset(self):
        return StaffQuerySet(self.model, using=self._db)

    def filter_by_category(self, category_id):
        return self.get_queryset().filter_by_category(category_id)


class CommentInfoManager(TranslatableManager):
    def get_queryset(self):
        return CommentInfoQuerySet(self.model, using=self._db)

    def filter_by_category(self, category_id):
        return self.get_queryset().filter_by_category(category_id)
