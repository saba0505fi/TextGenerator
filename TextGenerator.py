import random

def voice_genarate():
    select = 1
    #print("どんなやつ？ 普通:[1] 下品:[2]")
    #select = int(input())

    if(select == 1):
        word = ["…","……っ","！","ぁ","あ","あっ","ん","ふ","ぅ"] #サンプルの要素。適宜，追加可能
    #elif(select == 2):
        #word = ["…","……っ","！","ぁ","んほぉ","お","ん","んっ","ふっ","ゃ","゛"] #サンプルの要素。適宜，追加可能

    print("最大何文字？：")
    N = int(input()) #生成するサンプルの最大文字数ｎの取得
    print("いくつ作る？：")
    M = int(input()) #生成するサンプルの数ｍの取得
    print("攻めの名前は？(ひらがなで)：")
    name = str(input())
    n = list(name) #文字列を分割

    if(n[len(n)-1] == "う" or n[len(n)-1] == "を"):
        n[len(n)-1] = "ぉ"
    elif(n[len(n)-1] == "あ" or n[len(n)-1] == "か" or n[len(n)-1] == "さ" or n[len(n)-1] == "た" or n[len(n)-1] == "な" or n[len(n)-1] == "は" or n[len(n)-1] == "ま" or n[len(n)-1] == "や" or n[len(n)-1] == "ら" or n[len(n)-1] == "わ"):
        n.append("ぁ")
    elif(n[len(n)-1] == "い" or n[len(n)-1] == "き" or n[len(n)-1] == "し" or n[len(n)-1] == "ち" or n[len(n)-1] == "に" or n[len(n)-1] == "ひ" or n[len(n)-1] == "み" or n[len(n)-1] == "り"):
        n.append("ぃ")
    elif(n[len(n)-1] == "く" or n[len(n)-1] == "す" or n[len(n)-1] == "つ" or n[len(n)-1] == "ぬ" or n[len(n)-1] == "ふ" or n[len(n)-1] == "む" or n[len(n)-1] == "ゆ" or n[len(n)-1] == "る"):
        n.append("ぅ")
    elif(n[len(n)-1] == "え" or n[len(n)-1] == "け" or n[len(n)-1] == "せ" or n[len(n)-1] == "て" or n[len(n)-1] == "ね" or n[len(n)-1] == "へ" or n[len(n)-1] == "め" or n[len(n)-1] == "れ"):
        n.append("ぇ")
    elif(n[len(n)-1] == "お" or n[len(n)-1] == "こ" or n[len(n)-1] == "そ" or n[len(n)-1] == "と" or n[len(n)-1] == "の" or n[len(n)-1] == "ほ" or n[len(n)-1] == "も" or n[len(n)-1] == "よ" or n[len(n)-1] == "ろ"):
        n.append("ぉ")
    elif(n[len(n)-1] == "ん"):
        n.append("っ")

    word.append(''.join(map(str,n)))

    print("\n＝＝結果＝＝")

    for j in range(M): #サンプルの生成をｍ回繰り返す
        sentence = [[] for _ in range(N+1)] #サンプルを一時的に補完する配列の定義
        i = -1 #ループ開始時にインクリメントをしたいため，初期値は-1
        name_count = 0
        while(i < N): #文字数がｎに達するまで繰り返す
            i += 1
            if(i == (N-1)):
                sentence[i] = word[0]
                sentence[i+1] = None
                break
            sentence[i] = word[random.randint(0,len(word)-1)] #sentenceリストのｉ番目に，wordリストからランダムで１つを抽出して挿入
            if((sentence[i]=="！" and i>=int(N*0.8)) or ((sentence[i]=="…") and i>=int(N*0.8))): #"！"が来た場合そのサンプルを終わらせる為，その次の要素をNoneとする
                sentence[i+1] = None
                break #ループ終了
            if(i>=0): #一文字目から判定開始の条件式
                if(sentence[i] == "！" and i<5):
                    sentence[i] = None
                    i -= 1
            if(i>0): #2文字名以降から判定開始の条件式
                if(sentence[i-1] == sentence[i]): #同じ文字が二回連続で来た場合，
                    sentence[i] = None #その要素をNoneにして(リセット)，
                    i -= 1 #一つ前のループに戻る
                    continue
                elif(sentence[i] == word[len(word)-1]): #名前の要素が来た場合，
                    if(name_count < 1): #且つ，カウントが１未満であった場合
                        name_count += 1 #カウント+１
                    else: #且つ，カウントが１異常であった場合
                        sentence[i] = None #リセット
                        i -= 1
                    continue
                elif(sentence[i-1] == "あっ" and sentence[i] == "あ"):
                    sentence[i] = "……"
                    continue
                elif(sentence[i-1] == "あっ" and sentence[i] == "ふ"):
                    sentence[i] = "………、"
                    continue
                elif(sentence[i-1] == "ふ" and sentence[i] == "ん"):
                    sentence[i] = "ぅ"
                    continue
                elif(sentence[i-1] == "ふ" and sentence[i] == "！"):
                    sentence[i] = "ぁ"
                    continue
                elif(sentence[i-1] == word[len(word)-1] and sentence[i] == "！"):
                    sentence[i] = "……っ"
                    continue
                elif(sentence[i-1] == "あ" and sentence[i] == "ふ"):
                    sentence[i] = "っ、"
                    continue
                elif(sentence[i-1] == "ぅ" and sentence[i] == "！"):
                    sentence[i] = "……、"
                    continue

            if(i>1): #3文字目以降から判定開始の条件式
                if(sentence[i-2] == sentence[i]): #i番目の文字が二つ前の文字と一緒だった場合
                    sentence[i] = None #リセット
                    i -= 1
                    continue
                elif(sentence[i-2] == "ふ" and sentence[i-1] == "ぁ" and sentence[i] == "ん"):
                    sentence[i] = None #リセット
                    i -= 1
                    continue
        l = 0 #別のループのための変数ｌを導入
        result = [[] for _ in range(i+1)] #少し余裕を持って決定版のサンプルを入れる空のリストを生成
        while(sentence[l] != None): #Noneが来るまで繰り返す(最後には必ずNoneが来る)
            result[l] = sentence[l]
            l += 1
        print(''.join(map(str,result))) #リストを連結して表示する

