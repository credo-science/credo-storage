# CREDO storage handler

This package receives messages from AMQP and uploads them to mysql compatible database, and s3 storage. Relational database handles metadata, and complicated query processing, while s3 acts as a dedicated blob storage, which handles heavy image data.


## Development and installation
All of the configuration variables are handled by supplying an env var, or directly changing the `config.py` file.

Env is controlled through `pipenv`, packaging is done with `easy_install`.


## Contributing

Fork & develop & pull request


## Authors
* Maciej Pawlik <m.pawlik@cyfronet.pl>
* Reserved for you
