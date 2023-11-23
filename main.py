import gradio as gr
from transformers import pipeline

translation_pipeline = pipeline('translation_en_to_de')
results = translation_pipeline('I love programming')
results[0]['translation_text']


def translate_transformers(from_text):
    results = translation_pipeline(from_text)
    return results[0]['translation_text']

translate_transformers('My name is Victor')


interface = gr.Interface(fn=translate_transformers,
                         inputs=gr.Textbox(lines=2, placeholder='Text to translate'),
                        outputs='text')

interface.launch()


