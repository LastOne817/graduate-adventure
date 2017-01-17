from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from core.models import Course
from course.crawler import Crawler


class Command(BaseCommand):
    help = 'Course crawler'

    def add_arguments(self, parser):
        parser.add_argument('start', nargs=1, type=int)
        parser.add_argument('--end', nargs=1, type=int)

    def handle(self, *args, **options):
        start = options['start'][0]
        try:
            end = options['end'][0]
        except TypeError:
            end = start + 1

        self.stdout.write('starting course crawler...')

        crawler = Crawler()
        courses = crawler.crawl_courses(start, end)

        new_count, already_exists_count, error_count = 0, 0, 0

        for course in courses:
            new_course = Course(**course)
            try:
                new_course.save()
                self.stdout.write('course "{code} {title} - {number} ({year})" saved.'.format(
                    code=course['code'],
                    title=course['title'],
                    number=course['number'],
                    year=course['year'],
                ))
                new_count += 1
            except (ValidationError, IntegrityError):
                self.stdout.write('! course "{code} {title} - {number}" already exists.'.format(
                    code=course['code'],
                    title=course['title'],
                    number=course['number'],
                ))
                already_exists_count += 1
            except Exception as err:
                self.stderr.write(str(err))
                error_count += 1

        self.stdout.write('\ncourse crawling process Done!')
        self.stdout.write('\t* newly added - {0}\n\t* already_exists - {1}\n\t* error - {2}'.format(
            new_count, already_exists_count, error_count
        ))