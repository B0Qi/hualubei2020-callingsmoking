

cfg = {
    "model_name": "adv-efficientnet-b4",
    #adv-efficientnet-b2 se_resnext50_32x4d  xception resnext101_32x8d_wsl
    "img_size": 600,
    'GPU_ID': '0',
    "class_number": 4,
    'mode': '-mutillabel',
    #train
    'batch_size':5,
    'early_stop_patient':26,
    'learning_rate':0.0002,
    'epochs':35,
    'save_start_epoch':5,
    'train_path':"/media/qifubo/_data/cv_data/train",
    "k_flod":5,
    'optims':'Ranger',  #adam  SGD AdaBelief Ranger
    'schedu':'SGDR1', #default  SGDR1 2  CVPR   step1 2
    'use_warmup':0,
    'weight_decay' : 0.0001,
    'use_distill':0,
    'label_smooth':0,
    'model_path':None,
    'start_fold':0,
    #test
    'test_path':"/media/qifubo/_data/cv_data/test",#_resize_rotate
    'use_TTA':0,
    'test_batch_size': 4,
    #fixed
    "save_dir": "save",
    "random_seed":42,
    }
