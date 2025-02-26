import os
import google.generativeai as genai
from shiny import ui, reactive , render , App , run_app
from multiprocessing import Process, freeze_support
from dotenv import load_dotenv
load_dotenv()

cwd = os.getcwd().replace("\\","/") #current working directory cwd

def server(input,output,session): 
    @output
    @render.text
    @reactive.event(input.ip_ab_submit)
    def output_llm_response():
        prompt_sys = "Give the desired output for the asked input"
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

        # Create the model
        generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 65536,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-thinking-exp-01-21",
        generation_config=generation_config,
        system_instruction = prompt_sys
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(input.ip_txt())

        op = response.text
        return(op.replace("**",""))
    
def app_ui():
    return \
       ui.page_fluid(
           ui.include_css(f'{cwd}/style.css'),
           ui.div(
               ui.div(
                    ui.tags.mark('How can I help you today?',id='id__mark'),
                    id='id_div__mark',
                ),
                ui.tags.br(),
                ui.div(
                    ui.input_text_area("ip_txt", label='',resize='none'),
                    id='id_div_inputtxt',
                ),
                ui.tags.br(),
                ui.div(
                    ui.input_action_button("ip_ab_submit", "Submit"),
                    id='id_div_inputab_submit',
                ),
                id='id_div__body'
           ),
           ui.HTML("<br>"),
           ui.output_text_verbatim("output_llm_response")
       )
app = App(app_ui(),server)

if __name__ == '__main__':
    freeze_support()
    Process(target = run_app('miniBot:app',reload=True)).start() 
        
