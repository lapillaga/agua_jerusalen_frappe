from datetime import datetime, date


def before_save(doc, method):
    # If customer age is more than 65, set the customer type to Senior
    doc.adulto_mayor = False
    if not doc.fecha_de_nacimiento:
        return

    today = date.today()
    birth_date = datetime.strptime(doc.fecha_de_nacimiento, '%Y-%m-%d')

    age = today.year - birth_date.year - ((today.month, today.day) < (
        birth_date.month,
        birth_date.day
    ))

    if age > 65:
        doc.adulto_mayor = True
