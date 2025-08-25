# Intelligent Product Analysis Assistant

## Project Overview

This project is an AI-powered service that utilizes **Vision Language Models (VLM)** and **Large Language Models (LLM)** to analyze product images and generate marketing content.

## Key Features

* **Product Image Analysis**: Accurate recognition and description of products using the Qwen2.5-VL model
* **Marketing Content Generation**: Creation of product names, engaging descriptions, and relevant hashtags
* **Persian Language Support**: All outputs are generated in Persian
* **RESTful API**: Simple and accessible interface
* **Docker Support**: Easy deployment and execution

## Technical Architecture

### Technologies Used

* **Backend**: FastAPI (Python)
* **AI Models**:

  * VLM: Qwen2.5-VL-7B (OpenRouter)
  * LLM: Qwen2.5-72B (HuggingFace)
* **Containerization**: Docker & Docker Compose
* **Image Processing**: Pillow
* **API Integration**: OpenAI Client

### Project Structure

```
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose setup
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
└── src/
    ├── app/
    │   ├── main.py            # Main FastAPI server
    │   ├── vlm_caption.py     # Image analysis module
    │   └── llm_generation.py  # Content generation module
    ├── demo/                  # Sample files
    └── uploads/               # Image upload folder
```

## How to Run

### Prerequisites

* Docker and Docker Compose
* `.env` file with required API keys

### Steps

1. **Clone the repository**

```bash
git clone <repository-url>
cd ai-product-assistant
```

2. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env and add your API keys
```

3. **Run with Docker Compose**

```bash
docker-compose up --build
```

## Configuration

### Required Environment Variables

```env
VLM_MODEL_API_KEY=your_openrouter_api_key
LLM_MODEL_API_KEY=your_huggingface_api_key
```

### Ports

* **API Server**: 8080
* **Health Check**: every 30 seconds

## API Endpoints

### `POST /upload`

Upload a product image and receive analysis.

**Request:**

* `file`: Image file (JPG, PNG, etc.)

**Response:**

```json
{
  "product_name": "Product Name",
  "description": "Engaging product description",
  "category": ["Category 1", "Category 2"],
  "hashtags": ["#hashtag_1", "#hashtag_2"]
}
```

### `GET /`

Check service status.

## Docker Commands

### Build and Run

```bash
# Build image
docker build -t ai-product-assistant .

# Run container
docker run -p 8080:8080 ai-product-assistant

# Run with Docker Compose
docker-compose up -d
```

## Health Check

The service includes an automatic health check that monitors the API status every 30 seconds.

## Troubleshooting

### Common Issues

1. **API Key Error**: Verify your API keys in `.env`
2. **Port Issues**: Ensure port 8080 is available
3. **Docker Errors**: Check Docker service status

## Contributing

To contribute:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

## License

This project is licensed under MIT.









