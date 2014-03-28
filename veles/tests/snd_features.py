"""
Created on May 22, 2013

@author: Markovtsev Vadim <v.markovtsev@samsung.com>
"""


import logging
import numpy
import unittest
from veles.snd_features import SoundFeatures
from libSoundFeatureExtraction.python.sound_feature_extraction.library import Library


class Test(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        Library("/home/markhor/Development/SoundFeatureExtraction/build/src/"
                ".libs/libSoundFeatureExtraction.so")

    def tearDown(self):
        pass

    def testSoundFeatures(self):
        sf = SoundFeatures()
        sf.inputs = [{"data": numpy.ones(100000, dtype=numpy.short) * 1000,
                      "sampling_rate": 16000}]
        sf.add_feature("WPP[Window(length=512, type=rectangular), DWPT, "
                       "SubbandEnergy, Log, DWPT(order=4, tree=1 2 3 3)]")
        sf.initialize()
        sf.run()
        sf.save_to_file("/tmp/test_snd_features.xml",
                        ["First and only input"])
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSoundFeatures']
    unittest.main()