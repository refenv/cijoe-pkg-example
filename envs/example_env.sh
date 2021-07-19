#!/usr/bin/env bash
#
# Reference environment for shipping with cijoe-pkg-example
#
# This example uses the commonly used remote configuration as described in the cijoe documentation,
# along with a environment variables specific to the 'cijoe-pkg-example
#
# Adjust these to match your *test-target*, e.g. the remote host and username, and the specifics
# for the cijoe-pkg-example
#

#
# Remote access to *test-target*
#
export SSH_HOST=your-remote-host
export SSH_USER=root

#
# Here a "Device-Under-Test" (DUT) is needed by 'cijoe-pkg-example' are referred to by the
# environment variable "EXAMPLE_DUT".
#
export EXAMPLE_DUT=type_your_device_path_here

# On Unix-ish *test-targets* this would be a path in the device-filesystem at /dev/
#export EXPORT_DUT=/dev/nvme0n1

# On Windows *test-targets*, this might look something like below, in case of a hard-drive
#export EXAMPLE_DUT="\Device\Harddisk1"
