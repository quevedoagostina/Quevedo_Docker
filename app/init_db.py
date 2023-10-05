from app import app, db
from models import Categoria

with app.app_context():
# Crea algunas categorías
    categoria1 = Categoria(nombre='Personal')
    categoria2 = Categoria(nombre='Deportes')
    categoria3 = Categoria(nombre='Moda')
    categoria4= Categoria(nombre='Juegos')
    categoria5= Categoria(nombre='Espectaculo')

    # Agrega las categorías a la sesión
    db.session.add(categoria1)
    db.session.add(categoria2)
    db.session.add(categoria3)
    db.session.add(categoria4)
    db.session.add(categoria5)

    # Guarda los cambios en la base de datos
    db.session.commit()
