FROM ubuntu:latest

# install dependencies
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		apache2 \
	&& rm -r /var/lib/apt/lists/*

CMD ["apachectl", "-D", "FOREGROUND"]
# Ports
EXPOSE 80