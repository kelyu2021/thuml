
import triton
import triton.language as tl
from torch._inductor.ir import ReductionHint
from torch._inductor.ir import TileHint
from torch._inductor.triton_heuristics import AutotuneHint, pointwise
from torch._inductor.utils import instance_descriptor
from torch._inductor import triton_helpers

@pointwise(
    size_hints=[16777216], 
    filename=__file__,
    triton_meta={'signature': {0: '*fp32', 1: '*fp32', 2: '*fp32', 3: 'i32'}, 'device': 0, 'device_type': 'cuda', 'constants': {}, 'configs': [instance_descriptor(divisible_by_16=(0, 1, 2, 3), equal_to_1=(), ids_of_folded_args=(), divisible_by_8=(3,))]},
    inductor_meta={'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_constant_pad_nd_26', 'mutated_arg_names': []},
    min_elem_per_thread=0
)
@triton.jit
def triton_(in_ptr0, in_ptr1, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xnumel = 9437184
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x1 = (xindex // 512) % 512
    x2 = (xindex // 262144) % 3
    x3 = (xindex // 786432)
    x4 = xindex % 262144
    x6 = xindex
    tmp0 = x1
    tmp1 = tl.full([1], 513, tl.int64)
    tmp2 = tmp0 < tmp1
    tmp3 = tl.load(in_ptr0 + (x4 + (262656*x2) + (787968*x3) + (787968*((x4 + (262656*x2)) // 787968))), tmp2, other=0.0)
    tmp4 = (x4 // 513)
    tmp5 = tl.full([1], 256, tl.int64)
    tmp6 = tmp4 < tmp5
    tmp7 = tmp6 & tmp2
    tmp8 = x4 % 513
    tmp9 = tl.full([1], 257, tl.int64)
    tmp10 = tmp8 < tmp9
    tmp11 = tmp10 & tmp7
    tmp12 = tl.load(in_ptr1 + (256 + x4 + (131328*x2) + (525312*x3) + (525312*((x4 + (262656*x2)) // 787968))), tmp11, other=0.0)
    tmp13 = tl.full(tmp12.shape, 0.0, tmp12.dtype)
    tmp14 = tl.where(tmp11, tmp12, tmp13)
    tmp15 = 0.0
    tmp16 = tl.where(tmp10, tmp14, tmp15)
    tmp17 = tl.full(tmp16.shape, 0.0, tmp16.dtype)
    tmp18 = tl.where(tmp7, tmp16, tmp17)
    tmp19 = tl.where(tmp6, tmp18, tmp15)
    tmp20 = tmp3 + tmp19
    tmp21 = tl.full(tmp20.shape, 0.0, tmp20.dtype)
    tmp22 = tl.where(tmp2, tmp20, tmp21)
    tl.store(out_ptr0 + (x6), tmp22, None)
