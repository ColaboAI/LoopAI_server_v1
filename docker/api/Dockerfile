FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ARG USER_NAME=default_user
ARG ostype=Linux
ARG USER_ID
ARG GROUP_ID

ENV WORK_DIR=/code
ENV USER_NAME=${USER_NAME}
ENV PYTHONPATH "${PYTHONPATH}:/"
ENV ENV=dev
ENV PORT=8000

RUN bash -c 'if [ ${ostype} == Linux ]; then groupadd -r --gid ${GROUP_ID} ${USER_NAME}; fi && \
    useradd -r --create-home --shell /bin/bash --uid ${USER_ID} --gid ${GROUP_ID} ${USER_NAME}' && \
    mkdir -p ${WORK_DIR} && chown ${USER_NAME} ${WORK_DIR}

# RUN useradd ${USER_NAME}
# RUN mkdir ${WORK_DIR}
# RUN chown ${USER_NAME}:${USER_NAME} ${WORK_DIR}


COPY --chown=${USER_NAME}:${USER_NAME} . ${WORK_DIR}
WORKDIR ${WORK_DIR}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
USER ${USER_NAME}

RUN chmod a+x ${WORK_DIR}/docker/api/startup.sh
ENTRYPOINT ${WORK_DIR}/docker/api/startup.sh