def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    end = len(array) - 1    #末端の位置
    begin = 0               #先頭の位置
    to_back = begin         #先頭からの探索位置
    to_forward = end        #末端からの探索位置

    #先頭からの探索と末端からの探索がぶつかるまでループ
    while 1:
        #先頭から基準値以上の値を探索
        while array[to_back] < pivot:
            #先頭からの探索と、末端からの探索がぶつかった時点で探索を終了
            if to_back==to_forward:
                break
            to_back+=1

        #末尾から基準値未満の値の探索
        while array[to_forward] >= pivot:
            #先頭からの探索と、末端からの探索がぶつかった時点で探索を終了
            if to_back==to_forward:
                break
            to_forward-=1

        #値の交換
        temp = array[to_back]
        array[to_back] = array[to_forward]
        array[to_forward] = temp

        #ぶつかっていない場合、次に備えて探索位置をずらす
        if to_back!=to_forward:
            to_back+=1
        if to_back!=to_forward:
            to_forward-=1

        #探索がぶつかっている場合、ループを抜ける
        if to_back==to_forward:
            break

    meet_num = array[to_back]   #探索がぶつかった位置の値

    lower_group=[]      #基準値未満のグループ
    higher_group=[]     #基準値以上のグループ

    #探索がぶつかるまで値の交換がなかった場合
    if to_forward == 0 & to_back == 0:
        lower_group.append(meet_num)
        to_forward += 1
        higher_group.append(array[to_forward])
    

    #探索済み基準値未満の値を追加
    for i in range(0,to_back):
        lower_group.append(array[i])

    #探索がぶつかった位置の値が基準値未満の場合、基準値未満のグループの末尾に追加
    if meet_num < pivot:
        lower_group.append(meet_num)

    #再帰の実行
    lower_group = sort(lower_group)


    #探索がぶつかった位置の値が基準値以上の場合、基準値以上のグループの先頭に追加
    if meet_num >= pivot:
        higher_group.append(meet_num)

    #探索済み基準値以上の値を追加
    for i in range(to_forward+1,end+1):
        higher_group.append(array[i])

    #再帰の実行
    higher_group = sort(higher_group)

    return lower_group + higher_group

    # ここまで記述

if __name__ == '__main__':
    main()
