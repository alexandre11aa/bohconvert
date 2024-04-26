# BOHConvert

[BOHConcert](https://hub.docker.com/repository/docker/alexandre11aa/bohconvert/general) - Repositório no Docker Hub que contém a imagem da aplicação.

### Docker

Para criar montar a imagem e criar os containers da presente aplicação em Docker, basta copiar o presente repositório, entrar na pasta onde está presente o arquivo *docker-compose.yml* e executar o seguinte comando:

```shell
$ docker-compose up --build
```

Alguns comandos gerais podem ser vistos abaixo:

```shell
$ docker images # Verifica as imagens existentes em disco
$ docker ps -a # Verifica os containers existentes em disco
$ docker exec -it <nome_do_container> sh # Entra em container em execução
$ docker logs <nome_do_container> # Exibe os logs do container
$ docker start <ID_do_container> # Inicia a execução de um container
$ docker stop <nome_do_container> # Finaliza execução de um container
$ docker restart <ID_do_container> # Reinicia a execução de um container
```

Alguns comandos para limpeza podem ser vistos abaixo:

```shell
$ docker rm <nome_do_container> # Exclui container que não está em execução
$ docker rmi <nome_da_imagem> # Exclui imagem
$ docker image prune # Apaga todas as imagens não utilizadas
$ docker container prune # Apaga todos containers parados
$ docker service prune # Apaga todos os serviços não utilizadas
$ docker volume prune # Apaga todos os volumes não utilizadas
$ docker network prune # Apaga todos os networks não utilizadas
```
