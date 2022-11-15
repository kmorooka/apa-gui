"""
#!/Users/morookak/opt/anaconda3/bin/python
# coding:utf-8
"""
"""
#!/usr/bin/python 
File: apa_auto.py
Fuction: Analyze data & make graph files for APA
Version: v3.3.0 (Sync ver.rel w/ APA excel sheet ver, mod is for myself.)
"""
import sys
import os, time
import shutil
# from shutil import make_archive
import re
from matplotlib.colors import Normalize
import pandas as pd
import matplotlib as mpl
mpl.use("Agg")  # To avoid Assertion ~~ error in flask & matplotlib.
import matplotlib.pyplot as plt
import seaborn as sns
from apa_config import *  # Read Excel column name from apa-config.py file.
import threading

# Initial Kanji Font setting
# Cash clear for Matplotlib Font
# mpl.font_manager._rebuild()  <-2021.10.18 Comment out due to matplotlib 3.4 not support function.
# font = {'family': 'IPAexGothic'}
font = {'family': JP_FONT}
# font = {'family': 'Meiryo'}
mpl.rc('font', **font)

# 並列処理を可能にするため、出力先ファイルパスをスレッド毎に保存する。
output = threading.local()

# ----------------------------------------------------
# exec_serv() 
#    arg: server dataframe, flag if ME used(True)or nor(False).
# ----------------------------------------------------
def exec_serv(df, flag_me):
    if flag_me == False:  # サーバー一覧（手入力用）
        # print("exec_serv(): サーバー一覧（手入力用）")
        plot_pie(df, SERV_NAME1)
        plot_pie(df, SERV_NAME2)
        plot_pie(df, SERV_CONSOLI_NAME)
        plot_pie(df, SERV_SYSTEM)
        plot_pie(df, SERV_ENV)
        plot_pie(df, SERV_USAGE)
        plot_pie(df, SERV_TYPE)
        plot_pie(df, SERV_LOCATION)
        plot_pie(df, SERV_APPLIANCE)
        plot_pie(df, SERV_APPLIANCE_NAME)
        plot_pie(df, SERV_PYSVM)
        plot_pie(df, SERV_PROSERV)
        plot_pie(df, SERV_COREPROC)
        plot_pie(df, SERV_CORE)
        plot_pie(df, SERV_MEM)
        plot_pie(df, SERV_PEAK_CPU)
        plot_pie(df, SERV_PEAK_MEM)
        plot_pie(df, SERV_STORAGE)
        plot_pie(df, SERV_STORAGE_USAGE)
        plot_pie(df, SERV_SSDHDD)
        plot_pie(df, SERV_OPTIMIZE)
        plot_pie(df, SERV_HYP)
        plot_pie(df, SERV_OS)
        plot_pie(df, SERV_OSVER)
        plot_pie(df, SERV_OSOTHER)
        plot_pie(df, SERV_DB)
        plot_pie(df, SERV_DBVER)
        plot_pie(df, SERV_DBOTHER)
        plot_pie(df, SERV_ORACLE_EE)
        plot_pie(df, SERV_HA)
        plot_pie(df, SERV_HANAME)
        plot_pie(df, SERV_PRICE)
        plot_pie(df, SERV_APPENDIX)
        plot_scatter(df, 'CORExMEM（手動）')    # Heat map - Core x Mem
        plot_bar(df, 'ストレージ（手動）')       # Bar graph - Storage
    else:       # サーバー一覧（ME用） flag_me==True
        # print("exec_serv(): サーバー一覧（ME用）")
        plot_pie(df, ME_NAME)
        plot_pie(df, ME_ENV)
        plot_pie(df, ME_APPL)
        plot_scatter(df, 'CORExMEM（ME）')     # ME scatter graph
        plot_bar(df, 'ストレージ（ME）')     # bar graph
        plot_pie(df, ME_TYPE)
        plot_pie(df, ME_CORE)
        plot_pie(df, ME_RAM)
        plot_pie(df, ME_STORAGE)
        plot_pie(df, ME_OS)
        plot_pie(df, ME_HYPERVISOR)
        plot_pie(df, ME_SQL)
        plot_pie(df, ME_SQLVER)
        # same w/ server tab item
        plot_pie(df, SERV_NAME2)
        plot_pie(df, SERV_SYSTEM)
        plot_pie(df, SERV_ENV) 
        plot_pie(df, SERV_CONSOLI_NAME)
        plot_pie(df, SERV_TYPE)
        plot_pie(df, SERV_LOCATION)
        plot_pie(df, SERV_APPLIANCE)
        plot_pie(df, SERV_APPLIANCE_NAME)
        plot_pie(df, SERV_DB)
        plot_pie(df, SERV_DBVER)
        plot_pie(df, SERV_DBOTHER)
        plot_pie(df, SERV_ORACLE_EE)
        plot_pie(df, SERV_HA)
        plot_pie(df, SERV_HANAME)
        plot_pie(df, SERV_PRICE)
        plot_pie(df, SERV_APPENDIX)

    return(0)
