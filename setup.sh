echo '[Adding config to .bashrc]'
echo >> ~/.bashrc
echo '# PEN ENV VAR UPDATE' >> ~/.bashrc
echo "trap 'exported=\$(cat ~/.penta); export PEN=\"$exported\"' DEBUG" >> ~/.bashrc

echo '[Creating a "pen" command in /usr/bin/pen]'
sudo ln $PWD/pen.py /usr/bin/pen
