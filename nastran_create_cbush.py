import os
import sys
import pyNastran
import numpy

from pyNastran.bdf.bdf import BDF, read_bdf, CaseControlDeck

# ドロップされたファイルのパスを取得
# ドロップされていない場合は例外で落とす
try:
    path_dropped = sys.argv[1]
except IndexError:
    print('Inputファイルを直接Dropしてください！　キーを押すと終了します...')
    input()
    sys.close(1)

# メッセージ
print("Inputファイルを確認しました。")
print(path_dropped)

# BDFでモデルを読み込む
model_input = BDF()
model_input.read_bdf(path_dropped)

print("GRID番号を入力してください。")
print("(例) 99000001,1,99000002,2,99000003,3")
nodelist = input().split(',')
#list_input_node = [99000001,1,99000002,2,99000003,3,99000004,4,99000005,5]

model_output = BDF()
pid_pbush = 99000000
prop_pbush_k =[1.0e+8,1.0e+8,1.0e+8,1.0e+12,1.0e+12,1.0e+12]
model_output.add_pbush(pid_pbush,prop_pbush_k,'','')

list_len = int(len(list_input_node) / 2 )
count = -1

for ta in range(list_len):
    count = count + 1
    id_grid_new = int(list_input_node[count])

    count = count + 1
    id_grid_input = int(list_input_node[count])
    grid_input = model_input.Node(id_grid_input)

    grid_input_pos = grid_input.get_position()
    model_output.add_grid(id_grid_new,grid_input_pos)

    list_node_pair = [id_grid_new,id_grid_input]
    model_output.add_cbush(id_grid_new,pid_pbush,list_node_pair,'','',0)

model_output.write_bdf('cbush.bdf')







