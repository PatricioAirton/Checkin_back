from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Contato(Base):
    __tablename__ = 'contato'

    id = Column(Integer, primary_key=True)
    telefone= Column(String(15))
    tipo= Column(String(10)) # Celular ou telefone fixo#
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o contato e o passageiro.
    # Aqui está sendo definido a coluna 'passageiro' que vai guardar
    # a referencia ao passageiro, a chave estrangeira que relaciona
    # um passageiro ao contato.
    passageiro = Column(Integer, ForeignKey("passageiro.pk_passageiro"), nullable=False)

    def __init__(self, texto:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Contato

        Arguments:
            texto: o texto de um contato.
            data_insercao: data de quando o contato foi informado ou inserido
                           à base
        """
        self.texto = texto
        if data_insercao:
            self.data_insercao = data_insercao
