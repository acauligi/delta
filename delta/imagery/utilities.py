# Copyright © 2020, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# The DELTA (Deep Earth Learning, Tools, and Analysis) platform is
# licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Miscellaneous utility classes/functions.
"""
import os
import sys
import shutil
import zipfile
import tarfile

def unpack_to_folder(compressed_path, unpack_folder):
    """
    Unpack a file into the given folder.
    """

    tmpdir = os.path.normpath(unpack_folder) + '_working'

    ext = os.path.splitext(compressed_path)[1]
    try:
        if ext.lower() == '.zip':
            with zipfile.ZipFile(compressed_path, 'r') as zf:
                zf.extractall(tmpdir)
        else: # Assume a tar file
            with tarfile.TarFile(compressed_path, 'r') as tf:
                tf.extractall(tmpdir)
    except:
        shutil.rmtree(tmpdir)
        raise
    # make this atomic so we don't have incomplete data
    os.rename(tmpdir, unpack_folder)

def progress_bar(text, fill_amount, prefix = '', length = 80): #pylint: disable=W0613
    """
    Prints a progress bar. Call multiple times with increasing progress to
    overwrite the printed line.
    """
    filled_length = int(length * fill_amount)
    fill_char = '█' if sys.stdout.encoding.lower() == 'utf-8' else 'X'
    prog_bar = fill_char * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s' % (prefix, prog_bar, text), end = '\r')
