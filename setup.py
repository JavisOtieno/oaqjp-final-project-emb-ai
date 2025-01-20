from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # List any dependencies required by your package
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="An emotion detection package using Watson NLP.",
    url="https://github.com/javisotieno/EmotionDetection",
)
