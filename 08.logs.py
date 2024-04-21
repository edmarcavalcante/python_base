import os
import logging
from logging import handlers

# Nossa instância
log_level = os.getenv("LOG_LEVEL", 'WARNING').upper
log = logging.Logger("Edmar", log_level)
#level
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=300
    backupCount=10,
)

# formatação
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctimes)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

#ch.setFormatter(fmt)
fh.setFormatter(fmt)

#destino
#log.addHandler(ch)
log.addHandler(fh)

log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuário")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma única execução.")
log.critical("Deu Problema Geral.")

try:
    1/0
except ZeroDivisionError as e:
    logging.error("Deu erro")