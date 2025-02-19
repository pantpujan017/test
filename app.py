import streamlit as st
import time
from PIL import Image
import base64
import os

def main():
    st.set_page_config(page_title="Happy Birthday Sonu! 🎉", layout="wide")
    
    # Initialize session state
    if 'current_state' not in st.session_state:
        st.session_state.current_state = 'dark'
    if 'music_playing' not in st.session_state:
        st.session_state.music_playing = False
    
    # Enhanced CSS styling
    st.markdown("""
        <style>
        @keyframes disco {
            0% { background-color: rgba(255, 0, 0, 0.2); }
            25% { background-color: rgba(0, 255, 0, 0.2); }
            50% { background-color: rgba(0, 0, 255, 0.2); }
            75% { background-color: rgba(255, 255, 0, 0.2); }
            100% { background-color: rgba(255, 0, 255, 0.2); }
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
        }
        
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        
        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }

        .disco-room {
            animation: disco 2s infinite;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            min-height: 400px;
        }
        
        .dark-room {
            background-color: #1a1a1a;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            min-height: 400px;
        }

        .photo-container {
            max-width: 150px;
            margin: auto;
            padding: 10px;
        }

        .photo-frame {
            border: 5px solid #FFD700;
            border-radius: 10px;
            padding: 5px;
            box-shadow: 0 0 20px rgba(255,215,0,0.5);
            transition: transform 0.3s;
            margin: auto;
            overflow: hidden;
        }

        .photo-frame img {
            width: 100% !important;
            height: 120px !important;
            object-fit: cover !important;
            border-radius: 5px !important;
        }

        .blinking-lights { 
            animation: blink 1s infinite; 
            font-size: 2em; 
            letter-spacing: 15px; 
        }
        .floating { 
            animation: float 3s infinite ease-in-out; 
            display: inline-block; 
        }
        .heartbeat { 
            animation: heartbeat 1s infinite; 
            display: inline-block; 
        }
        .message { 
            font-size: 24px; 
            color: #FF69B4; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3); 
            margin: 20px 0; 
        }
        .cake { 
            font-size: 100px; 
            margin: 20px 0; 
            display: inline-block; 
            animation: float 3s infinite ease-in-out; 
        }
        .photo-frame:hover { 
            transform: scale(1.05); 
        }
        .celebration { 
            font-size: 3em; 
            position: fixed; 
            animation: float 3s infinite ease-in-out; 
        }
        
        /* Hide the default audio player when not needed */
        .hide-audio-player {
            display: none;
        }
        
        /* Style music control buttons */
        .music-control-btn {
            background-color: #FF69B4;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        .music-control-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        
        /* Streamlit elements customization */
        div.stButton > button {
            background-color: #FF69B4;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        div.stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }
        
        /* Audio player container positioning */
        .audio-player-container {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
            width: 50px;
            height: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Create a sidebar container for the music player that will persist across all states
    with st.sidebar:
        st.header("🎵 Music Controls")
        
        # Load audio file
        try:
            audio_file = open("play.mp3", "rb")
            audio_bytes = audio_file.read()
            
            if st.button("🎵 Play/Pause Music", key="global_music_toggle"):
                st.session_state.music_playing = not st.session_state.music_playing
            
            # Display audio player based on state
            if st.session_state.music_playing:
                st.audio(audio_bytes, format='audio/mp3', start_time=0)
                st.write("🔊 Music Playing")
            else:
                st.write("🔇 Music Paused")
                
        except FileNotFoundError:
            st.error("Music file 'play.mp3' not found! Please make sure it's in the same directory as this script.")
            
    # Only show the title in specific states
    if st.session_state.current_state in ['photos']:
        st.markdown('<h1 style="text-align: center; color: #FF69B4; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">✨ Happy Birthday My Love! ✨</h1>', unsafe_allow_html=True)

    # State transition functions
    def change_to_lights():
        st.session_state.current_state = 'lights'
        st.balloons()

    def change_to_balloons():
        st.session_state.current_state = 'balloons'
        st.snow()

    def change_to_cake():
        st.session_state.current_state = 'cake'
        st.balloons()

    def change_to_photos():
        st.session_state.current_state = 'photos'

    # Main content with improved state management
    if st.session_state.current_state == 'dark':
        with st.container():
            st.markdown('<div class="dark-room">', unsafe_allow_html=True)
            st.markdown('<p class="message">Shh... The party is about to begin! 🤫</p>', unsafe_allow_html=True)
            st.button("✨ Start the Magic ✨", on_click=change_to_lights)
            st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.current_state == 'lights':
        with st.container():
            st.markdown('<div class="disco-room">', unsafe_allow_html=True)
            st.markdown('<div class="blinking-lights">💫✨💫✨💫</div>', unsafe_allow_html=True)
            st.markdown('<p class="floating">🎈</p>', unsafe_allow_html=True)
            st.button("🎊 Release the Balloons! 🎊", on_click=change_to_balloons)
            st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.current_state == 'balloons':
        with st.container():
            st.markdown('<div class="disco-room">', unsafe_allow_html=True)
            st.markdown('<div class="blinking-lights">🎈🎊🎈</div>', unsafe_allow_html=True)
            st.markdown('<p class="cake floating">🎂</p>', unsafe_allow_html=True)
            st.markdown('<p class="message heartbeat">Make a wish! ✨</p>', unsafe_allow_html=True)
            st.button("🔮 Cut the Cake 🔮", on_click=change_to_cake)
            st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.current_state == 'cake':
        with st.container():
            st.markdown('<div class="disco-room">', unsafe_allow_html=True)
            st.markdown('<div class="blinking-lights">✨🎂✨</div>', unsafe_allow_html=True)
            st.markdown('<p class="floating">🍰</p>', unsafe_allow_html=True)
            st.markdown('<p class="message">Your wish is my command! 💫</p>', unsafe_allow_html=True)
            st.button("💝 See Your Special Memories 💝", on_click=change_to_photos)
            st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.current_state == 'photos':
        with st.container():
            st.markdown('<div class="disco-room">', unsafe_allow_html=True)
            st.markdown('<div class="blinking-lights">💖💫💖</div>', unsafe_allow_html=True)
            st.markdown('<h2 style="text-align: center; color: #FF1493;">Our Beautiful Journey Together 💑</h2>', unsafe_allow_html=True)

            # Photo gallery
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<div class="photo-container">', unsafe_allow_html=True)
                st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
                st.image("IMG_6176.png", caption="The Day We Met 💘", width=150)
                st.markdown('</div></div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="photo-container">', unsafe_allow_html=True)
                st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
                st.image("IMG_6177.png", caption="Our Favorite Holiday 🌟", width=150)
                st.markdown('</div></div>', unsafe_allow_html=True)

            with col3:
                st.markdown('<div class="photo-container">', unsafe_allow_html=True)
                st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
                st.image("IMG_6178.jpg", caption="Just Us Being Silly ✨", width=150)
                st.markdown('</div></div>', unsafe_allow_html=True)

            # Final message
            st.markdown("""
            <div style="text-align: center; margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 10px;">
                <p class="heartbeat" style="font-size: 24px; color: #FF1493;">💝 My Dearest Love 💝</p>
                <p style="font-size: 18px; color: #333;">
                Remember Pokhara? The sunsets, your laughter, the way we chased the light—just like you've filled my life with colors I never knew.
                But it's more than the adventures. It's your kindness, your honesty, the way you love without conditions. You've taught me strength, just as your family taught you.
                And when we were apart? That song… 'मनलाइ बुझाइ, कतेर नौ डाडाँ…' I'd play it and miss you, but no distance could ever change what you mean to me.
                Today isn't just about celebrating you—it's about thanking the universe for every 'Sonu' moment. You turned my 'me' into 'we,' and I'll spend forever proving you're the best thing that ever happened to me.
                Here's to your day… and to every day after, together. 🫂
                Your sonu nonu 
                </p>
                <p class="floating" style="font-size: 20px; color: #FF1493;">
                Happy Birthday, my Sonu 🎂✨
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Floating celebration emojis
            st.markdown(
                '<div style="position: fixed; top: 50px; left: 20px;" class="celebration">🎉</div>' +
                '<div style="position: fixed; top: 150px; right: 20px;" class="celebration">🎈</div>' +
                '<div style="position: fixed; bottom: 50px; left: 50px;" class="celebration">✨</div>' +
                '<div style="position: fixed; bottom: 150px; right: 50px;" class="celebration">💫</div>',
                unsafe_allow_html=True
            )
            st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()