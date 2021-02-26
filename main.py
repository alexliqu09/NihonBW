import streamlit as st 
import torch
import os
import smtplib
import mimetypes
from pytorchpix2pix.options.test_options import TestOptions
from pytorchpix2pix.data import create_dataset
from pytorchpix2pix.models import create_model
from pytorchpix2pix.util.visualizer import save_images
from pytorchpix2pix.util import html
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.encoders import encode_base64
from PIL import Image
import time
class Model():
        
        
        def __init__(self):

              self.name_real=None
              self.name_fake=None
              self.name_BW=None
              self.inicio=None
              self.final=None

        def send_image(self, path,name,caption,width):
                '''
                   Esta Función plotea cualquier imágen a la interfaz Gŕafica , con excepción de las generadas 
                   por las inferencias de los modelos.
                   path = Estamos pasando la ruta relativa de la imágen.
                   name ="El nombre de la Imagen  a la cual vamos a plotear.
                   caption = El titulo de de la imágen ploteada.
                   width = El tamaño de la imágen.
                '''
                image=Image.open(path+name)
                st.image(image,caption=caption,width=width)    
        
        def load_image_model(self, Option,name,caption,width):
                '''
                Esta función sirve para subir las imágenes generadas unicamente por los modelos
                Option = Variable  a la cual se le pasa por parámetros Pix2Pix,InstColorization para enviar la imagen desde su ruta relativa
                name = Nombre de la imagen.
                caption = titulo de la imagen
                width= tamaño de la imagen
                '''
                if Option=="Pix2Pix":
                        image=Image.open("../NihongoBW/test_pix2pix/"+name)
                        st.image(image,caption=caption,width=width)

        def loadImage(self, Option_model):
                '''
                Esta función le pide a tú pc una imagen de tipo jpg , png o jpeg (Recomendación usar JPG ya que 
                los modelos usan este tipo de archivo).
                Option = Le damos de opciones BW , Pix2Pix , InstColorization.
                '''
                uploaded_file = st.file_uploader("Choose an image...", type="jpg"or"png"or"jpeg")   # uploaded_file es tipo ByteIO
                if uploaded_file is not None:
                        image = Image.open(uploaded_file)
                        if Option_model =='BW':
                                self.name_BW=str(uploaded_file)+'.jpg'
                                image.save("../NihongoBW/BW/Images/"+self.name_BW)
                                self.bw("../NihongoBW/BW/Images/")
                        if Option_model=='Pix2Pix':
                                self.name_real=str(uploaded_file)+'.jpg'
                                self.name_fake=str(uploaded_file)+'_fake_B_rgb.png'
                                image.save('../NihongoBW/imgs/'+str(uploaded_file)+'.jpg')
                                image.save('../NihongoBW/pytorchpix2pix/colorization/test/'+'test.jpg')
        
        def Pix2Pix(self):
                opt = TestOptions().parse()  # get test options
                # hard-code some parameters for test
                opt.num_threads = 0   # test code only supports num_threads = 0
                opt.batch_size = 1    # test code only supports batch_size = 1
                opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
                opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
                opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
                dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options
                model = create_model(opt)      # create a model given opt.model and other options
                model.setup(opt)               # regular setup: load and print networks; create schedulers
                # create a website
                web_dir = os.path.join(opt.results_dir, opt.name, '{}_{}'.format(opt.phase, opt.epoch))  # define the website directory
                if opt.load_iter > 0:  # load_iter is 0 by default
                        web_dir = '{:s}_iter{:d}'.format(web_dir, opt.load_iter)
                print('creating web directory', web_dir)
                webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.epoch))
                # test with eval mode. This only affects layers like batchnorm and dropout.
                # For [pix2pix]: we use batchnorm and dropout in the original pix2pix. You can experiment it with and without eval() mode.
                # For [CycleGAN]: It should not affect CycleGAN as CycleGAN uses instancenorm without dropout.
                if opt.eval:
                        model.eval()
                for i, data in enumerate(dataset):
                        if i >= opt.num_test:  # only apply our model to opt.num_test images.
                                break
                        model.set_input(data)  # unpack data from data loader
                        self.inicio=time.time()             
                        model.test()           # run inference
                        self.final=time.time()
                        visuals = model.get_current_visuals()  # get image results
                        img_path = model.get_image_paths()     # get image paths
                        if i % 5 == 0:  # img_path = model.get_isave images to an HTML file
                                print('processing (%04d)-th image... %s' % (i, img_path))
                                save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize)
                webpage.save()  # save the HTML
        
        def bw(self, ruta):
                '''
                Esta función convierta ha blanco y negro la imagen
                ruta = "Le pasa la ruta relativa donde se encuentra imágen.
                '''
                img=Image.open(ruta+self.name_BW).convert('L')
                img.save("../NihongoBW/BW/Result/"+self.name_BW)

        def message(self, correo,password,Option):
                '''
                Esta función nos permite enviar al correo las imagenes utilizando los protocolo smtp
                (protocolo básico que permite que los emails viajen a través de Internet)
                Nota: necesitas desactivar la protección de accesos de apps menos seguros, ver este link: [https://myaccount.google.com/lesssecureapps], 
                o este link https://support.google.com/accounts/answer/6010255?hl=es-419#zippy=%2Csi-est%C3%A1-activada-la-opci%C3%B3n-acceso-de-apps-menos-seguras
                -Correo = Le pasas de parámetro de correo.
                -Password = Le pasas tú contraseña.
                -Option = Le damos de opciones BW , Pix2Pix , InstColorization.
                '''
                if Option=="BW":
                        path="../NihongoBW/BW/Result/"+self.name_BW
                if Option=="Pix2Pix":
                        path="../NihongoBW/test_pix2pix/"+self.name_fake
                msg = MIMEMultipart() 
                msg['From']=correo
                msg['To']=correo
                msg['Subject']="Su Imagen Solicitada"
                file = open(path,"rb")
                attach_image = MIMEImage(file.read(),_subtype="jpg")   
                attach_image.add_header('Content-Disposition', 'attachment; filename = "Imagen.png"')
                msg.attach(attach_image)  
                mailServer = smtplib.SMTP('smtp.gmail.com',587)
                mailServer.ehlo()  
                mailServer.starttls() 
                mailServer.ehlo()
                mailServer.login(correo,password)
                mailServer.sendmail(correo,correo, msg.as_string())
                mailServer.close()

        def time(self):
                '''
                Esta función se encarga de ver el tiempo de inferencia del modelo.
                '''
                return self.final-self.inicio
        def img_to_bytes(self , img_path):
                img_bytes = Path(img_path).read_bytes()
                encoded = base64.b64encode(img_bytes).decode()
                return encoded
