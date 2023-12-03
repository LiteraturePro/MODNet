import numpy as np
import streamlit as st
from PIL import Image, ImageOps
import time
import os
from io import BytesIO
import uuid
import inference_onnx
import shutil

#shutil.rmtree('input')
#os.mkdir('input')

def convert_bytes_to_image(img__name,img_bytes):
    #将bytes结果转化为字节流
    bytes_stream = img_bytes
    # BytesIO(img_bytes)
    #读取到图片
    if bytes_stream == None:
        pass
    else:
        # roiimg = Image.open(bytes_stream)
        roiimg = bytes_stream
        img_path = os.path.join('./input', img__name + ".jpg")
        imgByteArr = BytesIO()    #初始化一个空字节流
        roiimg.save(imgByteArr,format('PNG'))     #把我们得图片以‘PNG’保存到空字节流
        imgByteArr = imgByteArr.getvalue()    #无视指针，获取全部内容，类型由io流变成bytes。
        with open(img_path,'wb') as f:
            f.write(imgByteArr)
    return img_path
    

st.write("""
         # One click human matting 🍄
         """
         )
st.markdown('[![Github](http://jaywcjlove.github.io/sb/github/green-star.svg)](https://github.com/LiteraturePro/MODNet)')
st.write("This is a simple portrait to background web application, implemented using Modnet algorithm.")
imagetest = Image.open('./src/image.png')
st.image(imagetest)
file = st.file_uploader("", type=["jpg","jpeg", "png", "webp"])


if file is None:
    st.text("You haven't uploaded an image file.🎓")
else:
    imaget = Image.open(file)
    # st.write(image)
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,imaget)
    output_img_path = os.path.join('./output', img_name + ".png")
    image_save = os.path.join('./image_save', img_name + ".png")
    
    st.image(imaget,caption='Original Image',  use_column_width=True)
    # images = Image.open("C:\\Users\\literature\\Desktop\\测试图像\\imgs.png")
    # st.image(images, caption='Sunrise by the mountains', use_column_width=True)
    
    if st.button("Start"):
        # If the user uploads an image
            if imaget is not None:
                # Opening our image
                # image = Image.open(images)
                st.text("Please wait...")
                my_bar = st.progress(0)
                inference_onnx.main(input_img_path,output_img_path)
                image = Image.open(input_img_path)
                matte = Image.open(output_img_path)
                image.putalpha(matte)
                image.save(image_save)
                
                for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                st.success('Done! 🚀')
                st.balloons()
                if os.path.exists(input_img_path):  # 如果文件存在
                    os.remove(input_img_path)
                else:
                    st.error('no such file')  # 则返回文件不存在

                st.image(image_save, caption='Processed Image', use_column_width=True)
                st.subheader('Tips: Right click to save the picture!')
                if os.path.exists(output_img_path):  # 如果文件存在
                    os.remove(output_img_path)
                else:
                    st.error('no such file')  # 则返回文件不存在
                if os.path.exists(image_save):  # 如果文件存在
                    os.remove(image_save)
                else:
                    st.error('no such file')  # 则返回文件不存在
            else:
                st.slider("Can you please upload an image 🙇🏽‍♂️")
