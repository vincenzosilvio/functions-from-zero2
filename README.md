# functions-from-zero2

Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 222634383508.dkr.ecr.us-east-1.amazonaws.com
Nota: se ricevi un errore durante l'utilizzo di AWS CLI, assicurati di avere installato la versione più recente di AWS CLI e del Docker.
Crea la tua immagine del Docker utilizzando il seguente comando. Per informazioni sulla creazione di un file Docker da zero, vedi le istruzioni qui . Puoi ignorare questa fase se la tua immagine è già stata creata:

docker build -t logistics .
Una volta completata la compilazione, aggiungi un tag alla tua immagine in modo da poterla inviare a questo repository:

docker tag logistics:latest 222634383508.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
Esegui il seguente comando per inviare questa immagine al repository AWS appena creato:

docker push 222634383508.dkr.ecr.us-east-1.amazonaws.com/logistics:latest