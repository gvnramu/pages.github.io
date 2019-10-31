from crontab import CronTab

cron = CronTab(user='syntizen')
job = cron.new(command='python3 /home/syntizen/RAMU/workspace/email/sample.py')
job.minute.every(1)

cron.write()