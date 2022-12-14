from functools import cached_property
from pathlib import Path
from typing import Any
import yaml


class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

    @cached_property
    def _config(self) -> Any:
        with open(self.config_path) as f:
            try:
                return yaml.safe_load(f)["params"]
            except yaml.YAMLError as e:
                raise e

    @property
    def _random_algorithm(self) -> Any:
        return self._config["random_algorithm"]

    @property
    def _genetic_algorithm(self) -> Any:
        return self._config["genetic_algorithm"]

    @cached_property
    def selected_instances(self) -> list[Path]:
        return [Path(filename) for filename in self._config["selected_instances"]]

    @property
    def random_number_of_instances(self):
        return self._random_algorithm["number_of_instances"]

    @property
    def genetic_executions(self):
        return self._genetic_algorithm["executions"]

    @property
    def genetic_population_size(self):
        return self._genetic_algorithm["population_size"]

    @property
    def genetic_generations(self):
        return self._genetic_algorithm["generations"]

    @property
    def genetic_init_method(self):
        return self._genetic_algorithm["init_method"]

    @property
    def genetic_crosover_method(self):
        return self._genetic_algorithm["crosover_method"]

    @property
    def genetic_crosover_probability(self):
        return self._genetic_algorithm["crosover_probability"]

    @property
    def genetic_tournament_size(self):
        return self._genetic_algorithm["tournament_size"]

    @property
    def genetic_selection_method(self):
        return self._genetic_algorithm["selection_method"]

    @property
    def genetic_mutation_method(self):
        return self._genetic_algorithm["mutation_method"]

    @property
    def genetic_mutation_rate(self):
        return self._genetic_algorithm["mutation_rate"]

    @property
    def logs_output_dir(self) -> Path:
        return Path(self._config["logs_output_path"])

    def output_file_name(self, testing_instance: Path) -> str:
        return f"result_{testing_instance.stem}__mutation_method_{self.genetic_mutation_method}_pm_{self.genetic_mutation_rate}__selection_method_{self.genetic_selection_method}_sm_{self.genetic_selection_method}__"
