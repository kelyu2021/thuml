from __future__ import annotations



def forward(self):
    # File: /workspace/youkaichao/miniconda3/envs/build_torch/lib/python3.10/site-packages/transformers/models/bart/modeling_bart.py:97, code: mask_cond = torch.arange(mask.size(-1), device=device)
    iota: "i64[1024]" = torch.ops.prims.iota.default(1024, start = 0, step = 1, dtype = torch.int64, device = device(type='cuda', index=0), requires_grad = False)
    
    # File: /workspace/youkaichao/miniconda3/envs/build_torch/lib/python3.10/site-packages/transformers/models/bart/modeling_bart.py:98, code: mask.masked_fill_(mask_cond < (mask_cond + 1).view(mask.size(-1), 1), 0)
    add: "i64[1024]" = torch.ops.aten.add.Tensor(iota, 1)
    view: "i64[1024, 1]" = torch.ops.aten.reshape.default(add, [1024, 1]);  add = None
    lt: "b8[1024, 1024]" = torch.ops.aten.lt.Tensor(iota, view);  iota = view = None
    full_default_1: "f32[]" = torch.ops.aten.full.default([], 0.0, dtype = torch.float32, layout = torch.strided, device = device(type='cuda', index=0), pin_memory = False)
    
    # File: /workspace/youkaichao/miniconda3/envs/build_torch/lib/python3.10/site-packages/transformers/models/bart/modeling_bart.py:96, code: mask = torch.full((tgt_len, tgt_len), torch.finfo(dtype).min, device=device)
    full_default: "f32[1024, 1024]" = torch.ops.aten.full.default([1024, 1024], -3.4028234663852886e+38, dtype = torch.float32, layout = torch.strided, device = device(type='cuda', index=0), pin_memory = False)
    
    # File: /workspace/youkaichao/miniconda3/envs/build_torch/lib/python3.10/site-packages/transformers/models/bart/modeling_bart.py:98, code: mask.masked_fill_(mask_cond < (mask_cond + 1).view(mask.size(-1), 1), 0)
    where: "f32[1024, 1024]" = torch.ops.aten.where.self(lt, full_default_1, full_default);  lt = full_default_1 = full_default = None
    
    # No stacktrace found for following nodes
    unsqueeze_2: "f32[1, 1024, 1024]" = torch.ops.aten.unsqueeze.default(where, 0);  where = None
    unsqueeze_3: "f32[1, 1, 1024, 1024]" = torch.ops.aten.unsqueeze.default(unsqueeze_2, 1);  unsqueeze_2 = None
    slice_3: "f32[1, 1, 1024, 1024]" = torch.ops.aten.slice.Tensor(unsqueeze_3, 2, 0, 9223372036854775807);  unsqueeze_3 = None
    slice_4: "f32[1, 1, 1024, 1024]" = torch.ops.aten.slice.Tensor(slice_3, 3, 0, 9223372036854775807);  slice_3 = None
    expand_1: "f32[1, 1, 1024, 1024]" = torch.ops.aten.expand.default(slice_4, [1, 1, 1024, 1024]);  slice_4 = None
    return (expand_1,)
    