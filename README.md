
# Swiftickets

A swiftickets vem como solução para o crescente problema do cambismo no mercado de venda de ingressos para eventos de entretenimento!




## Stack utilizada

**Front-end:** React, Chakra UI

**Back-end:** Django


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/Seguidores-do-Pato/Swiftickets-backend.git
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Exclua as migrações, o banco e o cache. Após isso, rode as migrações

```bash
  python manage.py migrate
```

Inicie o servidor

```bash
  python manage.py runserver
```

#### O projeto irá abrir em: http://127.0.0.1:8000/
