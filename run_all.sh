##### simple_fuse_20_ready #####
unzip -q simple_fuse_20_ready.zip
cd simple_fuse_20_ready
python3 train.py
cd ../

cp -r  simple_fuse_20_ready simple_fuse_20_ready_done
rm -rf simple_fuse_20_ready_done/outputs/images
zip -q -r simple_fuse_20_ready_done.zip simple_fuse_20_ready_done
rm -rf simple_fuse_20_ready_done

##### 2RDB_ready #####
unzip -q 2RDB_ready.zip
cd 2RDB_ready 
python3 train.py
cd ../

cp -r  2RDB_ready 2RDB_ready_done
rm -rf 2RDB_ready_done/outputs/images
zip -q -r 2RDB_ready_done.zip 2RDB_ready_done
rm -rf 2RDB_ready_done


##### 4RDB_ready #####
unzip -q 4RDB_ready.zip
cd 4RDB_ready
python3 train.py
cd ../

cp -r  4RDB_ready 4RDB_ready_done
rm -rf 4RDB_ready_done/outputs/images
zip -q -r 4RDB_ready_done.zip 4RDB_ready_done
rm -rf 4RDB_ready_done

##### rm_residual_HSE_ready #####
unzip -q rm_residual_HSE_ready.zip
cd rm_residual_HSE_ready
python3 train.py
cd ../

cp -r  rm_residual_HSE_ready rm_residual_HSE_ready_done
rm -rf rm_residual_HSE_ready_done/outputs/images
zip -q -r rm_residual_HSE_ready_done.zip rm_residual_HSE_ready_done
rm -rf rm_residual_HSE_ready_done


##### rm_residual_MSE_ready #####
unzip -q rm_residual_MSE_ready.zip
cd rm_residual_MSE_ready
python3 train.py
cd ../

cp -r  rm_residual_MSE_ready rm_residual_MSE_ready_done
rm -rf rm_residual_MSE_ready_done/outputs/images
zip -q -r rm_residual_MSE_ready_done.zip rm_residual_MSE_ready_done
rm -rf rm_residual_MSE_ready_done

##### rm_cat_rdball_HSE_ready #####
unzip -q rm_cat_rdball_HSE_ready.zip
cd rm_cat_rdball_HSE_ready
python3 train.py
cd ../

cp -r  rm_cat_rdball_HSE_ready rm_cat_rdball_HSE_ready_done
rm -rf rm_cat_rdball_HSE_ready_done/outputs/images
zip -q -r rm_cat_rdball_HSE_ready_done.zip rm_cat_rdball_HSE_ready_done
rm -rf rm_cat_rdball_HSE_ready_done

##### rm_shuffling_ready #####
unzip -q rm_shuffling_ready.zip
cd rm_shuffling_ready
python3 train.py
cd ../

cp -r  rm_shuffling_ready rm_shuffling_ready_done
rm -rf rm_shuffling_ready_done/outputs/images
zip -q -r rm_shuffling_ready_done.zip rm_shuffling_ready_done
rm -rf rm_shuffling_ready_done

