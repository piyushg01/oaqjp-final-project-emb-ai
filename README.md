# ci-cd-final-project

## Project Name

ci-cd-final-project

## Description

This project implements a Product Service using Test-Driven Development (TDD) and Behavior-Driven Development (BDD).

The Product Service provides REST APIs for managing products, including creating, reading, updating, deleting, listing, and searching products.

## Features

- Create a Product
- Read a Product
- Update a Product
- Delete a Product
- List all Products
- Search Products by Name
- Search Products by Category
- Search Products by Availability

## Technology Stack

- Python
- Flask
- PostgreSQL
- unittest
- Factory Boy
- Behave
- Flake8
- Nose
- GitHub Actions
- OpenShift
- Tekton
- Buildah

## Testing

The project contains unit tests for the Product model and REST API routes.

BDD scenarios are implemented using Behave to validate product operations through the application interface.

## CI/CD

GitHub Actions is used for Continuous Integration.

The CI workflow performs:

1. Checkout source code
2. Set up Python
3. Install dependencies
4. Lint the code using Flake8
5. Run unit tests using Nose

OpenShift Pipelines and Tekton are used for Continuous Delivery.

The deployment pipeline contains:

1. Cleanup
2. Git clone
3. Flake8
4. Nose
5. Buildah
6. OpenShift deployment