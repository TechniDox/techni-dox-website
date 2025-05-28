import gradio as gr

def inclusivity_review(text):
    # Replace with your AI agent logic
    return f"Review summary for inclusivity: {text[:100]}..."

def onboarding_guide(role):
    guides = {
        "Developer": "Welcome Developer! Here's how to get started...",
        "PM": "Welcome Product Manager! Here's your onboarding...",
        "Designer": "Welcome Designer! Let's walk you through..."
    }
    return guides.get(role, "Role not recognized.")

def file_feedback(file):
    content = file.read().decode("utf-8")
    # Replace with your AI agent logic
    return f"Feedback on file:\n{content[:200]}..."

with gr.Blocks() as demo:
    gr.Markdown("### 🧠 TechniDox AI Agent Demo")

    with gr.Tab("Inclusivity Review"):
        text_input = gr.Textbox(lines=10, placeholder="Paste your doc here...")
        review_output = gr.Textbox(label="AI Feedback")
        text_input.change(fn=inclusivity_review, inputs=text_input, outputs=review_output)

    with gr.Tab("Onboarding Guide"):
        role = gr.Dropdown(["Developer", "PM", "Designer"], label="Select your role")
        guide_output = gr.Textbox(label="Onboarding Guide")
        role.change(fn=onboarding_guide, inputs=role, outputs=guide_output)

    with gr.Tab("Markdown Feedback"):
        file_input = gr.File(file_types=[".md"], label="Upload your .md file")
        file_output = gr.Textbox(label="AI Feedback")
        file_input.change(fn=file_feedback, inputs=file_input, outputs=file_output)

demo.launch()
