from django.db import models


class DateTimeDBOps(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_cadastro'
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True,
        db_column='dt_atualizacao'
    )

    class Meta:
        abstract = True


class Author(DateTimeDBOps):
    id = models.BigAutoField(primary_key=True, db_column='id')
    name = models.CharField(db_column='name', max_length=255, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'author'
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Notice(DateTimeDBOps):
    id = models.BigAutoField(primary_key=True, db_column='id')
    title = models.CharField(db_column='title', max_length=255, null=False, blank=False)
    notice = models.TextField(db_column='notice', null=False, blank=False)

    author = models.ForeignKey(Author, db_column='author_id', null=False, related_name='notice_set',
                               on_delete=models.CASCADE)

    def __str__(self):
        return 'Notice {}'.format(self.title)

    class Meta:
        db_table = 'notice'
        ordering = ['id']
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'
