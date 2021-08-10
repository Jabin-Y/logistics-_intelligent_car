python3 paddleocr.py --image_dir=./imgs/$1 \
 --det_model_dir=./inference/ch_ppocr_mobile_v2.0_det_infer/ \
 --rec_model_dir=./inference/ch_ppocr_mobile_v2.0_rec_infer/ \
 --cls_model_dir=./inference/ch_ppocr_mobile_v2.0_cls_infer/  \
 --use_angle_cls=True --use_space_char=True
