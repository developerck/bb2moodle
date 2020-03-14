import os
import sys
import optparse

import bb9_course
full_in_name = '/var/www/html/poc/bb2modle/data/bb.zip'
full_out_name = '/var/www/html/poc/bb2modle/data/mc.zip'
try:
    bb9_course.create_moodle_zip(full_in_name, full_out_name)
except Exception as e:
    print 'Error converting %s' % e