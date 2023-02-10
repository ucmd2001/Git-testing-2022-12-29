# <h3>Git add </h3>

將輸入的檔案加到git暫存庫中
>git add XXX  

去看當前git的資料夾架構

>tree .git/ 

看當前.git資料夾的所有架構

>tree /F .git/ 

查看當前資料夾檔案

>git ls-files  

列出當前資料夾檔案詳細訊息 

>git ls-files -s 
    輸出: 100644 (權限) e2129701f1a4d54dc44f03c93bca0a2aec7c5449 (blob對象) 0 ()       file1.txt(檔案名稱)

---

## <h3>git 文件狀態</h3>

    Untracked - 沒有被放到git中(在工作區域中創建的新檔案)

    Modified - 被更改過的檔案 (已經被git add/commit過的檔案) 

    Staged - 被增加到暫存庫狀態

    Unmodified - 資料被git commit 新增到代碼倉庫後的狀態

---

## <h3>Git log</h3>

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

## <h3> git commit </h3>

commit 檔案 "1st commit" 可自訂，知道當前的Commit是甚麼即可 -m 指的是message

>git commit -m "1st commit"  

    輸出畫面:
    >[master (root-commit) a3be96d] 1st commit  根root 
    > 2 files changed, 5 insertions(+)  >兩個檔案被改變，有五行變化
    > create mode 100644 file1.txt  > 建立兩個100644檔案
    > create mode 100644 file2.txt  

<h3>如何寫好一個好的 commit訊息 </h3>

    1.區分subject 和 Body用一個空行隔開

    2.Subject 
        一般不超過50個字 如果寫超過代表這次改版太多了,建議分幾次commit上傳 
        
        首字母大寫 結尾不需要句點

    3.body 
        詳細描述這次改版內容與功能 一行約在72字

<h3>修改 最後一次 commit 訊息 </h3>

>git commit --amend 

* 修改最後一次 commit 訊息,沒有push前使用都可以,已經push就來不及了 ,只能重新commit一次
* 透過amend 會更改 commit的歷史 ,如果push後force 強制更改git log歷史會導致其他人沒辦法push (有衝突)

* 建議已經push的就直接再commit一次去修改訊息

直接跳過edit 畫面 ,有時候不需要修改commit訊息的時候就能使用

>git commit --amend --no-edit 


<h5>修改 commit 作者訊息</h5>

可以修改上一次commit中的 author 及 commit訊息 (會重新load .gitconfig檔)

>git commit --amend--reset-author  
---
## <h3>git branch 分支指令</h3>

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

## <h3>分支合併</h3>

把分支合併到Master上,要在master分支上

>git merge bugfix 

    輸出 >
        Updating 98278ad..cb1974c      把指針指向9827 指向cb19
        Fast-forward                   
        test2.txt | 1 +
        1 file changed, 1 insertion(+)  
        create mode 100644 test2.txt

把當前分支變成 Master接到後面,令其符合fast forward

>git rebase master 

* 不建議rebase master分支,因為大家共同協作的時候有可能會影響到其他正在工作的人。只建議在自己的分支上進行

---
## <h3>Git remote 遠程倉庫</h3>

查看遠程倉庫

>git remote  

查看本地與遠端的倉庫差別(看看自己有沒有改)

>git remote -v 

可以看到remote 與 分支訊息

>cat .git/config 

查看遠端倉庫的branch資訊

>git branch -r  

查看地端倉庫的branch資訊

>git branch -l  

查看本地與遠程的branch資訊

>git branch -a  

查看地端倉庫的分支詳細訊息

>git branch -vv 

查看現在遠端倉庫refs對準的資料

>cat .git/packed-refs 

查看每個分支的狀況,並且進行同步(如果刪除一個分支,fetch並不會同步刪除)

>git fetch  

把本地有,遠端沒有的分支刪除

>git fetch --prune 

顯示目前遠端倉庫名字

>git remote 

顯示遠程倉庫url (fetch,push)

>git remote -v 

顯示遠程倉庫 Origin與目前地端倉庫的相關性

>git remote show origin 

刪除遠端倉庫已經刪除的分支(透過fetch刪除需要加 --prune)

>git remote prune 

把遠端倉庫origin的master分支進行更新

>git merge origin/master 

取代git fetch + git merge ,讓他跟遠端倉庫進行同步

>git pull 

把地端倉庫push到遠端Origin倉庫的Master分支上

>git push origin master  

* 可以直接git pull 然後在Vs code內解決衝突後重新push

* 有時候使用git pull 會有Conflict 可以先使用git fetch 確認是否有衝突,如果有衝突先解決衝突

