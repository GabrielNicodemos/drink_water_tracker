def validate_positive_value(value):
    if value <= 0:
        raise ValidationError('Quantity must be a positive number.')

def name_not_alpha(name):
    return not name.isalpha()