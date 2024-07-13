import gradio as gr
from modules import scripts_postprocessing
from modules.ui_components import InputAccordion
from face_manipulation.main import process, alignImage



class FaceManipulationExtras(scripts_postprocessing.ScriptPostprocessing):
    name = "Face manipulation"
    order = 20500

    def ui(self):
        global METHODS
        with InputAccordion(False, label=self.name) as enable:
            selectedFactor = gr.Textbox(visible=False, value="age")
            with gr.Tabs():
                with gr.Tab("Age") as age:
                    ageChoice = gr.Radio(value="all", choices=["all", "kid", "teen", "adult", "old"], type="index", label="")
            includeOriginal = gr.Checkbox(value=True, label="Include aligned original")
        age.select(fn=lambda: "age", inputs=[], outputs=[selectedFactor])
        args = {
            'enable': enable,
            'selectedFactor': selectedFactor,
            'ageChoice': ageChoice,
            'includeOriginal': includeOriginal,
        }
        return args


    def process(self, pp: scripts_postprocessing.PostprocessedImage, **args):
        if args['enable'] == False:
            return
        results = []

        factor = args['selectedFactor'].lower()
        choice = 0
        if factor == 'age':
            choice = args['ageChoice']
        index = None
        if choice > 0:
            index = choice - 1

        for face in alignImage(pp.image):
            if args['includeOriginal']:
                results.append(face)
            processed = process(face, 'age', index)
            results.extend(processed)

        if not results:
            pp.info[self.name] = "faces weren't detected"
            return

        pp.image = results[0]
        if len(results) > 1:
            pp.extra_images.extend(results[1:])

        pp.info[self.name] = "age: all"

