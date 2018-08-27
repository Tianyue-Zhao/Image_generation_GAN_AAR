mv /home/victor/AAR/demo/blurred/* /home/victor/AAR/demo/blurred_archive
mv /home/victor/AAR/demo/*.jpg /home/victor/AAR/demo/archive_photos
#ssh -i ~/.ssh/id_rsa pi@raspberrypi.local <<EOF
#cd demo
#raspistill -w 512 -h 512 -o demo1.jpg
#raspistill -w 512 -h 512 -o demo2.jpg
#exit
#EOF
#sftp -i ~/.ssh/id_rsa pi@raspberrypi.local <<EOF
#cd demo
#mget *.jpg /home/victor/AAR/demo/
#exit
#EOF
echo 'python'
python /home/victor/AAR/demo/crop.py
echo 'python'
#original portion
sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mput /home/victor/AAR/demo/*.jpg /home/kuz22/AAR/real_sketches/A
exit
EOF
#<<EOF lets the program perform commands until it reads EOF
ssh -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
bash /home/kuz22/AAR/bin/auto_run_server_original.sh
exit
EOF
mv /home/victor/AAR/demo/original_output/* /home/victor/AAR/demo/original_output_archive
sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mget /home/kuz22/additional_programs/pix2pix/results/edges2handbags/latest_net_G_val/images/output/* /home/victor/AAR/demo/original_output
exit
EOF
#blurred portion
sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mput /home/victor/AAR/demo/blurred/* /home/kuz22/AAR/real_sketches/A
exit
EOF
#<<EOF lets the program perform commands until it reads EOF
ssh -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
bash /home/kuz22/AAR/bin/auto_run_server.sh
exit
EOF
mv /home/victor/AAR/demo/blurred_output/* /home/victor/AAR/demo/blurred_output_archive
sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mget /home/kuz22/additional_programs/pix2pix/results/edges2handbags_blurred/latest_net_G_val/images/output/* /home/victor/AAR/demo/blurred_output
exit
EOF
mv /home/victor/AAR/demo/display/* /home/victor/AAR/demo/display_archive
python display.py
