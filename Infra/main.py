from Infra.repository.funcionario_repository import FuncionarioRepository
import logging


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='./Infra/log/program.log'
    )
    
    repo = FuncionarioRepository()
    data = repo.select_all()
    print(data[0].nome)