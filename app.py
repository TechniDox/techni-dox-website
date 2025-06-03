import gradio as gr

def inclusivity_review(text):
    return f"🔍 Inclusivity feedback summary:\n{text[:100]}..."

def onboarding_guide(role):
    guides = {
        "Developer": "👩‍💻 Welcome Developer! Let's get you started with TechniDox.",
        "PM": "📊 Welcome Product Manager! Here's your onboarding path.",
        "Designer": "🎨 Welcome Designer! Here's your visual documentation toolkit."
    }
    return guides.get(role, "🤔 Role not found.")

def file_feedback(file):
    content = file.read().decode("utf-8")
    return f"📝 First 300 characters of your file:\n{content[:300]}..."

custom_css = """
body {
    background-color: #ffffff;
    font-family: 'Inter', sans-serif;
}
.gradio-container {
    max-width: 850px;
    margin: auto;
}
textarea, input, select, .gr-button {
    border-radius: 8px;
    border: 1px solid #d9d9d9;
}
h1, h2, h3 {
    color: #2c1e4a;
}
.gr-button {
    background-color: #1a8dc5;
    color: white;
    font-weight: 600;
}
.gr-button:hover {
    background-color: #056590;
}
a {
    color: #1a8dc5;
    font-weight: 600;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
"""

with gr.Blocks(css=custom_css, title="TechniDox AI Agent") as demo:
    gr.Markdown("""
    <div style="text-align:center">
        <img src="https://technidox.dev/logo.png" height="80px" style="margin-bottom: 20px;" />
        <h1 style="margin-bottom: 0;">🧠 TechniDox AI Agent</h1>
        <p style="color:#433362; font-size: 16px;">
            Streamline documentation. Empower inclusivity. Built for dev teams and contributors.
        </p>
        <div style="margin-top: 10px;">
            <a href="https://technidox.dev" target="_blank">🌐 Website</a> |
            <a href="https://discord.gg/technidox" target="_blank">💬 Discord</a> |
            <a href="https://github.com/TechniDox" target="_blank">💻 GitHub</a>
        </div>
    </div>
    """)

    with gr.Tab("🔍 Inclusivity Review"):
        text_input = gr.Textbox(label="Paste your documentation here", lines=10, placeholder="e.g. README.md section")
        review_output = gr.Textbox(label="AI Feedback")
        text_input.change(fn=inclusivity_review, inputs=text_input, outputs=review_output)

    with gr.Tab("🚀 Onboarding Guide"):
        role = gr.Dropdown(["Developer", "PM", "Designer"], label="Select your role")
        guide_output = gr.Textbox(label="Your personalized onboarding path")
        role.change(fn=onboarding_guide, inputs=role, outputs=guide_output)

    with gr.Tab("📁 Markdown File Feedback"):
        file_input = gr.File(file_types=[".md"], label="Upload your .md file")
        file_output = gr.Textbox(label="Markdown file feedback")
        file_input.change(fn=file_feedback, inputs=file_input, outputs=file_output)

demo.launch()