* 或是使用git diff origin/master  查看一下本地與遠端差別,確認衝突與否,再進行merge

* 如果不清楚是否有衝突,還是先fetch一次,再去merge

* git fetch > 再git pull  >然後  git reset --hard ORIG_HEAD 
 可以把pull中第二步的merge 取消 ,這樣做可以把merge錯的部分取消,可以再度merge正確的版本

## <h3>Git Remote 遠端倉庫(用GitHub示範)</h3>

    1.git remote add origin https://github.com/ucmd2001/git-demo.git  

	    > 把地端的代碼倉庫(commit完之後的),上傳到remote的倉庫,可以在.git/config檔案看到差別

    2.git push -u origin master 
        > 把地端的代碼倉庫Push到remote上  (-u =--set-upstream )

    輸出 >　

        Enumerating objects: 11, done.					11個object
        Counting objects: 100% (11/11), done.				
        Delta compression using up to 8 threads
        Compressing objects: 100% (7/7), done.				壓縮檔案到7個
        Writing objects: 100% (11/11), 865 bytes | 865.00 KiB/s, done.  
        Total 11 (delta 2), reused 0 (delta 0), pack-reused 0
        remote: Resolving deltas: 100% (2/2), done.
        To https://github.com/ucmd2001/git-demo.git
        * [new branch]      master -> master				創建一個新的名為master的branch到remote 倉庫
        branch 'master' set up to track 'origin/master'.


    3.git clone https://github.com/ucmd2001/git-demo  
        > 把遠端代碼倉庫的目錄整個複製到當前目錄下


    4.git clone https://github.com/ucmd2001/git-demo my-local-git-demo  
        > 把遠端代碼倉庫的整個目錄複製到自己指定的目錄下


---
## <h3>Git tag</h3>

tag標籤在日常生活中可以解釋成標示簡單訊息的小牌子,跟分支一樣標籤也會指向某個Commit ，但是並不會像分支一樣隨著 Commit 移動。因此，兩者之間最大的差異在於：分支會隨著 Commit 移動，而標籤則是固定留在某個 Commit 上。



創建tag v1.0.0

> git tag v1.0.0 

刪除tag v1.0.0

> git tag -d v1.0.0 

創建一個tag Message為 "v1.0.0" 的v1.0.0 tag

> git tag -a v1.0.0 -m "v1.0.0" 

看特定tag和與其相對應的commit 訊息

> git show v1.4

推送地端tag到遠程倉庫

> git push origin *tagname*

看一下4cb75 裡面的內容,會顯示tag為多少 tagger是誰

    git cat-file -p 4cb752075 

    Ex:
        object 95433bd7cb271739e25ebe627aa14331644b564e
        type commit
        tag v1.0.0
        tagger test <test@gmail.com> 1668583241 +0800

可以同步tag 更新 , 但不會刪除本地倉庫中的tag 需要自己刪除

> git fetch 

刪除遠端倉庫origin的v1.0 tag

>git push --delete origin v1.0 

---

## <h3>git reset 版本回復</h3>

**mixed模式(默認)** : 會保留檔案修改 ,後續commit文件變化會保留 ,保留的變化會存在緩存區

>git reset `commit-id` 

修改完之後再次 add commit push即可

**soft** : 與mixed模式的區別是 ,會把更改過後的檔案放到工作區內 (modified 是綠色的)

>git reset --soft `commit-id` 
				
會直接把之後更改的檔案內容直接加進來 ,如果不要的話就是直接進行更改再add commit push即可

**hrad** : 在這次commit 之後的修改都會被刪除 ,git status會全部為空,要注意使用 --hard 

>git reset --hard `commit-id`  

* 備註 : 由於在地端進行版本回復,會導致其他人的git log歷史與遠端倉庫不同 ,這時候需要依照git 給的指示進行回復,不建議使用 git push -f origin master 會導致其他人的歷史也不同

把Head指針往前移到上一個commit,然後把最新的commit刪除,可以重新add commit一次

>git reset ORIG_HEAD 

---

## <h3>git clone </h3>

    1. 遠端現有倉庫 ,直接clone 到地端 (會有遠端git log)
        > 創一個新資料夾 >  輸入git clone git@github.com:git/git.git

    2. 現有空白git 倉庫 ,clone遠端倉庫資料 (git log是空白) > 
        > 創一個新資料夾 > 輸入git init >  git clone git@github.com:git/git.git

    3. 現場已經有檔案, 直接clone檔案到地端 (git log會維持地端,push的時候需要注意)
        > 輸入  git clone git@github.com:git/git.git

    4. git clone git@github.com:git/git.git git-test --depth=1
        > 只clone最新的一次commit中的所有檔案 ,不包含之前的歷史紀錄 ,可以用git log看

