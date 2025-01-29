# filepath: /Z:/Projects/te/scripts/ambari_script.py
from main import BaseScript, ScriptResult
from ambari import Ambari

class AmbariScript(BaseScript):
    def __init__(self, ambari_client: Ambari):
        self.ambari_client = ambari_client

    def run(self) -> ScriptResult:
        try:
            # Пример вызова метода из класса Ambari
            self.ambari_client.some_method()
            return ScriptResult.SUCCESS
        except Exception as e:
            print(f"Error: {e}")
            return ScriptResult.FAILURE