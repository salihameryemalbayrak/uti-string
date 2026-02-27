"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.String.src.utils.response import build_response_string
from components.String.src.models.PackageModel import PackageModel


class String(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.data = self.request.get_param("inputData")
        self.text_list = []
        self.configSelectedKeyValue = self.request.get_param("configSelectedKey")
        self.text_list = [t.strip() for t in self.configSelectedKeyValue.split(',')]
        self.configReplace = self.request.get_param("configReplace")
        if self.configReplace =="replaceEnabled":
            self.replaceValue = self.request.get_param("replaceValue")
            self.targetValue = self.request.get_param("targetValue")
        self.configLength = self.request.get_param("configLength")
        self.configCount = self.request.get_param("configCount")
        if self.configCount == "countEnabled":
            self.countValue = self.request.get_param("countValue")
        self.configFind = self.request.get_param("configFind")
        if self.configFind == "findEnabled":
            self.findValue = self.request.get_param("findValue")
        self.configCaseConversions = self.request.get_param("configCaseConversions")
        self.configEdgeTrimming = self.request.get_param("configEdgeTrimming")
        if self.configEdgeTrimming == "removeSuffix":
            self.suffixValue = self.request.get_param("suffixValue")
        elif self.configEdgeTrimming == "removePrefix":
            self.prefixValue = self.request.get_param("prefixValue")
        elif self.configEdgeTrimming == "strip":
            self.stripValue = self.request.get_param("stripValue")
        elif self.configEdgeTrimming == "lStrip":
            self.lStripValue = self.request.get_param("lStripValue")
        elif self.configEdgeTrimming == "rStrip":
            self.rStripValue = self.request.get_param("rStripValue")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        items_to_process = self.data if isinstance(self.data, list) else [self.data]
        for item in items_to_process:
            if isinstance(item, dict):
                for key_path in self.text_list:
                    keys = key_path.split('.')

                    current_level = item
                    for i in range(len(keys) - 1):
                        current_key = keys[i]
                        if isinstance(current_level, dict) and current_key in current_level:
                            current_level = current_level[current_key]
                        else:
                            current_level = None
                            break

                    target_key = keys[-1]
                    if isinstance(current_level, dict) and target_key in current_level:
                        val = current_level[target_key]
                        if self.configReplace == "replaceEnabled":
                            val = val.replace(self.targetValue, self.replaceValue)

                        match self.configCaseConversions:
                            case "capitalize":
                                val = val.capitalize()
                            case "lower":
                                val = val.lower()
                            case "upper":
                                val = val.upper()
                            case "title":
                                val = val.title()
                            case "swapcase":
                                val = val.swapcase()
                            case "caseConversionsDisabled":
                                pass

                        match self.configEdgeTrimming:
                            case "removeSuffix":
                                val = val.removesuffix(self.suffixValue)
                            case "removePrefix":
                                val = val.removeprefix(self.prefixValue)
                            case "strip":
                                val = val.strip(self.stripValue)
                            case "lStrip":
                                val = val.lstrip(self.lStripValue)
                            case "rStrip":
                                val = val.rstrip(self.rStripValue)
                            case "edgeTrimmingDisabled":
                                pass
                        current_level[target_key] = val

                        if self.configLength == "lengthEnabled":
                            print(val)
                            current_level[f"{target_key}Length"] = len(str(val))
                        if self.configCount == "countEnabled":
                            current_level[f"{target_key}Count{self.countValue}"] = val.count(self.countValue)
                        if self.configFind == "findEnabled":
                            found_indices = []
                            search_term = self.findValue

                            if isinstance(val, str) and search_term:
                                start_index = 0
                                while True:
                                    idx = val.find(search_term, start_index)
                                    if idx == -1:
                                        break
                                    found_indices.append(idx)
                                    start_index = idx + len(search_term)

                            current_level[f"{target_key}FindIndex"] = found_indices

        self.outputData = self.data
        return build_response_string(context=self)


if "__main__" == __name__:
    Executor(sys.argv[1]).run()