def sentence_remake():
    word = ["…","………っ","…、","……！"] #wordの定義

    print("文章を入力してください：")
    sentence = str(input())
    sep = list(sentence)
    sep.append(None)

    count = 0
    k = 0
    num = 0
    sep3 = []
    while(count <= len(sep)):
        num = random.randint(2,4)
        count += num
        sep2 = [[] for _ in range(num)]
        for i in range(num):
            if(sep[k] != None):
                sep2[i] = sep[k]
                k += 1
            else:
                break
        sep3.append(''.join(map(str,sep2)))
        sep2 = None
    sep3.append(None)

    result = [[] for _ in range(len(sep3)*3-2)]

    l = 0
    n = 0
    while(sep3[n] != None):
        result[l] = word[random.randint(0,len(word)-1)]
        l += 1
        result[l] = sep3[n]
        l += 1
        result[l] = word[random.randint(0,len(word)-1)]
        l += 1
        n += 1
    
    joined = ''.join(map(str,result))
    res = list(joined)

    t = 0
    result = [[] for _ in range(len(res))]
    while(res[t] != "["):
        result[t] = res[t]
        t += 1
    for j in range(len(res)-t):
        result[t+j] = "　"
    print("\n＝＝結果＝＝")
    print(''.join(map(str,result)))



    #print(''.join(map(str,sep3)))




#ココからMainプログラム
print("\n＜R18物書きサポートプログラム＞")
print("\n　～モード選択～\n　　＞声ジェネレータ：[1]\n　　＞文章エッチ加工：[2]")
scan = int(input())

if(scan!=1 and scan!=2 and scan!="１" and scan!="２"):
    while(scan!=1 and scan!=2 and scan!="１" and scan!="２"):
        print("エラー：「1」または「2」を入力してください")
        print("　＞声ジェネレータ：[1]\n　＞文章加工　　　：[2]")
        scan = int(input())

if(scan == 1 or scan==int("１")):
    print("\n　～声ジェネレータ～\n　　指定文字数以下のあえぎ声を指定個数分，生成するプログラムです。\n　　画面の指示に従って，数値・文字を入力してください。\n")
    voice_genarate()
elif(scan == 2 or scan==int("２")):
    print("\n　～文章加工～\n　　入力された文章をエッチにして返すプログラムです。\n　　画面の指示に従って，文章を入力してください。\n")
    sentence_remake()