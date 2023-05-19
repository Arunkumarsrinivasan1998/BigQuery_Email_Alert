def email(request):
        from google.cloud import bigquery
        from pretty_html_table import build_table
        import os
        import pandas_gbq
        import sendgrid
        from sendgrid.helpers.mail import Mail

        client = bigquery.Client()

        query_one="""Select * from `TestData.TestTable`"""

        #query_job_one = client.query(query_one)
        
        df = pandas_gbq.read_gbq(query_one)
        output_table = build_table(df, 'blue_light')

        #for row in query_job_one:
            #query_job_one_results = row[0]
            #print(query_job_one_results)
        print(output_table)

        message = Mail(
              from_email= 'xxxx@gmail.com',
              to_emails='xxxx@gmail.com',
              subject="Big Query Reporting",
              html_content='Please find the results of the Query below<br>'+output_table+'')
        try:
              #sg = sendgrid.SendGridAPIClient('xxxxx')
			  sg = sendgrid.SendGridAPIClient(os.environ.get("EMAIL_API_KEY"))
              response = sg.send(message)
              print (response.status_code)
              print(response.body)
              print (response.headers)
        except Exception as e:
              print(e.message)
