# BigQuery_Email_Alert
Code to run report on Big Query and generate email alert using GCP Services like cloud functions, cloud scheduler and SMTP Protocols


To enable email alerts based on a BigQuery table results query using Python in Cloud Functions and Cloud Scheduler with the SendGrid API, follow these step-by-step instructions:

Set up a SendGrid account: Create an account on the SendGrid platform (sendgrid.com) if you haven't already. Obtain your SendGrid API key, as you will need it to send emails.

Create a Cloud Function:

Go to the Cloud Functions section of the Google Cloud Console (console.cloud.google.com/functions).
Click "Create Function" and provide a name for your function.
Choose the runtime as "Python" and select the desired region.
In the "Trigger" section, choose "Cloud Pub/Sub" as the trigger type.
Create a new topic or select an existing one.
Click "Next" to proceed to the code editor.
Write the Cloud Function code:

Replace the sample code in the code editor with Python code that performs the following steps:
Imports necessary libraries (google-cloud-bigquery, sendgrid, and os).
Defines the main function to execute the BigQuery query and send an email.
Executes the query using the google-cloud-bigquery library.
Checks if the query result is not empty.
If the query result is not empty, sends an email using the SendGrid API, including the query result in the email body.
Configure the Cloud Function:

Specify the function's entry point as the main function you defined.
Set the environment variables for your SendGrid API key and other required parameters.
Set the memory allocated and the timeout duration based on your requirements.
Save and deploy the function.
Set up Cloud Scheduler:

Go to the Cloud Scheduler section of the Google Cloud Console (console.cloud.google.com/cloudscheduler).
Click "Create Job" to create a new job.
Provide a name and description for the job.
Set the schedule frequency and timezone for running the job.
Save the job.


Ensure that the service account associated with the Cloud Function has the required permissions to access BigQuery and send emails via SendGrid. You can grant the appropriate roles to the service account (e.g., BigQuery Data Viewer) in the IAM & Admin section of the Google Cloud Console.
Test and monitor:

Manually trigger the Cloud Function to check if it executes the query and sends an email.
Monitor the Cloud Function logs and the SendGrid email delivery status for any errors or issues.
