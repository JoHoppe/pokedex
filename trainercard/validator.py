from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 485760:
        raise ValidationError("The maximum file size is 0.5MB")
    else:
        return value