from setuptools import setup, find_packages

setup(
    name='jarvis-core',
    version='0.1.0',
    packages=find_packages(),
    description='Jarvis AI Assistant Core Application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jarvis Development Team',
    author_email='dev@jarvis-assistant.com',
    url='https://github.com/plcpp-2/jarvis-assistant',
    install_requires=[
        'dynaconf>=3.1.7',
        'azure-identity>=1.12.0',
        'openai>=0.27.0',
        'langchain>=0.0.150',
        'fastapi>=0.68.0',
        'uvicorn>=0.15.0',
        'asyncio>=3.4.3',
        'pydantic>=1.8.0',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.5',
            'mypy>=0.812',
            'black>=21.5b1',
        ],
        'ml': [
            'torch>=1.9.0',
            'transformers>=4.10.0',
            'scikit-learn>=0.24.2',
        ],
    },
    entry_points={
        'console_scripts': [
            'jarvis=jarvis_core.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
)
