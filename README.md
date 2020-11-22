# speedtest-with-chart-report
This setup will run the speedtest script from Ookla on a linux server every 6 hours, log these in /var/log/speedtest and generate a graphical report of the download and upload speeds once a week to be sent by email to the user. Tested on Ubuntu server 18.04

## install
- install speedtest-cli for command line from ookla https://www.speedtest.net/apps/cli matching your distribution.
- copy the contents of the folders etc, var and srv to /etc, /var and /srv respectively.
- add the following to the crontab: 
0 */6   * * *   root /srv/speedtest/speedtest.sh

- make sure you have a working cron setup that calls the folder /etc/cron.weekly with run-parts or run the script /etc/cron.weekly/speedreport manually. Don't forget to change the email address to yours in this script.

Feel free to fork or adapt to your needs.

See "speedtest.png" for an example of the graphical output.
