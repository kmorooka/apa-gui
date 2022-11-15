"""
File: apa_config.py
Fuction:
    Define column name, global parameters.
    Include ME excel tab.
Arguments: No
Version: v3.3.0  棚卸しシートv3.3用 (Sync ver.rel w/ APA excel sheet ver, mod is for myself.)
"""

#----- General parameter -----
ZIP_FNAME = 'apa-gui-output' # zip for all plot png files.
PLOT_MAX = 20  # Plot Top 20 items for Bar plot.
TAB_SYSTEM = "システム一覧"  # Excel Tab Name
TAB_SERVER = "サーバー一覧（手入力用）"  # Excel Tab Name
TAB_SERVER_ME = "サーバー一覧（ME利用時用）"  # Excel Tab Name
JP_FONT = "IPAexGothic"  # Japanese font for plot.
FNT_SIZE = 6  # Japanese font size for explanatory notes.
ONP_OR_CLOUD = 'cloud'  # 空欄時の4象限作成デフォルト処理：'cloud'=クラウド寄り、'onp'=オンプレ寄り

#----- System data column -----
SYS_G1 = "[概01] システム名称"
SYS_G2 = "[概02] システム配置先"
SYS_G3 = "[概03] システムオーナー部門"
SYS_G4 = "[概04] システム用途"
SYS_G5 = "[概05] システムアーキテクチャ"
SYS_G6 = "[概06] 主要なアプリケーション開発言語"
SYS_G7 = "[概07] パッケージアプリケーションか？"
SYS_G8 = "[概08] パッケージ提供ベンダー"
SYS_G9 = "[概09] システム更改予定時期"
SYS_G10 = "[概10] 現時点でのクラウド化に対する姿勢"
SYS_G11 = "[概11] クラウド化を進めたい理由"
SYS_G12 = "[概12] クラウド化にネガティブな理由"
SYS_G13 = "[概13] 主要なシステム課題"
SYS_G14 = "[概14] RPO"
SYS_G15 = "[概15] RTO"
SYS_G16 = "[概16] 保持している環境面数"
SYS_T1 = "[適01] 従量課金による無駄の削減"
SYS_T2 = "[適02] 長期的な負荷変動への対応力"
SYS_T3 = "[適03] 短期的な負荷変動への対応力"
SYS_T4 = "[適04] 環境確保の俊敏性・柔軟性"
SYS_T5 = "[適05] 高度な可用性"
SYS_T6 = "[適06] 高度なセキュリティ"
SYS_T7 = "[適07] コスト管理の精度向上"
SYS_T8 = "[適08] グローバル展開の容易性"
SYS_T9 = "[適09] 最小コストでの実験の反復"
SYS_T10 = "[適10] ライセンス&保守コスト削減"
SYS_T11 = "[適11] 運用コスト削減"
SYS_T12 = "[適12] 開発スピード向上"
SYS_T13 = "[適13] 開発柔軟性向上"
SYS_T14 = "[適14] 魅力的なデジタルサービスの開発"
SYS_T15 = "[適15] モダンなデータ分析基盤の構築"
SYS_N1 = "[難01] ビジネス上の重要度"
SYS_N2 = "[難02] 機密情報の保存"
SYS_N3 = "[難03] 監督官庁への報告義務"
SYS_N4 = "[難04] コンプライアンス"
SYS_N5 = "[難05] インフラ下位レイヤへの完全な統制"
SYS_N6 = "[難06] 極めて高度な稼働率目標"
SYS_N7 = "[難07] オンプレ機器との低レイテンシー要件"
SYS_N8 = "[難08] アプライアンス製品の利用"
SYS_N9 = "[難09] レガシープラットフォームの利用"
SYS_N10 = "[難10] ベンダーによる動作保証がないソフトウェア"
SYS_N11 = "[難11] IPベースではない通信プロトコル"
SYS_N12 = "[難12] 共有ストレージ型クラスタ構成"
SYS_N13 = "[難13] 保守切れバージョンの利用"
SYS_N14 = "[難14] ハードコードされたIPアドレス"
SYS_N15 = "[難15] 他システムとの密結合"

#----- Server data column -----
SERV_NAME1 = "サーバー名"
SERV_NAME2 = "サーバー名称"
SERV_CONSOLI_NAME = "集約サーバー名"
SERV_SYSTEM = "システム名称（略称）"
SERV_ENV = "環境区分"
SERV_USAGE = "サーバーの稼働率（％）"
SERV_TYPE = "サーバー種別"
SERV_LOCATION = "ロケーション"
SERV_APPLIANCE = "アプライアンスか？"
SERV_APPLIANCE_NAME = "アプライアンス製品名"
SERV_PYSVM = "物理/仮想"
SERV_PROSERV = "プロセッサー数／サーバー"
SERV_COREPROC = "コア数／プロセッサ"
SERV_CORE = "総コア数"
SERV_MEM = "メモリ容量（GB）"
SERV_PEAK_CPU = "ピーク時のCPU使用率"
SERV_PEAK_MEM = "ピーク時のメモリ使用率"
SERV_STORAGE = "ストレージ容量(GB)"
SERV_STORAGE_USAGE = "ストレージ利用率(%)"
SERV_SSDHDD = "SSD/HDD"
SERV_OPTIMIZE = "最適化（CPU／メモリ／ストレージ）"
SERV_HYP = "Hypervisor"
SERV_OS = "OS名"
SERV_OSVER = "OSバージョン"
SERV_OSOTHER = "その他OSの場合のOS名とバージョン"
SERV_DB = "DBMS名"
SERV_DBVER = "DBMS バージョン"
SERV_DBOTHER = "その他DBの場合のDBMS名とバージョン"
SERV_ORACLE_EE = "Oracle の場合  Enterprise Edition か？"
SERV_HA = "HA構成の有無"
SERV_HANAME = "HA製品名 or HA技術名"
SERV_PRICE = "サーバー購入価格（万円）"
SERV_APPENDIX = "備考"

#----- ME(Migration Evaluator) diff data column -----
ME_NAME = "Server Name"
ME_ENV = "Environment"
ME_APPL = "Application"
ME_TYPE = "Type"
ME_CORE ="Provisioning | vCPU Total Cores"
ME_RAM = "Provisioning | RAM (GB)"
ME_STORAGE = "Provisioning | Storage Size (GB)"
ME_OS = "Provisioning | Operating System"
ME_HYPERVISOR ="Virtualization | Hypervisor"
ME_SQL ="SQL | Edition"
ME_SQLVER ="SQL | Version"

# ----------------------------------------------------
# System 4 dimension column 
# ----------------------------------------------------
# ----- クラウド適合度 -----
# OK_MIGRATION = "[合計] クラウド適合度（Migrationによる価値）"
# OK_MODERNIZATION = "[合計] クラウド適合度（Modernizationによる価値）"
OK_CLOUD = "[合計] クラウド適合度"
# ----- クラウド移行難易度　-----
# 移行難易度1_移行不可判断（0:No, 1:Yes）
NG_CLOUD = "[合計] 移行難易度"
# ----- 推奨移行戦略 -----
RECOMMEND_PATH ="推奨移行戦略（4象限）"
# ----------------------------------------------------
# End of File
# ----------------------------------------------------
