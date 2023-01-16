#!/usr/bin/bash
mkdir ./s1
mkdir ./s1/s3
mkdir ./s1/s2
mkdir ./s1/s2/Advanced
touch ./s1/s3/conf.txt
echo 'virtual environments are my favorite new technology' > ./s1/s3/conf.txt
touch ./s1/s2/text_chunk1.txt
echo 'virtual environments are good for managing package dependencies' > ./s1/s2/text_chunk1.txt
cp ./s1/s2/text_chunk1.txt ./s1/s2/Advanced/text_chunk2.txt
echo 'I like them because they ensure everything is compatible and keep development organized' >> ./s1/s2/Advanced/text_chunk2.txt
echo 'Directories and Files were created!'
