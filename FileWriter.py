import os

from .mkdir_p import mkdir_p
from .mkdir_rev import mkdir_rev,getUniqueBasedir

class FileWriter(object):
    @staticmethod
    def make_rev_dir(outputDir):
        rev_dir = getUniqueBasedir(outputDir)
        mkdir_p(rev_dir)
        return rev_dir
