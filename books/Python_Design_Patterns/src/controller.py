
# coding: utf-8
# 사용자가 압축된 URL을 가지고 오면 Redirect 함수를 사용해서 원래 주소로 연결한다.
# Request는 HTTP 요청을 캡슐화 하는데 사용한다.
# 여기에 요청 메소드, 요청 속성, 관련 정보를 갖고있다.
from flask import redirect, render_template, request, Flask
from werkzeug.exceptions import BadRequest, NotFound

import models


# Flask 애플리케이션 초기화
app = Flask(__name__, template_folder='views')


@app.route('/')
def index():
    """메인 페이지 표시"""
    return render_template('main_page.html')


@app.route('/shorten/')
def shorten():
    """요청받은 full_url를 가지고 short_url를 반환한다."""
    # 사용자 입력 검증
    full_url = request.args.get('url')
    if not full_url:
        raise BadRequest
        

    # short_url 프로퍼티와 함께 객체를 반환하는 모델
    url_model = models.Url.shorten(full_url)

    # 뷰에 데이터를 전달하고 화면 표시 메소드를 호출
    short_url = request.host + '/' + url_model.short_url
    return render_template('success.html', short_url=short_url)


@app.route('/<path:path>')
def redirect_to_full(path=''):
    """압축된 URL을 받아와서 일치하는 원래 주소가 있다면 그 곳으로 사용자를 연결한다."""
    # full_url 프로퍼티와 함께 객체를 반환하는 모델
    url_model = models.Url.get_by_short_url(path)
    # 검증 모델 반환
    if not url_model:
        raise NotFound()
        
    return redirect(url_model.full_url)


if __name__== '__main__':
    app.run(debug=True)