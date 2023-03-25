import frappe
from frappe import auth


@frappe.whitelist(allow_guest=True)
def login(email, password):
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=email, pwd=password)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response['message'] = {
            'message': 'No se pudo iniciar sesión. Por favor, verifique sus credenciales e intente nuevamente.',
            'status': 'error',
            'traceback': frappe.get_traceback(),
        }
        return

    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)
    image_url = None
    if user.user_image:
        image_path = frappe.utils.get_files_path(user.user_image)
        image_url = frappe.utils.get_url(image_path)

    frappe.response['message'] = {
        'sid': frappe.session.sid,
        'apiKey': user.api_key,
        'apiSecret': api_generate,
        'status': 'success',
        'user': {
            'username': user.username,
            'fullName': user.full_name,
            'email': user.email,
            'image': image_url
        }
    }


def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()

    return api_secret
