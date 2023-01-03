import streamlit as st
import whisper

st.title('文字起こしアプリ ~ OpenAIのWhisper')

# プレースホルダー
place_holder = st.empty()
place_holder.text('インストール中です...少々お待ちください...')
model = whisper.load_model("tiny")
place_holder.text('')

# upload file
upload_file = st.file_uploader('ファイルのアップロード', type=['mp3', 'wav'])

if upload_file is not None:
    content = upload_file.read()
    st.subheader('ファイル詳細')
    file_details = {'FileName': upload_file.name, 'FileType': upload_file.type, 'FileSize': upload_file.size}
    st.write(file_details)
    st.subheader('音声の再生')
    st.audio(content)
        
    st.write('文字起こし')
    if st.button('開始'):
        comment = st.empty()
        comment.write('文字起こしを開始します')
        # transcribe_file(content, lang=option)
        result = model.transcribe(upload_file, verbose=True)
        for l in result['segments']:
            t = f"[{l['start']:04.2f} --> {l['end']:.2f}] {l['text']}"
            st.write(t)
        
        comment.write('完了しました')