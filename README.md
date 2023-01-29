Detecting insider threats in an organization by analyzing user computer data using LSTM autoencoder model

Dataset can be downloaded from : https://web.cs.dal.ca/~lcd/data/CERTr5.2/day-r5.2.csv.gz

Each user/employee has access to two computers. PC0 and PC2.  PC2 can be avirtual server or computer which can be accessed from PC0

The user employee can log off after his working hours ends or he can work over time after his working hours have ended and can log off later



The features are: 



1) email_n-pc2 - Count of total number of emails processed in PC2 till logging off (sent + receieved)

2) email_send_mail_n-pc2 - Count of total number of emails sent from PC2 

3) usb_mean_usb_dur - Fraction of time for which the user uses the usb . 0 if the user does not use any usb. -1 if the user uses the usb till he logs out 

4) workhouremail_n-pc2 - Count of total number of emails processed in PC2 during working hours (sent + receieved)

5) n_usb - Count of total number of usb devices used by the user till logging off

6) usb_mean_file_tree_len - average file tree depth inside the usbs used by the user

7) workhouremail_send_mail_n-pc2 - Count of total number of emails sent from PC2  during working hours

8) workhourusb_n-pc0 - Count of total number of usb devices used on PC0 by the user during working hours

9) workhourusb_mean_usb_dur - Fraction of time based on working hours for which the user uses the usb . 0 if the user does not use any usb during working hours. -1 if 	the user uses the usb till the end of his working hours

10) usb_n-pc0 - Count of total number of usb devices used on PC0 by the user till logging off

11) n_workhourusb - Count of total number of usb devices used the user during working hours on both PC0 and PC2

12) http_leakf_mean_url_len - The average clicks required to reach the http websites/pages the employee have visited

13) http_n-pc0 - total number of http websites visited by the user on PC0 till logging off 

14) day -  the number of days the employee has been working in the company