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
        self.configReplace = self.request.get_param("configReplace")
        if self.configReplace =="replaceEnabled":
            self.replaceValue = self.request.get_param("replaceValue")
            self.targetValue = self.request.get_param("targetValue")
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

        self.configClasses = self.request.get_param("configClasses")


    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}


    def run(self):

        self.outputData = self.data
        return build_response_string(context=self)


if "__main__" == __name__:
    Executor(sys.argv[1]).run()