import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="KABURA KURIA", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/c9c9f2f9-6c92-450f-987e-14d3f6e70b7e/lePlzenP35.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am KABURA KURIA")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python, flutter, Cybersec, AI, Animations to create mental health solutions. Currently. i'm working on a small project known as ATUNAFSI ."
    )
    st.write("[Volunteer for project ATUNAFSI >](https://docs.google.com/forms/d/e/1FAIpQLScjvjpUttnRWAATWuaqF826rkb1PaPXpnO9HNm7cQY7tLIx6g/viewform?usp=sf_link)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("FEATURES IN ATUNAFSI")
        st.write("##")
        st.write(
            """
            1. Social Media Timer: A timer feature that helps users manage their social media usage.

            2. Sensory Experience and Voice: Atunafsi will provide a sensory experience and voice feature that will enhance the user's experience.
            
            3. Find a Therapist - GPS: A GPS-enabled feature that helps users find a therapist in their area.
            
            4. Four User Roles: Atunafsi will have four user roles, including parent, psychologist, client under 18, and client above 18.
            
            5. Psychoeducation: A feature that provides users with educational resources related to mental health.
            
            6. Chat and Chat GPT: A chat feature that allows users to communicate with each other and a Chat GPT feature that provides automated responses.
            
            7. Customer Service and Emergency Helpline: A customer service feature that provides users with support and an emergency helpline feature that provides immediate assistance.
            
            8. Daraja API and Game Feature: Atunafsi will integrate the Daraja API for payment processing and a game feature that provides users with a fun and engaging experience.
            
            9. Crypto Feature: A crypto feature that allows users to use tokens or other forms of cryptocurrency.
            
            10. Light and Dark Mode: Atunafsi will have a light and dark mode feature that allows users to customize the app's appearance.
            
            11. Drawer and Calendar: A drawer feature that provides users with easy access to app features and a calendar feature that helps users manage their schedules.
            
            12. Analytics Dashboard and Progress Bars: An analytics dashboard that provides users with insights into their app usage and progress bars that track their progress.
            
            13. Journals: Atunafsi will have five journal features, including unexpected, social, emotional, cognitive, and physical.
            
            14. Social Factor Meter: A feature that helps users track their social interactions and relationships.
            
            15. Fitness and Well-being Features: Atunafsi will have fitness and well-being features that help users maintain a healthy lifestyle.
            
            16. Environmental Friendliness: Atunafsi will be designed to be environmentally friendly, with features that promote sustainability and reduce waste.
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
   

with st.container():
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """)

        st.markdown("<div>Teachable Machine Image Model</div>", unsafe_allow_html=True)
        st.markdown("<button type='button' onclick='init()'>Start</button>", unsafe_allow_html=True)
        st.markdown("<div id='webcam-container'></div>", unsafe_allow_html=True)
        st.markdown("<div id='label-container'></div>", unsafe_allow_html=True)

        # Add the JavaScript code as a string
        script = """
        <script src='https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js'></script>
        <script src='https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js'></script>
        <script type="text/javascript">
            // the link to your model provided by Teachable Machine export panel
            const URL = 'https://teachablemachine.withgoogle.com/models/pQe5QZukx/';
        
            let model, webcam, labelContainer, maxPredictions;
        
            // Load the image model and setup the webcam
            async function init() {
                const modelURL = URL + 'model.json';
                const metadataURL = URL + 'metadata.json';
        
                // load the model and metadata
                model = await tmImage.load(modelURL, metadataURL);
                maxPredictions = model.getTotalClasses();
        
                // Convenience function to setup a webcam
                const flip = true; // whether to flip the webcam
                webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
                await webcam.setup(); // request access to the webcam
                await webcam.play();
                window.requestAnimationFrame(loop);
        
                // append elements to the DOM
                document.getElementById('webcam-container').appendChild(webcam.canvas);
                labelContainer = document.getElementById('label-container');
                for (let i = 0; i < maxPredictions; i++) { // and class labels
                    labelContainer.appendChild(document.createElement('div'));
                }
            }
        
            async function loop() {
                webcam.update(); // update the webcam frame
                await predict();
                window.requestAnimationFrame(loop);
            }
        
            // run the webcam image through the image model
            async function predict() {
                // predict can take in an image, video or canvas html element
                const prediction = await model.predict(webcam.canvas);
                for (let i = 0; i < maxPredictions; i++) {
                    const classPrediction = prediction[i].className + ': ' + prediction[i].probability.toFixed(2);
                    labelContainer.childNodes[i].innerHTML = classPrediction;
                }
            }
        </script>
        """
        
        # Render the JavaScript code
        st.markdown(script, unsafe_allow_html=True)
        
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/alvinkuria369@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
