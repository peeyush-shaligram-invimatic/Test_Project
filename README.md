# Setting Up Jenkins Locally on Windows

This guide provides step-by-step instructions to configure Jenkins on a Windows machine for local development.

## Prerequisites

1. **Java Installation**:
   - Jenkins requires Java to run. Install the latest version of Java Development Kit (JDK).
   - Set the `JAVA_HOME` environment variable:
     - **Variable Name**: `JAVA_HOME`
     - **Variable Value**: Path to the JDK installation directory (e.g., `C:\Program Files\Java\jdk-17`)

2. **Download Jenkins**:
   - Download the Jenkins `.war` file from the [official Jenkins website](https://www.jenkins.io/download/).

## Steps to Configure Jenkins

### Step 1: Start Jenkins

1. Open a terminal or command prompt.
2. Navigate to the directory where the Jenkins `.war` file is located.
3. Run the following command to start Jenkins:
   ```
   java -jar jenkins.war
   ```
4. Jenkins will start and be accessible at `http://localhost:8080`.

### Step 2: Unlock Jenkins

1. Open a browser and navigate to `http://localhost:8080`.
2. Jenkins will prompt for an administrator password. Retrieve it by:
   - Checking the terminal output for the password location.
   - Navigate to the specified file (e.g., `C:\Users\<YourUser>\.jenkins\secrets\initialAdminPassword`).
   - Copy the password and paste it into the Jenkins setup page.

### Step 3: Install Suggested Plugins

1. After unlocking Jenkins, it will prompt you to install plugins.
2. Choose the option to **Install Suggested Plugins**.
3. Wait for the installation to complete.

### Step 4: Create an Admin User

1. Fill in the required details to create an admin user.
2. Save and continue.

### Step 5: Configure Jenkins Home Directory (Optional)

1. By default, Jenkins stores its data in `C:\Users\<YourUser>\.jenkins`.
2. To change this location:
   - Stop Jenkins.
   - Move the `.jenkins` folder to the desired location.
   - Set the `JENKINS_HOME` environment variable:
     - **Variable Name**: `JENKINS_HOME`
     - **Variable Value**: Path to the new Jenkins home directory.
   - Restart Jenkins.

### Step 6: Install Required Plugins

1. Navigate to `Manage Jenkins > Manage Plugins`.
2. Search for and install the following plugins:
   - **Pipeline**
   - **Git**
   - **Docker Pipeline**
   - **Amazon ECR**

### Step 7: Configure Environment Variables for AWS and Docker

1. **AWS CLI**:
   - Install the AWS CLI from the [official AWS CLI website](https://aws.amazon.com/cli/).
   - Configure AWS credentials:
     ```
     aws configure
     ```
     Provide the following details:
     - AWS Access Key ID
     - AWS Secret Access Key
     - Default region

2. **Environment Variables**:
   - Add the following environment variables:
     - **Variable Name**: `AWS_REGION`
       - **Value**: Your AWS region (e.g., `us-east-1`)
     - **Variable Name**: `AWS_ACCOUNT_ID`
       - **Value**: Your AWS account ID

3. **Docker**:
   - Install Docker Desktop for Windows.
   - Ensure Docker is running and accessible from the command line.

### Step 8: Configure Jenkins Pipeline

1. Create a `Jenkinsfile` in your project repository.
2. Add the necessary stages for building, testing, and deploying your application.
3. Example `Jenkinsfile`:
   ```groovy
   pipeline {
       agent any

       stages {
           stage('Checkout') {
               steps {
                   checkout scm
               }
           }

           stage('Build') {
               steps {
                   sh 'echo Building...'
               }
           }

           stage('Deploy') {
               steps {
                   sh 'echo Deploying...'
               }
           }
       }
   }
   ```

### Step 9: Run Jenkins Pipeline

1. Navigate to your Jenkins dashboard.
2. Create a new pipeline job.
3. Point the pipeline to your repository containing the `Jenkinsfile`.
4. Run the pipeline and monitor the output.

### Comments

- Ensure all required tools (Java, AWS CLI, Docker) are installed and properly configured.
- Use the Jenkins logs to troubleshoot any issues during setup or pipeline execution.

This completes the Jenkins setup on Windows for local development.