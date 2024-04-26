# BOHConvert

Para criar um cluster em kubernetes da presente aplicação, basta seguir os passos abaixo:

### Passo 1 - Criação das máquinas virtuais

Baixe o VirtualBox e crie duas máquinas virtuais **(use as configurações presentes no *vm_config.txt* como guia)**, uma para o nó *master*, e outra para o nó *worker*. Com as máquinas virtuais criadas abra dois *shells*, sendo um para cada nó, e execute o código:

```shell
$ ssh <usuario_da_maquina_virtual>@<ip_da_maquina_virtual>
```

Em caso de dúvidas quanto ao IP da máquina virtual, basta executar o comando:

```shell
$ hostname -I
```

### Passo 2 - Instalação do kubernetes nas máquinas virtuais

Com o *ssh* ativo para os dois nós, basta instalar as configurações do ambiente kubernetes. A instalação do ambiente do nó master pode ser feita com os comandos presentes no *k8s_install_master.md* presente neste repositório. Já a instalação do ambiente do nó worker pode ser feita com os comandos presentes no *k8s_install_worker.md*, também presente neste repositório. Para verificar se os nós estão devidamente instalados e em perfeita execução, basta ir no *ssh* do nó master, e executar o seguinte comando:

```shell
$ kubectl get nodes
```

Quando os dois nós criados estiverem com o status *Ready*, então tudo estará pronto para o próximo passo.

### Passo 3 - Configuração do arquivo .yaml no kubernetes

Com os ambientes dos nós devidamente configurados e em funcionamento, para criar os pods e instalar a aplicação se faz necessária a criação de um arquivo *.yml*. Para isso basta ir no ambiente *ssh* do nó master e executar o seguinte comando:

```shell
$ nano mypod.yaml
```

Dentro do arquivo, basta colar tudo que está escrito no documento *mypod.yml* presente neste repositório, apertar as teclas **CTRL + X**, digitar **Yes** e apertar a tecla **ENTER**.

### Passo 4 - Instalando aplicação no kubernetes

Com o arquivo *.yml* devidamente configurado já é possível criar o pod com a aplicação, para isso basta executar o seguinte comando:

```shell
$ kubectl apply -f mypod.yaml
```

Para verificar se o pod foi criados com sucesso *(com o status de **Running**, sabendo que é necessário esperar um pouco para que ele atinja esse status)*, executa-se o seguinte comando:

```shell
$ kubectl get pods
```

Já para verificar se a aplicação instalada está rodando da forma correta, checando se o aplicativo em Django teve o servidor iniciado e está ativo, basta executando o seguinte comando:

```shell
kubectl logs dj-bohconvert-test -c dj-bohconvert
```

### Passo 5 - Abrindo aplicação no navegador

Para abrir a aplicação que está rodando no pod no navegador do computador, basta criar um serviço do tipo NodePort para expor a porta 8000 da aplicação para o host do Kubernetes, executando o seguinte comando:

```shell
$ kubectl expose pod dj-bohconvert-test --type=NodePort --port=8000
```

Isso criará um serviço que expõe a porta 8000 do seu pod para um porta aleatória no host do Kubernetes. Para verificar a porta atribuída, executa-se o comando:

```shell
$ kubectl get svc dj-bohconvert-test -o=jsonpath='{.spec.ports[0].nodePort}'
```

Após isso, basta executar o seguinte link no navegador: ***http://<ip_da_maquina_virtual_master>:<porta_aleatoria_gerada>/***

### OBS - Comandos para uso geral no kubernetes

```shell
$ kubectl describe pod <nome_do_pod> # Descreve detalhes sobre um pod específico
$ kubectl exec -it <nome_do_pod> -c <nome_do_container> -- /bin/sh -c "kill 1" # Reinicia um container específico de um pod
$ kubectl exec -it <nome_do_pod> -- /bin/sh # Abre um shell interativo dentro de um pod específico
$ kubectl delete pod <nome_do_pod> # Exclui um pod forçando seu reinício
$ kubectl delete pod <nome_do_pod> --grace-period=0 --force # Exclui um pod permanentemente
$ kubectl delete deployment <nome_do_deployment> # Exclui um deployment específico
$ kubectl delete service <nome_do_service> # Exclui um serviço específico do cluster
```
