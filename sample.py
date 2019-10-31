from smtplib import SMTP    
import smtplib          # sending email
from email.mime.text import MIMEText  # constructing messages

from jinja2 import Environment        # Jinja2 templating

TEMPLATE = """
<html>
    <head>
        <title>Chart</title>
    </head>
    <body>
        <div id="chart" width="50%">
            
        </div>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>

    <script>

    var options = {
        chart: {
            height: 350,
            width:500,
            type: 'bar',
            stacked: false
        },
        dataLabels: {
            enabled: false
        },
        series: [{
            name: 'Yesterday',
            type: 'column',
            data: [1.4, 2, 2.5, 1.5, 2.5]
        }, {
            name: 'Total',
            type: 'column',
            data: [1.1, 3, 3.1, 4, 4.1]
        }],
        stroke: {
            width: [1, 1, 4]
        },
        title: {
            text: 'Bobby - Top 5 performers report',
            align: 'left',
            offsetX: 110
        },
        xaxis: {
            categories: ['Kerala State   Mission', 'Bank of Baroda', 'Andhra Bank', 'Canara Bank', 'SBI'],
        },
        yaxis: [
            {
            axisTicks: {
                show: true,
            },
            axisBorder: {
                show: true,
                color: '#008FFB'
            },
            labels: {
                style: {
                color: '#008FFB',
                }
            },
            title: {
                text: "Transactions",
                style: {
                color: '#008FFB',
                }
            },
            tooltip: {
                enabled: true
            }
            }
        ],
        
        legend: {
            horizontalAlign: 'left',
            offsetX: 40
        }
        }

        var chart = new ApexCharts(
        document.querySelector("#chart"),
        options
        );


        chart.render();    
    </script>
</html>

"""  # Our HTML Template

# Create a text/html message from a rendered template
msg = MIMEText(
    Environment().from_string(TEMPLATE).render(
        title='Hello World!',
        name='Ramu'
    ), "html"
)

subject = "Subject Sample"
sender= "gvnramu@gmail.com"
recipient = "gvnramu@gmail.com"

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = recipient

# Send the message via our own local SMTP server.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.ehlo()
s.login(sender, "google@gvnr")
s.sendmail(sender, recipient, msg.as_string())
s.quit()