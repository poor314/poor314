- Insert新增:
- 依據binary tree的規則「左小右大」來新增資料
![image](https://github.com/poor314/poor314/blob/master/image/insert.jpg)
- Delete刪除
- 1.沒有子節點-直接刪除
- 2.只有一個子節點-刪除後，子節點取代原來的位置
- 3.有兩個子節點-刪除後，右子節點取代原來的位置
![image](https://github.com/poor314/poor314/blob/master/image/delete.jpg)
- Search搜尋(假設搜尋x)
- 1.若binary tree為空樹，或binary tree裡面沒有x，則搜尋失敗
- 2.若x小於root則往左子樹查找，找到x時，回傳x以及它的子節點
- 3.若x大於root則往右子樹查找，找到x時，回傳x以及它的子節點
![image](https://github.com/poor314/poor314/blob/master/image/search.jpg)
- Modify修改
- 1.若binary tree為空樹，或binary tree裡面沒有target，回傳錯誤
- 2.先搜尋target，找到後將它修改為新的值
![image](https://github.com/poor314/poor314/blob/master/image/modify.jpg)
參考資料:
- 1 https://emn178.pixnet.net/blog/post/94574434
- 2 https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
