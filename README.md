# Serverless AWS Lambda Template Project

This is a simple Pytohn Lambda project deployed using the Serverless Framework and serverless-wsgi plugin. It provides a basic function as a starting point for your serverless applications.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- [Node.js](https://nodejs.org/) (Node.js 18.x)
- [Python](https://www.python.org) (Python 3.11)
- [Serverless Framework](https://www.serverless.com/)
- [AWS CLI](https://aws.amazon.com/cli/)

## Setup

1. Configure AWS CLI with your AWS credentials:

   ```bash
   aws configure
   ```

2. Install project Serverless dependencies:

   ```bash
   npm install
   ```

3. Deploy the project to AWS Lambda:
   ```bash
   npm run deploy
   ```
