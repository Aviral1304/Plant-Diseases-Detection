from plotly.validators.layout import margin
from tensorflow import keras
import numpy as np
from keras.utils import load_img, img_to_array
import PIL as Image

Li = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy',
      'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
      'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
      'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
      'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
      'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
      'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight',
      'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
      'Strawberry___Leaf_scorch',
      'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
      'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
      'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
      'Tomato___healthy']
import streamlit as st

st.title("Plant Diseases Detection")
st.header("Convolutional Neural Network (CNN) for Plant Disease Classification")
st.text("Upload a Plant leaf image to check your plant health :")

def import_and_classify(image_path, weights_file):
    model = keras.models.load_model(weights_file)
    new_img = keras.utils.load_img(image_path, target_size=(256, 256))
    img = keras.utils.img_to_array(new_img)
    img = np.expand_dims(img, axis=0)
    img = img / 255
    prediction = model.predict(img)
    probabilty = prediction.flatten()
    max_prob = probabilty.max()
    index = prediction.argmax(axis=-1)[0]
    class_name = Li[index]
    return class_name


uploaded_file = st.file_uploader("Choose a Plant Image", type=("jpg", "png", "jpeg"))
st.text("Accepted Plant leaf image | only jpg & jpeg & png files")

# To show sample
plant_scan = st.checkbox("How does an Plant image look")
if plant_scan:
    Image_1 = Image.open(r"C:\Users\avira\Final_Project\Mix_Plant\Web_folder\Image20230314214828.jpg")
    st.image(Image_1, width=300, caption='Sample Plant image')

