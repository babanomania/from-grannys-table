# **From Grannys Table**  
🍴 *Where Tradition Meets Modern Vegan Cooking*  

**From Grannys Table** is an AI-powered blog generator that combines the warmth of a grandmother's kitchen with modern vegan culinary trends. Using **Crew AI**, this project creates engaging, intergenerational content written in the voice of a wise grandmother and her tech-savvy granddaughter. Perfect for food bloggers, recipe enthusiasts, or anyone who loves a good story with their meal!  

---

## **Features**  
- 🥕 **Authentic Recipes**: Traditional vegan dishes with a personal touch.  
- 🕰️ **Nostalgic Stories**: Heartwarming anecdotes from "Granny's" kitchen.  
- 🌱 **Modern Hacks**: Time-saving tips and nutritional insights from the granddaughter.  
- 📸 **Image Integration**: Automatically sourced public domain images for visual appeal.  
- 🤖 **Flexible AI Backends**: Supports **OpenAI**, **Ollama**, and **DeepSeek-V3** for LLM-powered content generation.  

---

## **Tech Stack**  
- **Crew AI**: Multi-agent framework for orchestrating the grandmother-granddaughter duo.  
- **LLM Backends**:  
  - **OpenAI GPT-3.5/4**: Default LLM for high-quality content generation.  
  - **Ollama**: Run local LLMs (e.g., LLaMA 2, Mistral) for privacy and customization.  
  - **DeepSeek-V3**: High-performance LLM for cost-effective and efficient content creation.  
- **Unsplash API**: For sourcing beautiful, royalty-free images.  
- **Markdown**: Easy-to-read and portable blog formatting.  

---

## **Getting Started**  

### **Prerequisites**  
1. Python 3.8+  
2. API Keys:  
   - **Unsplash**: [Register for an API key](https://unsplash.com/developers)  
   - (Optional) **DeepSeek-V3**: [Sign up for access](https://www.deepseek.com/)  
3. (Optional) **Ollama**: [Install Ollama](https://ollama.ai/) and download a model (e.g., `ollama pull llama2`).  


## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
