# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 20:16
from __future__ import unicode_literals

from django.db import migrations
from django.db import connection
from addons.wiki.models import NodeWikiPage
from django.contrib.contenttypes.models import ContentType

def reverse_func(state, schema):
    return NodeWikiPage.objects.update(former_guid='')

def add_guid_field(state, schema):
    content_type_id = ContentType.objects.get_for_model(NodeWikiPage).id
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE addons_wiki_nodewikipage as nwp
            SET former_guid=(
                  SELECT _id
                  FROM osf_guid
                  WHERE object_id = nwp2.id and content_type_id = %s
                  LIMIT 1
              )
            FROM addons_wiki_nodewikipage as nwp2
            WHERE nwp.id = nwp2.id
            """, [content_type_id]
        )
    return


class Migration(migrations.Migration):

    dependencies = [
        ('addons_wiki', '0007_nodewikipage_former_guid'),
    ]

    operations = [
        migrations.RunPython(add_guid_field, reverse_func)
    ]
