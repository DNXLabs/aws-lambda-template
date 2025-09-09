FROM public.ecr.aws/lambda/python:3.11

# Copia o código
COPY ./src/app.py ${LAMBDA_TASK_ROOT}

# Comando default (handler: nome_do_arquivo.nome_da_função)
CMD ["app.lambda_handler"]
