# 🔥 Roast My Bio

An AI-powered web app that roasts your LinkedIn or Twitter bio in 3 funny sentences.

## Live Demo
[Click here to try it](YOUR_S3_URL)

## What It Does
- Paste your bio
- Click "Roast Me"
- Get a funny AI-generated roast instantly

## Tech Stack
| Service | Purpose |
|---------|---------|
| Amazon S3 | Hosts the frontend |
| AWS Lambda | Runs backend logic |
| Amazon API Gateway | Connects frontend to Lambda |
| Amazon Bedrock (Nova Lite) | Generates the roast |

## Architecture
User Browser → S3 (HTML) → API Gateway → Lambda → Bedrock Nova Lite
## How To Deploy

### 1. Lambda
- Create a Lambda function (Python 3.12)
- Paste code from `lambda/lambda_function.py`
- Attach `AmazonBedrockFullAccess` IAM policy

### 2. API Gateway
- Create HTTP API
- Add POST /roast route
- Connect to Lambda
- Enable CORS

### 3. S3
- Create bucket
- Enable static website hosting
- Upload index.html
- Add public bucket policy

## Local Setup
No local setup needed. This runs entirely on AWS.

## Author
Built for AWS Creative App Weekend Challenge 2026
# Architecture Overview

## Diagram
┌─────────────────────────────────────────────┐
│ USER │
│ (Opens S3 website URL) │
└──────────────────┬──────────────────────────┘
│
▼
┌─────────────────────────────────────────────┐
│ AMAZON S3 │
│ Static Website Hosting │
│ (index.html) │
└──────────────────┬──────────────────────────┘
│ HTTP POST /roast
▼
┌─────────────────────────────────────────────┐
│ AMAZON API GATEWAY │
│ HTTP API │
│ POST /roast route │
└──────────────────┬──────────────────────────┘
│ Triggers
▼
┌─────────────────────────────────────────────┐
│ AWS LAMBDA │
│ Python 3.12 │
│ - Receives bio text │
│ - Builds prompt │
│ - Calls Bedrock │
│ - Returns roast │
└──────────────────┬──────────────────────────┘
│ invoke_model API
▼
┌─────────────────────────────────────────────┐
│ AMAZON BEDROCK │
│ Nova Lite Model │
│ - Generates funny roast │
│ - Returns text response │
└─────────────────────────────────────────────┘
## AWS Services Used
- **S3** — Static website hosting (free tier)
- **Lambda** — Serverless compute (free tier: 1M requests/month)
- **API Gateway** — HTTP API (free tier: 1M calls/month)
- **Bedrock Nova Lite** — AI model (pay per token, ~$0.00 for testing)

## Why This Architecture
- No servers to manage
- Scales automatically
- Almost zero cost
- Deploy in under 2 hours
