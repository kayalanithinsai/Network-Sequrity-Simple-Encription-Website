from django.http import HttpResponse
from django.template import loader


# Create your views here.
def encrypt_func(encrypt_str):
    """
    :param encrypt_str:
    :return encrypted string:
    if the character is between A and Z or a and z we encrypt these characters else we leave other characters.
    The ith alphabet from the beginning is mapped to ith character from the end.
    we could use this function for both encryption and decryption purposes.
    """

    encrypted_str = ''
    for c in encrypt_str:
        if 'A' <= c <= 'Z':
            extra = ord(c) - ord('A')
            encrypted_str += chr(ord('A') + 25 - extra)
        elif 'a' <= c <= 'z':
            extra = ord(c) - ord('a')
            encrypted_str += chr(ord('a') + 25 - extra)
        else:
            encrypted_str += c
    return encrypted_str


def first_view(request):
    if request.method == "GET":
        template = loader.get_template('simple_enc_dec/index.html')
        return HttpResponse(template.render({'encrypt_str': '', 'decrypt_str': ''}, request))
    else:
        if request.POST.get('submit_type') == 'encrypt':
            encrypt_str = request.POST.get('encrypt_str')
            template = loader.get_template('simple_enc_dec/index.html')
            encrypted_str = encrypt_func(encrypt_str)
            return HttpResponse(template.render({'encrypt_str': encrypt_str, 'decrypt_str': encrypted_str}, request))
        else:
            decrypt_str = request.POST.get('encrypt_str')
            template = loader.get_template('simple_enc_dec/index.html')
            decrypted_str = encrypt_func(decrypt_str)
            return HttpResponse(template.render({'encrypt_str': decrypt_str, 'decrypt_str': decrypted_str}, request))

