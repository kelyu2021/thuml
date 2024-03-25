def __transformed_code_0_for_resume_in_forward(___stack0, self, labels, return_dict):
    attention_mask = None; global_attention_mask = None; head_mask = None; input_ids = None; inputs_embeds = None; loss_fct = None; masked_lm_loss = None; output = None; output_attentions = None; output_hidden_states = None; outputs = None; position_ids = None; prediction_scores = None; sequence_output = None; token_type_ids = None # this line helps the compiler to generate bytecode with at least the same number of local variables as the original function

    graph_out_0 = __compiled_fn_11(___stack0.last_hidden_state, labels)
    import importlib
    return importlib.import_module(
        'transformers.models.longformer.modeling_longformer'
        ).LongformerMaskedLMOutput(loss=graph_out_0[0], logits=graph_out_0[1],
        hidden_states=___stack0.hidden_states, attentions=___stack0.attentions,
        global_attentions=___stack0.global_attentions)
