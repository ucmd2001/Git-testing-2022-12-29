<h3>Git基本命令</h3>

<h6>初始化代碼倉庫</h6>

> git init

<h6>查看當前工作區與索引區的差別</h6>

> git status

<h6>把檔案添加到索引區</h6>

> git add test 

<h6>把檔案從索引區刪除 </h6>

> git rm test

<h6> 把檔案從索引區的狀態還原 </h6>

> git restore 

<h6> 把檔案傳到代碼倉庫 </h6>

> git commit test 

<h6>查看commit的更改內容/歷史紀錄</h6>

>git log

<h6>查看檔案的大小(-s),內容(-p),類型(-t)</h6>

> git cat-file

<h6>顯示索引區的檔案狀態 </h6>

>git ls-files -s

<h6> 看到unstaged 文件和現有文件的差別 </h6>

>git diff

<h6>顯示這個檔案的更改歷程,誰做更動的,時間與內容</h6>

>git blame index.html

---
<h3> 第一次建立 </h3>

需要先建立 SSH 並上傳 github/gitlab

    1.在cmd輸入

        ssh-keygen -o -t rsa -b 4096 -C "test@gmail.com"

    2.然後輸入
        cat ~/.ssh/id_ed25519.pub

    3.複製得到的文字 大約會長這樣

        ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILIqkcvYxeEKDWNY6oDa4tTRxC87UPTJnP9Usl/Yzb7R test@gmail.com

    4.之後到Git lab/ Git Hub / Settings  / SSH Key / New SSH key 新增SSH Key

    5.這樣你之後就可以使用SSH 方式進行git 遠端連線

*備註 :　如果是私領域的就需要使用SSH 通訊協定,公開網路例如Git hub可以選用 https ,但依然是需要做這一步驟

<h3>新增/初始化地端倉庫</h3>

有兩種方法 開啟Git Bash 
1. cd到自己建立好的資料夾中 在Bash/cmd中輸入 git init
2. cd到自己要建立的位置 Bash/cmd中輸入 git clone `git@192.168.14.21:test/test`
   方法2是在遠端倉庫上已經有建立好的專案,才能使用這個

<h3> 上傳至遠端倉庫步驟 </h3>

1. git add .     將當前資料夾的所有檔案加入索引區

2. git commit -m "version 1.0.0"  commit將檔案加入當前地端暫存區,-m 是指 message可自訂義

3. git remote add origin `git@192.168.14.21:test/test`  將地端倉庫與遠端倉庫做連結,只需要做一次

4. git push origin master 將地端倉庫commit暫存區的東西 push到遠端倉庫

*備註1: 可隨時用 git status 去查看當前檔案狀態
*備註2: 上傳後可用 git log 去察看歷史commit 紀錄

<h3> 更新過後上傳 </h3>

    1.git add .

	2.git commit -m "version 2.0.0"

	3.git push origin master

---
<h3>合併分支</h3>

把分支合併到Master上,要在master分支上

>git merge bugfix 

    輸出 >
        Updating 98278ad..cb1974c      把指針指向9827 指向cb19
        Fast-forward                   
        test2.txt | 1 +
        1 file changed, 1 insertion(+)  
        create mode 100644 test2.txt

    合併完成

把當前分支變成 Master接到後面,令其符合fast forward

>git rebase master 

* 不建議rebase master分支,因為大家共同協作的時候有可能會影響到其他正在工作的人。只建議在自己的分支上進行

---

<h3>修改 最後一次 commit 訊息</h3>

> git commit --amend 

修改最後一次 commit 訊息 ,沒有push前使用都可以 ,已經push就來不及了 ,只能重新commit一次
		     
透過amend 會更改commit的歷史 ,如果push後force 強制更改git log歷史會導致其他人沒辦法push (有衝突)

建議已經push的就直接再commit一次去修改訊息


> git commit --amend --no-edit 

直接跳過edit 畫面 ,有時候不需要修改commit訊息的時候就能使用

<h5>修改 commit 作者訊息</h5>

> git commit --amend--reset-author 

可以修改上一次commit中的 author 及 commit訊息 (會重新load .gitconfig檔)

---
<h3>回復到上一版</h3>

    1.git log --oneline -5      看一下線上最新五筆的版本紀錄 --oneline:以一行顯示
      git log --oneline

    2.git log                  看一下現在地端自己在哪一版本

    3.git reset --hard HEAD~1  回復到上一次的版本,刪除最新的提交   *備註1 
      git reset --soft HEAD~1  回復到上一版,保留最新的提交

    4.git log                  看一下現在地端自己是不是在正確的版本

    5.確認完更新後,完成新更改

    6.再次重新 add > commit > push   *備註2 備註3

*備註1:隨時使用git log看一下版本,確認自己是否再正確自己想要的版本,跟最新版本是否要刪除
*備註2:每次push前建議先切到本地master把origin拉下來，再去本地分支做rebase，解conflict，再push出去比較好
*備註3:回復到之前版本,再度執行push,實際上不會真的回到之前的版本,只會回到當初的版本狀態,你的Git Tree 還是繼續往前而非真的回到過去
*備註4:如果修改了內容，執行了git add，但沒有執行git commit 執行 git reset --hard 會刪除了已git add 但未git commit 的修改內容。

---
<h3> 取消add/commit操作 </h3>

1. git reflog 查看最近操作

2. git reset --hard 5a15e35 輸入上一次操作的SHA值,回復到上一動

