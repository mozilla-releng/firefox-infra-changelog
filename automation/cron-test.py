from crontab import CronTab

cron = CronTab(user='riman')
job = cron.new(command='bash MAIN_script.sh')
job.minute.every(1)

cron.write()
