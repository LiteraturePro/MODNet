mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

apt update 
apt install libgl1-mesa-glx 
apt install libglib2.0-dev
