# AWS Lambda Serverless Application

## **Project Overview**

This project demonstrates serverless application development using AWS Lambda. It simulates Lambda function execution locally to understand event-driven computing, function deployment, and serverless application architecture before deploying to AWS.

---

## **Project Goal**

- Develop AWS Lambda functions
- Simulate Lambda execution locally
- Understand event-driven architecture
- Prepare serverless applications for AWS deployment

---

## **Architecture**

See: `diagrams/architecture.md`

---

## **Technologies**

- AWS Lambda
- Python
- JSON
- AWS CLI
- Conda

---

## **Features**

- Local Lambda simulation
- Python-based Lambda function
- Event-driven execution
- Lightweight serverless architecture
- AWS-ready project structure

---

## **Project Structure**

```text
.
├── lambda_function.py
├── test_lambda.py
├── diagrams/
│   └── architecture.md
├── LICENSE
└── README.md
```

---

## **Deployment**

Activate the Conda environment:

```bash
conda activate sagemaker_dryrun
```

Run the Lambda simulation:

```bash
python test_lambda.py
```

---

## **Key Learnings**

- Developing AWS Lambda functions
- Understanding serverless computing
- Testing Lambda locally
- Event-driven application design

---

## **Status**

Completed

---

## **Future Improvements**

- API Gateway integration
- Amazon S3 event triggers
- DynamoDB integration
- CloudWatch logging
- IAM least-privilege policies
