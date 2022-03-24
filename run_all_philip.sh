##### rm_residual_HSE_ready #####

cd rm_residual_HSE_ready
python3 train.py
cd ../

cp -r  rm_residual_HSE_ready rm_residual_HSE_ready_done
rm -rf rm_residual_HSE_ready_done/outputs/images
zip -q -r rm_residual_HSE_ready_done.zip rm_residual_HSE_ready_done
rm -rf rm_residual_HSE_ready_done


##### rm_residual_MSE_ready #####

cd rm_residual_MSE_ready
python3 train.py
cd ../

cp -r  rm_residual_MSE_ready rm_residual_MSE_ready_done
rm -rf rm_residual_MSE_ready_done/outputs/images
zip -q -r rm_residual_MSE_ready_done.zip rm_residual_MSE_ready_done
rm -rf rm_residual_MSE_ready_done

##### rm_cat_rdball_HSE_ready #####

cd rm_cat_rdball_HSE_ready
python3 train.py
cd ../

cp -r  rm_cat_rdball_HSE_ready rm_cat_rdball_HSE_ready_done
rm -rf rm_cat_rdball_HSE_ready_done/outputs/images
zip -q -r rm_cat_rdball_HSE_ready_done.zip rm_cat_rdball_HSE_ready_done
rm -rf rm_cat_rdball_HSE_ready_done


##### simple_fuse_20_ready #####

cd simple_fuse_20_ready
python3 train.py
cd ../

cp -r  simple_fuse_20_ready simple_fuse_20_ready_done
rm -rf simple_fuse_20_ready_done/outputs/images
zip -q -r simple_fuse_20_ready_done.zip simple_fuse_20_ready_done
rm -rf simple_fuse_20_ready_done

##### rm_shuffling_ready #####

cd rm_shuffling_ready
python3 train.py
cd ../

cp -r  rm_shuffling_ready rm_shuffling_ready_done
rm -rf rm_shuffling_ready_done/outputs/images
zip -q -r rm_shuffling_ready_done.zip rm_shuffling_ready_done
rm -rf rm_shuffling_ready_done


