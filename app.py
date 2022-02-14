import gradio as gr


def greet(name):
    return "Hello " + name + "!"

def main():
    io = gr.Interface(fn=greet, inputs="text", outputs="text")
    io.launch(server_name="0.0.0.0", server_port=8000)

if __name__ == '__main__':
    main()
