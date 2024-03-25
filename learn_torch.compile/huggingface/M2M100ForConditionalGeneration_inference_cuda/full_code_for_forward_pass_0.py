
def __guard_0_for_forward_pass(L):
    return (___guarded_code.valid) \
        and (___check_global_state()) \
        and (___check_obj_id(L['mod'], 139649508490640)) \
        and (L['mod'].training == False) \
        and (___check_type_id(L['self'], 168531888)) \
        and (___check_type_id(L['inputs'], 7638432)) \
        and (set(L['inputs'].keys()) == {'input_ids', 'decoder_input_ids', 'labels'}) \
        and (___check_obj_id(L['self'].autocast, 37239888)) \
        and (hasattr(L['inputs']['labels'], '_dynamo_dynamic_indices') == False) \
        and (hasattr(L['inputs']['input_ids'], '_dynamo_dynamic_indices') == False) \
        and (hasattr(L['inputs']['decoder_input_ids'], '_dynamo_dynamic_indices') == False) \
        and (___check_obj_id(L['mod'].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[6], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[7], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[8], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[9], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[10], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[11], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[12], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[13], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[14], 7628576)) \
        and (___check_obj_id(L['mod'].forward.__defaults__[15], 7628576)) \
        and (utils_device.CURRENT_DEVICE == None) \
        and ((___skip_backend_check() or ___current_backend() == ___lookup_backend(139646233746960))) \
        and (___compile_config_hash() == 'ab4d4f7c17953a991f4d12459fb029be') \
        and (___check_obj_id(G['__import_transformers_dot_utils_dot_import_utils']._torch_available, 7677664)) \
        and (___check_type_id(G['__import_torch_dot_nn_dot_modules_dot_module']._global_forward_hooks, 7489504)) \
        and (set(G['__import_torch_dot_nn_dot_modules_dot_module']._global_forward_hooks.keys()) == set()) \
        and (___check_type_id(G['__import_torch_dot_nn_dot_modules_dot_module']._global_backward_hooks, 7489504)) \
        and (set(G['__import_torch_dot_nn_dot_modules_dot_module']._global_backward_hooks.keys()) == set()) \
        and (___check_obj_id(G['__import_transformers_dot_utils_dot_import_utils']._torch_fx_available, 7677664)) \
        and (___check_type_id(G['__import_torch_dot_nn_dot_modules_dot_module']._global_forward_pre_hooks, 7489504)) \
        and (set(G['__import_torch_dot_nn_dot_modules_dot_module']._global_forward_pre_hooks.keys()) == set()) \
        and (___check_type_id(G['__import_torch_dot_nn_dot_modules_dot_module']._global_backward_pre_hooks, 7489504)) \
        and (set(G['__import_torch_dot_nn_dot_modules_dot_module']._global_backward_pre_hooks.keys()) == set()) \
        and (___check_type_id(G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100'].torch.float16, 139651495786240)) \
        and (G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100'].torch.float16 == torch.float16) \
        and (___check_obj_id(G['__import_transformers_dot_integrations_dot_deepspeed']._hf_deepspeed_config_weak_ref, 7628576)) \
        and (___check_type_id(G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100']._make_causal_mask.__defaults__[0], 7640416)) \
        and (G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100']._make_causal_mask.__defaults__[0] == 0) \
        and (___check_type_id(G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100'].create_position_ids_from_input_ids.__defaults__[0], 7640416)) \
        and (G['__import_transformers_dot_models_dot_m2m_100_dot_modeling_m2m_100'].create_position_ids_from_input_ids.__defaults__[0] == 0) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[6], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[7], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[8], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[9], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[10], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[11], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[12], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[13], 7628576)) \
        and (___check_obj_id(L['mod'].model.forward.__defaults__[14], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[6], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[7], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[8], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[9], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.forward.__defaults__[6], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[10], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.forward.__defaults__[11], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[4], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[5], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[6], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].forward.__defaults__[7], 7677664)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].forward.__defaults__[0], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[0].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[1].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[2].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[3].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[4].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[5].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[6].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[7].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[8].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[9].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[10].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].self_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].self_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].self_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].self_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.layers[11].self_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[0].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[1].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[2].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[3].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[4].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[5].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[6].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[7].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[8].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[9].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[10].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].encoder_attn.forward.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].encoder_attn.forward.__defaults__[1], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].encoder_attn.forward.__defaults__[2], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].encoder_attn.forward.__defaults__[3], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.layers[11].encoder_attn.forward.__defaults__[4], 7677632)) \
        and (___check_obj_id(L['mod'].model.decoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.decoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[1], 7628576)) \
        and (___check_type_id(L['mod'].model.decoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[2], 7640416)) \
        and (L['mod'].model.decoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[2] == 0) \
        and (___check_obj_id(L['mod'].model.encoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[0], 7628576)) \
        and (___check_obj_id(L['mod'].model.encoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[1], 7628576)) \
        and (___check_type_id(L['mod'].model.encoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[2], 7640416)) \
        and (L['mod'].model.encoder.embed_positions.forward.__closure__[1].cell_contents.__defaults__[2] == 0) \
        and (___check_tensors(L['inputs']['labels'], L['inputs']['input_ids'], L['inputs']['decoder_input_ids'], tensor_check_names=tensor_check_names))

# Note: please refer to the graph code in __compiled_fn_0*.py.
# Captured Graph: Dynamo generated graph (debuggable when using eager backend).
# Joint graph: joint forward+backward graph from aot autograd.
# Forward graph: forward graph from aot autograd (debuggable when using aot_eager backend).
# Backward graph: backward graph from aot autograd (debuggable when using aot_eager backend).
# AFTER XXX: graph processed by inductor (not debuggable).
def __compiled_fn_0(*args, **kwargs):
    pass

def __transformed_code_0_for_forward_pass(self, mod, inputs, collect_outputs):
    graph_out_0 = __compiled_fn_0(inputs['labels'], inputs['decoder_input_ids'],
        inputs['input_ids'])
    import importlib
    return importlib.import_module('transformers.modeling_outputs'
        ).Seq2SeqLMOutput(loss=graph_out_0[0], logits=graph_out_0[1],
        past_key_values=((graph_out_0[2], graph_out_0[3], graph_out_0[4],
        graph_out_0[5]), (graph_out_0[6], graph_out_0[7], graph_out_0[8],
        graph_out_0[9]), (graph_out_0[10], graph_out_0[11], graph_out_0[12],
        graph_out_0[13]), (graph_out_0[14], graph_out_0[15], graph_out_0[16],
        graph_out_0[17]), (graph_out_0[18], graph_out_0[19], graph_out_0[20],
        graph_out_0[21]), (graph_out_0[22], graph_out_0[23], graph_out_0[24],
        graph_out_0[25]), (graph_out_0[26], graph_out_0[27], graph_out_0[28],
        graph_out_0[29]), (graph_out_0[30], graph_out_0[31], graph_out_0[32],
        graph_out_0[33]), (graph_out_0[34], graph_out_0[35], graph_out_0[36],
        graph_out_0[37]), (graph_out_0[38], graph_out_0[39], graph_out_0[40],
        graph_out_0[41]), (graph_out_0[42], graph_out_0[43], graph_out_0[44],
        graph_out_0[45]), (graph_out_0[46], graph_out_0[47], graph_out_0[48],
        graph_out_0[49])), decoder_hidden_states=None, decoder_attentions=None,
        cross_attentions=None, encoder_last_hidden_state=graph_out_0[50],
        encoder_hidden_states=None, encoder_attentions=None)


# Note: if there is a transformed version below, this function might well not be executed directly. Please check the transformed version if possible.
def forward_pass(self, mod, inputs, collect_outputs):
    with self.autocast() as __temp_8:
        __temp_10 = {}
        __temp_10.update(inputs)
        return mod(*(), **__temp_10)
    return None

def transformed_forward_pass(self, mod, inputs, collect_outputs):
    L = {"self": self, "mod": mod, "inputs": inputs, "collect_outputs": collect_outputs}
    if __guard_0_for_forward_pass(L):
        return __transformed_code_0_for_forward_pass(self, mod, inputs, collect_outputs)
    # Note: this function might well not be executed directly. It might well be transformed again, i.e. adding one more guards and transformed code.
    return forward_pass(self, mod, inputs, collect_outputs)

#============ end of forward_pass ============#
