import json
import boto3
import cx_Oracle

# Initialize S3 client and define Oracle database connection parameters
s3client = boto3.client('s3')

oracle_host = 'your-oracle-hostname'
oracle_port = 1521  # Example port for Oracle
oracle_sid = 'your-sid'  # Replace with your Oracle SID
oracle_user = 'your_username'  # Replace with your Oracle username
oracle_password = 'your_password'  # Replace with your Oracle password

def lambda_handler(event, context):
    try:
        print("Starting Lambda function execution.")
        
        # Check if the event is triggered by an S3 event
        if 'Records' in event and event['Records'][0]['eventSource'] == 'aws:s3':
            # Extract bucket and key information from S3 event
            bucket = event['Records'][0]['s3']['bucket']['name']
            key = event['Records'][0]['s3']['object']['key']
            
            print(f"Fetching file from S3. Bucket: {bucket}, Key: {key}")
            
            # Fetch the file from S3
            response = s3client.get_object(Bucket=bucket, Key=key)
            
            # Read and decode text file content
            lines = response['Body'].read().decode('utf-8').splitlines()
            
            print("Parsing text file content.")
            results = []
            for line in lines:
                # Split each line by '|' delimiter
                row = line.split('|')
                # Assuming the order of columns matches your insert query, adjust as needed
                result = {
                    'CREDITSCORE': row[0],
                    'FIRSTPAYMENTDATE': row[1],
                    'FIRSTTIMEHOMEBUYERFLAG': row[2],
                    'MATURITYDATE': row[3],
                    'METROPOLITANSTATISTICALAREA': row[4],
                    'MORTGAGEINSURANCEPERCENTAGE': row[5],
                    'NUMBEROFUNITS': row[6],
                    'OCCUPANCYSTATUS': row[7],
                    'ORIGINALCOMBINEDLOANTOVALUE': row[8],
                    'ORIGINALDEBTTOINCOMERATIO': row[9],
                    'ORIGINALUPB': row[10],
                    'ORIGINALLOANTOVALUE': row[11],
                    'ORIGINALINTERESTRATE': row[12],
                    'CHANNEL': row[13],
                    'PREPAYMENTPENALTYMORTGAGEFLAG': row[14],
                    'AMORTIZATIONTYPE': row[15],
                    'PROPERTYSTATE': row[16],
                    'PROPERTYTYPE': row[17],
                    'POSTALCODE': row[18],
                    'LOANSEQUENCENUMBER': row[19],
                    'LOANPURPOSE': row[20],
                    'ORIGINALLOANTERM': row[21],
                    'NUMBEROFBORROWERS': row[22],
                    'SELLERNAME': row[23],
                    'SERVICERNAME': row[24],
                    'SUPERCONFORMINGFLAG': row[25],
                    'PREHARPLOANSEQUENCENUMBER': row[26],
                    'PROGRAMINDICATOR': row[27],
                    'HARPINDICATOR': row[28],
                    'PROPERTYVALUATIONMETHOD': row[29],
                    'INTERESTONLYINDICATOR': row[30],
                    'MORTGAGEINSURANCECANCELLATIONINDICATOR': row[31]
                }
                results.append(result)
            
            print("Parsed data as dictionaries:")
            for result in results:
                print(result)
            
            print("Connecting to Oracle database.")
            
            # Construct Oracle DSN (Data Source Name)
            dsn = cx_Oracle.makedsn(oracle_host, oracle_port, sid=oracle_sid)
            
            # Establish connection to Oracle database
            connection = cx_Oracle.connect(
                user=oracle_user,
                password=oracle_password,
                dsn=dsn
            )

            print("Successfully connected to Oracle database.")
            
            # Example: Inserting data into Oracle 
            oracle_insert_query = """
                INSERT INTO originationsdata (
                    CREDITSCORE, FIRSTPAYMENTDATE, FIRSTTIMEHOMEBUYERFLAG, MATURITYDATE, 
                    METROPOLITANSTATISTICALAREA, MORTGAGEINSURANCEPERCENTAGE, NUMBEROFUNITS, 
                    OCCUPANCYSTATUS, ORIGINALCOMBINEDLOANTOVALUE, ORIGINALDEBTTOINCOMERATIO, 
                    ORIGINALUPB, ORIGINALLOANTOVALUE, ORIGINALINTERESTRATE, CHANNEL, 
                    PREPAYMENTPENALTYMORTGAGEFLAG, AMORTIZATIONTYPE, PROPERTYSTATE, PROPERTYTYPE, 
                    POSTALCODE, LOANSEQUENCENUMBER, LOANPURPOSE, ORIGINALLOANTERM, NUMBEROFBORROWERS, 
                    SELLERNAME, SERVICERNAME, SUPERCONFORMINGFLAG, PREHARPLOANSEQUENCENUMBER, 
                    PROGRAMINDICATOR, HARPINDICATOR, PROPERTYVALUATIONMETHOD, INTERESTONLYINDICATOR, 
                    MORTGAGEINSURANCECANCELLATIONINDICATOR
                ) VALUES (
                    :CREDITSCORE, :FIRSTPAYMENTDATE, :FIRSTTIMEHOMEBUYERFLAG, :MATURITYDATE, 
                    :METROPOLITANSTATISTICALAREA, :MORTGAGEINSURANCEPERCENTAGE, :NUMBEROFUNITS, 
                    :OCCUPANCYSTATUS, :ORIGINALCOMBINEDLOANTOVALUE, :ORIGINALDEBTTOINCOMERATIO, 
                    :ORIGINALUPB, :ORIGINALLOANTOVALUE, :ORIGINALINTERESTRATE, :CHANNEL, 
                    :PREPAYMENTPENALTYMORTGAGEFLAG, :AMORTIZATIONTYPE, :PROPERTYSTATE, :PROPERTYTYPE, 
                    :POSTALCODE, :LOANSEQUENCENUMBER, :LOANPURPOSE, :ORIGINALLOANTERM, :NUMBEROFBORROWERS, 
                    :SELLERNAME, :SERVICERNAME, :SUPERCONFORMINGFLAG, :PREHARPLOANSEQUENCENUMBER, 
                    :PROGRAMINDICATOR, :HARPINDICATOR, :PROPERTYVALUATIONMETHOD, :INTERESTONLYINDICATOR, 
                    :MORTGAGEINSURANCECANCELLATIONINDICATOR
                )
            """
            
            print("Executing Oracle SQL insert query.")
            cursor = connection.cursor()
            for row in results:
                cursor.execute(oracle_insert_query, row)  # Bind parameters from each row dictionary
            
            connection.commit()
            print("Data inserted into Oracle table (originationsdata).")
            
            # Close cursor and connection
            cursor.close()
            connection.close()
        
        else:
            print("Event does not appear to be an S3 event.")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        # Handle exceptions