# ----------------------------------------------------
# exec_sys() 
#    arg: system dataframe, System column name
# ----------------------------------------------------
def exec_sys(df):

    #　システム特性の項目
    plot_pie(df, SYS_G1)
    plot_pie(df, SYS_G2)
    plot_pie(df, SYS_G3)
    plot_pie(df, SYS_G4)
    plot_pie(df, SYS_G5)
    plot_pie(df, SYS_G6)
    plot_pie(df, SYS_G7)
    plot_pie(df, SYS_G8)
    plot_pie(df, SYS_G9)
    plot_pie(df, SYS_G10)
    plot_pie(df, SYS_G11)
    plot_pie(df, SYS_G12)
    plot_pie(df, SYS_G13)
    plot_pie(df, SYS_G14)
    plot_pie(df, SYS_G15)
    plot_pie(df, SYS_G16)

    # クラウド適合の項目 
    plot_pie(df, SYS_T1)
    plot_pie(df, SYS_T2)
    plot_pie(df, SYS_T3)
    plot_pie(df, SYS_T4)
    plot_pie(df, SYS_T5)
    plot_pie(df, SYS_T6)
    plot_pie(df, SYS_T7)
    plot_pie(df, SYS_T8)
    plot_pie(df, SYS_T9)
    plot_pie(df, SYS_T10)
    plot_pie(df, SYS_T11)
    plot_pie(df, SYS_T12)
    plot_pie(df, SYS_T13)
    plot_pie(df, SYS_T14)
    plot_pie(df, SYS_T15)

    # 移行難易度の項目
    plot_pie(df, SYS_N1)
    plot_pie(df, SYS_N2)
    plot_pie(df, SYS_N3)
    plot_pie(df, SYS_N4)
    plot_pie(df, SYS_N5)
    plot_pie(df, SYS_N6)
    plot_pie(df, SYS_N7)
    plot_pie(df, SYS_N8)
    plot_pie(df, SYS_N9)
    plot_pie(df, SYS_N10)
    plot_pie(df, SYS_N11)
    plot_pie(df, SYS_N12)
    plot_pie(df, SYS_N13)
    plot_pie(df, SYS_N14)
    plot_pie(df, SYS_N15)

    # 4象限の散布図、推奨移行戦略の円グラフを描画
    plot_4dim(df[[OK_CLOUD, NG_CLOUD]])
    # plot_pie(df, RECOMMEND_PATH)

    return(0)

# ----------------------------------------------------
# plot_pie_no_nan : Analyze & Drop NaN from SERVER data & Pie
#   arg1: Dataframe name of server list.
#   arg2: Parameter for plot.
#   CURRENTLY, NOT USED. In this func, NaN will be dropped.
# ----------------------------------------------------
def plot_pie_no_nan(df, item):
    # print('apa-gui : plot_pie_no_nan({})'.format(item))

    # Drop NaN data from DataFrame.
    df_item = df.dropna(subset=[item])
    list_col_name = df_item[item].to_numpy().tolist()
    col_unique = df_item[item].unique()

    list_col_num = []
    for i in col_unique:
        rc = list_col_name.count(i)
        list_col_num.append(rc)
    # print('list_col_num = {}'.format(list_col_num))
    fig = plt.figure()
    plt.pie(list_col_num, labels=col_unique, autopct=make_autopct(list_col_num))
    # Making png file name by removing / \n etc from "item" strings.
    # print('--- item file name = {} ---'.format(re.sub('/', '', item)))
    fn = re.sub('/', '', item)   # itemカラムにあるスラッシュを削除
    fn = re.sub('\n', '', fn)   # 改行コードを除去
    fig.savefig("{}/{}.png".format(output.path, fn), bbox_inches='tight')
    fig.clear()  # Avoid overdrawing

    return(0)
# ----------------------------------------------------
# make_autopct : make pie chart label w/ % & values.
# ----------------------------------------------------
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

