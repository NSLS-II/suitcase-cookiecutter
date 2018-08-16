# Tests should generate (and then clean up) any files they need for testing. No
# binary files should be included in the repository.

import hashlib
import json
import unittest
from typing import List

suitcase = None


class TestRheology(unittest.TestCase):

    def setUp(self):
        """Generate test files and headers"""
        self.paths = []
        self.header = {}

    def test_forward_rheology(self):
        """
        Translate native format to Event Model; check that reversing the translation gives back a file with the same
        checksum.

        """

        # Generate initial checksum
        pre_transform_checksum = hash_files(self.paths)

        # Transform forward/back
        args = self.paths
        kwargs = {}

        header = suitcase.ingest(*args, **kwargs)
        export_paths = suitcase.export(header)

        # Generate final checksum
        post_transform_checksum = hash_files(export_paths)

        assert post_transform_checksum == pre_transform_checksum

    def test_reverse_rheology(self):
        """
        Translate from an Event Model header to a native format; check that reversing the translation gives back an Event
        Model header with the same checksum.

        """

        # Generate initial checksum
        pre_transform_checksum = hash_dict(self.header)

        # Transform forward/back
        export_paths = suitcase.export(self.header)
        args = export_paths
        kwargs = {}
        header = suitcase.ingest(*args, **kwargs)

        # Generate final checksum
        post_transform_checksum = hash_dict(header)

        assert pre_transform_checksum == post_transform_checksum


def hash_files(paths: List[str]):
    """
    MD5 checksum a list of file paths
    """
    return map(hash_file, paths)


def hash_file(path: str):
    """
    MD5 checksum a file
    """
    return hashlib.md5(path).hexdigest()


def hash_dict(d: dict) -> str:
    return hashlib.md5(json.dumps(d, sort_keys=True)).hexdigest()


if __name__ == '__main__':
    unittest.main()
