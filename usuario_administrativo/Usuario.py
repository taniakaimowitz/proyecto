"""Modulo usuario para control de accinoes de usuario"""
from passlib.hash import pbkdf2_sha256

USERLOGINS = {
    "pablo": ["pablo", 1234]
}

def check_if_user_exists(username):
    """Verifica que el usuario exista"""
    return USERLOGINS.get(username, "True")
    

def add_user(username, password):
    """Agrega un Usuario a la lista"""
    if(check_if_user_exists(username) == "True"):
        USERLOGINS[username] = [username, encode_password(password)]
        print ("El usuario ha sido creado exitosamente\n")
    else:
        print ("El nombre de usuario ya existe, por favor intente de nuevo\n")
        

def show_users():
    """Devuelve la lista con todos los usuarios"""
    return USERLOGINS

def encode_password(password):
    """codifica el password para almacenarlo"""
    hash = pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16)
    return hash

def update_username(oldUsername, newUsername):
    """Actualiza el nombre de usuario seleccionado"""
    rl = USERLOGINS[oldUsername]    
    originalPassword = rl[1]
    nl = [newUsername, originalPassword]
    USERLOGINS.pop(oldUsername)
    USERLOGINS[newUsername] = [newUsername, originalPassword]
    print("Usuario actualizado correctamente")

def update_password(username, newPassword):
    """Actualiza el password del usuario seleccionado"""
    rl = USERLOGINS[username]    
    hashedPwd = encode_password(newPassword)
    nl = [username, hashedPwd]
    USERLOGINS[username] = nl
    print("Usuario actualizado correctamente\n")

def delete_user(username):
    del USERLOGINS[username]
    print("Usuario ha sido eliminado correctamente\n")

def check_password(clear_password, password_hash):
    """valida que el password ingresado coincida con el que esta almacenado"""
    return pbkdf2_sha256.verify(clear_password, password_hash)