if __name__ == '__main__':

        Radio =st.sidebar.radio("Select",("Home","Pix2Pix","BW","InstColorization","About"))
        M=Model()
        if  Radio=='Home':

                st.markdown("<h1 style='text-align: center; color: red;'> NihonBW </h1>", unsafe_allow_html=True)
                M.send_image('../NihongoBW/src/Images/',"NihonBW.jpeg","The Imperial House of Japan",750)  
                st.title("About the work")
                st.markdown("NihonBW is a project that provides a service to convert Black and white Image to Color and this model  focus of black and white image , and Why the NihonBW?, because the data have used in my project is from the culture , Japanese ,\n where I gathered different image from some  prefecture of Japan \n , e.g- Hokkaido , Tokyo , Kyoto , Osaka and more hope you delight to this work.")
                st.title("Pix2Pix model")
                st.markdown("This model was developed to apply  an approach to multiple problems, e.g- day to night ,\n border to photos, aerial map, black and white color ,\n the paper is available [here](https://phillipi.github.io/pix2pix/) . We have available  BW to Color model .")
                M.send_image('../NihongoBW/src/Images/',"Pix2Pix_model.jpg","Pix2Pix model",600) 
                st.title("InstColorization: ")
                st.markdown("Instance conscious color is a modern approach to the problem of image color, which is based on the use \n of detection models and thus avoid the problem of previous models could not focus on an object.")
                M.send_image('../NihongoBW/src/Images/',"InstColorization_proof.jpg","InstColorization",600)                   
                st.title("BW: ")
                st.markdown("We have Available the function convert Color image to Black and White")
                M.send_image('../NihongoBW/src/Images/',"HBW.jpg","Result BW",600)   
        
        if Radio=='Pix2Pix':

                st.markdown("<h1 style='text-align: center; color: red;'> Pix2Pix model </h1>", unsafe_allow_html=True)
                M.send_image('../NihongoBW/src/Images/',"Pix2Pix.jpg","Pix2Pix",750)
                st.title("Write your Email")
                Correo =st.text_input("Correo","")
                password=st.text_input("password","",type='password')
                M.loadImage('Pix2Pix')
                st.header("Press the buttom, and convert your BW image")
                buttom=st.button("Pix2Pix")

                if buttom:

                        M.Pix2Pix()
                        st.header("Images")
                        M.send_image('../NihongoBW/pytorchpix2pix/colorization/test/','test.jpg',"your image",300)
                        image=Image.open('../NihongoBW/pytorchpix2pix/results/experiment_name/test_latest/images/test_fake_B_rgb.png')
                        image.save('../NihongoBW/test_pix2pix/'+M.name_fake)
                        M.send_image('../NihongoBW/pytorchpix2pix/results/experiment_name/test_latest/images/',"test_real_A.png","convert_images",300)
                        M.load_image_model("Pix2Pix",M.name_fake,"Result",300)
                        #st.write("tiempo de inferencia de pix2pix: "+str(M.time()))
                        M.message(Correo,password,"Pix2Pix")
                        print("the time inference is: "+str(M.time()))
                        #st.write(str(M.time()))

        if Radio=='BW':

                st.markdown("<h1 style='text-align: center; color: red;'> Convert Color Images to Black and White </h1>", unsafe_allow_html=True)
                M.send_image('../NihongoBW/src/Images/',"BW.jpg","Result BW",750)
                st.title("Write your Email")
                Correo =st.text_input("Correo","")
                password=st.text_input("password","",type='password')
                M.loadImage('BW')
                st.header("Press the buttom for convert the Image")
                buttom=st.button("BW")
                if buttom:
                        st.header("Images")
                        M.send_image("../NihongoBW/BW/Images/",M.name_BW,"Original",400)
                        M.send_image("../NihongoBW/BW/Result/",M.name_BW,"Result",400)
                        M.message(Correo,password,"BW")

        if Radio=='InstColorization':

                st.markdown("<h1 style='text-align: center; color: red;'> InstColorization </h1>", unsafe_allow_html=True)
                M.send_image('../NihongoBW/src/Images/',"InstColorization.png","InstColorization",750)
                st.title("Coming Soon")
                st.write("This model will be available soon, at the moment you have this colab available to train the [model](https://colab.research.google.com/github/alexliqu09/NihonBW/blob/main/Notebook_colabs/InstColorization/InstanceColorization.ipynb) yourself.")
                st.title("Some results")
                M.send_image("../NihongoBW/src/Images/","Image_proof_instance.jpg","Image 1",500)
                M.send_image("../NihongoBW/src/Images/","Image_proof_instcolorizatib2.jpg","Image 2",500)
                M.send_image("../NihongoBW/src/Images/","Image3.jpg","Image 3",500)
        if Radio=='About':
                
                st.markdown("<h1 style='text-align:left; color: red;'> About </h1>", unsafe_allow_html=True)
                M.send_image('../NihongoBW/src/Images/',"Author.jpg","Author",400)
                st.title("Me")
                st.markdown("I am researcher of Deep Learning. I think the AI is the present and future of technology development. \n My motivation to carry out this project is because I want to deep in the Image Processing \n and also I wanted to learn about the culture and apply the data of Japan. \n")
                st.title("Contact me")
                st.markdown("If want to contact me ,you should see: \n My Email is [here](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=alexander.lique.l@uni.pe) \n My Github is [here](https://github.com/alexliqu09),\n My Twitter is [here](https://twitter.com/lique_alex)")