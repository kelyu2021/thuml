def __transformed_code_0_for_forward_pass(self, mod, inputs, collect_outputs):
    graph_out_0 = __compiled_fn_0(inputs[0], inputs[1])
    import importlib
    return importlib.import_module('transformers.modeling_outputs'
        ).Seq2SeqLMOutput(loss=None, logits=graph_out_0[0], past_key_values=((
        graph_out_0[1], graph_out_0[2], graph_out_0[3], graph_out_0[4]), (
        graph_out_0[5], graph_out_0[6], graph_out_0[7], graph_out_0[8]), (
        graph_out_0[9], graph_out_0[10], graph_out_0[11], graph_out_0[12]), (
        graph_out_0[13], graph_out_0[14], graph_out_0[15], graph_out_0[16]), (
        graph_out_0[17], graph_out_0[18], graph_out_0[19], graph_out_0[20]), (
        graph_out_0[21], graph_out_0[22], graph_out_0[23], graph_out_0[24])),
        decoder_hidden_states=None, decoder_attentions=None, cross_attentions=
        None, encoder_last_hidden_state=graph_out_0[25], encoder_hidden_states=
        None, encoder_attentions=None)
