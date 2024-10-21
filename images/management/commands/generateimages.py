from django.core.management.base import BaseCommand, CommandError
from images.models import Rectangle, Image
from random import randint

class Command(BaseCommand):
    color = ["red", "green", "blue", "yellow", "black", "white", "purple", "orange", "pink", "brown"]
    help = "Generate random image with given names, size ranges from 500-1000, up to 5 random rectangles"

    def add_arguments(self, parser):
        parser.add_argument("img_name", nargs="+", type=str)

    def handle(self, *args, **options):
        for img_name in options["img_name"]:
            try:
                img = Image.objects.get(name=img_name)
                raise CommandError('Image "%s" exists' % img_name)
            except Image.DoesNotExist:
                img = Image(name=img_name, height=randint(500,1000), width=randint(500,1000))
                img.save()
                rectcount = randint(1,5)
                for i in range(rectcount):
                    rec = Rectangle(picture=img, height=randint(10,img.height-1), width=randint(10,img.width-1), color=self.color[randint(0,9)], x=randint(0,img.width), y=randint(0,img.height))
                    rec.save()
                self.stdout.write(
                    self.style.SUCCESS('Successfully created image "%s"' % img_name)
                )