sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mput /home/victor/AAR/auto-run/* /home/kuz22/AAR/real_sketches/A
exit
EOF
#<<EOF lets the program perform commands until it reads EOF
ssh -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
bash /home/kuz22/AAR/bin/auto_run_server.sh
exit
EOF
sftp -i ~/.ssh/id_rsa kuz22@130.203.139.111 <<EOF
mget /home/kuz22/additional_programs/pix2pix/results/edges2handbags_blurred/latest_net_G_val/images/output/* /home/victor/AAR/auto-run-output
exit
EOF