# ----------------------------------------------------
# chk_all_nan : Check if data item are all NaN.
#   arg1: Dataframe name of server list.
#   arg2: Item of Dataframe column.
# ----------------------------------------------------
def chk_all_nan(df, item):
    # print('apa-gui : chk_all_nan()')
    rc = df[item].isna().all()
    if rc == True:
        print('apa-gui: <<{}>> is all Blank(NaN). NOT make the graph file!'.format(item))
        return(True)
    return(False)

# ----------------------------------------------------
# plot_pie : Analyze SERVER data & Pie graph
#   arg1: Dataframe name of server list.
#   arg2: Parameter for plot.
#   plot_pie() use ONE parm for analisys.
#   All NaN INCLUDED & Plot. Count no. of parm & plot pie.
#   Use Matplotlib due to seaborn don't support pie plot.
# ----------------------------------------------------
# --- This func include NaN.
def plot_pie(df, item):

    print('apa-gui: {}'.format(item))
    if True == chk_all_nan(df, item):
        return(0)

    # Include NaN data for process is as below.
    # list_col_name = df[item].to_numpy().tolist()
    list_col_name = df[item].tolist()
    # print('list_col_name = {}'.format(list_col_name))
    col_unique = df[item].unique()
    # print('col_unique = {}'.format(col_unique))

    list_col_num = []
    for i in col_unique:
        rc = list_col_name.count(i)
        list_col_num.append(rc)
    # print('list_col_num = {}'.format(list_col_num))
    fig = plt.figure()

    # グラフにラベルをつけるかどうか：labels=None, or col_unique 
    # 12時位置から反時計回りで描画：startangle=90, counterclock=False
    # ドーナツグラフのためにwedgeprops を設定。外すと円グラフになる。 
    wedgeprops = {"edgecolor":"white", "width":0.3}
    plt.pie(list_col_num, labels=col_unique, autopct=make_autopct(list_col_num), startangle=90, counterclock=False, wedgeprops=wedgeprops)

    plt.rcParams['font.size'] = FNT_SIZE
    plt.legend(col_unique, fontsize=FNT_SIZE, loc=('best')) #重ならない位置に凡例表示

    # Making png file name by removing / \n etc from "item" strings.
    # print('--- item file name = {} ---'.format(re.sub('/', '', item)))
    fn = re.sub('/', '', item)   # itemカラムにあるスラッシュを削除
    fn = re.sub('\n', '', fn)   # 改行コードを除去
    # fig.savefig("{}/{}.png".format(DATA_DIR, fn), format='png')
    fig.savefig("{}/{}.png".format(output.path, fn), bbox_inches='tight')
    fig.clear()  # Avoid overdrawing

    return(0)

# ----------------------------------------------------
# plot_scatter : Core x Memory Scatter plot
#   arg1: Dataframe name of server list.
#   arg2: item name of server/system
#   plot_scatter() use TWO parm for analisys.
# ----------------------------------------------------
def plot_scatter(df, item):

    print('apa-gui: {}'.format(item))
    # 出力ファイル名のために入力itemで処理分離。    
    #------------------------
    # 手動用のカラム名を使うこと！
    #------------------------
    if item == 'CORExMEM（手動）':  # 手入力の場合
        fig = plt.figure()
        sns.set(style="whitegrid", color_codes=True)
        sns.set(font_scale=1.0) # default 1.0 & >=1.0
        # sns.set(font='Meiryo')
        # sns.set(font='IPAexGothic')
        sns.set(font=JP_FONT)

        # get max from core, mem for plot slim,ylim.
        max_mem = df[SERV_MEM].max()
        max_core = df[SERV_CORE].max()
        # g = sns.jointplot(data=df, x=SERV_MEM, y=SERV_CORE, xlim=(0,max_mem), ylim=(0,max_core))
        # g = sns.jointplot(data=df, x=SERV_MEM, y=SERV_CORE, kind="hist")
        # g = sns.jointplot(data=df, x=SERV_MEM, y=SERV_CORE)
        g = sns.jointplot(data=df, x=SERV_MEM, y=SERV_CORE, height=5, ratio=2, marginal_ticks=True)
        g.set_axis_labels(SERV_MEM, SERV_CORE)

        plt.savefig("{}/{}".format(output.path, 'Core-Memory.png'), bbox_inches='tight')
        fig.clear()  # Avoid overdrawing
        return(0)
    #----------------------
    # ME用のカラム名を使うこと！
    #----------------------
    elif item == 'CORExMEM（ME）':  # MEの場合
        fig = plt.figure()
        sns.set(style="whitegrid", color_codes=True)
        sns.set(font_scale=1.0) # default 1.0 & >=1.0
        # sns.set(font='Meiryo')
        # sns.set(font='IPAexGothic')
        sns.set(font=JP_FONT)
        # get max from core, mem for plot slim,ylim.
        max_mem = df[ME_RAM].max()
        max_core = df[ME_CORE].max()
        g = sns.jointplot(data=df, x=ME_RAM, y=ME_CORE, xlim=(0,max_mem), ylim=(0,max_core))
        # g = sns.jointplot(data=df, x=ME_RAM, y=ME_CORE)
        g.set_axis_labels(ME_RAM, ME_CORE)
        plt.savefig("{}/{}".format(output.path, 'ME-Core-Memory.png'), bbox_inches='tight')
        fig.clear()  # Avoid overdrawing
        return(0)
    else:                  # Modify For anyother parm Heatmap.
        col1 = 'ERR'
        col2 = 'ERR'
        # print('apa-gui: plot_scatter(): column ERR.')
        return(1)

