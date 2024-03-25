python -u run.py \
  --is_training 1 \
  --root_path ./dataset/traffic/ \
  --data_path traffic.csv \
  --model_id traffic_96_48 \
  --model Koopa \
  --data custom \
  --features M \
  --seq_len 96 \
  --pred_len 48 \
  --seg_len 48 \
  --dynamic_dim 512 \
  --hidden_dim 256 \
  --hidden_layers 3 \
  --num_blocks 1 \
  --enc_in 862 \
  --dec_in 862 \
  --c_out 862 \
  --des 'Exp' \
  --learning_rate 0.001 \
  --itr 1 \
  --gpu 0

python -u run.py \
  --is_training 1 \
  --root_path ./dataset/traffic/ \
  --data_path traffic.csv \
  --model_id traffic_192_96 \
  --model Koopa \
  --data custom \
  --features M \
  --seq_len 192 \
  --pred_len 96 \
  --seg_len 96 \
  --dynamic_dim 64 \
  --hidden_dim 128 \
  --hidden_layers 2 \
  --num_blocks 3 \
  --enc_in 862 \
  --dec_in 862 \
  --c_out 862 \
  --des 'Exp' \
  --learning_rate 0.001 \
  --itr 1 \
  --gpu 0

python -u run.py \
  --is_training 1 \
  --root_path ./dataset/traffic/ \
  --data_path traffic.csv \
  --model_id traffic_288_144 \
  --model Koopa \
  --data custom \
  --features M \
  --seq_len 288 \
  --pred_len 144 \
  --seg_len 144 \
  --dynamic_dim 128 \
  --hidden_dim 128 \
  --hidden_layers 2 \
  --num_blocks 1 \
  --enc_in 862 \
  --dec_in 862 \
  --c_out 862 \
  --des 'Exp' \
  --learning_rate 0.001 \
  --itr 1 \
  --gpu 0

python -u run.py \
  --is_training 1 \
  --root_path ./dataset/traffic/ \
  --data_path traffic.csv \
  --model_id traffic_384_192 \
  --model Koopa \
  --data custom \
  --features M \
  --seq_len 384 \
  --pred_len 192 \
  --seg_len 192 \
  --dynamic_dim 128 \
  --hidden_dim 128 \
  --hidden_layers 2 \
  --num_blocks 1 \
  --enc_in 862 \
  --dec_in 862 \
  --c_out 862 \
  --des 'Exp' \
  --learning_rate 0.001 \
  --itr 1 \
  --gpu 0