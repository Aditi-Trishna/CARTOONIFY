# Cartoonify MLOps Pipeline

**Phase 1: Headless API & Object-Oriented Refactoring**

An industrial-grade REST API that transforms standard images into cartoonized versions using computer vision. This repository represents the foundational phase of a larger MLOps pipeline, transitioning a traditional GUI-dependent OpenCV script into a scalable, headless web service.

## Architecture Highlights

* **Headless Execution:** Stripped of all local GUI dependencies (e.g., `Tkinter`, `cv2.imshow`), making the application cloud-ready and server-safe.
* **Separation of Concerns:** The web routing is completely decoupled from the mathematical processing, ensuring high maintainability.
* **Object-Oriented Design:** The core computer vision logic is encapsulated within a `Cartoonifier` class. This allows parameters to be tuned at runtime and prepares the architecture for future stateful AI model loading.
* **Interactive Documentation:** Leverages FastAPI to automatically generate a Swagger UI for instant endpoint testing and validation.

## Project Structure

```text
CARTOONIFY/
│
├── core_logic.py        # OOP class containing the OpenCV processing pipeline
├── main.py              # FastAPI server, route definitions, and error handling
├── requirements.txt     # Locked dependencies for predictable environments
├── .gitignore           # Git exclusions (venv, cache, OS files)
└── README.md            # Project documentation
```

## Tech Stack
- Language: Python 3.9+

- Web Framework: FastAPI

- ASGI Server: Uvicorn

- Computer Vision: OpenCV (Headless)

- Data Manipulation: NumPy

## Local Development Setup
1. Clone the repository

```Bash
git clone [https://github.com/Aditi-Trishna/CARTOONIFY.git](https://github.com/Aditi-Trishna/CARTOONIFY.git)
cd CARTOONIFY
```
2. Create and activate a Virtual Environment

```Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```Bash
pip install -r requirements.txt
```

4. Run the Local Server
Start the Uvicorn server with live-reloading enabled for development.

```Bash
uvicorn main:app --reload
```

## Testing the API
Once the server is running, navigate to http://localhost:8000/docs in your web browser.


## Project Roadmap
[x] Step 1: Refactor logic into an OOP, Headless FastAPI service.

[ ] Step 2: Containerization (Docker) & CI/CD integration.

[ ] Step 3: Integration of Agentic AI / Deep Learning models (e.g., AnimeGAN).