if st.button('Check Results'):
    if uploaded_file is not None:
        image = load_img(uploaded_file, target_size=(256, 256))
        st.image(image, width=400, caption='Uploaded Plant image')
        st.write("")
        label = import_and_classify(uploaded_file.name, 'model_3.h5')  # Model Directory
        # st.write(label)
        for i in range(len(Li)):
            if label == Li[i]:
                b = i

        if b == 0:
            st.write("Apple___Apple_scab")
            st.write('''Treatment :
Apple scab is a fungal disease that affects apple trees and can cause significant damage to the fruit and leaves. The disease is caused by the fungus Venturia inaequalis and can be treated with various methods. Pruning: Pruning is an effective method for treating apple scab. Remove infected leaves and fruit from the tree as soon as possible, and prune the tree to increase air circulation. Fungicides: Fungicides can be used to treat apple scab, but they should be used as a last resort. Apply fungicides early in the season, before the disease appears, to prevent it from spreading. Cultural controls: Cultural controls include removing fallen leaves and fruit from the ground and keeping the area around the tree free of debris. This can help reduce the amount of fungal spores that are present. Resistant varieties: Planting resistant varieties of apple trees can be an effective way to prevent apple scab. Resistant varieties include Liberty, Enterprise, and GoldRush. Biological controls: Biological controls include using beneficial insects and fungi to control the spread of the disease. For example, the fungus Beauveria bassiana can be used to kill the larvae of the codling moth, which can spread apple scab.
''')
        elif b == 1:
            st.write("Apple___Black_rot")
            st.write('''Treatment :
Apple black rot is a fungal disease that affects apple trees and can cause significant damage to fruit and leaves. The disease is caused by the fungus Botryosphaeria obtusa and can be treated with various methods. Pruning: Pruning is an effective method for treating apple black rot. Remove infected branches, leaves, and fruit from the tree as soon as possible. Prune the tree to increase air circulation and reduce the amount of moisture in the canopy. Fungicides: Fungicides can be used to treat apple black rot. Apply fungicides early in the season, before the disease appears, to prevent it from spreading. Fungicides that are effective against apple black rot include captan, mancozeb, and thiophanate-methyl. Cultural controls: Cultural controls include removing fallen leaves and fruit from the ground and keeping the area around the tree free of debris. This can help reduce the amount of fungal spores that are present. Resistant varieties: Planting resistant varieties of apple trees can be an effective way to prevent apple black rot. Resistant varieties include Liberty, Enterprise, and GoldRush. Biological controls: Biological controls include using beneficial insects and fungi to control the spread of the disease. For example, the fungus Trichoderma harzianum can be used to reduce the severity of apple black rot.''')
        elif b == 2:
            st.write("Apple___Cedar_apple_rust")
            st.write('''Treatment :
Apple Cedar apple rust is a fungal disease that affects apple trees. The fungus responsible for the disease has a complex life cycle that requires two hosts to complete. The disease causes yellow or orange spots on the leaves, and it may also affect the fruit, causing it to become distorted and drop prematurely. The best way to prevent Cedar apple rust is to remove any nearby juniper trees, which can serve as a host for the fungus. Fungicides can also be used to control the disease, but they must be applied at the right time and with the right frequency to be effective.''')

        elif b == 3:
            st.write("Apple___healthy")

        elif b == 4:
            st.write("Blueberry___healthy")

        elif b == 5:
            st.write("Cherry_(including_sour)___healthy")

        elif b == 6:
            st.write("Cherry_(including_sour)___Powdery_mildew")
            st.write('''Treatment :
Cherry trees, including sour cherries, can be susceptible to powdery mildew, a fungal disease that can affect many types of plants. Treatment: If you notice powdery mildew on your cherry trees, you can try treating it with a fungicide. Look for products that are specifically labeled for powdery mildew on cherry trees, and follow the instructions carefully. You may also want to consult with a professional arborist or horticulturist for more personalized advice on treating the disease.
''')
        elif b == 7:
            st.write("Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot")
            st.write('''Treatment :
Cercospora leaf spot and gray leaf spot are two common fungal diseases that can affect corn, also known as maize. Treatment: If you notice Cercospora or gray leaf spot on your corn plants, you can try treating them with a fungicide. Look for products that are specifically labeled for these diseases on corn, and follow the instructions carefully. You may also want to consult with a professional agronomist for more personalized advice on treating the disease.
''')

        elif b == 8:
            st.write("Corn_(maize)___Common_rust_")
            st.write('''Treatment :
Common rust is a fungal disease that can affect corn, also known as maize. Treatment: If you notice common rust on your corn plants, you can try treating them with a fungicide. Look for products that are specifically labeled for common rust on corn, and follow the instructions carefully. You may also want to consult with a professional agronomist for more personalized advice on treating the disease.''')
        elif b == 9:
            st.write("Corn_(maize)___healthy")
        elif b == 10:
            st.write("Corn_(maize)___Northern_Leaf_Blight")
            st.write('''Treatment :
Northern leaf blight is a fungal disease that can affect corn, also known as maize. Treatment: If you notice northern leaf blight on your corn plants, you can try treating them with a fungicide. Look for products that are specifically labeled for northern leaf blight on corn, and follow the instructions carefully. You may also want to consult with a professional agronomist for more personalized advice on treating the disease.''')

        elif b == 11:
            st.write("Grape___Black_rot")
            st.write('''Treatment :
Black rot is a fungal disease that can affect grapevines. Treatment: If you notice black rot on your grapevines, you can try treating them with a fungicide. Look for products that are specifically labeled for black rot on grapes, and follow the instructions carefully. It is important to note that once black rot has infected the grapes, there is no cure, and fungicides are not effective. Therefore, it's important to practice prevention and early detection.''')
        elif b == 12:
            st.write("Grape___Esca_(Black_Measles)")
            st.write('''Treatment :
Esca, also known as black measles, is a fungal disease that can affect grapevines. Treatment: If you notice esca on your grapevines, there is no known cure for the disease, and fungicides are not effective. However, there are several cultural practices that can help manage the disease, including cutting out infected wood, using wound protectants, and managing the canopy to reduce humidity and improve air circulation. It is important to note that early detection and prevention are key to managing esca.
''')
        elif b == 13:
            st.write("Grape___healthy")
        elif b == 14:
            st.write("Grape___Leaf_blight_(Isariopsis_Leaf_Spot)")
            st.write('''Treatment :
Grape leaf blight, also known as Isariopsis leaf spot, is a fungal disease that affects the leaves of grapevines. Treatment: If you notice grape leaf blight on your grapevines, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning, removing infected plant debris, and avoiding overhead irrigation can help manage the disease.''')
        elif b == 15:
            st.write("Orange___Haunglongbing_(Citrus_greening)")
            st.write('''Treatment :
Huanglongbing (HLB), also known as citrus greening, is a bacterial disease that affects citrus trees, including oranges. Treatment: Currently, there is no known cure for HLB, and affected trees will eventually decline and die. However, there are several management practices that can help extend the life of infected trees, including regular nutrient and water management, maintaining a healthy root system, and controlling secondary pests and diseases.
''')
        elif b == 16:
            st.write("Peach___Bacterial_spot")
            st.write('''Treatment :
Bacterial spot is a common disease of peach trees caused by the bacterium Xanthomonas arboricola pv. pruni. Treatment: If you notice bacterial spot on your peach trees, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.''')
        elif b == 17:
            st.write("Peach___healthy")
        elif b == 18:
            st.write("Pepper,_bell___Bacterial_spot")
            st.write('''Treatment :
Bacterial spot is a common disease of pepper plants, including bell peppers, caused by the bacterium Xanthomonas campestris pv. vesicatoria. Treatment: If you notice bacterial spot on your pepper plants, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.
''')
        elif b == 19:
            st.write("Pepper,_bell___healthy")
        elif b == 20:
            st.write("Potato___Early_blight")
            st.write('''Treatment :
Early blight is a common fungal disease of potato plants caused by the fungus Alternaria solani. Treatment: If you notice early blight on your potato plants, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.''')
        elif b == 21:
            st.write("Potato___healthy")
        elif b == 22:
            st.write("Potato___Late_blight")
            st.write('''Treatment :
Late blight is a destructive fungal disease of potato plants caused by the water mold Phytophthora infestans. Treatment: If you notice late blight on your potato plants, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.''')
        elif b == 23:
            st.write("Raspberry___healthy")
        elif b == 24:
            st.write("Soybean___healthy")
        elif b == 25:
            st.write("Squash___Powdery_mildew")
            st.write('''Treatment :
Powdery mildew is a common fungal disease of squash plants caused by the fungus Podosphaera xanthii. Treatment: If you notice powdery mildew on your squash plants, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.''')
        elif b == 26:
            st.write("Strawberry___healthy")
        elif b == 27:
            st.write("Strawberry___Leaf_scorch")
            st.write('''Treatment :
Leaf scorch is a common fungal disease of strawberry plants caused by the fungus Diplocarpon earliana. Treatment: If you notice leaf scorch on your strawberry plants, there are several fungicides available that can help manage the disease. However, it is important to note that fungicides are most effective when applied preventatively or at the first sign of disease. Additionally, cultural practices such as pruning and removing infected plant material can help manage the disease.''')

        elif b == 28:
            st.write("Tomato___Bacterial_spot")
            st.write('''Treatment :
Copper fungicides are the most commonly recommended treatment for bacterial leaf spot. Use copper fungicide as a preventive measure after you’ve planted your seeds but before you’ve moved the plants into their permanent homes. You can use copper fungicide spray before or after a rain, but don’t treat with copper fungicide while it is raining. If you’re seeing signs of bacterial leaf spot, spray with copper fungicide for a seven- to 10-day period, then spray again for one week after plants are moved into the field. Perform maintenance treatments every 10 days in dry weather and every five to seven days in rainy weather.''')

        elif b == 29:
            st.write("Tomato___Early_blight")
            st.write('''Treatment :
Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic..''')

        elif b == 30:
            st.write("Tomato___healthy")

        elif b == 31:
            st.write("Tomato___Late_blight")
            st.write('''Treatment :
Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic..''')
        elif b == 32:
            st.write("Tomato___Leaf_Mold")
            st.write('''Treatment :
Use drip irrigation and avoid watering foliage. Use a stake, strings, or prune the plant to keep it upstanding and increase airflow in and around it. Remove and destroy (burn) all plants debris after the harvest.''')

        elif b == 33:
            st.write("Tomato___Septoria_leaf_spot")
            st.write('''Treatment :
Removing infected leaves: Remove infected leaves immediately, and be sure to wash your hands and pruners thoroughly before working with uninfected plants.
Consider organic fungicide options: Fungicides containing either copper or potassium bicarbonate will help prevent the spreading of the disease. Begin spraying as soon as the first symptoms appear and follow the label directions for continued management.
Consider chemical fungicides: While chemical options are not ideal, they may be the only option for controlling advanced infections. One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil).
''')

        elif b == 34:
            st.write("Tomato___Spider_mites Two-spotted_spider_mite")
            st.write('''Treatment :
For control, use selective products whenever possible. Selective products which have worked well in the field include: bifenazate (Acramite): Group UN, a long residual nerve poison abamectin (Agri-Mek): Group 6, derived from a soil bacterium spirotetramat (Movento): Group 23, mainly affects immature stages spiromesifen (Oberon 2SC): Group 23, mainly affects immature stages OMRI-listed products include: insecticidal soap (M-Pede) neem oil (Trilogy) soybean oil (Golden Pest Spray Oil) With most miticides (excluding bifenazate), make 2 applications, approximately 5-7 days apart, to help control immature mites that were in the egg stage and protected during the first application. Alternate between products after 2 applications to help prevent or delay resistance.''')
        elif b == 35:
            st.write("Tomato___Target_Spot")
            st.write('''Treatment :
Many fungicides are registered to control of target spot on tomatoes. Growers should consult regional disease management guides for recommended products. Products containing chlorothalonil, mancozeb, and copper oxychloride have been shown to provide good control of target spot in research trials''')
        elif b == 36:
            st.write("Tomato___Tomato_mosaic_virus")
            st.write('''Treatment :
There are no cures for viral diseases such as mosaic once a plant is infected. As a result, every effort should be made to prevent the disease from entering your garden.
1.Fungicides will NOT treat this viral disease.
2.Plant resistant varieties when available or purchase transplants from a reputable source.
3.Do NOT save seed from infected crops.
4.Spot treat with least-toxic, natural pest control products, such as Safer Soap, Bon-Neem and diatomaceous earth, to reduce the number of disease carrying insects.
5.Harvest-Guard® row cover will help keep insect pests off vulnerable crops/ transplants and should be installed until bloom.
6.Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.
7.The virus can be spread through human activity, tools and equipment. Frequently wash your hands and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4 parts water) to reduce the risk of contamination.
8.Avoid working in the garden during damp conditions (viruses are easily spread when plants are wet).
9.Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.
10.Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost.''')

        elif b == 37:
            st.write("Tomato___Tomato_Yellow_Leaf_Curl_Virus")
            st.write('''Treatment :
Inspect plants for whitefly infestations two times per week. If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or insecticidal soap. For more effective control, it is recommended that at least two of the above insecticides be rotated at each spraying.''')