**想要clone特定版本的 檔案**

    1. git init git-test  > 先初始化一個新資料夾 

    2. cd git-test

    3. git remote add origin git@github.com:git/git.git > 把遠端倉庫add進來, 但千萬不要pull / fetch

    4. 有兩種方法  方法1 : git fetch origin 15.0.1 > fetch 指定的版本		(會包含歷史訊息)
            方法2 : git -c protocol.version=2 fetch origin 15.0.1 --depth=1  (只fetch該版本該tag的檔案)

    5. ls 看一下檔案 應該會有一個HEAD

    6. git checkout FETCH_HEAD > 會直接到該版本的SHA分支

* 備註: 可以在git clone前輸入 time 結束後會給你花費時間

* 備註2:  git clone git@github.com:git/git.git 可以輸入名字 

	例如: git clone git@github.com:git/git.git test 會建立一個資料夾名稱為test的資料夾 裡面放你clone下來的資料

* 備註3: 想要clone特定版本手續比較麻煩 需要多嘗試
---

## <h3>Group Project Member Settings 權限管理</h3>


    Project 會員等級 > Guest ,Reporter ,Developer ,Master

    Guest > 只能看,不能寫,只能留評論,不能做任何更改

    Reporter > 能Pull ,能改程式, 但要Merge回Master的時候需要經過同意 (類似於公開倉庫要提交,需要通過Maintaner同意)

    Developer > 都能做 ,但在創建分支的時候會預設為分支 ,在Merge回Master的時候也需要經過同意

    Master > 都能做


    *Group 也是同理,多一個Owner可以設定為團隊擁有者 ,可以設定更多層級

---

## <h3>Merge Requeset </h3>

權限管理的一種,可以透過這種方式透過Code Review再進行Merge

Merge 

    方法1. 在本地創建分支後Push上去

    方法2. 在遠端創建後再Pull下來

        在Gitlab 左側欄位 > Merge Request > Add new Merge Request > Commit Request > 
        ....等待同意 > Merge (可以勾選Remove Source Branch)

    方法3.  Fork後再Pull 回遠端倉庫,跟GitHub完全相同

        Frok完之後就是個人領域甚麼都能做,改完之後再提交Merge request


---
## <h3>.gitignore  </h3>

建立.gitignore來過濾我們不需要的文件

在裡面可以建立各種我們想要忽略的文件 ,不只增加資安也能加快上傳下載速度

例如: 不需要的txt,作為註解的內容  ,多餘的測試 .py檔等

善用.gitignore 可以增加很多效率

忽略 secret.yml 檔案
>secret.yml

忽略 config 目錄下的 database.yml 檔案
>config/database.yml

