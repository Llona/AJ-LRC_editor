# AJ-LRC_editor
LRC format file editor

Now only have adjust LRC time tag function

only adjust time tag and won't change lrc format

# Usage:
python lrc_editor.py [lrc file path] [milliseconds]

### Example:

python lrc_editor.py .\music\apple.lrc -1500

# AJ-LRC_editor
小弟有點強迫症, 不喜歡用offset調整lrc時間軸

喜歡所有時間軸是調整好的

但現有的LRC editor不是很難調時間, 不然就是調整完會自己重排格式

一怒之下自己寫一個!!

1. 可簡單調整時間
2. 不會動到格式

目前只有CLR方式執行, Editor完整功能和GUI有空再說

# Usage:
python lrc_editor.py [lrc file path] [milliseconds]

### Example:
python lrc_editor.py .\music\apple.lrc -1500
