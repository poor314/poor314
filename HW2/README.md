Heap Sort
- 特徵:第一個node具有最大值
- 步驟:
- 1.把「第一個node」和「最後一個node」互換位置
- 2.假裝heap的「最後一個node」從此消失不見
- 3.對「第一個node」進行heapify
- 重複以上步驟，從heap的最後一個node開始，一路往上，直到root，便能得到排好序的矩陣
- 參考資料:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

Merge Sort
- 步驟:
- 1.將陣列分割直到只有一個元素
- 2.開始兩兩合併，每次合併同時進行排序，合併出排序過的陣列
- 3.重複2的動作直接全部合併完成
- 參考資料:https://emn178.pixnet.net/blog/post/87965707
