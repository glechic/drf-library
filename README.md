# Library

## Overview
It's a simple django rest framework project that emulate library using two simple model User and Book.

## Run

#### To run postgres:

```sh
docker run \
	--name postgres\
	-e POSTGRES_PASSWORD='postgres'\
	-dp 5432:5432\
	-v postdata:/var/lib/postgresql/data\
	--rm postgres
```

#### To load data from fixtures:

```sh
./manage.sh loaddata
```

#### To run django server:

```sh
./manage.py runserver
```

#### To run simple front server:

```sh
python -m http.server -d site
```
 	
