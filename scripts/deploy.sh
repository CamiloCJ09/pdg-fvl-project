#!/bin/bash
SSH_KEY="../prediction-system-infra/tf_key.pem"
cd .. || exit
cd prediction-system-infra/ || exit
INSTANCE_IP=$(terraform output -raw public_ip)

#echo "$(pwd)"

cd ../ || exit && cd scripts/ || exit

#echo "$(pwd)"


#echo "$INSTANCE_IP"

echo "Deploying to production..."

scp -o StrictHostKeyChecking=no -i $SSH_KEY -r docker-compose.yml ubuntu@"$INSTANCE_IP":/home/ubuntu

ssh -o StrictHostKeyChecking=no -i $SSH_KEY ubuntu@"$INSTANCE_IP" << EOF
  sudo docker compose -f docker-compose.yml up -d
EOF

echo "Deployment complete!"