# ----------------------------------------------------
# plot_bar : Making bar & save file.
#   arg1: Dataframe name of server/system list.
#   arg2: Item name of server/system.
#   plot_scatter() use GroupBy for Two parm.
#   STORAGE: groupby.sum() / Sum all the storage broupby System name.
#   Others: groupby.count()?? Depends on the parameter!
# ----------------------------------------------------
def plot_bar(df, item):

    print('apa-gui: {}'.format(item))
    # if True == chk_all_nan(df, item):
    #     return(0)

    #--- Modify for each parameter style.
    #------------------------
    # 手動用のカラム名を使うこと！
    #------------------------
    if item == 'ストレージ（手動）':
        col1 = SERV_SYSTEM    # 手動
        col2 = SERV_STORAGE   # 手動
    #----------------------
    # ME用のカラム名を使うこと！
    #----------------------
    elif item == 'ストレージ（ME）':  # In case of other parm bar plot.
        col1 = SERV_SYSTEM    # 手動とMEは共通
        col2 = ME_STORAGE   # ME用
    else:
        # 以下はエラー表示なのでコメントアウトしないこと！
        print('apa-gui: Error. plot_bar(): Neither Storage nor Storage(ME)!')
        col1 = 'ERR'
        col2 = 'ERR'
        return(1)

    # print('plot_bar(): plt.figure()')
    fig = plt.figure()

    #--- Sum all storage groupby system name.
    df_tmp = df.groupby(col1)[col2].sum().sort_values(ascending=True).head(PLOT_MAX).plot(kind='barh')
    # print('plot_bar(): df_tmp TOP 20 =\n {}'.format(df_tmp))

    fn = re.sub('/', '', item)   # itemカラムにあるスラッシュを削除
    fn = re.sub('\n', '', fn)   # 改行コードを除去
    # print('plot_bar() save png file.')
    # plt.savefig("{}/{}.png".format(DATA_DIR, fn), bbox_inches='tight')
    fig.savefig("{}/{}.png".format(output.path, fn), bbox_inches='tight')
    fig.clear()  # Avoid overdrawing

    return(0)

# ----------------------------------------------------
# plot_4dim() 
#    arg1: data frame name for 4 dim calc
#    Plot 4 dimenstion scatter
# ----------------------------------------------------
def plot_4dim(df):

    # print('apa-gui: plot_4dim({})'.format(OK_CLOUD+" / "+NG_CLOUD))
    print('apa-gui: {}'.format(OK_CLOUD+" / "+NG_CLOUD))
    #--- Modify for each parameter style.
    fig = plt.figure()
    sns.set(style="whitegrid", color_codes=True)
    sns.set(font_scale=1.0)
    # sns.set(font='Meiryo')
    # sns.set(font='IPAexGothic')
    sns.set(font=JP_FONT)
        
    # g = sns.lmplot(data=df, x=NG_SUM, y=OK_SUM)
    g = sns.jointplot(data=df, x=NG_CLOUD, y=OK_CLOUD, xlim=(-1,27), ylim=(-1,25))
    # plt.xlim(0, 20)   # 4dim score sum range 0~20
    # plt.ylim(0, 20)
    plt.savefig("{}/{}".format(output.path, '4-Dimension.png'), bbox_inches='tight')
    fig.clear()  # Avoid overdrawing
    return(0)

# ----------------------------------------------------
# zip_files() 
#    arg: directory path to zip for plot files.
# ----------------------------------------------------
def zip_files(dirname):

    # print('zip_files(): dirname= {}'.format(dirname))
    shutil.make_archive(ZIP_FNAME, 'zip', root_dir=dirname)
    shutil.move(ZIP_FNAME + '.zip', dirname)
    return(0)

