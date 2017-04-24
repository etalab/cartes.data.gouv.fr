# cartes.data.gouv.fr


## Install

Create a `umap` database in your PostgreSQL instance:

    createdb umap -O youruser

Activate PostGIS:

    psql umap
    create extension postgis;

Activate unaccent:

    create extension unaccent;

Clone project:

    git clone https://github.com/etalab/cartes.data.gouv.fr
    cd cartes.data.gouv.fr
    export UMAP_SETTINGS=`pwd`/local.py

Create a virtualenv:

    virtualenv umap
    source umap/bin/activate

Install umap:
    pip install umap-project
    umap migrate
    umap collectstatic
    umap compress

Create a superuser:

    umap createsuperuser


More at http://umap-project.readthedocs.io/en/latest/install/


## Testing

   umap runserver

Then open your browser and go to: http://localhost:8000/
