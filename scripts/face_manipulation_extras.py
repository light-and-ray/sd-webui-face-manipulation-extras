import gradio as gr
from modules import scripts_postprocessing
from modules.ui_components import InputAccordion
from face_manipulation.main import process, alignImage

AGE = ["kid", "teen", "adult", "old"]
GENDER = ["male", "female"]
ETHNICITY = ["black", "white", "asian"]
HAIR = ["brunette", "blond", "bald", "red", "black", "white"]
BEARD = ["beard", "mustache", "goatee", "shaved"]
GLASSES = ["glasses", "shades", "no glasses"]

class FaceManipulationExtras(scripts_postprocessing.ScriptPostprocessing):
    name = "Face manipulation"
    order = 20500

    def ui(self):
        global METHODS
        with InputAccordion(False, label=self.name) as enable:
            selectedFactor = gr.Textbox(visible=False, value="age")
            with gr.Tabs():
                with gr.Tab("Age") as age:
                    ageChoice = gr.Radio(value="all", choices=["all"]+AGE, label="")

                with gr.Tab("Gender") as gender:
                    genderChoice = gr.Radio(value="all", choices=["all"]+GENDER, label="")

                with gr.Tab("Ethnicity") as ethnicity:
                    ethnicityChoice = gr.Radio(value="all", choices=["all"]+ETHNICITY, label="")

                with gr.Tab("Hair") as hair:
                    hairChoice = gr.Radio(value="all", choices=["all"]+HAIR, label="")

                with gr.Tab("Facial hair") as beard:
                    beardChoice = gr.Radio(value="all", choices=["all"]+BEARD, label="")

                with gr.Tab("Glasses") as glasses:
                    glassesChoice = gr.Radio(value="all", choices=["all"]+GLASSES, label="")

            includeOriginal = gr.Checkbox(value=True, label="Include aligned original")

        age.select(fn=lambda: "age", inputs=[], outputs=[selectedFactor])
        gender.select(fn=lambda: "gender", inputs=[], outputs=[selectedFactor])
        ethnicity.select(fn=lambda: "ethnicity", inputs=[], outputs=[selectedFactor])
        hair.select(fn=lambda: "hair_color", inputs=[], outputs=[selectedFactor])
        beard.select(fn=lambda: "beard", inputs=[], outputs=[selectedFactor])
        glasses.select(fn=lambda: "glasses", inputs=[], outputs=[selectedFactor])

        args = {
            'enable': enable,
            'selectedFactor': selectedFactor,
            'ageChoice': ageChoice,
            'genderChoice': genderChoice,
            'ethnicityChoice': ethnicityChoice,
            'hairChoice': hairChoice,
            'beardChoice': beardChoice,
            'glassesChoice': glassesChoice,
            'includeOriginal': includeOriginal,
        }
        return args


    def process(self, pp: scripts_postprocessing.PostprocessedImage, **args):
        if args['enable'] == False:
            return
        results = []

        factor = args['selectedFactor'].lower()

        choices = None
        choice = None
        if factor == 'age':
            choice = args['ageChoice']
            choices = AGE
        elif factor == 'gender':
            choice = args['genderChoice']
            choices = GENDER
        elif factor == 'ethnicity':
            choice = args['ethnicityChoice']
            choices = ETHNICITY
        elif factor == 'hair_color':
            choice = args['hairChoice']
            choices = HAIR
        elif factor == 'beard':
            choice = args['beardChoice']
            choices = BEARD
        elif factor == 'glasses':
            choice = args['glassesChoice']
            choices = GLASSES


        index = None
        if choice != "all":
            index = choices.index(choice)

        for face in alignImage(pp.image):
            if args['includeOriginal']:
                results.append(face)
            processed = process(face, factor, index)
            results.extend(processed)

        if not results:
            pp.info[self.name] = "faces weren't detected"
            return

        pp.image = results[0]
        if len(results) > 1:
            pp.extra_images.extend(results[1:])

        pp.info[self.name] = f"{factor}: {choice}"

