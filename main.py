from enum import Enum
from abc import ABC, abstractmethod
import logging

from ambari import Ambari
from scripts.ambari_script import AmbariScript

class ScriptResult(Enum):
    SUCCESS = 1
    FAILURE = 2
    PARTIAL_SUCCESS = 3

class BaseScript(ABC):
    @abstractmethod
    def run(self) -> ScriptResult:
        pass

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def main():
    logger = setup_logger('master_script')
    logger.info("Starting master script")

    ambari_client = Ambari()
    scripts = [
        AmbariScript(ambari_client),
        # Добавьте другие скрипты здесь
    ]

    for script in scripts:
        result = script.run()
        logger.info(f"Script {script.__class__.__name__} finished with result: {result.name}")

if __name__ == "__main__":
    main()