from pydantic import BaseModel
from typing import Optional, List
from model.passageiro import Passageiro

from schemas import ContatoSchema


class PassageiroSchema(BaseModel):
    """ Define como um novo passageiro a ser inserido deve ser representado
    """
    nome: str = "José Airton Patricio"
    cpf: str= "123.456.785-77"
    peso: float = 79.0


class PassageiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do passageiro.
    """
    cpf: str= 123456785-77


class ListagemPassageirosSchema(BaseModel):
    """ Define como uma listagem de passageiro será retornada.
    """
    passageiro:List[PassageiroSchema]

class PassageiroUpdateSchema(BaseModel):
    """ Define como um passageiro a ser atualizado deve ser representado
    """
    id: int =1
    nome: str = "Joao da Silva"
    cpf: str = "433.345.437-26"
    peso: float = 72.50


def apresenta_passageiros(passageiros: List[Passageiro]):
    """ Retorna uma representação do produto seguindo o schema definido em
        PassageiroSchema.
    """
    result = []
    for Passageiro in passageiros:
        result.append({
            "nome": Passageiro.nome,
            "cpf": Passageiro.cpf,
            "peso": Passageiro.peso,
        })

    return {"passageiros": result}


class PassageiroViewSchema(BaseModel):
    """ Define como um passageiro será retornado: passageiro + contatos.
    """
    id: int = 1
    nome: str = "José Airton Patricio"
    cpf: str = 123456785-77
    peso: float = 79.0
    total_contatos: int = 1
    contato:List[ContatoSchema]


class PassageiroDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_passageiro(passageiro: Passageiro):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroViewSchema.
    """
    return {
        "id": passageiro.id,
        "nome": passageiro.nome,
        "cpf": passageiro.cpf,
        "peso": passageiro.peso,
        "total_contatos": len(passageiro.contatos),
        "contatos": [{"telefone": c.telefone, "tipo":c.tipo} for c in passageiro.contatos]
    }
