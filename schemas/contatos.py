from pydantic import BaseModel


class ContatoSchema(BaseModel):
    """ Define como um novo contato a ser inserido deve ser representado
    """
    passageiro_id: int = 1
    telefone: str = "+ 55 11 9864 1234"
    tipo:str = "Celular"
