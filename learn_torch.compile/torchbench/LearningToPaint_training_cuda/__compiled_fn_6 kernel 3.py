
import triton
import triton.language as tl
from torch._inductor.ir import ReductionHint
from torch._inductor.ir import TileHint
from torch._inductor.triton_heuristics import AutotuneHint, pointwise
from torch._inductor.utils import instance_descriptor
from torch._inductor import triton_helpers

@pointwise(
    size_hints=[32768], 
    filename=__file__,
    triton_meta={'signature': {0: '*fp32', 1: '*fp32', 2: '*fp32', 3: '*fp32', 4: '*fp32', 5: 'i32'}, 'device': 0, 'device_type': 'cuda', 'constants': {}, 'configs': [instance_descriptor(divisible_by_16=(0, 1, 2, 3, 4, 5), equal_to_1=(), ids_of_folded_args=(), divisible_by_8=(5,))]},
    inductor_meta={'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_avg_pool2d_backward_convolution_backward_native_batch_norm_backward_threshold_backward_2', 'mutated_arg_names': []},
    min_elem_per_thread=0
)
@triton.jit
def triton_(in_ptr0, in_ptr1, in_ptr2, in_ptr3, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xnumel = 32768
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x3 = xindex
    x0 = xindex % 512
    x2 = (xindex // 8192)
    tmp0 = tl.load(in_ptr0 + (x3), None)
    tmp3 = tl.load(in_ptr1 + (x0 + (512*x2)), None, eviction_policy='evict_last')
    tmp11 = tl.load(in_ptr2 + (x0), None, eviction_policy='evict_last')
    tmp15 = tl.load(in_ptr3 + (x0), None, eviction_policy='evict_last')
    tmp1 = 0.0
    tmp2 = tmp0 <= tmp1
    tmp4 = tmp3 / 16
    tmp5 = tl.full([1], 0, tl.int32)
    tmp6 = tl.full([1], 1, tl.int32)
    tmp7 = tmp5 < tmp6
    tmp8 = tmp7 & tmp7
    tmp9 = tl.where(tmp8, tmp4, tmp1)
    tmp10 = tl.where(tmp2, tmp1, tmp9)
    tmp12 = 1e-05
    tmp13 = tmp11 + tmp12
    tmp14 = tl.math.rsqrt(tmp13)
    tmp16 = tmp14 * tmp15
    tmp17 = tmp10 * tmp16
    tl.store(out_ptr0 + (x3), tmp17, None)
