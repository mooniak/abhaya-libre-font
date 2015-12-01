#
# bootstrap.sh
#
# Copyright (c) 2015,
# Mooniak <hello@mooniak.com>
# Ayantha Randika <paarandika@gmail.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE file for details.

#!/usr/bin/env bash

apt-get update > /dev/null
sudo apt-get install software-properties-common -y
apt-get install python-software-properties -y
echo "Installing Git..."
apt-get install git -y > /dev/null

echo "Installing Fontforge"
add-apt-repository ppa:fontforge/fontforge -y > /dev/null
apt-get update > /dev/null
apt-get install fontforge -y > /dev/null
apt-get install python-fontforge -y > /dev/null

echo "Installing unzip..."
apt-get install unzip -y > /dev/null

echo "Installing setuptools..."
apt-get install python-setuptools -y > /dev/null

echo "Installing Robofab..."
git clone https://github.com/robofab-developers/robofab.git
cd robofab
git checkout ufo3k
python setup.py install
cd ..

echo "Installing FontTools..."
git clone https://github.com/behdad/fonttools.git
cd fonttools
python setup.py install
cd ..


echo "Adding Kern Scripts..."
git clone https://github.com/adobe-type-tools/python-modules.git
cd python-modules
cp WriteFeaturesKernFDK.py /usr/local/lib/python2.7/dist-packages
cp WriteFeaturesMarkFDK.py /usr/local/lib/python2.7/dist-packages
cd ..

echo "Installing MutatorMath..."
git clone https://github.com/LettError/MutatorMath.git
cd MutatorMath
python setup.py install
cd ..

echo "Installing fontMath..."
git clone https://github.com/typesupply/fontMath.git
cd fontMath
git checkout ufo3
python setup.py install
cd ..

echo "Installing defcon..."
git clone https://github.com/typesupply/defcon.git
cd defcon
git checkout ufo3
python setup.py install
cd ..

echo "Installing Numpy..."
apt-get install python-numpy -y > /dev/null

echo "Installing hindkit..."
git clone https://github.com/mooniak/hindkit.git
cd hindkit
python setup.py install
cd ..

echo "Installing AFDKO..."
wget http://download.macromedia.com/pub/developer/opentype/FDK.2.5.64655/FDK-2.5.64655-LINUX.zip > /dev/null
unzip FDK-2.5.64655-LINUX.zip > /dev/null
cd FDK
./FinishInstallLinux
printf '%s\n%s\n' 'FDK_EXE="/home/vagrant/FDK/Tools/linux"' 'PATH=${PATH}:"/home/vagrant/FDK/Tools/linux" export PATH export FDK_EXE' 'export PATH' 'export FDK_EXE'>> /home/vagrant/.profile
