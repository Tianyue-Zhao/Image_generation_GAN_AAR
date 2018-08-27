source .bashrc
rm /home/kuz22/AAR/real_sketches/val/*
rm /home/kuz22/additional_programs/pix2pix/results/edges2handbags_blurred/latest_net_G_val/images/output/*
python /home/kuz22/AAR/bin/make_AB.py
cd additional_programs/pix2pix
DATA_ROOT=/home/kuz22/AAR/real_sketches name=edges2handbags_blurred which_direction=AtoB phase=val th test.lua
cd ~
rm /home/kuz22/AAR/real_sketches/A/*
