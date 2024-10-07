FROM qgis/qgis:3.38.3-noble

# from `print(pyproj.datadir.get_data_dir())` in python
ENV PROJ_DOWNLOAD_DIR=/usr/share/proj

RUN DEBIAN_FRONTEND=noninteractive apt update && apt upgrade -y
RUN apt install -y python3-geopandas
RUN apt install -y curl
RUN apt install -y unzip
RUN apt install -y zip
RUN curl --fail-with-body "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && ./aws/install && rm awscliv2.zip

# This downloads a lot of PROJ files...800+ MB
RUN aws s3 sync s3://cdn.proj.org ${PROJ_DOWNLOAD_DIR} --no-sign-request

ENV QGIS_PREFIX_PATH=/usr
ENV QT_QPA_PLATFORM=offscreen
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

WORKDIR /app

COPY . .
