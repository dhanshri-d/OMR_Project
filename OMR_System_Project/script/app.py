import streamlit as st
import streamlit.components.v1 as stc
import numpy as np

# File Processing Pkgs
import pandas as pd
from PIL import Image 
from finalReview import grade_exam
img=None

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 



def main():
	st.title("File Upload")

	menu = ["Home","Dataset","DocumentFiles","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
		if image_file is not None:
		
			# To See Details
			st.write(type(image_file))
			st.write(dir(image_file))
			file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
			img = load_image(image_file)
			print("Image:", img)
			print("Image type:", type(img))
			print("Image is None:", img is None)
			#print("Image is a PIL image:", isinstance(img, Image.Image))
			#print("Image is a numpy array:", isinstance(img, np.ndarray))
			#print("Image shape:", img.shape)
			#print("Image data type:", img.dtype)
			img = np.array(img)
			st.write(file_details)

            

			OMR_prediction = grade_exam(img)#img = load_image(image_file)
			#print("SCore of student is: "grade_exam(img))
			st.write("OMR prediction %: ", OMR_prediction)#OMR_prediction = grade_exam(OMR_model, img)
			#st.write("OMR prediction: 80%")
            #image = load_image('example.png')
            #grade = grade_exam(image)
			#st.image(img,width=250,height=250)
   
   
   
	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.info("Created By Dhanashri")
		st.text("Dhanashri D")



import pickle


#OMR_model = pickle.load(open('OMR_DETECTION.sav','rb'))
#OMR_Prediction = OMR_model.grade_exam(img)
#
if __name__ == '__main__':
	main()
 
 


#python -m streamlit run 'app.py'

#streamlit run /home/dhanshri/Desktop/MajorProjectWork_2023/MyProject/app.py [ARGUMENTS]