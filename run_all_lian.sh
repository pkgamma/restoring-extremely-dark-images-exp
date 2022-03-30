git pull

##### simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready #####
unzip -q simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready.zip
cd simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready
python3 train.py
cd ../

cp -r  simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready_done
cd simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready_done
rm -rf outputs/images
rm -rf outputs/weights/weights_2 outputs/weights/weights_70002 outputs/weights/weights_100002
rm -rf *.py
cd ../

zip -q -r simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready_done.zip simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready_done
rm -rf simple_fuse_12_LSE_2conv_4_12_4_k3_MSE_32_G24_ready_done

##### simple_fuse_12_MSE32_G24_ready #####
unzip -q simple_fuse_12_MSE32_G24_ready.zip
cd simple_fuse_12_MSE32_G24_ready
python3 train.py
cd ../

cp -r  simple_fuse_12_MSE32_G24_ready simple_fuse_12_MSE32_G24_ready_done
cd simple_fuse_12_MSE32_G24_ready_done
rm -rf outputs/images
rm -rf outputs/weights/weights_2 outputs/weights/weights_70002 outputs/weights/weights_100002
rm -rf *.py
cd ../

zip -q -r simple_fuse_12_MSE32_G24_ready_done.zip simple_fuse_12_MSE32_G24_ready_done
rm -rf simple_fuse_12_MSE32_G24_ready_done

