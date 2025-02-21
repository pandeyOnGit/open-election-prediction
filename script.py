#!/usr/bin/env python3
import os

def create_dir(path):
    """Create a directory with a .gitkeep file if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
        # Create a placeholder file so that the directory is not empty
        gitkeep_path = os.path.join(path, ".gitkeep")
        with open(gitkeep_path, "w") as f:
            pass
        print(f"Created placeholder file: {gitkeep_path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path):
    """Create an empty file if it doesn't exist."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

def main():
    base_dir = os.getcwd()  # Use the current directory as base
    print(f"Updating directory structure in: {base_dir}")

    # List of directories to create (relative to base_dir)
    directories = [
        # Frontend directories
        "frontend/src/app",
        "frontend/src/components",
        "frontend/src/styles",
        "frontend/src/lib",
        "frontend/src/types",
        "frontend/public",
        "frontend/tests",

        # Backend directories
        "backend/src/controllers",
        "backend/src/models",
        "backend/src/routes",
        "backend/src/middleware",
        "backend/src/services",
        "backend/src/utils",
        "backend/config",
        "backend/tests",

        # ML Pipeline directories
        "ml_pipeline/src/data_collection/social_media",
        "ml_pipeline/src/data_collection/news_scraper",
        "ml_pipeline/src/data_collection/youtube_api",
        "ml_pipeline/src/data_collection/manifesto_parser",
        
        # Data pipeline moved inside ml_pipeline
        "ml_pipeline/src/data_pipeline/collectors",
        "ml_pipeline/src/data_pipeline/transformers",
        "ml_pipeline/src/data_pipeline/loaders",
        "ml_pipeline/src/data_pipeline/schedulers",
        
        "ml_pipeline/src/preprocessing/text_cleaning",
        "ml_pipeline/src/preprocessing/feature_engineering",
        "ml_pipeline/src/preprocessing/data_integration",
        
        "ml_pipeline/src/models/sentiment_analysis",
        "ml_pipeline/src/models/topic_modeling",
        "ml_pipeline/src/models/prediction",
        
        "ml_pipeline/src/rag_engine/document_store",
        "ml_pipeline/src/rag_engine/embeddings",
        "ml_pipeline/src/rag_engine/retrieval",
        
        "ml_pipeline/src/evaluation",
        "ml_pipeline/notebooks",
        "ml_pipeline/data/raw",
        "ml_pipeline/data/processed",
        "ml_pipeline/data/external",
        "ml_pipeline/tests",
        
        # Documentation directories
        "docs/api",
        "docs/ml",
        "docs/deployment",
        "docs/development"
    ]

    # List of root-level files to create
    files = [
        "README.md",
        "LICENSE",
        ".gitignore",
        "docker-compose.yml",
        "requirements.txt",
        "package.json"
    ]

    # Create all directories
    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        create_dir(dir_path)

    # Create all files
    for file in files:
        file_path = os.path.join(base_dir, file)
        create_file(file_path)

if __name__ == "__main__":
    main()
