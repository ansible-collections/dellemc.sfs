#!/bin/sh

namespace=$(grep -w "namespace" galaxy.yml |  awk  '{print $2}')
name=$(grep -w "name" galaxy.yml |  awk  '{print $2}')
version=$(grep -w "version" galaxy.yml |  awk  '{print $2}')
collection_file="$namespace-$name-$version.tar.gz"
#echo "$collection_file"

rm -f /root/ansible_log.log
rm -rf /root/.ansible/collections/ansible_collections/dellemc/sfs
rm "$collection_file"
ansible-galaxy collection build --force 

ansible-galaxy collection install "$collection_file" --force-with-deps

