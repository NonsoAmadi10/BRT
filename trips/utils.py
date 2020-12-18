
import functools
import datetime
from BRT.response import failure_response
from rest_framework import status


def format_date(x):
    # Check if the date format is in the order YYYY-MM_DD
    date_format = '%Y-%m-%d'
    return datetime.datetime.strptime(x, date_format).date()


def convert_date(func):
    @functools.wraps(func)
    def wrapper(_, request, *args, **kwargs):

        today_date = datetime.date.today()

        try:
            _format_date = format_date(request.data['trip_date'])

            if today_date > _format_date:
                return failure_response({}, 'Trip date can only include today and beyond', status.HTTP_400_BAD_REQUEST)
            else:
                request.data['trip_date'] = _format_date
                request.data['fare'] = float(request.data['fare'])

                return func(_, request, *args, **kwargs)
        except ValueError:
            return failure_response({}, 'Incorrect data format, should be YYYY-MM-DD', status.HTTP_400_BAD_REQUEST)
    return wrapper
