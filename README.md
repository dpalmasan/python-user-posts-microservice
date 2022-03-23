# Blog Posts Service

This is part of the microservices demo I am working on. This service deals with blog data, in which an authenticated user should be able to:

* Create a Blog entry
* Update a Blog entry
* Get blogs based on different criteria
* Get blog entry details

## Config file

Use `config.template.yaml` file to generate a configuration for the service. Once done, rename it as `config.yaml` as it is used to configure the service (e.g. mongodb, etc).

## Tech Stack

The API is implemented using `FastAPI`. A custom middleware is sit in front of requests, which validates authentication tokens (in this `JWT`) that where issued by an [authentication service](https://github.com/dpalmasan/go-auth-microservice). The approach to do this is using a `gRPC` endpoint which will receive the message containing the token and will validate it to check the token was not expired and was not changed allong the way.

### Data Layer

To enable fast developments, `MongoDB` was used as the DB engine.

### Dependency Management

For dependency management `poetry` was the tool of choice, so we can have reproducible environments, and we don't end up in inconsistencies on the dependency graph.

## Starting the Service

The easiest way of running the service is just doing `poetry install && poetry run uvicorn main:app`

# Running Service on Kubernetes

You can run it in `minikube` by running:

```
# Install dependencies (charts)
cd helm && helm dependency build && cd -

# Run application
helm \
    --kube-context=minikube \
    --create-namespace \
    --namespace=blog-svc \
    upgrade --install --force --recreate-pods\
    blog-svc \
    helm
```