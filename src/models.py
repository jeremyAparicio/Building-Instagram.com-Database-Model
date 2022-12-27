import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer,primary_key=True)
    nombre = Column(String(50),)
    apellido = Column(String(50))
    correo = Column(String(50))
    contraseña = Column(String(50))

class Post(Base):
    __tablename__ = "post"
    id_post = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))    
    descripcion = Column(String(250))
    fecha = Column(DateTime)
    relacion_usuario = relationship("Usuario")
     

class Likes(Base):
    __tablename__ = "likes"
    id_like = Column(Integer,primary_key=True)
    usuario_post = Column(Integer,ForeignKey("post.id")) 
    usuario_id = Column(Integer,ForeignKey("usuario.id"))   
    relacion_usuario = relationship("Usuario") 
    relacion_post = relationship("Post")


class Comentarios(Base):
    __tablename__ = "comentarios"
    id_comentario = Column(Integer,primary_key=True)
    usuario_post = Column(Integer,ForeignKey("post.id")) 
    usuario_id = Column(Integer,ForeignKey("usuario.id")) 
    comentario = Column(String(250))
    relacion_usuario = relationship("Usuario")
    relacion_post = relationship("Post")

class Seguidores(Base):
    __tablename__ = "seguidores"
    id_seguidores = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))
    seguidor_id = Column(Integer,ForeignKey("usuario.id"))
    relacion_usuario = relationship("Usuario", foreign_keys=[usuario_id])
    relacion_seguidor = relationship("Usuario", foreign_keys=[seguidor_id])

class UsuariosSeguidos(Base):
    __tablename__ = "usuarios_seguidos"
    id_usuariosSeguidos = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))
    seguido_id = Column(Integer,ForeignKey("usuario.id"))
    relacion_usuario = relationship("Usuario", foreign_keys=[usuario_id])
    relacion_seguido = relationship("Usuario", foreign_keys=[seguido_id])

class PaginasSeguidas(Base):
    __tablename__ = "paginas_seguidas"
    id_paginasSeguidas = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))
    pagina_id = Column(Integer,ForeignKey("pagina.id"))
    relacion_usuario = relationship("Usuario")
    relacion_pagina = relationship("Pagina")

class Paginas(Base):
    __tablename__ = "pagina"
    id_pagina = Column(Integer,primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(250))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
