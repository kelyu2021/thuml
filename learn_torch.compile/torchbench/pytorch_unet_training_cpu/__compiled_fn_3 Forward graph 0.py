from __future__ import annotations



def forward(self, primals_1: "f32[64, 3, 3, 3]", primals_2: "f32[64]", primals_3: "f32[64]", primals_4: "f32[64]", primals_5: "f32[64, 64, 3, 3]", primals_6: "f32[64]", primals_7: "f32[64]", primals_8: "f32[64]", primals_9: "f32[128, 64, 3, 3]", primals_10: "f32[128]", primals_11: "f32[128]", primals_12: "f32[128]", primals_13: "f32[128, 128, 3, 3]", primals_14: "f32[128]", primals_15: "f32[128]", primals_16: "f32[128]", primals_17: "f32[256, 128, 3, 3]", primals_18: "f32[256]", primals_19: "f32[256]", primals_20: "f32[256]", primals_21: "f32[256, 256, 3, 3]", primals_22: "f32[256]", primals_23: "f32[256]", primals_24: "f32[256]", primals_25: "f32[512, 256, 3, 3]", primals_26: "f32[512]", primals_27: "f32[512]", primals_28: "f32[512]", primals_29: "f32[512, 512, 3, 3]", primals_30: "f32[512]", primals_31: "f32[512]", primals_32: "f32[512]", primals_33: "f32[512, 512, 3, 3]", primals_34: "f32[512]", primals_35: "f32[512]", primals_36: "f32[512]", primals_37: "f32[512, 512, 3, 3]", primals_38: "f32[512]", primals_39: "f32[512]", primals_40: "f32[512]", primals_41: "f32[512, 1024, 3, 3]", primals_42: "f32[512]", primals_43: "f32[512]", primals_44: "f32[512]", primals_45: "f32[256, 512, 3, 3]", primals_46: "f32[256]", primals_47: "f32[256]", primals_48: "f32[256]", primals_49: "f32[256, 512, 3, 3]", primals_50: "f32[256]", primals_51: "f32[256]", primals_52: "f32[256]", primals_53: "f32[128, 256, 3, 3]", primals_54: "f32[128]", primals_55: "f32[128]", primals_56: "f32[128]", primals_57: "f32[128, 256, 3, 3]", primals_58: "f32[128]", primals_59: "f32[128]", primals_60: "f32[128]", primals_61: "f32[64, 128, 3, 3]", primals_62: "f32[64]", primals_63: "f32[64]", primals_64: "f32[64]", primals_65: "f32[64, 128, 3, 3]", primals_66: "f32[64]", primals_67: "f32[64]", primals_68: "f32[64]", primals_69: "f32[64, 64, 3, 3]", primals_70: "f32[64]", primals_71: "f32[64]", primals_72: "f32[64]", primals_73: "f32[2, 64, 1, 1]", primals_74: "f32[2]", primals_75: "f32[64]", primals_76: "f32[64]", primals_77: "i64[]", primals_78: "f32[64]", primals_79: "f32[64]", primals_80: "i64[]", primals_81: "f32[128]", primals_82: "f32[128]", primals_83: "i64[]", primals_84: "f32[128]", primals_85: "f32[128]", primals_86: "i64[]", primals_87: "f32[256]", primals_88: "f32[256]", primals_89: "i64[]", primals_90: "f32[256]", primals_91: "f32[256]", primals_92: "i64[]", primals_93: "f32[512]", primals_94: "f32[512]", primals_95: "i64[]", primals_96: "f32[512]", primals_97: "f32[512]", primals_98: "i64[]", primals_99: "f32[512]", primals_100: "f32[512]", primals_101: "i64[]", primals_102: "f32[512]", primals_103: "f32[512]", primals_104: "i64[]", primals_105: "f32[512]", primals_106: "f32[512]", primals_107: "i64[]", primals_108: "f32[256]", primals_109: "f32[256]", primals_110: "i64[]", primals_111: "f32[256]", primals_112: "f32[256]", primals_113: "i64[]", primals_114: "f32[128]", primals_115: "f32[128]", primals_116: "i64[]", primals_117: "f32[128]", primals_118: "f32[128]", primals_119: "i64[]", primals_120: "f32[64]", primals_121: "f32[64]", primals_122: "i64[]", primals_123: "f32[64]", primals_124: "f32[64]", primals_125: "i64[]", primals_126: "f32[64]", primals_127: "f32[64]", primals_128: "i64[]", primals_129: "f32[2, 3, 640, 959]"):
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution: "f32[2, 64, 640, 959]" = torch.ops.aten.convolution.default(primals_129, primals_1, primals_2, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_2 = None
    convert_element_type: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_75, torch.float32)
    convert_element_type_1: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_76, torch.float32)
    add: "f32[64]" = torch.ops.aten.add.Tensor(convert_element_type_1, 1e-05);  convert_element_type_1 = None
    sqrt: "f32[64]" = torch.ops.aten.sqrt.default(add);  add = None
    reciprocal: "f32[64]" = torch.ops.aten.reciprocal.default(sqrt);  sqrt = None
    mul: "f32[64]" = torch.ops.aten.mul.Tensor(reciprocal, 1);  reciprocal = None
    unsqueeze: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type, -1);  convert_element_type = None
    unsqueeze_1: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze, -1);  unsqueeze = None
    unsqueeze_2: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(mul, -1);  mul = None
    unsqueeze_3: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_2, -1);  unsqueeze_2 = None
    sub: "f32[2, 64, 640, 959]" = torch.ops.aten.sub.Tensor(convolution, unsqueeze_1);  unsqueeze_1 = None
    mul_1: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(sub, unsqueeze_3);  sub = unsqueeze_3 = None
    unsqueeze_4: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_3, -1)
    unsqueeze_5: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_4, -1);  unsqueeze_4 = None
    mul_2: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(mul_1, unsqueeze_5);  mul_1 = unsqueeze_5 = None
    unsqueeze_6: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_4, -1);  primals_4 = None
    unsqueeze_7: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_6, -1);  unsqueeze_6 = None
    add_1: "f32[2, 64, 640, 959]" = torch.ops.aten.add.Tensor(mul_2, unsqueeze_7);  mul_2 = unsqueeze_7 = None
    relu: "f32[2, 64, 640, 959]" = torch.ops.aten.relu.default(add_1);  add_1 = None
    convolution_1: "f32[2, 64, 640, 959]" = torch.ops.aten.convolution.default(relu, primals_5, primals_6, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_6 = None
    convert_element_type_2: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_78, torch.float32)
    convert_element_type_3: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_79, torch.float32)
    add_2: "f32[64]" = torch.ops.aten.add.Tensor(convert_element_type_3, 1e-05);  convert_element_type_3 = None
    sqrt_1: "f32[64]" = torch.ops.aten.sqrt.default(add_2);  add_2 = None
    reciprocal_1: "f32[64]" = torch.ops.aten.reciprocal.default(sqrt_1);  sqrt_1 = None
    mul_3: "f32[64]" = torch.ops.aten.mul.Tensor(reciprocal_1, 1);  reciprocal_1 = None
    unsqueeze_8: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_2, -1);  convert_element_type_2 = None
    unsqueeze_9: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_8, -1);  unsqueeze_8 = None
    unsqueeze_10: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(mul_3, -1);  mul_3 = None
    unsqueeze_11: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_10, -1);  unsqueeze_10 = None
    sub_1: "f32[2, 64, 640, 959]" = torch.ops.aten.sub.Tensor(convolution_1, unsqueeze_9);  unsqueeze_9 = None
    mul_4: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(sub_1, unsqueeze_11);  sub_1 = unsqueeze_11 = None
    unsqueeze_12: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_7, -1)
    unsqueeze_13: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_12, -1);  unsqueeze_12 = None
    mul_5: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(mul_4, unsqueeze_13);  mul_4 = unsqueeze_13 = None
    unsqueeze_14: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_8, -1);  primals_8 = None
    unsqueeze_15: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_14, -1);  unsqueeze_14 = None
    add_3: "f32[2, 64, 640, 959]" = torch.ops.aten.add.Tensor(mul_5, unsqueeze_15);  mul_5 = unsqueeze_15 = None
    relu_1: "f32[2, 64, 640, 959]" = torch.ops.aten.relu.default(add_3);  add_3 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:39, code: return self.maxpool_conv(x)
    max_pool2d_with_indices = torch.ops.aten.max_pool2d_with_indices.default(relu_1, [2, 2], [2, 2])
    getitem: "f32[2, 64, 320, 479]" = max_pool2d_with_indices[0]
    getitem_1: "i64[2, 64, 320, 479]" = max_pool2d_with_indices[1];  max_pool2d_with_indices = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_2: "f32[2, 128, 320, 479]" = torch.ops.aten.convolution.default(getitem, primals_9, primals_10, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_10 = None
    convert_element_type_4: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_81, torch.float32)
    convert_element_type_5: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_82, torch.float32)
    add_4: "f32[128]" = torch.ops.aten.add.Tensor(convert_element_type_5, 1e-05);  convert_element_type_5 = None
    sqrt_2: "f32[128]" = torch.ops.aten.sqrt.default(add_4);  add_4 = None
    reciprocal_2: "f32[128]" = torch.ops.aten.reciprocal.default(sqrt_2);  sqrt_2 = None
    mul_6: "f32[128]" = torch.ops.aten.mul.Tensor(reciprocal_2, 1);  reciprocal_2 = None
    unsqueeze_16: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_4, -1);  convert_element_type_4 = None
    unsqueeze_17: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_16, -1);  unsqueeze_16 = None
    unsqueeze_18: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(mul_6, -1);  mul_6 = None
    unsqueeze_19: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_18, -1);  unsqueeze_18 = None
    sub_2: "f32[2, 128, 320, 479]" = torch.ops.aten.sub.Tensor(convolution_2, unsqueeze_17);  unsqueeze_17 = None
    mul_7: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(sub_2, unsqueeze_19);  sub_2 = unsqueeze_19 = None
    unsqueeze_20: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_11, -1)
    unsqueeze_21: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_20, -1);  unsqueeze_20 = None
    mul_8: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(mul_7, unsqueeze_21);  mul_7 = unsqueeze_21 = None
    unsqueeze_22: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_12, -1);  primals_12 = None
    unsqueeze_23: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_22, -1);  unsqueeze_22 = None
    add_5: "f32[2, 128, 320, 479]" = torch.ops.aten.add.Tensor(mul_8, unsqueeze_23);  mul_8 = unsqueeze_23 = None
    relu_2: "f32[2, 128, 320, 479]" = torch.ops.aten.relu.default(add_5);  add_5 = None
    convolution_3: "f32[2, 128, 320, 479]" = torch.ops.aten.convolution.default(relu_2, primals_13, primals_14, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_14 = None
    convert_element_type_6: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_84, torch.float32)
    convert_element_type_7: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_85, torch.float32)
    add_6: "f32[128]" = torch.ops.aten.add.Tensor(convert_element_type_7, 1e-05);  convert_element_type_7 = None
    sqrt_3: "f32[128]" = torch.ops.aten.sqrt.default(add_6);  add_6 = None
    reciprocal_3: "f32[128]" = torch.ops.aten.reciprocal.default(sqrt_3);  sqrt_3 = None
    mul_9: "f32[128]" = torch.ops.aten.mul.Tensor(reciprocal_3, 1);  reciprocal_3 = None
    unsqueeze_24: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_6, -1);  convert_element_type_6 = None
    unsqueeze_25: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_24, -1);  unsqueeze_24 = None
    unsqueeze_26: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(mul_9, -1);  mul_9 = None
    unsqueeze_27: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_26, -1);  unsqueeze_26 = None
    sub_3: "f32[2, 128, 320, 479]" = torch.ops.aten.sub.Tensor(convolution_3, unsqueeze_25);  unsqueeze_25 = None
    mul_10: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(sub_3, unsqueeze_27);  sub_3 = unsqueeze_27 = None
    unsqueeze_28: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_15, -1)
    unsqueeze_29: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_28, -1);  unsqueeze_28 = None
    mul_11: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(mul_10, unsqueeze_29);  mul_10 = unsqueeze_29 = None
    unsqueeze_30: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_16, -1);  primals_16 = None
    unsqueeze_31: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_30, -1);  unsqueeze_30 = None
    add_7: "f32[2, 128, 320, 479]" = torch.ops.aten.add.Tensor(mul_11, unsqueeze_31);  mul_11 = unsqueeze_31 = None
    relu_3: "f32[2, 128, 320, 479]" = torch.ops.aten.relu.default(add_7);  add_7 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:39, code: return self.maxpool_conv(x)
    max_pool2d_with_indices_1 = torch.ops.aten.max_pool2d_with_indices.default(relu_3, [2, 2], [2, 2])
    getitem_2: "f32[2, 128, 160, 239]" = max_pool2d_with_indices_1[0]
    getitem_3: "i64[2, 128, 160, 239]" = max_pool2d_with_indices_1[1];  max_pool2d_with_indices_1 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_4: "f32[2, 256, 160, 239]" = torch.ops.aten.convolution.default(getitem_2, primals_17, primals_18, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_18 = None
    convert_element_type_8: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_87, torch.float32)
    convert_element_type_9: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_88, torch.float32)
    add_8: "f32[256]" = torch.ops.aten.add.Tensor(convert_element_type_9, 1e-05);  convert_element_type_9 = None
    sqrt_4: "f32[256]" = torch.ops.aten.sqrt.default(add_8);  add_8 = None
    reciprocal_4: "f32[256]" = torch.ops.aten.reciprocal.default(sqrt_4);  sqrt_4 = None
    mul_12: "f32[256]" = torch.ops.aten.mul.Tensor(reciprocal_4, 1);  reciprocal_4 = None
    unsqueeze_32: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_8, -1);  convert_element_type_8 = None
    unsqueeze_33: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_32, -1);  unsqueeze_32 = None
    unsqueeze_34: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(mul_12, -1);  mul_12 = None
    unsqueeze_35: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_34, -1);  unsqueeze_34 = None
    sub_4: "f32[2, 256, 160, 239]" = torch.ops.aten.sub.Tensor(convolution_4, unsqueeze_33);  unsqueeze_33 = None
    mul_13: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(sub_4, unsqueeze_35);  sub_4 = unsqueeze_35 = None
    unsqueeze_36: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_19, -1)
    unsqueeze_37: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_36, -1);  unsqueeze_36 = None
    mul_14: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(mul_13, unsqueeze_37);  mul_13 = unsqueeze_37 = None
    unsqueeze_38: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_20, -1);  primals_20 = None
    unsqueeze_39: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_38, -1);  unsqueeze_38 = None
    add_9: "f32[2, 256, 160, 239]" = torch.ops.aten.add.Tensor(mul_14, unsqueeze_39);  mul_14 = unsqueeze_39 = None
    relu_4: "f32[2, 256, 160, 239]" = torch.ops.aten.relu.default(add_9);  add_9 = None
    convolution_5: "f32[2, 256, 160, 239]" = torch.ops.aten.convolution.default(relu_4, primals_21, primals_22, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_22 = None
    convert_element_type_10: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_90, torch.float32)
    convert_element_type_11: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_91, torch.float32)
    add_10: "f32[256]" = torch.ops.aten.add.Tensor(convert_element_type_11, 1e-05);  convert_element_type_11 = None
    sqrt_5: "f32[256]" = torch.ops.aten.sqrt.default(add_10);  add_10 = None
    reciprocal_5: "f32[256]" = torch.ops.aten.reciprocal.default(sqrt_5);  sqrt_5 = None
    mul_15: "f32[256]" = torch.ops.aten.mul.Tensor(reciprocal_5, 1);  reciprocal_5 = None
    unsqueeze_40: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_10, -1);  convert_element_type_10 = None
    unsqueeze_41: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_40, -1);  unsqueeze_40 = None
    unsqueeze_42: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(mul_15, -1);  mul_15 = None
    unsqueeze_43: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_42, -1);  unsqueeze_42 = None
    sub_5: "f32[2, 256, 160, 239]" = torch.ops.aten.sub.Tensor(convolution_5, unsqueeze_41);  unsqueeze_41 = None
    mul_16: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(sub_5, unsqueeze_43);  sub_5 = unsqueeze_43 = None
    unsqueeze_44: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_23, -1)
    unsqueeze_45: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_44, -1);  unsqueeze_44 = None
    mul_17: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(mul_16, unsqueeze_45);  mul_16 = unsqueeze_45 = None
    unsqueeze_46: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_24, -1);  primals_24 = None
    unsqueeze_47: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_46, -1);  unsqueeze_46 = None
    add_11: "f32[2, 256, 160, 239]" = torch.ops.aten.add.Tensor(mul_17, unsqueeze_47);  mul_17 = unsqueeze_47 = None
    relu_5: "f32[2, 256, 160, 239]" = torch.ops.aten.relu.default(add_11);  add_11 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:39, code: return self.maxpool_conv(x)
    max_pool2d_with_indices_2 = torch.ops.aten.max_pool2d_with_indices.default(relu_5, [2, 2], [2, 2])
    getitem_4: "f32[2, 256, 80, 119]" = max_pool2d_with_indices_2[0]
    getitem_5: "i64[2, 256, 80, 119]" = max_pool2d_with_indices_2[1];  max_pool2d_with_indices_2 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_6: "f32[2, 512, 80, 119]" = torch.ops.aten.convolution.default(getitem_4, primals_25, primals_26, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_26 = None
    convert_element_type_12: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_93, torch.float32)
    convert_element_type_13: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_94, torch.float32)
    add_12: "f32[512]" = torch.ops.aten.add.Tensor(convert_element_type_13, 1e-05);  convert_element_type_13 = None
    sqrt_6: "f32[512]" = torch.ops.aten.sqrt.default(add_12);  add_12 = None
    reciprocal_6: "f32[512]" = torch.ops.aten.reciprocal.default(sqrt_6);  sqrt_6 = None
    mul_18: "f32[512]" = torch.ops.aten.mul.Tensor(reciprocal_6, 1);  reciprocal_6 = None
    unsqueeze_48: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_12, -1);  convert_element_type_12 = None
    unsqueeze_49: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_48, -1);  unsqueeze_48 = None
    unsqueeze_50: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(mul_18, -1);  mul_18 = None
    unsqueeze_51: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_50, -1);  unsqueeze_50 = None
    sub_6: "f32[2, 512, 80, 119]" = torch.ops.aten.sub.Tensor(convolution_6, unsqueeze_49);  unsqueeze_49 = None
    mul_19: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(sub_6, unsqueeze_51);  sub_6 = unsqueeze_51 = None
    unsqueeze_52: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_27, -1)
    unsqueeze_53: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_52, -1);  unsqueeze_52 = None
    mul_20: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(mul_19, unsqueeze_53);  mul_19 = unsqueeze_53 = None
    unsqueeze_54: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_28, -1);  primals_28 = None
    unsqueeze_55: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_54, -1);  unsqueeze_54 = None
    add_13: "f32[2, 512, 80, 119]" = torch.ops.aten.add.Tensor(mul_20, unsqueeze_55);  mul_20 = unsqueeze_55 = None
    relu_6: "f32[2, 512, 80, 119]" = torch.ops.aten.relu.default(add_13);  add_13 = None
    convolution_7: "f32[2, 512, 80, 119]" = torch.ops.aten.convolution.default(relu_6, primals_29, primals_30, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_30 = None
    convert_element_type_14: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_96, torch.float32)
    convert_element_type_15: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_97, torch.float32)
    add_14: "f32[512]" = torch.ops.aten.add.Tensor(convert_element_type_15, 1e-05);  convert_element_type_15 = None
    sqrt_7: "f32[512]" = torch.ops.aten.sqrt.default(add_14);  add_14 = None
    reciprocal_7: "f32[512]" = torch.ops.aten.reciprocal.default(sqrt_7);  sqrt_7 = None
    mul_21: "f32[512]" = torch.ops.aten.mul.Tensor(reciprocal_7, 1);  reciprocal_7 = None
    unsqueeze_56: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_14, -1);  convert_element_type_14 = None
    unsqueeze_57: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_56, -1);  unsqueeze_56 = None
    unsqueeze_58: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(mul_21, -1);  mul_21 = None
    unsqueeze_59: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_58, -1);  unsqueeze_58 = None
    sub_7: "f32[2, 512, 80, 119]" = torch.ops.aten.sub.Tensor(convolution_7, unsqueeze_57);  unsqueeze_57 = None
    mul_22: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(sub_7, unsqueeze_59);  sub_7 = unsqueeze_59 = None
    unsqueeze_60: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_31, -1)
    unsqueeze_61: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_60, -1);  unsqueeze_60 = None
    mul_23: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(mul_22, unsqueeze_61);  mul_22 = unsqueeze_61 = None
    unsqueeze_62: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_32, -1);  primals_32 = None
    unsqueeze_63: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_62, -1);  unsqueeze_62 = None
    add_15: "f32[2, 512, 80, 119]" = torch.ops.aten.add.Tensor(mul_23, unsqueeze_63);  mul_23 = unsqueeze_63 = None
    relu_7: "f32[2, 512, 80, 119]" = torch.ops.aten.relu.default(add_15);  add_15 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:39, code: return self.maxpool_conv(x)
    max_pool2d_with_indices_3 = torch.ops.aten.max_pool2d_with_indices.default(relu_7, [2, 2], [2, 2])
    getitem_6: "f32[2, 512, 40, 59]" = max_pool2d_with_indices_3[0]
    getitem_7: "i64[2, 512, 40, 59]" = max_pool2d_with_indices_3[1];  max_pool2d_with_indices_3 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_8: "f32[2, 512, 40, 59]" = torch.ops.aten.convolution.default(getitem_6, primals_33, primals_34, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_34 = None
    convert_element_type_16: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_99, torch.float32)
    convert_element_type_17: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_100, torch.float32)
    add_16: "f32[512]" = torch.ops.aten.add.Tensor(convert_element_type_17, 1e-05);  convert_element_type_17 = None
    sqrt_8: "f32[512]" = torch.ops.aten.sqrt.default(add_16);  add_16 = None
    reciprocal_8: "f32[512]" = torch.ops.aten.reciprocal.default(sqrt_8);  sqrt_8 = None
    mul_24: "f32[512]" = torch.ops.aten.mul.Tensor(reciprocal_8, 1);  reciprocal_8 = None
    unsqueeze_64: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_16, -1);  convert_element_type_16 = None
    unsqueeze_65: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_64, -1);  unsqueeze_64 = None
    unsqueeze_66: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(mul_24, -1);  mul_24 = None
    unsqueeze_67: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_66, -1);  unsqueeze_66 = None
    sub_8: "f32[2, 512, 40, 59]" = torch.ops.aten.sub.Tensor(convolution_8, unsqueeze_65);  unsqueeze_65 = None
    mul_25: "f32[2, 512, 40, 59]" = torch.ops.aten.mul.Tensor(sub_8, unsqueeze_67);  sub_8 = unsqueeze_67 = None
    unsqueeze_68: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_35, -1)
    unsqueeze_69: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_68, -1);  unsqueeze_68 = None
    mul_26: "f32[2, 512, 40, 59]" = torch.ops.aten.mul.Tensor(mul_25, unsqueeze_69);  mul_25 = unsqueeze_69 = None
    unsqueeze_70: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_36, -1);  primals_36 = None
    unsqueeze_71: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_70, -1);  unsqueeze_70 = None
    add_17: "f32[2, 512, 40, 59]" = torch.ops.aten.add.Tensor(mul_26, unsqueeze_71);  mul_26 = unsqueeze_71 = None
    relu_8: "f32[2, 512, 40, 59]" = torch.ops.aten.relu.default(add_17);  add_17 = None
    convolution_9: "f32[2, 512, 40, 59]" = torch.ops.aten.convolution.default(relu_8, primals_37, primals_38, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_38 = None
    convert_element_type_18: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_102, torch.float32)
    convert_element_type_19: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_103, torch.float32)
    add_18: "f32[512]" = torch.ops.aten.add.Tensor(convert_element_type_19, 1e-05);  convert_element_type_19 = None
    sqrt_9: "f32[512]" = torch.ops.aten.sqrt.default(add_18);  add_18 = None
    reciprocal_9: "f32[512]" = torch.ops.aten.reciprocal.default(sqrt_9);  sqrt_9 = None
    mul_27: "f32[512]" = torch.ops.aten.mul.Tensor(reciprocal_9, 1);  reciprocal_9 = None
    unsqueeze_72: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_18, -1);  convert_element_type_18 = None
    unsqueeze_73: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_72, -1);  unsqueeze_72 = None
    unsqueeze_74: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(mul_27, -1);  mul_27 = None
    unsqueeze_75: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_74, -1);  unsqueeze_74 = None
    sub_9: "f32[2, 512, 40, 59]" = torch.ops.aten.sub.Tensor(convolution_9, unsqueeze_73);  unsqueeze_73 = None
    mul_28: "f32[2, 512, 40, 59]" = torch.ops.aten.mul.Tensor(sub_9, unsqueeze_75);  sub_9 = unsqueeze_75 = None
    unsqueeze_76: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_39, -1)
    unsqueeze_77: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_76, -1);  unsqueeze_76 = None
    mul_29: "f32[2, 512, 40, 59]" = torch.ops.aten.mul.Tensor(mul_28, unsqueeze_77);  mul_28 = unsqueeze_77 = None
    unsqueeze_78: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_40, -1);  primals_40 = None
    unsqueeze_79: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_78, -1);  unsqueeze_78 = None
    add_19: "f32[2, 512, 40, 59]" = torch.ops.aten.add.Tensor(mul_29, unsqueeze_79);  mul_29 = unsqueeze_79 = None
    relu_9: "f32[2, 512, 40, 59]" = torch.ops.aten.relu.default(add_19);  add_19 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:57, code: x1 = self.up(x1)
    iota: "i64[80]" = torch.ops.prims.iota.default(80, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_20: "f64[80]" = torch.ops.prims.convert_element_type.default(iota, torch.float64);  iota = None
    mul_30: "f64[80]" = torch.ops.aten.mul.Tensor(convert_element_type_20, 1);  convert_element_type_20 = None
    add_20: "f64[80]" = torch.ops.aten.add.Tensor(mul_30, 0);  mul_30 = None
    convert_element_type_21: "f32[80]" = torch.ops.prims.convert_element_type.default(add_20, torch.float32);  add_20 = None
    iota_1: "i64[118]" = torch.ops.prims.iota.default(118, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_22: "f64[118]" = torch.ops.prims.convert_element_type.default(iota_1, torch.float64);  iota_1 = None
    mul_31: "f64[118]" = torch.ops.aten.mul.Tensor(convert_element_type_22, 1);  convert_element_type_22 = None
    add_21: "f64[118]" = torch.ops.aten.add.Tensor(mul_31, 0);  mul_31 = None
    convert_element_type_23: "f32[118]" = torch.ops.prims.convert_element_type.default(add_21, torch.float32);  add_21 = None
    mul_32: "f32[80]" = torch.ops.aten.mul.Tensor(convert_element_type_21, 0.4936708860759494);  convert_element_type_21 = None
    mul_33: "f32[118]" = torch.ops.aten.mul.Tensor(convert_element_type_23, 0.49572649572649574);  convert_element_type_23 = None
    convert_element_type_24: "i64[80]" = torch.ops.prims.convert_element_type.default(mul_32, torch.int64)
    ceil: "f32[80]" = torch.ops.aten.ceil.default(mul_32)
    clamp_max: "f32[80]" = torch.ops.aten.clamp_max.default(ceil, 39);  ceil = None
    convert_element_type_25: "i64[80]" = torch.ops.prims.convert_element_type.default(clamp_max, torch.int64);  clamp_max = None
    convert_element_type_26: "i64[118]" = torch.ops.prims.convert_element_type.default(mul_33, torch.int64)
    ceil_1: "f32[118]" = torch.ops.aten.ceil.default(mul_33)
    clamp_max_1: "f32[118]" = torch.ops.aten.clamp_max.default(ceil_1, 58);  ceil_1 = None
    convert_element_type_27: "i64[118]" = torch.ops.prims.convert_element_type.default(clamp_max_1, torch.int64);  clamp_max_1 = None
    unsqueeze_80: "f32[80, 1]" = torch.ops.aten.unsqueeze.default(mul_32, 1);  mul_32 = None
    unsqueeze_81: "i64[80, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_24, 1);  convert_element_type_24 = None
    unsqueeze_82: "i64[80, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_25, 1);  convert_element_type_25 = None
    _unsafe_index: "f32[2, 512, 80, 118]" = torch.ops.aten._unsafe_index.Tensor(relu_9, [None, None, unsqueeze_81, convert_element_type_26])
    _unsafe_index_1: "f32[2, 512, 80, 118]" = torch.ops.aten._unsafe_index.Tensor(relu_9, [None, None, unsqueeze_82, convert_element_type_26])
    _unsafe_index_2: "f32[2, 512, 80, 118]" = torch.ops.aten._unsafe_index.Tensor(relu_9, [None, None, unsqueeze_81, convert_element_type_27])
    _unsafe_index_3: "f32[2, 512, 80, 118]" = torch.ops.aten._unsafe_index.Tensor(relu_9, [None, None, unsqueeze_82, convert_element_type_27])
    sub_10: "f32[80, 1]" = torch.ops.aten.sub.Tensor(unsqueeze_80, unsqueeze_81);  unsqueeze_80 = None
    sub_11: "f32[80, 1]" = torch.ops.aten.sub.Tensor(1.0, sub_10)
    sub_12: "f32[118]" = torch.ops.aten.sub.Tensor(mul_33, convert_element_type_26);  mul_33 = None
    sub_13: "f32[118]" = torch.ops.aten.sub.Tensor(1.0, sub_12)
    mul_34: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(_unsafe_index, sub_11);  _unsafe_index = None
    mul_35: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(_unsafe_index_1, sub_10);  _unsafe_index_1 = None
    add_22: "f32[2, 512, 80, 118]" = torch.ops.aten.add.Tensor(mul_34, mul_35);  mul_34 = mul_35 = None
    mul_36: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(_unsafe_index_2, sub_11);  _unsafe_index_2 = sub_11 = None
    mul_37: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(_unsafe_index_3, sub_10);  _unsafe_index_3 = None
    add_23: "f32[2, 512, 80, 118]" = torch.ops.aten.add.Tensor(mul_36, mul_37);  mul_36 = mul_37 = None
    mul_38: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(add_22, sub_13);  add_22 = sub_13 = None
    mul_39: "f32[2, 512, 80, 118]" = torch.ops.aten.mul.Tensor(add_23, sub_12);  add_23 = None
    add_24: "f32[2, 512, 80, 118]" = torch.ops.aten.add.Tensor(mul_38, mul_39);  mul_38 = mul_39 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:62, code: x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
    constant_pad_nd: "f32[2, 512, 80, 119]" = torch.ops.aten.constant_pad_nd.default(add_24, [0, 1, 0, 0], 0.0);  add_24 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:67, code: x = torch.cat([x2, x1], dim=1)
    cat: "f32[2, 1024, 80, 119]" = torch.ops.aten.cat.default([relu_7, constant_pad_nd], 1);  constant_pad_nd = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_10: "f32[2, 512, 80, 119]" = torch.ops.aten.convolution.default(cat, primals_41, primals_42, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_42 = None
    convert_element_type_28: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_105, torch.float32)
    convert_element_type_29: "f32[512]" = torch.ops.prims.convert_element_type.default(primals_106, torch.float32)
    add_25: "f32[512]" = torch.ops.aten.add.Tensor(convert_element_type_29, 1e-05);  convert_element_type_29 = None
    sqrt_10: "f32[512]" = torch.ops.aten.sqrt.default(add_25);  add_25 = None
    reciprocal_10: "f32[512]" = torch.ops.aten.reciprocal.default(sqrt_10);  sqrt_10 = None
    mul_40: "f32[512]" = torch.ops.aten.mul.Tensor(reciprocal_10, 1);  reciprocal_10 = None
    unsqueeze_83: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_28, -1);  convert_element_type_28 = None
    unsqueeze_84: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_83, -1);  unsqueeze_83 = None
    unsqueeze_85: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(mul_40, -1);  mul_40 = None
    unsqueeze_86: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_85, -1);  unsqueeze_85 = None
    sub_14: "f32[2, 512, 80, 119]" = torch.ops.aten.sub.Tensor(convolution_10, unsqueeze_84);  unsqueeze_84 = None
    mul_41: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(sub_14, unsqueeze_86);  sub_14 = unsqueeze_86 = None
    unsqueeze_87: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_43, -1)
    unsqueeze_88: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_87, -1);  unsqueeze_87 = None
    mul_42: "f32[2, 512, 80, 119]" = torch.ops.aten.mul.Tensor(mul_41, unsqueeze_88);  mul_41 = unsqueeze_88 = None
    unsqueeze_89: "f32[512, 1]" = torch.ops.aten.unsqueeze.default(primals_44, -1);  primals_44 = None
    unsqueeze_90: "f32[512, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_89, -1);  unsqueeze_89 = None
    add_26: "f32[2, 512, 80, 119]" = torch.ops.aten.add.Tensor(mul_42, unsqueeze_90);  mul_42 = unsqueeze_90 = None
    relu_10: "f32[2, 512, 80, 119]" = torch.ops.aten.relu.default(add_26);  add_26 = None
    convolution_11: "f32[2, 256, 80, 119]" = torch.ops.aten.convolution.default(relu_10, primals_45, primals_46, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_46 = None
    convert_element_type_30: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_108, torch.float32)
    convert_element_type_31: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_109, torch.float32)
    add_27: "f32[256]" = torch.ops.aten.add.Tensor(convert_element_type_31, 1e-05);  convert_element_type_31 = None
    sqrt_11: "f32[256]" = torch.ops.aten.sqrt.default(add_27);  add_27 = None
    reciprocal_11: "f32[256]" = torch.ops.aten.reciprocal.default(sqrt_11);  sqrt_11 = None
    mul_43: "f32[256]" = torch.ops.aten.mul.Tensor(reciprocal_11, 1);  reciprocal_11 = None
    unsqueeze_91: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_30, -1);  convert_element_type_30 = None
    unsqueeze_92: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_91, -1);  unsqueeze_91 = None
    unsqueeze_93: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(mul_43, -1);  mul_43 = None
    unsqueeze_94: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_93, -1);  unsqueeze_93 = None
    sub_15: "f32[2, 256, 80, 119]" = torch.ops.aten.sub.Tensor(convolution_11, unsqueeze_92);  unsqueeze_92 = None
    mul_44: "f32[2, 256, 80, 119]" = torch.ops.aten.mul.Tensor(sub_15, unsqueeze_94);  sub_15 = unsqueeze_94 = None
    unsqueeze_95: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_47, -1)
    unsqueeze_96: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_95, -1);  unsqueeze_95 = None
    mul_45: "f32[2, 256, 80, 119]" = torch.ops.aten.mul.Tensor(mul_44, unsqueeze_96);  mul_44 = unsqueeze_96 = None
    unsqueeze_97: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_48, -1);  primals_48 = None
    unsqueeze_98: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_97, -1);  unsqueeze_97 = None
    add_28: "f32[2, 256, 80, 119]" = torch.ops.aten.add.Tensor(mul_45, unsqueeze_98);  mul_45 = unsqueeze_98 = None
    relu_11: "f32[2, 256, 80, 119]" = torch.ops.aten.relu.default(add_28);  add_28 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:57, code: x1 = self.up(x1)
    iota_2: "i64[160]" = torch.ops.prims.iota.default(160, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_32: "f64[160]" = torch.ops.prims.convert_element_type.default(iota_2, torch.float64);  iota_2 = None
    mul_46: "f64[160]" = torch.ops.aten.mul.Tensor(convert_element_type_32, 1);  convert_element_type_32 = None
    add_29: "f64[160]" = torch.ops.aten.add.Tensor(mul_46, 0);  mul_46 = None
    convert_element_type_33: "f32[160]" = torch.ops.prims.convert_element_type.default(add_29, torch.float32);  add_29 = None
    iota_3: "i64[238]" = torch.ops.prims.iota.default(238, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_34: "f64[238]" = torch.ops.prims.convert_element_type.default(iota_3, torch.float64);  iota_3 = None
    mul_47: "f64[238]" = torch.ops.aten.mul.Tensor(convert_element_type_34, 1);  convert_element_type_34 = None
    add_30: "f64[238]" = torch.ops.aten.add.Tensor(mul_47, 0);  mul_47 = None
    convert_element_type_35: "f32[238]" = torch.ops.prims.convert_element_type.default(add_30, torch.float32);  add_30 = None
    mul_48: "f32[160]" = torch.ops.aten.mul.Tensor(convert_element_type_33, 0.4968553459119497);  convert_element_type_33 = None
    mul_49: "f32[238]" = torch.ops.aten.mul.Tensor(convert_element_type_35, 0.4978902953586498);  convert_element_type_35 = None
    convert_element_type_36: "i64[160]" = torch.ops.prims.convert_element_type.default(mul_48, torch.int64)
    ceil_2: "f32[160]" = torch.ops.aten.ceil.default(mul_48)
    clamp_max_2: "f32[160]" = torch.ops.aten.clamp_max.default(ceil_2, 79);  ceil_2 = None
    convert_element_type_37: "i64[160]" = torch.ops.prims.convert_element_type.default(clamp_max_2, torch.int64);  clamp_max_2 = None
    convert_element_type_38: "i64[238]" = torch.ops.prims.convert_element_type.default(mul_49, torch.int64)
    ceil_3: "f32[238]" = torch.ops.aten.ceil.default(mul_49)
    clamp_max_3: "f32[238]" = torch.ops.aten.clamp_max.default(ceil_3, 118);  ceil_3 = None
    convert_element_type_39: "i64[238]" = torch.ops.prims.convert_element_type.default(clamp_max_3, torch.int64);  clamp_max_3 = None
    unsqueeze_99: "f32[160, 1]" = torch.ops.aten.unsqueeze.default(mul_48, 1);  mul_48 = None
    unsqueeze_100: "i64[160, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_36, 1);  convert_element_type_36 = None
    unsqueeze_101: "i64[160, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_37, 1);  convert_element_type_37 = None
    _unsafe_index_4: "f32[2, 256, 160, 238]" = torch.ops.aten._unsafe_index.Tensor(relu_11, [None, None, unsqueeze_100, convert_element_type_38])
    _unsafe_index_5: "f32[2, 256, 160, 238]" = torch.ops.aten._unsafe_index.Tensor(relu_11, [None, None, unsqueeze_101, convert_element_type_38])
    _unsafe_index_6: "f32[2, 256, 160, 238]" = torch.ops.aten._unsafe_index.Tensor(relu_11, [None, None, unsqueeze_100, convert_element_type_39])
    _unsafe_index_7: "f32[2, 256, 160, 238]" = torch.ops.aten._unsafe_index.Tensor(relu_11, [None, None, unsqueeze_101, convert_element_type_39])
    sub_16: "f32[160, 1]" = torch.ops.aten.sub.Tensor(unsqueeze_99, unsqueeze_100);  unsqueeze_99 = None
    sub_17: "f32[160, 1]" = torch.ops.aten.sub.Tensor(1.0, sub_16)
    sub_18: "f32[238]" = torch.ops.aten.sub.Tensor(mul_49, convert_element_type_38);  mul_49 = None
    sub_19: "f32[238]" = torch.ops.aten.sub.Tensor(1.0, sub_18)
    mul_50: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(_unsafe_index_4, sub_17);  _unsafe_index_4 = None
    mul_51: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(_unsafe_index_5, sub_16);  _unsafe_index_5 = None
    add_31: "f32[2, 256, 160, 238]" = torch.ops.aten.add.Tensor(mul_50, mul_51);  mul_50 = mul_51 = None
    mul_52: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(_unsafe_index_6, sub_17);  _unsafe_index_6 = sub_17 = None
    mul_53: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(_unsafe_index_7, sub_16);  _unsafe_index_7 = None
    add_32: "f32[2, 256, 160, 238]" = torch.ops.aten.add.Tensor(mul_52, mul_53);  mul_52 = mul_53 = None
    mul_54: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(add_31, sub_19);  add_31 = sub_19 = None
    mul_55: "f32[2, 256, 160, 238]" = torch.ops.aten.mul.Tensor(add_32, sub_18);  add_32 = None
    add_33: "f32[2, 256, 160, 238]" = torch.ops.aten.add.Tensor(mul_54, mul_55);  mul_54 = mul_55 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:62, code: x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
    constant_pad_nd_1: "f32[2, 256, 160, 239]" = torch.ops.aten.constant_pad_nd.default(add_33, [0, 1, 0, 0], 0.0);  add_33 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:67, code: x = torch.cat([x2, x1], dim=1)
    cat_1: "f32[2, 512, 160, 239]" = torch.ops.aten.cat.default([relu_5, constant_pad_nd_1], 1);  constant_pad_nd_1 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_12: "f32[2, 256, 160, 239]" = torch.ops.aten.convolution.default(cat_1, primals_49, primals_50, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_50 = None
    convert_element_type_40: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_111, torch.float32)
    convert_element_type_41: "f32[256]" = torch.ops.prims.convert_element_type.default(primals_112, torch.float32)
    add_34: "f32[256]" = torch.ops.aten.add.Tensor(convert_element_type_41, 1e-05);  convert_element_type_41 = None
    sqrt_12: "f32[256]" = torch.ops.aten.sqrt.default(add_34);  add_34 = None
    reciprocal_12: "f32[256]" = torch.ops.aten.reciprocal.default(sqrt_12);  sqrt_12 = None
    mul_56: "f32[256]" = torch.ops.aten.mul.Tensor(reciprocal_12, 1);  reciprocal_12 = None
    unsqueeze_102: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_40, -1);  convert_element_type_40 = None
    unsqueeze_103: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_102, -1);  unsqueeze_102 = None
    unsqueeze_104: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(mul_56, -1);  mul_56 = None
    unsqueeze_105: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_104, -1);  unsqueeze_104 = None
    sub_20: "f32[2, 256, 160, 239]" = torch.ops.aten.sub.Tensor(convolution_12, unsqueeze_103);  unsqueeze_103 = None
    mul_57: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(sub_20, unsqueeze_105);  sub_20 = unsqueeze_105 = None
    unsqueeze_106: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_51, -1)
    unsqueeze_107: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_106, -1);  unsqueeze_106 = None
    mul_58: "f32[2, 256, 160, 239]" = torch.ops.aten.mul.Tensor(mul_57, unsqueeze_107);  mul_57 = unsqueeze_107 = None
    unsqueeze_108: "f32[256, 1]" = torch.ops.aten.unsqueeze.default(primals_52, -1);  primals_52 = None
    unsqueeze_109: "f32[256, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_108, -1);  unsqueeze_108 = None
    add_35: "f32[2, 256, 160, 239]" = torch.ops.aten.add.Tensor(mul_58, unsqueeze_109);  mul_58 = unsqueeze_109 = None
    relu_12: "f32[2, 256, 160, 239]" = torch.ops.aten.relu.default(add_35);  add_35 = None
    convolution_13: "f32[2, 128, 160, 239]" = torch.ops.aten.convolution.default(relu_12, primals_53, primals_54, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_54 = None
    convert_element_type_42: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_114, torch.float32)
    convert_element_type_43: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_115, torch.float32)
    add_36: "f32[128]" = torch.ops.aten.add.Tensor(convert_element_type_43, 1e-05);  convert_element_type_43 = None
    sqrt_13: "f32[128]" = torch.ops.aten.sqrt.default(add_36);  add_36 = None
    reciprocal_13: "f32[128]" = torch.ops.aten.reciprocal.default(sqrt_13);  sqrt_13 = None
    mul_59: "f32[128]" = torch.ops.aten.mul.Tensor(reciprocal_13, 1);  reciprocal_13 = None
    unsqueeze_110: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_42, -1);  convert_element_type_42 = None
    unsqueeze_111: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_110, -1);  unsqueeze_110 = None
    unsqueeze_112: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(mul_59, -1);  mul_59 = None
    unsqueeze_113: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_112, -1);  unsqueeze_112 = None
    sub_21: "f32[2, 128, 160, 239]" = torch.ops.aten.sub.Tensor(convolution_13, unsqueeze_111);  unsqueeze_111 = None
    mul_60: "f32[2, 128, 160, 239]" = torch.ops.aten.mul.Tensor(sub_21, unsqueeze_113);  sub_21 = unsqueeze_113 = None
    unsqueeze_114: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_55, -1)
    unsqueeze_115: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_114, -1);  unsqueeze_114 = None
    mul_61: "f32[2, 128, 160, 239]" = torch.ops.aten.mul.Tensor(mul_60, unsqueeze_115);  mul_60 = unsqueeze_115 = None
    unsqueeze_116: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_56, -1);  primals_56 = None
    unsqueeze_117: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_116, -1);  unsqueeze_116 = None
    add_37: "f32[2, 128, 160, 239]" = torch.ops.aten.add.Tensor(mul_61, unsqueeze_117);  mul_61 = unsqueeze_117 = None
    relu_13: "f32[2, 128, 160, 239]" = torch.ops.aten.relu.default(add_37);  add_37 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:57, code: x1 = self.up(x1)
    iota_4: "i64[320]" = torch.ops.prims.iota.default(320, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_44: "f64[320]" = torch.ops.prims.convert_element_type.default(iota_4, torch.float64);  iota_4 = None
    mul_62: "f64[320]" = torch.ops.aten.mul.Tensor(convert_element_type_44, 1);  convert_element_type_44 = None
    add_38: "f64[320]" = torch.ops.aten.add.Tensor(mul_62, 0);  mul_62 = None
    convert_element_type_45: "f32[320]" = torch.ops.prims.convert_element_type.default(add_38, torch.float32);  add_38 = None
    iota_5: "i64[478]" = torch.ops.prims.iota.default(478, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_46: "f64[478]" = torch.ops.prims.convert_element_type.default(iota_5, torch.float64);  iota_5 = None
    mul_63: "f64[478]" = torch.ops.aten.mul.Tensor(convert_element_type_46, 1);  convert_element_type_46 = None
    add_39: "f64[478]" = torch.ops.aten.add.Tensor(mul_63, 0);  mul_63 = None
    convert_element_type_47: "f32[478]" = torch.ops.prims.convert_element_type.default(add_39, torch.float32);  add_39 = None
    mul_64: "f32[320]" = torch.ops.aten.mul.Tensor(convert_element_type_45, 0.49843260188087773);  convert_element_type_45 = None
    mul_65: "f32[478]" = torch.ops.aten.mul.Tensor(convert_element_type_47, 0.4989517819706499);  convert_element_type_47 = None
    convert_element_type_48: "i64[320]" = torch.ops.prims.convert_element_type.default(mul_64, torch.int64)
    ceil_4: "f32[320]" = torch.ops.aten.ceil.default(mul_64)
    clamp_max_4: "f32[320]" = torch.ops.aten.clamp_max.default(ceil_4, 159);  ceil_4 = None
    convert_element_type_49: "i64[320]" = torch.ops.prims.convert_element_type.default(clamp_max_4, torch.int64);  clamp_max_4 = None
    convert_element_type_50: "i64[478]" = torch.ops.prims.convert_element_type.default(mul_65, torch.int64)
    ceil_5: "f32[478]" = torch.ops.aten.ceil.default(mul_65)
    clamp_max_5: "f32[478]" = torch.ops.aten.clamp_max.default(ceil_5, 238);  ceil_5 = None
    convert_element_type_51: "i64[478]" = torch.ops.prims.convert_element_type.default(clamp_max_5, torch.int64);  clamp_max_5 = None
    unsqueeze_118: "f32[320, 1]" = torch.ops.aten.unsqueeze.default(mul_64, 1);  mul_64 = None
    unsqueeze_119: "i64[320, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_48, 1);  convert_element_type_48 = None
    unsqueeze_120: "i64[320, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_49, 1);  convert_element_type_49 = None
    _unsafe_index_8: "f32[2, 128, 320, 478]" = torch.ops.aten._unsafe_index.Tensor(relu_13, [None, None, unsqueeze_119, convert_element_type_50])
    _unsafe_index_9: "f32[2, 128, 320, 478]" = torch.ops.aten._unsafe_index.Tensor(relu_13, [None, None, unsqueeze_120, convert_element_type_50])
    _unsafe_index_10: "f32[2, 128, 320, 478]" = torch.ops.aten._unsafe_index.Tensor(relu_13, [None, None, unsqueeze_119, convert_element_type_51])
    _unsafe_index_11: "f32[2, 128, 320, 478]" = torch.ops.aten._unsafe_index.Tensor(relu_13, [None, None, unsqueeze_120, convert_element_type_51])
    sub_22: "f32[320, 1]" = torch.ops.aten.sub.Tensor(unsqueeze_118, unsqueeze_119);  unsqueeze_118 = None
    sub_23: "f32[320, 1]" = torch.ops.aten.sub.Tensor(1.0, sub_22)
    sub_24: "f32[478]" = torch.ops.aten.sub.Tensor(mul_65, convert_element_type_50);  mul_65 = None
    sub_25: "f32[478]" = torch.ops.aten.sub.Tensor(1.0, sub_24)
    mul_66: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(_unsafe_index_8, sub_23);  _unsafe_index_8 = None
    mul_67: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(_unsafe_index_9, sub_22);  _unsafe_index_9 = None
    add_40: "f32[2, 128, 320, 478]" = torch.ops.aten.add.Tensor(mul_66, mul_67);  mul_66 = mul_67 = None
    mul_68: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(_unsafe_index_10, sub_23);  _unsafe_index_10 = sub_23 = None
    mul_69: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(_unsafe_index_11, sub_22);  _unsafe_index_11 = None
    add_41: "f32[2, 128, 320, 478]" = torch.ops.aten.add.Tensor(mul_68, mul_69);  mul_68 = mul_69 = None
    mul_70: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(add_40, sub_25);  add_40 = sub_25 = None
    mul_71: "f32[2, 128, 320, 478]" = torch.ops.aten.mul.Tensor(add_41, sub_24);  add_41 = None
    add_42: "f32[2, 128, 320, 478]" = torch.ops.aten.add.Tensor(mul_70, mul_71);  mul_70 = mul_71 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:62, code: x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
    constant_pad_nd_2: "f32[2, 128, 320, 479]" = torch.ops.aten.constant_pad_nd.default(add_42, [0, 1, 0, 0], 0.0);  add_42 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:67, code: x = torch.cat([x2, x1], dim=1)
    cat_2: "f32[2, 256, 320, 479]" = torch.ops.aten.cat.default([relu_3, constant_pad_nd_2], 1);  constant_pad_nd_2 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_14: "f32[2, 128, 320, 479]" = torch.ops.aten.convolution.default(cat_2, primals_57, primals_58, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_58 = None
    convert_element_type_52: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_117, torch.float32)
    convert_element_type_53: "f32[128]" = torch.ops.prims.convert_element_type.default(primals_118, torch.float32)
    add_43: "f32[128]" = torch.ops.aten.add.Tensor(convert_element_type_53, 1e-05);  convert_element_type_53 = None
    sqrt_14: "f32[128]" = torch.ops.aten.sqrt.default(add_43);  add_43 = None
    reciprocal_14: "f32[128]" = torch.ops.aten.reciprocal.default(sqrt_14);  sqrt_14 = None
    mul_72: "f32[128]" = torch.ops.aten.mul.Tensor(reciprocal_14, 1);  reciprocal_14 = None
    unsqueeze_121: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_52, -1);  convert_element_type_52 = None
    unsqueeze_122: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_121, -1);  unsqueeze_121 = None
    unsqueeze_123: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(mul_72, -1);  mul_72 = None
    unsqueeze_124: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_123, -1);  unsqueeze_123 = None
    sub_26: "f32[2, 128, 320, 479]" = torch.ops.aten.sub.Tensor(convolution_14, unsqueeze_122);  unsqueeze_122 = None
    mul_73: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(sub_26, unsqueeze_124);  sub_26 = unsqueeze_124 = None
    unsqueeze_125: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_59, -1)
    unsqueeze_126: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_125, -1);  unsqueeze_125 = None
    mul_74: "f32[2, 128, 320, 479]" = torch.ops.aten.mul.Tensor(mul_73, unsqueeze_126);  mul_73 = unsqueeze_126 = None
    unsqueeze_127: "f32[128, 1]" = torch.ops.aten.unsqueeze.default(primals_60, -1);  primals_60 = None
    unsqueeze_128: "f32[128, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_127, -1);  unsqueeze_127 = None
    add_44: "f32[2, 128, 320, 479]" = torch.ops.aten.add.Tensor(mul_74, unsqueeze_128);  mul_74 = unsqueeze_128 = None
    relu_14: "f32[2, 128, 320, 479]" = torch.ops.aten.relu.default(add_44);  add_44 = None
    convolution_15: "f32[2, 64, 320, 479]" = torch.ops.aten.convolution.default(relu_14, primals_61, primals_62, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_62 = None
    convert_element_type_54: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_120, torch.float32)
    convert_element_type_55: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_121, torch.float32)
    add_45: "f32[64]" = torch.ops.aten.add.Tensor(convert_element_type_55, 1e-05);  convert_element_type_55 = None
    sqrt_15: "f32[64]" = torch.ops.aten.sqrt.default(add_45);  add_45 = None
    reciprocal_15: "f32[64]" = torch.ops.aten.reciprocal.default(sqrt_15);  sqrt_15 = None
    mul_75: "f32[64]" = torch.ops.aten.mul.Tensor(reciprocal_15, 1);  reciprocal_15 = None
    unsqueeze_129: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_54, -1);  convert_element_type_54 = None
    unsqueeze_130: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_129, -1);  unsqueeze_129 = None
    unsqueeze_131: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(mul_75, -1);  mul_75 = None
    unsqueeze_132: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_131, -1);  unsqueeze_131 = None
    sub_27: "f32[2, 64, 320, 479]" = torch.ops.aten.sub.Tensor(convolution_15, unsqueeze_130);  unsqueeze_130 = None
    mul_76: "f32[2, 64, 320, 479]" = torch.ops.aten.mul.Tensor(sub_27, unsqueeze_132);  sub_27 = unsqueeze_132 = None
    unsqueeze_133: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_63, -1)
    unsqueeze_134: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_133, -1);  unsqueeze_133 = None
    mul_77: "f32[2, 64, 320, 479]" = torch.ops.aten.mul.Tensor(mul_76, unsqueeze_134);  mul_76 = unsqueeze_134 = None
    unsqueeze_135: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_64, -1);  primals_64 = None
    unsqueeze_136: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_135, -1);  unsqueeze_135 = None
    add_46: "f32[2, 64, 320, 479]" = torch.ops.aten.add.Tensor(mul_77, unsqueeze_136);  mul_77 = unsqueeze_136 = None
    relu_15: "f32[2, 64, 320, 479]" = torch.ops.aten.relu.default(add_46);  add_46 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:57, code: x1 = self.up(x1)
    iota_6: "i64[640]" = torch.ops.prims.iota.default(640, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_56: "f64[640]" = torch.ops.prims.convert_element_type.default(iota_6, torch.float64);  iota_6 = None
    mul_78: "f64[640]" = torch.ops.aten.mul.Tensor(convert_element_type_56, 1);  convert_element_type_56 = None
    add_47: "f64[640]" = torch.ops.aten.add.Tensor(mul_78, 0);  mul_78 = None
    convert_element_type_57: "f32[640]" = torch.ops.prims.convert_element_type.default(add_47, torch.float32);  add_47 = None
    iota_7: "i64[958]" = torch.ops.prims.iota.default(958, start = 0, step = 1, dtype = torch.int64, device = device(type='cpu'), requires_grad = False)
    convert_element_type_58: "f64[958]" = torch.ops.prims.convert_element_type.default(iota_7, torch.float64);  iota_7 = None
    mul_79: "f64[958]" = torch.ops.aten.mul.Tensor(convert_element_type_58, 1);  convert_element_type_58 = None
    add_48: "f64[958]" = torch.ops.aten.add.Tensor(mul_79, 0);  mul_79 = None
    convert_element_type_59: "f32[958]" = torch.ops.prims.convert_element_type.default(add_48, torch.float32);  add_48 = None
    mul_80: "f32[640]" = torch.ops.aten.mul.Tensor(convert_element_type_57, 0.49921752738654146);  convert_element_type_57 = None
    mul_81: "f32[958]" = torch.ops.aten.mul.Tensor(convert_element_type_59, 0.4994775339602926);  convert_element_type_59 = None
    convert_element_type_60: "i64[640]" = torch.ops.prims.convert_element_type.default(mul_80, torch.int64)
    ceil_6: "f32[640]" = torch.ops.aten.ceil.default(mul_80)
    clamp_max_6: "f32[640]" = torch.ops.aten.clamp_max.default(ceil_6, 319);  ceil_6 = None
    convert_element_type_61: "i64[640]" = torch.ops.prims.convert_element_type.default(clamp_max_6, torch.int64);  clamp_max_6 = None
    convert_element_type_62: "i64[958]" = torch.ops.prims.convert_element_type.default(mul_81, torch.int64)
    ceil_7: "f32[958]" = torch.ops.aten.ceil.default(mul_81)
    clamp_max_7: "f32[958]" = torch.ops.aten.clamp_max.default(ceil_7, 478);  ceil_7 = None
    convert_element_type_63: "i64[958]" = torch.ops.prims.convert_element_type.default(clamp_max_7, torch.int64);  clamp_max_7 = None
    unsqueeze_137: "f32[640, 1]" = torch.ops.aten.unsqueeze.default(mul_80, 1);  mul_80 = None
    unsqueeze_138: "i64[640, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_60, 1);  convert_element_type_60 = None
    unsqueeze_139: "i64[640, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_61, 1);  convert_element_type_61 = None
    _unsafe_index_12: "f32[2, 64, 640, 958]" = torch.ops.aten._unsafe_index.Tensor(relu_15, [None, None, unsqueeze_138, convert_element_type_62])
    _unsafe_index_13: "f32[2, 64, 640, 958]" = torch.ops.aten._unsafe_index.Tensor(relu_15, [None, None, unsqueeze_139, convert_element_type_62])
    _unsafe_index_14: "f32[2, 64, 640, 958]" = torch.ops.aten._unsafe_index.Tensor(relu_15, [None, None, unsqueeze_138, convert_element_type_63])
    _unsafe_index_15: "f32[2, 64, 640, 958]" = torch.ops.aten._unsafe_index.Tensor(relu_15, [None, None, unsqueeze_139, convert_element_type_63])
    sub_28: "f32[640, 1]" = torch.ops.aten.sub.Tensor(unsqueeze_137, unsqueeze_138);  unsqueeze_137 = None
    sub_29: "f32[640, 1]" = torch.ops.aten.sub.Tensor(1.0, sub_28)
    sub_30: "f32[958]" = torch.ops.aten.sub.Tensor(mul_81, convert_element_type_62);  mul_81 = None
    sub_31: "f32[958]" = torch.ops.aten.sub.Tensor(1.0, sub_30)
    mul_82: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(_unsafe_index_12, sub_29);  _unsafe_index_12 = None
    mul_83: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(_unsafe_index_13, sub_28);  _unsafe_index_13 = None
    add_49: "f32[2, 64, 640, 958]" = torch.ops.aten.add.Tensor(mul_82, mul_83);  mul_82 = mul_83 = None
    mul_84: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(_unsafe_index_14, sub_29);  _unsafe_index_14 = sub_29 = None
    mul_85: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(_unsafe_index_15, sub_28);  _unsafe_index_15 = None
    add_50: "f32[2, 64, 640, 958]" = torch.ops.aten.add.Tensor(mul_84, mul_85);  mul_84 = mul_85 = None
    mul_86: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(add_49, sub_31);  add_49 = sub_31 = None
    mul_87: "f32[2, 64, 640, 958]" = torch.ops.aten.mul.Tensor(add_50, sub_30);  add_50 = None
    add_51: "f32[2, 64, 640, 958]" = torch.ops.aten.add.Tensor(mul_86, mul_87);  mul_86 = mul_87 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:62, code: x1 = F.pad(x1, [diffX // 2, diffX - diffX // 2,
    constant_pad_nd_3: "f32[2, 64, 640, 959]" = torch.ops.aten.constant_pad_nd.default(add_51, [0, 1, 0, 0], 0.0);  add_51 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:67, code: x = torch.cat([x2, x1], dim=1)
    cat_3: "f32[2, 128, 640, 959]" = torch.ops.aten.cat.default([relu_1, constant_pad_nd_3], 1);  constant_pad_nd_3 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    convolution_16: "f32[2, 64, 640, 959]" = torch.ops.aten.convolution.default(cat_3, primals_65, primals_66, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_66 = None
    convert_element_type_64: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_123, torch.float32)
    convert_element_type_65: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_124, torch.float32)
    add_52: "f32[64]" = torch.ops.aten.add.Tensor(convert_element_type_65, 1e-05);  convert_element_type_65 = None
    sqrt_16: "f32[64]" = torch.ops.aten.sqrt.default(add_52);  add_52 = None
    reciprocal_16: "f32[64]" = torch.ops.aten.reciprocal.default(sqrt_16);  sqrt_16 = None
    mul_88: "f32[64]" = torch.ops.aten.mul.Tensor(reciprocal_16, 1);  reciprocal_16 = None
    unsqueeze_140: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_64, -1);  convert_element_type_64 = None
    unsqueeze_141: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_140, -1);  unsqueeze_140 = None
    unsqueeze_142: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(mul_88, -1);  mul_88 = None
    unsqueeze_143: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_142, -1);  unsqueeze_142 = None
    sub_32: "f32[2, 64, 640, 959]" = torch.ops.aten.sub.Tensor(convolution_16, unsqueeze_141);  unsqueeze_141 = None
    mul_89: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(sub_32, unsqueeze_143);  sub_32 = unsqueeze_143 = None
    unsqueeze_144: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_67, -1)
    unsqueeze_145: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_144, -1);  unsqueeze_144 = None
    mul_90: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(mul_89, unsqueeze_145);  mul_89 = unsqueeze_145 = None
    unsqueeze_146: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_68, -1);  primals_68 = None
    unsqueeze_147: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_146, -1);  unsqueeze_146 = None
    add_53: "f32[2, 64, 640, 959]" = torch.ops.aten.add.Tensor(mul_90, unsqueeze_147);  mul_90 = unsqueeze_147 = None
    relu_16: "f32[2, 64, 640, 959]" = torch.ops.aten.relu.default(add_53);  add_53 = None
    convolution_17: "f32[2, 64, 640, 959]" = torch.ops.aten.convolution.default(relu_16, primals_69, primals_70, [1, 1], [1, 1], [1, 1], False, [0, 0], 1);  primals_70 = None
    convert_element_type_66: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_126, torch.float32)
    convert_element_type_67: "f32[64]" = torch.ops.prims.convert_element_type.default(primals_127, torch.float32)
    add_54: "f32[64]" = torch.ops.aten.add.Tensor(convert_element_type_67, 1e-05);  convert_element_type_67 = None
    sqrt_17: "f32[64]" = torch.ops.aten.sqrt.default(add_54);  add_54 = None
    reciprocal_17: "f32[64]" = torch.ops.aten.reciprocal.default(sqrt_17);  sqrt_17 = None
    mul_91: "f32[64]" = torch.ops.aten.mul.Tensor(reciprocal_17, 1);  reciprocal_17 = None
    unsqueeze_148: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(convert_element_type_66, -1);  convert_element_type_66 = None
    unsqueeze_149: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_148, -1);  unsqueeze_148 = None
    unsqueeze_150: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(mul_91, -1);  mul_91 = None
    unsqueeze_151: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_150, -1);  unsqueeze_150 = None
    sub_33: "f32[2, 64, 640, 959]" = torch.ops.aten.sub.Tensor(convolution_17, unsqueeze_149);  unsqueeze_149 = None
    mul_92: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(sub_33, unsqueeze_151);  sub_33 = unsqueeze_151 = None
    unsqueeze_152: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_71, -1)
    unsqueeze_153: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_152, -1);  unsqueeze_152 = None
    mul_93: "f32[2, 64, 640, 959]" = torch.ops.aten.mul.Tensor(mul_92, unsqueeze_153);  mul_92 = unsqueeze_153 = None
    unsqueeze_154: "f32[64, 1]" = torch.ops.aten.unsqueeze.default(primals_72, -1);  primals_72 = None
    unsqueeze_155: "f32[64, 1, 1]" = torch.ops.aten.unsqueeze.default(unsqueeze_154, -1);  unsqueeze_154 = None
    add_55: "f32[2, 64, 640, 959]" = torch.ops.aten.add.Tensor(mul_93, unsqueeze_155);  mul_93 = unsqueeze_155 = None
    relu_17: "f32[2, 64, 640, 959]" = torch.ops.aten.relu.default(add_55);  add_55 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:77, code: return self.conv(x)
    convolution_18: "f32[2, 2, 640, 959]" = torch.ops.aten.convolution.default(relu_17, primals_73, primals_74, [1, 1], [0, 0], [1, 1], False, [0, 0], 1);  primals_74 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    alias_25: "f32[2, 64, 320, 479]" = torch.ops.aten.alias.default(relu_15);  relu_15 = None
    alias_26: "f32[2, 64, 320, 479]" = torch.ops.aten.alias.default(alias_25);  alias_25 = None
    le_2: "b8[2, 64, 320, 479]" = torch.ops.aten.le.Scalar(alias_26, 0);  alias_26 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    alias_31: "f32[2, 128, 160, 239]" = torch.ops.aten.alias.default(relu_13);  relu_13 = None
    alias_32: "f32[2, 128, 160, 239]" = torch.ops.aten.alias.default(alias_31);  alias_31 = None
    le_4: "b8[2, 128, 160, 239]" = torch.ops.aten.le.Scalar(alias_32, 0);  alias_32 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    alias_37: "f32[2, 256, 80, 119]" = torch.ops.aten.alias.default(relu_11);  relu_11 = None
    alias_38: "f32[2, 256, 80, 119]" = torch.ops.aten.alias.default(alias_37);  alias_37 = None
    le_6: "b8[2, 256, 80, 119]" = torch.ops.aten.le.Scalar(alias_38, 0);  alias_38 = None
    
    # File: /workspace/youkaichao/code/torchbenchmark/torchbenchmark/models/pytorch_unet/pytorch_unet/unet/unet_parts.py:25, code: return self.double_conv(x)
    alias_43: "f32[2, 512, 40, 59]" = torch.ops.aten.alias.default(relu_9);  relu_9 = None
    alias_44: "f32[2, 512, 40, 59]" = torch.ops.aten.alias.default(alias_43);  alias_43 = None
    le_8: "b8[2, 512, 40, 59]" = torch.ops.aten.le.Scalar(alias_44, 0);  alias_44 = None
    return [convolution_18, primals_1, primals_3, primals_5, primals_7, primals_9, primals_11, primals_13, primals_15, primals_17, primals_19, primals_21, primals_23, primals_25, primals_27, primals_29, primals_31, primals_33, primals_35, primals_37, primals_39, primals_41, primals_43, primals_45, primals_47, primals_49, primals_51, primals_53, primals_55, primals_57, primals_59, primals_61, primals_63, primals_65, primals_67, primals_69, primals_71, primals_73, primals_75, primals_76, primals_78, primals_79, primals_81, primals_82, primals_84, primals_85, primals_87, primals_88, primals_90, primals_91, primals_93, primals_94, primals_96, primals_97, primals_99, primals_100, primals_102, primals_103, primals_105, primals_106, primals_108, primals_109, primals_111, primals_112, primals_114, primals_115, primals_117, primals_118, primals_120, primals_121, primals_123, primals_124, primals_126, primals_127, primals_129, convolution, relu, convolution_1, relu_1, getitem, getitem_1, convolution_2, relu_2, convolution_3, relu_3, getitem_2, getitem_3, convolution_4, relu_4, convolution_5, relu_5, getitem_4, getitem_5, convolution_6, relu_6, convolution_7, relu_7, getitem_6, getitem_7, convolution_8, relu_8, convolution_9, convert_element_type_26, convert_element_type_27, unsqueeze_81, unsqueeze_82, sub_10, sub_12, cat, convolution_10, relu_10, convolution_11, convert_element_type_38, convert_element_type_39, unsqueeze_100, unsqueeze_101, sub_16, sub_18, cat_1, convolution_12, relu_12, convolution_13, convert_element_type_50, convert_element_type_51, unsqueeze_119, unsqueeze_120, sub_22, sub_24, cat_2, convolution_14, relu_14, convolution_15, convert_element_type_62, convert_element_type_63, unsqueeze_138, unsqueeze_139, sub_28, sub_30, cat_3, convolution_16, relu_16, convolution_17, relu_17, le_2, le_4, le_6, le_8]
    