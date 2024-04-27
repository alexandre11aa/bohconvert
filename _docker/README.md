# BOHConvert

Se tratando da criação dos containers da aplicação sem a necessidade de copiar todo o repositóio, baixa-se a imagem desta diretamente do Docker Hub. Após isso sobe-se os containers no Docker a partir da imagem baixada. Para isso, inicia-se o *shell* no diretório do *docker-compose.yml*, e executa-se os comandos abaixo:

```shell
$ docker login
$ docker push alexandre11aa/bohconvert:latest
$ docker-compose up
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
