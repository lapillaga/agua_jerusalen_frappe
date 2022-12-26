from datetime import datetime, date


def before_save(doc, method):
    # If customer age is more than 65, set the customer type to Senior
    doc.is_older_adult = False
    if not doc.birth_date:
        return

    today = date.today()
    birth_date = datetime.strptime(doc.birth_date, '%Y-%m-%d')

    age = today.year - birth_date.year - ((today.month, today.day) < (
        birth_date.month,
        birth_date.day
    ))

    if age > 65:
        doc.is_older_adult = True
