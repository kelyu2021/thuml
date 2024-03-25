
import triton
import triton.language as tl
from torch._inductor.ir import ReductionHint
from torch._inductor.ir import TileHint
from torch._inductor.triton_heuristics import AutotuneHint, pointwise
from torch._inductor.utils import instance_descriptor
from torch._inductor import triton_helpers

@pointwise(
    size_hints=[4194304], 
    filename=__file__,
    triton_meta={'signature': {0: '*fp32', 1: '*fp32', 2: '*fp32', 3: 'i32'}, 'device': 0, 'device_type': 'cuda', 'constants': {}, 'configs': [instance_descriptor(divisible_by_16=(0, 1, 2, 3), equal_to_1=(), ids_of_folded_args=(), divisible_by_8=(3,))]},
    inductor_meta={'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_mul_sum_15', 'mutated_arg_names': []},
    min_elem_per_thread=0
)
@triton.jit
def triton_(in_ptr0, in_ptr1, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xnumel = 4194304
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x2 = (xindex // 524288)
    x3 = xindex % 524288
    x1 = (xindex // 4096) % 128
    x4 = xindex
    tmp0 = tl.load(in_ptr0 + (x3 + (1048576*x2)), None)
    tmp1 = tl.load(in_ptr1 + (x1 + (256*x2)), None, eviction_policy='evict_last')
    tmp2 = tl.load(in_ptr1 + (128 + x1 + (256*x2)), None, eviction_policy='evict_last')
    tmp6 = tl.load(in_ptr0 + (524288 + x3 + (1048576*x2)), None)
    tmp3 = tmp1 + tmp2
    tmp4 = tmp1 / tmp3
    tmp5 = tmp0 * tmp4
    tmp7 = tmp2 / tmp3
    tmp8 = tmp6 * tmp7
    tmp9 = tmp5 + tmp8
    tl.store(out_ptr0 + (x4), tmp9, None)
