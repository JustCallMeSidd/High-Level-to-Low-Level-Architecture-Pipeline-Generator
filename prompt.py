FINAL_PROMPT = """
You are a Senior Software Architect and System Designer.

Your task is to convert a HIGH-LEVEL BUSINESS REQUIREMENT
into LOW-LEVEL TECHNICAL SPECIFICATIONS.

Business Requirement:
{requirement}

Generate the output in the following format:

--------------------------------------------------

1. System Overview
- Brief description of the system and its purpose

2. Key Assumptions
- Any assumptions made while designing the system

3. Major System Modules
For each module, include:
- Module Name
- Responsibilities

4. API Design (REST APIs)
For each API, include:
- Endpoint
- HTTP Method
- Description

5. Database Design
List the main tables with fields:
- Table Name
- Fields (with data types if possible)

6. Core Workflow (Pseudocode)
Provide pseudocode for the main business flow

7. Non-Functional Requirements
- Performance
- Security
- Scalability

--------------------------------------------------

Important Rules:
- Keep the design simple and practical
- Avoid unnecessary complexity
- Use bullet points and clear formatting
- Assume a web-based application
"""
