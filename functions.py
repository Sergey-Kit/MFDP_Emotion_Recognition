import emotion
import pandas as pd
import msoffcrypto
import io
from PIL import Image
import requests
import os
import cv2

BASE_SAVE_PATH = './IMAGES'
PATH = 'URLsWithEmotionCat_aws.xlsx'

# Model usage
#args = emotion.parse_args()
#print(args)
#emotion.main(args)

#Excel parsing and emotion prediction loop
def read_excel(): 
    temp = io.BytesIO()
    with open(PATH, 'rb') as f:
        excel_file = msoffcrypto.OfficeFile(f)
        excel_file.load_key('A1015@1807')
        excel_file.decrypt(temp)
        df = pd.read_excel(temp)
        del temp
    return df

def limit_emotions(df):
    df1 = df[(df['angrily_disgusted'] != 1) & 
        (df['angrily_surprised'] != 1) &
        (df['appalled'] != 1) &
        (df['awed'] != 1) &
        (df['fearfully_angry'] != 1) &
        (df['fearfully_surprised'] != 1) &
        (df['happily_disgusted'] != 1) &
        (df['happily_surprised'] != 1) &
        (df['sadly_angry'] != 1) &
        (df['sadly_disgusted'] != 1)
        ].copy()
    df1.drop(columns=['angrily_disgusted',
                    'angrily_surprised',
                    'appalled',
                    'awed',
                    'fearfully_angry',
                    'fearfully_surprised',
                    'happily_disgusted',
                    'happily_surprised',
                    'sadly_angry',
                    'sadly_disgusted'], inplace=True)
    
    df1.reset_index(inplace=True)
    df1.drop(columns=['index'], inplace=True)
    dummies = df1.copy()
    df1['y'] = dummies.iloc[:, 2:].idxmax(1)
    df1 = df1[['url_server','y']]
    return df1


def save_img(im, img_name, ext):
    save_path = os.path.join(BASE_SAVE_PATH)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    #im.save(f'{img_name}.{ext}', 'JPEG')
    cv2.imwrite(os.path.join(save_path , f'{img_name}{ext}'), im)

def excel_parse():
    df = read_excel()
    url = df['url_server'][1]
    im = Image.open(requests.get(url, stream=True).raw)
    #image = cv2.imread(requests.get(url, stream=True).raw)
    f_name, ext = os.path.splitext(url)
    img_name = f_name.split('/')[-1]

    save_img(im, img_name, ext)

    return im

if __name__ == "__main__":
    df = read_excel()
    limit_emotions(df)