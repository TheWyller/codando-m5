from ...models import Language
from django.core.management.base import BaseCommand

languages_list = [
    "javascript",
    "python",
    "java",
    "php",
    "c#",
    "c++",
    "typescript",
    "ruby",
    "c",
    "swift",
    "r",
    "objective-c",
    "scala",
    "shell",
    "go",
    "powershell",
    "kotlin",
    "rust",
    "dart",
    "bash",
]


class Command(BaseCommand):
    help = "Populate languages list"

    def handle(self, *args, **kwargs):
        for language_name in languages_list:
            new_language, _ = Language.objects.get_or_create(
                defaults={"name": language_name.lower().strip()},
                name=language_name.lower().strip(),
            )
