Heap Sort
- 特徵:第一個node具有最大值
- Heap Sort為完全二元樹的一種，二元樹中每個父節點最多有兩個子節點，而第一個node具有最大值。
- 先看Toutube兩個影片之後再自行寫出流程圖:
- https://www.youtube.com/watch?v=MtQL_ll5KhQ
- https://www.youtube.com/watch?v=JSmFZMJURug
- 流程圖
![image](https://github.com/poor314/poor314/blob/master/image/heap.jpg)
- 步驟:
- 1.把「第一個node」和「最後一個node」互換位置
- 2.假裝heap的「最後一個node」從此消失不見
- 3.對「第一個node」進行heapify
- 重複以上步驟，從heap的最後一個node開始，一路往上，直到root，便能得到排好序的矩陣

- 參考資料:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

