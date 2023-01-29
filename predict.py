from tensorflow import keras
import pandas as pd
import numpy as np

model_1 = keras.models.load_model('model')

THRESHOLD = 71.073

threat_labels = {
    0 :'normal',
    1 : 'threat'}
input_df = pd.read_csv("input_data.csv")

output_list = []
for index, rows in input_df.iterrows():
    input_list =[rows.email_n_pc2,rows.email_send_mail_n_pc2,rows.usb_mean_usb_dur,rows.workhouremail_n_pc2,rows.n_usb,rows.usb_mean_file_tree_len,rows.workhouremail_send_mail_n_pc2,
         rows.workhourusb_n_pc0,rows.workhourusb_mean_usb_dur,rows.usb_n_pc0,rows.n_workhourusb,rows.http_leakf_mean_url_len,rows.http_n_pc0,rows.day]
    numx = np.array(input_list)
    numx.shape[0]
    X = np.reshape(numx, (1,14,1))

    y_pred= model_1.predict(X)

    reconstruction_loss = np.mean(np.abs(y_pred - X), axis=1)[0][0]
    # preds = np.max(y_pred, axis=1)


    if reconstruction_loss >THRESHOLD: 
        prediction_class = 1
    else:
        prediction_class = 0

    prediction_label = threat_labels[prediction_class]

    
    output_list.append({"user_id": rows.user_id,"result":prediction_label})
    
print("output user list", output_list)







# X = input_df.drop('insider',axis=1)
# #threat example
# email_n_pc2 = 6
# email_send_mail_n_pc2 = 56
# usb_mean_usb_dur = 8
# workhouremail_n_pc2 = 999 
# n_usb = 99
# usb_mean_file_tree_len = 100
# workhouremail_send_mail_n_pc2 = 99
# workhourusb_n_pc0 = 7
# workhourusb_mean_usb_dur = 6
# usb_n_pc0 = 500
# n_workhourusb = 10
# http_leakf_mean_url_len = 143
# http_n_pc0 = 500
# day = 5

# # normal example
# email_n_pc2 = 0
# email_send_mail_n_pc2 = 0
# usb_mean_usb_dur = 0
# workhouremail_n_pc2 = 0 
# n_usb = 0
# usb_mean_file_tree_len = 0
# workhouremail_send_mail_n_pc2 = 0
# workhourusb_n_pc0 = 0
# workhourusb_mean_usb_dur = 0
# usb_n_pc0 = 0
# n_workhourusb = 0
# http_leakf_mean_url_len = 0
# http_n_pc0 = 100
# day = 5

# input_list = [email_n_pc2,email_send_mail_n_pc2,usb_mean_usb_dur,workhouremail_n_pc2,n_usb,usb_mean_file_tree_len,workhouremail_send_mail_n_pc2,
#          workhourusb_n_pc0,workhourusb_mean_usb_dur,usb_n_pc0,n_workhourusb,http_leakf_mean_url_len,http_n_pc0,day]
