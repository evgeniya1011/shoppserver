Создать БД psql -U postgres

запуск приложение uvicorn main:app --reload

aerich init -t tortoise_config.TORTOISE_ORM - инициализация файла конфигурации и задать местоположение миграций командой
aerich init-db - инициализация БД
aerich migrate - применение миграций
aerich upgrade - обновление до последней версии
aerich downgrade -h - откат миграций