*備註: 如果已經Push了建議直接重新commit一次,或是用上述的方式解決,這些方法都只建議在分支操作,不建議在Master操作,如果真的不小心Merge回Master才發現怪怪的,建議直接發布一版新版Master進行修正即可

---
<h3> CONFLICT 處理 </h3> 


<h5>情境1 : 遠端倉庫Master更新,地端倉庫Master也更新,地端這邊push 不了 (已經做完add commit push,被停在push )</h5>

    1.git pull origin master   >  同步更新遠端倉庫

    2.開啟vs code 查看衝突內容,選擇衝突內容項目要解決哪一個

    3.重新git add > commit > push



<h5>情境2 : 分支dev更新,遠端Master也更新,我要Merge回Master  > 需要rebase回master最新的狀態 (在master分支上輸入git merge dev 失敗)</h5>

    1.git switch master / git checkout master  切換到master

    2.git pull   更新master分支

    3.git switch dev  切換到dev分支

    4.git rebase master  重新對準master基準

    5.解決confilct

    6.git rebase --continue  繼續rebase流程

    7.git log > 看一下目前的git log是否為正確,但目前還沒辦法push,因為地端的git log跟遠端的git log不同

        方法1 : git push -f　強制push (可以在自己分支上面做,但盡量不要在master做)

        方法2 : 依照git 指示做 (建議事項)

        方法3 : 直接刪除你gitlab上的分支 重新上傳一次

        方法4 : 在本地端Merge完之後再推回去 **備註1**

    8.git push origin master

*備註1 : 等於是你在地端先做rebase , merge ,把分支接回去master最後之後再把這個master push回去
*備註2 : 所有的CONFLICT解決方式都一樣,先pull遠端查看目前地端與遠端差距,解決CONFLICT後再重新Push

---
<h3>git branch 分支指令</h3>

查看當前分支狀況

>git branch

創建名為test的分支

>git branch test 

強制刪除名為test的分支 (全部清空,但有commit的檔案還是會留著)

>git branch -D test 

刪除名為test的分支 (會提醒你有在分支上有做事)

>git branch -d dev 

將dev分支重新命名為tmp

>git branch -m dev tmp 

換到dev的分支上(會跟master在同一個分支,如果沒有改動的話)

>git checkout dev 

切換到任意commit上的分支,可以在這裡進行修改,提交commit (回到舊版本的概念)

>git checkout a3be96d  

切換到tmp的分支上,直接使用tmp分支(如果他不存在會直接創建新的分支),Head會指向tmp分支

>git checkout -b tmp 

如果還沒有git add,加上檔名可以直接恢復到目前在索引區的存檔

>git checkout `README.md` 

顯示從以前到現在的所有 git log

>git reflog  

---

<h3>Git log</h3>

Git log查詢 (都能使用--oneline做顯示)

顯示git commit 的順序

>git log

將git log 的資料縮成一行顯示

>git log --oneline 

將最近兩筆 commit縮成一行顯示

>git log --oneline -2 

顯示最近兩筆commit(git log使用倒敘 故為最新兩次commit)

>git log -2 

顯示最近十筆,並且使用oneline顯示

>git log -10 --oneline 

顯示日期後的commit(不包含)

>git log --after="2022-10-03" 

顯示日期以前的commit(包含)

>git log --before="2022-10-03" 

根據目前commit歷史做總結,可以看到大家commit的次數

>git shortlog  

顯示每次commit的詳細內容,可以看到修改了甚麼,作者是誰,時間,針對那個檔案修改

>git log --stat 

用圖形顯示 git log,簡易版的Sourcetree或是vs code

>git log --graph 

根據Junio C Hamano這個作者搜索git log ,查看有關他的git紀錄

>git log --author="Junio C Hamano" 

查詢git log中有layer關鍵字的commit紀錄

>git log --grep="layer" 

查詢所有的merge紀錄 

>git log --merges  

依照作者名稱進行排序,會顯示作者名稱與commit訊息

>git shortlog 

依照作者commit次數做排序

>git shortlog -n 

依照commit次數 進行排序

>git shortlog -n -s 

依照commit次數 進行排序 並顯示email

>git shortlog -n -s -e 

---
<h3>版本命名規則</h3>

<h5> 1.0.0 (A.B.C)  </h5>

    A: 大版本, 大的Feature 更新

    B: 小版本, 小的Feature 更新

    C: Bug fix版本 ,只修復Bug ,無任何Feature加入

假設發布了2.9, 通常都要去下載最新的版本 ex :  2.9.7 

那如果要修復Bug (Master上也會有) ,版本應該在哪裡commit呢 ? Master還是Branch?  

<font color=#FF6600>答案是Branch,改完Bug之後再Merge回Master</font>

    1. 先建立一個分支 2.9.0-bug-fix 並更新Bug

    2. 發布新的tag 2.9.1 

    3. 依據這個2.9.0-bug-fix 版本 push到遠端倉庫

如果這個bug fix 確定要新增回Master

    1. 到Master上Merge 這個分支 
    2. 解決衝突 
    3. Merge成功 成為2.9.1版本


*備註: 之後bugfix就會在這個2.9.0-bug-fix上持續進行, 創立2.9.1-bug-fix / release/2.9.1 分支, 然後刪除2.9.0-bug-fix 重複以上動作 ,這個分支就稱作為release 版本 

---


