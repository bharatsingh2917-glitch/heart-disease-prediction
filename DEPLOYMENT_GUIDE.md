# Deployment Guide

## Local Development

### Prerequisites
- Python 3.8+
- Git
- pip or conda

### Setup

```bash
# Clone repository
git clone https://github.com/bharatsingh2917-glitch/heart-disease-prediction.git
cd heart-disease-prediction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app_enhanced.py
```

## Docker Deployment

### Build and Run

```bash
# Build image
docker build -t heart-disease-prediction:latest .

# Run container
docker run -p 8501:8501 heart-disease-prediction:latest

# Or use docker-compose
docker-compose up -d
```

### Verify Deployment

```bash
# Check container logs
docker logs <container-id>

# Access application
# Open http://localhost:8501
```

## Streamlit Cloud Deployment

### Step 1: Prepare GitHub Repository
```bash
# Push code to GitHub
git add .
git commit -m "Deploy to Streamlit Cloud"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Choose branch: `main`
5. Set main file path: `app_enhanced.py`
6. Click "Deploy"

### Step 3: Configure Secrets (Optional)

In Streamlit Cloud dashboard:
- Go to "App settings" → "Secrets"
- Add environment variables:

```yaml
# secrets.toml
admin_password = "your-secure-password"
database_url = "your-database-url"
```

## AWS Deployment

### Using Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize EB application
eb init -p docker heart-disease-prediction

# Create environment
eb create heart-disease-prod

# Deploy
eb deploy

# Monitor
eb logs
```

### Using EC2 + Docker

```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Install Docker
sudo yum install docker -y
sudo service docker start

# Clone and deploy
git clone <repo-url>
cd heart-disease-prediction
docker-compose up -d
```

## Google Cloud Platform

### Using App Engine

```bash
# Install gcloud CLI
# https://cloud.google.com/sdk/docs/install

# Deploy
gcloud app deploy

# View logs
gcloud app logs read -f
```

### Using Cloud Run

```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/PROJECT_ID/heart-disease-prediction

# Deploy
gcloud run deploy heart-disease-prediction \
  --image gcr.io/PROJECT_ID/heart-disease-prediction \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Production Checklist

- [ ] Change default credentials
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring and alerts
- [ ] Configure backup strategy
- [ ] Implement rate limiting
- [ ] Enable audit logging
- [ ] Set up error tracking (Sentry, etc.)
- [ ] Configure CDN for static assets
- [ ] Implement CI/CD pipeline
- [ ] Set up health checks
- [ ] Configure auto-scaling
- [ ] Regular security updates
- [ ] GDPR/HIPAA compliance check
- [ ] Load testing

## Performance Optimization

### Caching
```python
@st.cache_data
def load_model():
    return joblib.load('heart_disease_model.pkl')
```

### Database Connection Pooling
```python
@st.cache_resource
def init_connection():
    return create_database_connection()
```

### CDN Configuration
- Serve static files through CDN
- Enable gzip compression
- Minify CSS/JavaScript

## Monitoring & Logging

### Application Metrics
- Prediction latency
- API response times
- User sessions
- Error rates

### Health Checks
```bash
# Test endpoint
curl http://localhost:8501/_stcore/health
```

### Log Aggregation
- Use ELK Stack for logs
- CloudWatch for AWS
- Stackdriver for GCP

## Scaling Considerations

### Horizontal Scaling
- Load balancing (nginx, HAProxy)
- Multiple app instances
- Session persistence

### Vertical Scaling
- Increase server resources
- Optimize database queries
- Cache frequently accessed data

## Security Hardening

### SSL/TLS
```bash
# Generate self-signed certificate
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

### API Authentication
```python
# Use API keys
def verify_api_key(api_key):
    return api_key in VALID_API_KEYS
```

### Rate Limiting
```python
from streamlit_rate_limit import limiter

@limiter.limit("5 per minute")
def predict_endpoint():
    pass
```

## Backup & Recovery

### Database Backup
```bash
# Automated daily backup
0 2 * * * /backup/backup_database.sh
```

### Code Backup
- Regular commits to GitHub
- Enable branch protection
- Use semantic versioning

## Troubleshooting

### High Memory Usage
- Check for memory leaks
- Optimize data structures
- Use streaming for large datasets

### Slow Predictions
- Profile code with cProfile
- Optimize model loading
- Implement caching

### Database Connection Issues
- Check connection pooling
- Verify firewall rules
- Monitor connection limits

## Useful Commands

```bash
# Check Python version
python --version

# Verify dependencies
pip list

# Run tests
pytest test_model.py -v

# Generate requirements
pip freeze > requirements.txt

# Clean up
docker system prune
```

## Support & Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Documentation](https://docs.docker.com)
- [AWS Deployment Guide](https://docs.aws.amazon.com)
- [GCP Deployment Guide](https://cloud.google.com/docs)

## Additional Notes

- Keep dependencies up to date
- Monitor for security vulnerabilities
- Regular performance testing
- Collect user feedback
- Plan for disaster recovery
