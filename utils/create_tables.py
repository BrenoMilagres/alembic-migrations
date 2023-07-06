from utils.configs import settings
from utils.database import engine


async def create_tables() -> None:
    import models.user_model
    import models.analysis_model
    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
