from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)


def finish_sentence(sentence, max_length):
    input_ids = tokenizer.encode(sentence, return_tensors="pt")

    generator = model.generate(
        input_ids, max_length, num_beams=5, no_repeat_ngram_size=2, early_stopping=True
    )

    return tokenizer.decode(generator[0], skip_special_tokens=True)
