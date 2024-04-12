export CUDA_VISIBLE_DEVICES=3

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify0 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify0 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify1 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify1 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify2 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify2 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify3 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify3 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify4 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify4 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify5 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify5 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify6 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify6 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify7 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify7 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify8 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify8 2>&1 &

nohup python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/360_video_viewing_dataset/transfer_10_10 \
  --model_id UserIdentify9 \
  --model TimesNet \
  --data UEA \
  --e_layers 2 \
  --batch_size 16 \
  --d_model 32 \
  --d_ff 32 \
  --top_k 2 \
  --des 'Exp' \
  --itr 1 \
  --learning_rate 0.001 \
  --train_epochs 30 \
  --patience 10 \
  > dataset1_UserIdentify9 2>&1 &