# ----------------------------------------------------
# apa_excel_read
#   arg: Excel file name
#   return: pandas format {server, system, flag-ME} tab data.
#   func: check which tab is used, ME or Manual input.
# ----------------------------------------------------
def apa_excel_read(fn):

    # print('apa_excel_read(): Excel file name = {}'.format(fn))
    # サーバータブはME版か、手入力用かをタブの有無で確認してどちらかを引き渡すこと
    # ME用の場合、plot_pie()へ引き渡すパラメータも変わるので対応すること
    input_fn = pd.ExcelFile(fn)
    tabs = input_fn.sheet_names
    # print('--- apa_excel_read(): tabs = {}'.format(tabs))

    # サーバー一覧（MEまたは手入力）のタブを処理
    # シートに手入力だけがあり、MEがない場合は下記
    if (TAB_SERVER in tabs) and (TAB_SERVER_ME not in tabs):
        # print('apa_excel_read(): TAB_SERVER = {}'.format(TAB_SERVER)) 
        df_server = pd.read_excel(fn, sheet_name=TAB_SERVER)
        flag_me = False
    # シートに手入力がなく、MEだけの場合は下記
    elif (TAB_SERVER not in tabs) and (TAB_SERVER_ME in tabs):
        # print('apa_excel_read(): TAB_SERVER_ME = {}'.format(TAB_SERVER_ME)) 
        df_server = pd.read_excel(fn, sheet_name=TAB_SERVER_ME)
        flag_me = True
    else:
        # 下記エラー表示なのでコメントアウトしないこと
        print('apa-gui: Error. Excel sheet error. Check server sheets.')
        exit()

    # システム一覧(ME有無に関わらず共通利用)タブを処理
    df_system = pd.read_excel(fn, sheet_name=TAB_SYSTEM)
    return(df_server, df_system, flag_me)

    """  OLD code. Before ME func added, below is OK code.
    df_system = pd.read_excel(fn, sheet_name=TAB_SYSTEM)
    df_server = pd.read_excel(fn, sheet_name=TAB_SERVER)
    flag_me = False
    return(df_server, df_system, flag_me)
    """
# ----------------------------------------------------
# chk_serv() 
#    func: check data if mandatory item are filled in.
#    arg1: pandas data frame of server
#    arg2: pandas data frame of server
# ----------------------------------------------------
def chk_serv(df_serv, flag_me):

    # print('chk_serv(): starting.')
    # print('chk_serv(): flag_me = {}'.format(flag_me))

    # 必須項目、システム名称 がないとエラー終了
    if flag_me == False:  # manual data
        n = SERV_SYSTEM
    elif flag_me == True:  # ME data
        # 現時点でME、Manual で共通項目名なので一緒
        n = SERV_SYSTEM
    else:
        print('apa-gui: Error. arg flag_me is not correct value!')
        return(1)
    # その他の必須項目確認は、ここにコード追加

    # df_servの n カラム「システム名称」がすべて空欄ならエラーとして対応。
    if df_serv[n].isnull().all() == True:
        print('apa-gui: Error. {} are all NaN(blank field).'.format(n))
        exit()
    # print('chk_serv(): システム名称 OK 埋まってました!')
    return(0)
# ----------------------------------------------------
# chk_sys() 
#    func: check data if mandatory item are filled in.
#    arg: pandas data frame of system
# Currently, this func is not called from anybody.
# ----------------------------------------------------
def chk_sys(df_sys):
    # print('chk_sys(): starting.')
    return(0)
# ----------------------------------------------------
# main_plot() 
#    arg: Uploaded & stored Excel full-path file name.
# ----------------------------------------------------
def main_plot(fn, out):
    print('apa-gui: Starting ...') 
    print('apa-gui: Excel file = {}'.format(fn)) 

    output.path = out
    sheet = apa_excel_read(fn)
    df_serv = sheet[0]
    df_sys = sheet[1]
    flag_me = sheet[2]     # flag_me: ME=True, Manual=False
    # print('apa-gui: df_serv = {}'.format(df_serv))
    # print('apa-gui: df_sys = {}'.format(df_sys))
    # print('apa-gui: main_plot() flag_me = {}'.format(flag_me))

    chk_serv(df_serv, flag_me)    # check mandatory field
    # chk_sys(df_sys)   check mandatory field

    # print('apa-gui: Before exec_serv - flag_me = {}'.format(flag_me))
    exec_serv(df_serv, flag_me)
    exec_sys(df_sys)

    zip_files(out)
    print('apa-gui: End graph plot.') 

    return(0)
# ----------------------------------------------------
# End of File
# ----------------------------------------------------
