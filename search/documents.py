# -*- coding: utf-8 -*-
'''
from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from blog.models import Post

posts = Index('posts')

#@registry.register_document
@posts.document
class PostDocument(Document):
    class Django:
        model = Post
        
        fields = [
                'title',
        ]

posts.create()
'''