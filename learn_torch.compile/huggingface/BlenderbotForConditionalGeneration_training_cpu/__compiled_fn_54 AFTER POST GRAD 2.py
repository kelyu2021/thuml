from __future__ import annotations



def forward(self, iota: "i64[128]", tangents_1: "f32[128, 2560]"):
    # File: /workspace/youkaichao/code/pytorch/torch/nn/modules/sparse.py:163, code: return F.embedding(
    full_default: "b8[128, 1]" = torch.ops.aten.full.default([128, 1], False, dtype = torch.bool, layout = torch.strided, device = device(type='cpu'), pin_memory = False)
    full_default_1: "f32[]" = torch.ops.aten.full.default([], 0.0, dtype = torch.float32, layout = torch.strided, device = device(type='cpu'), pin_memory = False)
    where: "f32[128, 2560]" = torch.ops.aten.where.self(full_default, full_default_1, tangents_1);  full_default = full_default_1 = tangents_1 = None
    full_default_2: "f32[128, 2560]" = torch.ops.aten.full.default([128, 2560], 0, dtype = torch.float32, layout = torch.strided, device = device(type='cpu'), pin_memory = False)
    _unsafe_index_put: "f32[128, 2560]" = torch.ops.prims._unsafe_index_put_.default(full_default_2, [iota], where, True);  full_default_2 = iota = where = None
    return [_unsafe_index_put]
    