忽略所有 db 目錄下附檔名是 .sqlite3 的檔案
>/db/*.sqlite3

忽略所有附檔名是 .tmp 的檔案
>*.tmp

當然你要忽略自己也可以，只是通常不會這麼做
>.gitignore

---

## <h3>hook</h3>

使用: .git檔案夾中 > 刪除.sample檔名 > 即可啟用

直接跳過hook強制commit(不建議使用,除非Hotfix需要緊急修復)

>git commit -m `'update test.py'` --no-verify  

---

## <h3>git gc 壓縮</h3>

壓縮檔案, git add  > git commit 完之後 輸入 ,會壓縮Pack中的同樣項目,讓其重複項壓縮,只保留變更項

>git gc  

查看目前.git/objects 的檔案內容與大小

>du -h .git/objects 

* git gc 是針對每次commit的重複項進行壓縮,只保留修改的地方

tree .git/objects/pack 中間有一個.idx文件,是索引值,方便git快速查找文件

會保存之前的所有變更的idx,可以直接查看過去的所有index

>git verify-pack -v .git/objects/pack/pack-d519bf64a6aeb93b836f09dea2130020987bc25d.idx 

* 壓縮優點是對未來下載跟上傳方便,缺點是要去看特定歷史blob和tree檔會比較慢

**git objects 解壓縮**

將壓縮檔進行解壓縮到objects 目錄

>git unpack-objects < .git/objects/pack/pack-d519bf64a6aeb93b836f09dea2130020987bc25d.pack

---

## <h3>git 垃圾 objects 清理  </h3>

把無用 Unreachable的objects 刪除(tree檔/blob檔)

模擬執行prune 但不會真的刪除檔案

>git prune -n 

執行垃圾objects刪除

>git prune 

**深度清理 **

    git -c gc.reflogExpire=0 -c gc.reflogExpireUnreachable=0 \
    -c gc.rerereresolved=0 -c gc.rerereunresolved=0 \
    -c gc.pruneExpire=now gc "$@"  

* 這是針對地端,上傳時已經把指令都執行完了,執行完prune後再執行Push會說Everything up-to-date

---

## <h3>git stash</h3>

>git stash  緩存  可以將目前沒有完成的檔案加入緩存,但不會加入 add 狀態內

1. 把目前沒有commit 的檔案進行暫存 ,之後可以繼續完成工作

>git stash save 

2. 可以將stash 進行命名並把工作儲存 ,然後移動至其他分支(master) ,結束後再pop緩存即可

>git stash --include-untracked "feature-1 stash" 

3. 把最新的緩存拿出來 (FILO)

>git stash pop 

4. 可以看到stach 所有指令

>git stash -f  

5. 刪除stash

>git stash drop *stash* 

6. 回朔上一次工作狀態, 類似於git stash pop

>git stash apply “stash@{index}” 


* stash 是存在本地的緩存,並不會存在遠端倉庫,如果本地環境改變(關機),會導致stash消失

* 如果真的要保存暫存檔,建議還是可以add commit ,之後再次完成 
 
  或是 add > stash 然後再進行切換分支 之後再pop出來 或是 git stash apply “stash@{index}”回朔上一次工作狀態

* 如果沒有stash完,直接切換到master,會導致未完成工作一起被帶到master分支

---

## <h3>git worktree</h3>

工作目錄  在地端的一個特定文件夾內,把某一個分支checkout出來

添加一個新的worktree ,指定路徑為上一層的../git-demo-master 資料夾
                                          
1. 以master為新的分支開頭 ,可以使用cd 進行切換分支

>git worktree add ../git-demo-master master 

2. 新增一個基於 master 的新 branch，這個 branch 叫 enhancement/gradle_upgrade
位於 <上層目錄>/gradle_update 資料夾，是全新的一個工作目錄。

>git worktree add -b enhancement/gradle_upgrade ../gradle_update master 

3. 查看目前worktree中的所有列表

>git worktree list 

4. 刪除工作目錄

>git worktree remove *worktree*


* Worktree指令可以讓你不用離開目前的工作階段，在其他的資料夾新增另一個工作目錄，在那裡進行變更。就像是多了幾條軌道，不用誰讓位就可以繼續前進。

---

## <h3>git Submodule</h3>

當一個code 倉庫需要依賴於 另一個 資料庫或是.dll資料庫等 ,會使用submodule

目前很少使用 ,通常都會直接再語言內部進行語言的代碼下載與安裝 ,有時候無法通過網路等方式引入module,就可以使用submodule進行子module來進行引入及儲存

對於git 來說 submodule是文件, 而非是一個資料夾 ,因為不會在這個submodule中進行更改 ,只會更改主要的分支

新增一個submodule 進目前的倉庫內

>git submodule add `git@192.168.14.21`:test/test-123.git 

* git pull 下來會沒有submodule 資料庫 ,只會有主要的module ,需要submodule的話需要手動輸入

>git submodule update --init --recursive 

**如果需要子倉庫更新的話**

1. 情況一 : 遠端子倉庫更新,地端子倉庫也想要更新

	>git submodule update --remote

	可以輸入 git status 去看情況,正常需要add commite push 

2. 情況二 : 地端子倉庫更新,遠端倉庫也想要更新

	可以刪除目前的子倉庫 ,然後重複上面的步驟
---

## <h3>Git objects </h3>

    git status > 查看目前資料夾git 的狀態

    git cat-file -t 8d04e1 > -t 查看對象類型

    git cat-file -p 8d04e1 > -p 查看對象類型內容

    git cat-file -s 8d04e1 > -s 查看對象內容大小

    以上三個加起來就能看到他的SHA值為多少

    cat hello.txt > 也可以查詢對象內容

    cat 8d/0e41234f24b6da002d962a26c2495ea16a425f > 執行後得到Hash過的值

    shasum shattered-* > 顯示當下資料夾的hash值

    
* 如果hash過兩個資料夾的值為相同，git add 就不會更新資料夾，會判斷成它是相同的檔案，須注意。

---

## <h3>git diff </h3>

    diff --git a/file1.txt b/file1.txt
    index a0b12c3..bd931c3 100644  左邊是索引區的內容,右邊是工作區的內容
    --- a/file1.txt    索引區的文件
    +++ b/file1.txt	   工作區的文件	
    @@ -1,4 +1,4 @@    顯示索引區的內容,從第一行開始到第四行

    紅字顯示索引區內容
    綠字顯示工作區內容

* 備註: git add file1.txt 後 使用git diff --cached 可以看到剛剛git add的內容