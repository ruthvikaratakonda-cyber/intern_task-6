import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

logger.info(
    "Employee created successfully"
)