import streamlit as st

def analyze_sentiment(text):
    # Dummy sentiment analysis
    if "good" in text or "happy" in text:
        return "Positive"
    elif "bad" in text or "sad" in text:
        return "Negative"
    else:
        return "Neutral"

st.title("Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment.")

# Text input
user_input = st.text_area("Type your text here:")

if user_input:
    # Get sentiment analysis result
    sentiment = analyze_sentiment(user_input)
    
    # Display the result
    st.write(f"Sentiment: **{sentiment}**")



# import cv2
# import streamlit as st

# # Load the Haar Cascade for face detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# def detect_faces(frame):
#     if frame is None:
#         return None
    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     return frame

# # Streamlit app
# st.title("Webcam Face Detection")
# st.write("Open your webcam to detect faces.")

# # Initialize webcam state
# if 'webcam_running' not in st.session_state:
#     st.session_state.webcam_running = False
#     st.session_state.stop_button_counter = 0  # Counter for stop button

# # Start webcam button
# if st.button("Start Webcam", key="start_webcam_button"):
#     st.session_state.webcam_running = True

# if st.session_state.webcam_running:
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         st.error("Unable to open the webcam. Please check your camera.")
#     else:
#         stframe = st.empty()  # Create a placeholder for the webcam feed

#         while st.session_state.webcam_running:
#             ret, frame = cap.read()
#             if not ret:
#                 st.error("Failed to capture frame.")
#                 break
            
#             frame = detect_faces(frame)  # Detect faces in the frame

#             # Convert the frame to RGB
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             stframe.image(frame)  # Display the frame in the Streamlit app

#             # Stop button with unique key
#             if st.button(f"Stop Webcam {st.session_state.stop_button_counter}", key=f"stop_webcam_button_{st.session_state.stop_button_counter}"):
#                 st.session_state.webcam_running = False
#                 cap.release()
#                 st.session_state.stop_button_counter += 1  # Increment the counter
#                 st.success("Webcam stopped.")
#                 break  # Exit the loop

#         # Release the webcam when done
#         cap.release()
# else:
#     st.warning("Press the button to start the webcam.")


