# Lea_Record_Shop
#
# Requisitos local:
#
# docker instalado e configurado
#
# banco de dados POSTGRESQL
#
# configurar as credenciais do banco no arquivo .env
#
# PASSO 1
# Docker Build:
# Executar o comando para buildar a imagem
# docker image build -t lea_record_shop:latest .
# 
# PASSO 2
# Executar o comando para iniciar a imagem no container
# docker container run -it -v ${pwd}:/usr/src/app --env-file .env -p 81:80 --name lea_record_shop lea_record_shop:latest
#
#
