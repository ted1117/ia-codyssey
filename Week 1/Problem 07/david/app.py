import base64
import os
from io import BytesIO

from flask import Flask, Response, render_template, request
from gtts import gTTS
from gtts.tts import gTTSError

DEFAULT_LANG = os.getenv("DEFAULT_LANG", "ko")
app = Flask(__name__)


class EmptyTextError(Exception):
    pass


@app.route("/")
def home() -> Response:

    text = "Hello, DevOps"

    lang = request.args.get("lang", DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype="audio/mpeg")  # 페이지 전달없이 바로 재생


@app.route("/index", methods=["GET", "POST"])
def listen():
    index_page = "index_new.html"
    lang_tuple = ("ko", "en", "jp", "es")

    if request.method == "POST":
        lang = request.form.get("lang", DEFAULT_LANG)
        text = request.form.get("input_text", None)

        try:
            if not text or text.isspace():
                raise EmptyTextError("공백 문자 외의 단어를 입력하세요.")

            fp = BytesIO()
            gTTS(text=text, tld="com", lang=lang).write_to_fp(fp)
            fp.seek(0)

            audio_data = base64.b64encode(fp.read()).decode("utf-8")

            return render_template(index_page, audio=audio_data)

        except EmptyTextError as e:
            return render_template(index_page, error=e, status=400)

        except ValueError as e:
            if "Language not supported" in str(e):
                error_msg = f"선택하신 언어 {lang}은 지원되지 않습니다."
            else:
                error_msg = str(e)
            return render_template(index_page, error=error_msg, status=400)

        except gTTSError:
            error_msg = "gTTS 생성 과정에서 오류가 발생했습니다."
            return render_template(index_page, error=error_msg, status=500)

        except Exception as e:
            return render_template(index_page, error=e, status=500)

    return render_template(index_page)


# @app.route("/index")
# def index():
#     index_page = "index_new.html"

#     return render_template(index_page)


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
