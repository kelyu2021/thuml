export CUDA_VISIBLE_DEVICES=3

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10ps 

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10

python -u run.py \
  --task_name classification \
  --is_training 1 \
  --root_path ./dataset/UserBehaviorsInSphericalVideoStreaming/transfer_10_10 \
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
  --patience 10