#
# File: app.py
# Function: flask gui for apa-gui.py.
# Arg: no
# Version: 3.2.0  (Sync ver.rel w/ excel-ver, mod is for myself.)
#
from flask import Flask, render_template, redirect, session, request, url_for, Response, make_response
from markupsafe import escape
from werkzeug.utils import secure_filename
from apa_auto import *  # Read apa_auto.py
import traceback
import tempfile
import threading

app = Flask(__name__)
# matplotlib はスレッドセーフではないらしいので、マルチスレッドは諦めてメイン処理全体を排他制御する
lock_for_processing = threading.Lock()

@app.route("/")
def index():
    return render_template('index.html')

# ファイルアップロード
@app.route('/upload', methods=['POST', 'GET'])
def upload_and_process():

    if request.method == 'GET':
        #GETでアクセスされた時、uploadsを表示
        return render_template('upload.html')

    #GETでなければPOSTとし、ファイルを受け取って処理する
    f = request.files["the_file"]
    save_fn = secure_filename(f.filename)
    # print('--- uploaded save_fn = {}'.format(save_fn))
    # Stay in HTML if upload file is blank/null.
    if '' == save_fn:
        print('apa-gui : Error. Blank upload file name.')
        return render_template('upload.html')

    # Store upload file to the directory.
    with lock_for_processing, tempfile.TemporaryDirectory(prefix='tmp-', dir='.') as tmp_dir, tempfile.TemporaryDirectory(prefix='out-', dir='.') as out_dir:
        target_filepath = tmp_dir + '/' + secure_filename(save_fn)
        # print('--- uploaded filepath = {}'.format(target_filepath))
        f.save(target_filepath)

        try:
            # print('apa-gui : start main_plot : filepath = {}'.format(target_filepath))
            main_plot(target_filepath, out_dir)
            response = make_response()
            fn_zip = out_dir + '/' + ZIP_FNAME + '.zip'
            # print('apa-gui : app.py/waiting(): fn_zip = {}'.format(fn_zip))
            response.data  = open(fn_zip, "rb").read()

            response.headers['Content-Type'] = 'application/octet-stream'
            response.headers['Content-Disposition'] = 'attachment; filename=apa-output.zip'
            return response

        except:
            print('apa-gui : Exception/main_plot()')
            print(traceback.format_exc())
            return render_template('error.html')


# ----------------------------------------------
# アプリケーション起動
if __name__ == '__main__':
    # app.run(debug=True)   <-OK for local run.
    #--- add host, port for AWS AppRunner
    # app.run(debug=True, host="0.0.0.0", port=8080) # accept from everyone in 8080.
    app.run(debug=True)  # for run in local PC. Default = 127.0.0.1:5000 as flask.

    
