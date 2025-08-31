# Docker-project
/students_app
  ├── app.py
  ├── Dockerfile
  ├── requirements.txt
  └── init_db.py

How to run:

Put all files in a folder (students_app)

Build the image:

docker build -t students-app .


Run the container:

docker run -p 5000:5000 students-app


Open your browser and go to:

http://localhost:5000/


You’ll see a neat table showing students’ names, class, marks, total marks, and percentage.

If you getting any Error please follow the below steps

1. Check Security Group inbound rules (AWS EC2)

Go to your AWS console → EC2 → Instances → Select your instance

Scroll down to Security groups, click it

Under Inbound rules, make sure you have a rule like:

Type	Protocol	Port Range	Source
Custom TCP	TCP	5000	0.0.0.0/0

If missing, Add rule to allow inbound TCP traffic on port 5000 from anywhere (or your IP range).

2. Check OS firewall on your server (like ufw or firewalld)

For Ubuntu with UFW:

sudo ufw status
sudo ufw allow 5000/tcp
<img width="1142" height="200" alt="image" src="https://github.com/user-attachments/assets/31deb658-8e04-432a-a3d7-3cd08151904a" />

<img width="1918" height="1025" alt="image" src="https://github.com/user-attachments/assets/9a406ab1-f754-4de3-b655-e99c4a327b5a" />

✅ Official Docker URL:

👉 https://docs.docker.com/engine/install/ubuntu/

📦 Docker Install Commands for Ubuntu

Run the following commands one by one:

# 1. Update package index
sudo apt-get update

# 2. Install prerequisite packages
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y

# 3. Add Docker’s official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Set up the stable Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Update package index (again)
sudo apt-get update

# 6. Install Docker Engine and CLI
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# 7. Verify Docker installation
docker --version

🧪 Test Docker works

Run a test container:

sudo docker run hello-world


You should see a message saying Docker is installed and working properly.
