##### useReLU6_ready #####

cd useReLU6_ready
python3 train.py
cd ../

cp -r  useReLU6_ready useReLU6_ready_done
rm -rf useReLU6_ready_done/outputs/images
zip -q -r useReLU6_ready_done.zip useReLU6_ready_done
rm -rf useReLU6_ready_done

##### rm_HSE_ready #####

cd rm_HSE_ready
python3 train.py
cd ../

cp -r  rm_HSE_ready rm_HSE_ready_done
rm -rf rm_HSE_ready_done/outputs/images
zip -q -r rm_HSE_ready_done.zip rm_HSE_ready_done
rm -rf rm_HSE_ready_done

##### rm_MSE_ready #####

cd rm_MSE_ready
python3 train.py
cd ../

cp -r  rm_MSE_ready rm_MSE_ready_done
rm -rf rm_MSE_ready_done/outputs/images
zip -q -r rm_MSE_ready_done.zip rm_MSE_ready_done
rm -rf rm_MSE_ready_done

##### rm_LSE_ready #####
cd rm_LSE_ready
python3 train.py
cd ../

cp -r  rm_LSE_ready rm_LSE_ready_done
rm -rf rm_LSE_ready_done/outputs/images
zip -q -r rm_LSE_ready_done.zip rm_LSE_ready_done
rm -rf rm_LSE_ready


##### growthr_16_ready #####

cd growthr_16_ready
python3 train.py
cd ../

cp -r  growthr_16_ready growthr_16_ready_done
rm -rf growthr_16_ready_done/outputs/images
zip -q -r growthr_16_ready_done.zip growthr_16_ready_done
rm -rf growthr_16_ready_done


##### 2RDB_ready #####

cd 2RDB_ready 
python3 train.py
cd ../

cp -r  2RDB_ready 2RDB_ready_done
rm -rf 2RDB_ready_done/outputs/images
zip -q -r 2RDB_ready_done.zip 2RDB_ready_done
rm -rf 2RDB_ready_done


##### 4RDB_ready #####

cd 4RDB_ready
python3 train.py
cd ../

cp -r  4RDB_ready 4RDB_ready_done
rm -rf 4RDB_ready_done/outputs/images
zip -q -r 4RDB_ready_done.zip 4RDB_ready_done
rm -rf 4RDB_ready_done
