# aiotieba使用教程

## 命名约定

如果你希望从贴吧后端获取数据，那么你应该对以下字段的含义有一个基本的认识

### BDUSS

> 贴吧的服务端使用`BDUSS`来确认用户身份
> 
> `BDUSS`是一串由纯`ascii`字符组成的，长度为`192`的字符串
> 
> 使用`BDUSS`可以完成**一切**不需要手机/邮箱验证码的操作，包括**发帖**/**发私信**/**获取账号上的所有历史发言**
> 
> `BDUSS`没有时效性，只能通过退出登录或修改密码使其失效
> 
> 因此将`BDUSS`泄露给不受信任的人可能导致长期的账号安全风险和隐私泄露风险
> 
> 在浏览器的`Cookie`和各种表单参数中你都能看到它的身影
> 
> 搜索 `你的浏览器型号`+`如何查看网站的Cookie` 就能知道如何获取你的贴吧账号的`BDUSS`了
> 
> 以`Chorme`为例，在任何一个贴吧网页下按<kbd>F12</kbd>调出开发者选项，然后你就能在下图的位置找到它

![Chrome Cookie](https://user-images.githubusercontent.com/48282276/179938990-77139ea2-2d94-4d38-8d7d-9c6a3d99b69e.png)

### user_name

> 用户名
> 
> 每个贴吧用户的用户名都是唯一的，但用户可以没有用户名
> 
> 请注意将其与可重复的昵称`nick_name`相区分
> 
> 在`utf-8`编码下，用户名的长度一般不会超过`14`个字节

### portrait

> 头像ID
> 
> 每个贴吧用户都有且仅有一个`portrait`
> 
> `portrait`是一串由纯`ascii`字符组成的，以`tb.1.`作为开头的，长度为`33~36`的字符串（仅有一些远古时期的ip账号不符合这个规则）
> 
> 譬如我的`portrait`就是`tb.1.8277e641.gUE2cTq4A4z5fi2EHn5k3Q`
> 
> 你可以通过`portrait`获取用户头像，例如[我的头像](http://tb.himg.baidu.com/sys/portraith/item/tb.1.8277e641.gUE2cTq4A4z5fi2EHn5k3Q)
> 
> 你可以在[client.py](../aiotieba/client.py)中搜索`user.portrait`来查看`portrait`的具体应用场合

### user_id

> 用户ID
> 
> 每个贴吧用户都有且仅有一个`user_id`
> 
> 请注意将其与用户个人主页的`tieba_uid`相区分
> 
> `user_id`是一个`uint64`值（仅有一些远古时期的ip账号不符合这个规则）
> 
> 你可以在[client.py](../aiotieba/client.py)中搜索`user.user_id`来查看`user_id`的具体应用场合
> 
> `user_name` `portrait` `user_id` 都是满足唯一性的用户标识符，并可以通过其中任意一个的值反查其余两个

### tieba_uid

> 用户个人主页ID
> 
> 每个贴吧用户都有且仅有一个`tieba_uid`
> 
> 请注意将其与用户的`user_id`相区分
> 
> `tieba_uid`是一个`uint64`值（仅有一些远古时期的ip账号不符合这个规则）
> 
> 可以通过`tieba_uid`的值反查`user_name` `portrait` `user_id`

### fid

> 吧ID
> 
> 每个贴吧都有且仅有一个`fid`
> 
> `fid`是一个`uint64`值
> 
> 你可以在[client.py](../aiotieba/client.py)中搜索`fid: int`来查看使用了`fid`作为参数的接口
> 
> 在贴吧混乱的字段命名中，它在某些场合下会被命名为`forum_id`

### tid

> 主题帖ID
> 
> 每个主题帖都有且仅有一个`tid`
> 
> `tid`是一个`uint64`值
> 
> 你可以在[client.py](../aiotieba/client.py)中搜索`tid: int`来查看使用了`tid`作为参数的接口
> 
> 在贴吧混乱的字段命名中，它在某些场合下会被命名为`thread_id`

### pid

> 回复ID
> 
> 每个楼层、楼中楼都有且仅有一个`pid`
> 
> `pid`是一个`uint64`值
> 
> 你可以在[client.py](../aiotieba/client.py)中搜索`pid: int`来查看使用了`pid`作为参数的接口
> 
> 在贴吧混乱的字段命名中，它在某些场合下会被命名为`post_id`

## Python异步编程入门

想要用好`aiotieba`库，你必须初步掌握`Python`异步编程

如果你不熟悉`Python`异步编程，建议阅读下列教程：

+ [轻松理解Python中的async/await](https://blog.csdn.net/Likianta/article/details/90123678) 非常易于理解的入门案例
+ [Python官方文档 协程与任务](https://docs.python.org/zh-cn/3/library/asyncio-task.html) 包含详尽Reference和配套案例的官方文档，更适合有一定基础的初学者
+ [Python Async/Await入门指南](https://zhuanlan.zhihu.com/p/27258289) 已经是17年的文章了，从生成器`yield`的角度出发介绍`Python`异步，对初学者不太友好，更适合拔高阅读
+ [深入理解JavaScript中的async/await](https://www.cnblogs.com/youma/p/10475214.html) `JavaScript`中的`Promise`与`Python`中的`Future`概念很相似，该教程可以帮助你快速地从`Promise`异步模式出发理解`async-await`异步模式

如果你已经对异步编程的相关知识非常熟悉，那么我建议你按`4-1-2-3`的顺序阅读

如果你只是编程初学者或者对各种异步模式一窍不通，那么我建议你按`1-2-3`的顺序阅读

当然即便你没有阅读上面的教程，我也会针对异步编程的初学者为每一行异步代码撰写详细的注释

## 案例1 配置BDUSS并获取账号信息

如果你刚刚已经运行过下列代码

```python
import asyncio

import aiotieba


async def main():
    async with aiotieba.Client() as client:
        print(await client.get_threads("图拉丁"))


asyncio.run(main())
```

那么你可能注意到了一条日志输出

```log
<2022-07-16 20:13:54.514> [WARNING] [<module>] 配置文件已生成 请参考[https://github.com/Starry-OvO/Tieba-Manager/blob/master/docs/tutorial.md]完成对./aiotieba.toml的配置
...
```

在工作目录下，你能看到自动生成的`aiotieba.toml`配置文件

如果你需要使用账号相关的功能，那么你需要将你的`BDUSS`填入该文件的正确位置

填写完毕的`aiotieba.toml`大概长这样

```toml
[User]

[User.default]
BDUSS = "2dNNk1wMXVSZmw2MnpkWDNqMnM4MmFaeFZYNVVPUEhPS0thNFZzUERjME52V1KpSVFBQUFBJCQAAAAAAQAAAAEAAAA0lUwndl9ndWFyZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0wPmINMD5iY" # 把你的那一串长长的BDUSS放在这
```

然后复制下列代码并运行

```python
import asyncio

import aiotieba as tb


# 定义异步函数main
# 需要明确async def...和def...在定义函数上的区别
# 对于def定义的同步函数func，func()会直接返回结果
# 而对于async def定义的异步函数afunc，afunc()只会返回一个可等待（Awaitable）的协程
# 你需要使用await或asyncio.run或其他语句来等待协程执行完毕后才能拿到返回结果
async def main():
    # 使用键名"default"对应的BDUSS创建客户端
    # async with会先调用tb.Client的__init__方法同步地创建一个实例
    # 再异步调用__aenter__方法来自动完成一些资源初始化工作（如创建连接池），并将返回值赋给client变量
    # 最后，在async with的作用域结束时，tb.Client的__aexit__方法会被自动地异步调用以完成一些清理工作（如关闭所有连接并释放资源）
    # async with...as...与with...as...的用途类似，都是为了实现优雅的初始化操作与退出操作
    # 区别仅仅在于前者调用的__aenter__和__aexit__都是异步方法，而后者调用的__enter__和__exit__都是同步方法
    # 参考官方文档：异步上下文管理器
    # https://docs.python.org/zh-cn/3/reference/datamodel.html#asynchronous-context-managers
    async with tb.Client("default") as client:
        # client.get_self_info()是一个协程对象
        # 通过在它前面添加一个await语句，我们可以以一种非阻塞的方式等待它执行完毕
        # 该协程执行完毕时，将会返回对应贴吧账号的非敏感个人信息
        # 参考官方文档：可等待对象
        # https://docs.python.org/zh-cn/3/library/asyncio-task.html#awaitables
        user = await client.get_self_info()

    # 将获取的信息打印到日志
    tb.LOG.info(f"当前用户信息: {user!r}")


# 执行协程main()
# 参考官方文档：运行asyncio程序
# https://docs.python.org/zh-cn/3/library/asyncio-task.html#running-an-asyncio-program
asyncio.run(main())
```

如果你的`BDUSS`填写无误，你会获得类似下面这样的结果

```log
<2022-07-16 20:14:34.597> [INFO] [main] 当前用户信息: {'user_id': 957339815, 'user_name': 'kk不好玩', 'portrait': 'tb.1.8277e641.gUE2cTq4A4z5fi2EHn5k3Q'}
```

## 案例2 简单并发爬虫

复制下列代码并运行

```python
import asyncio

import aiotieba as tb


async def main():
    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as client:
        # 下面这行语句会同时请求用户个人信息和图拉丁吧首页前30帖
        # 你可以将若干协程作为参数传入asyncio.gather，这里传入的参数为client.get_self_info()和client.get_threads('图拉丁')
        # asyncio.gather会为每个传入的协程创建对应的任务来同时执行它们（并发）
        # 同时asyncio.gather(...)也会返回一个协程，在前面添加await等待其执行完毕
        # 执行完毕后，返回数据的顺序与传入参数的顺序一致，即user对应client.get_self_info()，threads对应client.get_threads('图拉丁')
        # 参考官方文档：并发运行任务
        # https://docs.python.org/zh-cn/3/library/asyncio-task.html#running-tasks-concurrently
        user, threads = await asyncio.gather(client.get_self_info(), client.get_threads('图拉丁'))

    # 将获取的信息打印到日志
    tb.LOG.info(f"当前用户信息: {user}")
    for thread in threads:
        # threads支持迭代，因此可以使用for循环逐条打印主题帖信息
        tb.LOG.info(f"tid: {thread.tid} 最后回复时间戳: {thread.last_time} 标题: {thread.title}")


# 使用asyncio.run执行协程main
asyncio.run(main())
```

运行效果如下所示

```log
<2022-07-16 20:56:47.006> [INFO] [main] 当前用户信息: {'user_id': 957339815, 'user_name': 'kk不好玩', 'portrait': 'tb.1.8277e641.gUE2cTq4A4z5fi2EHn5k3Q'}
<2022-07-16 20:56:47.006> [INFO] [main] tid: 7924884407 最后回复时间戳: 1657877692 标题: 分享贴子
<2022-07-16 20:56:47.016> [INFO] [main] tid: 2949701560 最后回复时间戳: 1655038527 标题: 【重要更新】百度图拉丁吧吧规 20140329
<2022-07-16 20:56:47.017> [INFO] [main] tid: 7896485738 最后回复时间戳: 1657976199 标题: 装机其他配件陆陆续续都买齐了，就差显示器了。
<2022-07-16 20:56:47.017> [INFO] [main] tid: 7926932272 最后回复时间戳: 1657976200 标题: 散人求问！就这，10块钱买到的！
<2022-07-16 20:56:47.018> [INFO] [main] tid: 7926963000 最后回复时间戳: 1657976195 标题: 有人福利价两条DDR38G内存条吗
<2022-07-16 20:56:47.018> [INFO] [main] tid: 7926025065 最后回复时间戳: 1657976194 标题: 果真电脑店都是奸商
<2022-07-16 20:56:47.019> [INFO] [main] tid: 7926209178 最后回复时间戳: 1657976191 标题: 怎么能阻止我爸玩我电脑
<2022-07-16 20:56:47.019> [INFO] [main] tid: 7926950537 最后回复时间戳: 1657976189 标题: 带佬们，擦了擦cpu，结果点不亮了。结果发现主板cpu卡槽
<2022-07-16 20:56:47.020> [INFO] [main] tid: 7926605589 最后回复时间戳: 1657976185 标题: 咸鱼到手刀真恶心
<2022-07-16 20:56:47.020> [INFO] [main] tid: 7926961253 最后回复时间戳: 1657976186 标题: 牛爷爷们，预算5-6k求个单子
<2022-07-16 20:56:47.021> [INFO] [main] tid: 7925878206 最后回复时间戳: 1657976184 标题: 这个配置怎么样？
<2022-07-16 20:56:47.022> [INFO] [main] tid: 7925341844 最后回复时间戳: 1657976180 标题: 这么高的配置打lol开团卡成幻灯片
<2022-07-16 20:56:47.022> [INFO] [main] tid: 7926838704 最后回复时间戳: 1657976180 标题: 完蛋了，换了主板，不会插线了，救命！
<2022-07-16 20:56:47.023> [INFO] [main] tid: 7926597738 最后回复时间戳: 1657976180 标题: 淘宝翻车我转手就上拼多多
<2022-07-16 20:56:47.023> [INFO] [main] tid: 7926952718 最后回复时间戳: 1657976175 标题: 兄弟们，这个电脑我要是入手什么价格合适
<2022-07-16 20:56:47.024> [INFO] [main] tid: 7926078320 最后回复时间戳: 1657976174 标题: 3050真的是垃圾卡吗🤔
<2022-07-16 20:56:47.025> [INFO] [main] tid: 7926962437 最后回复时间戳: 1657976170 标题:
<2022-07-16 20:56:47.025> [INFO] [main] tid: 7925259456 最后回复时间戳: 1657976170 标题: 求大佬看看可不可入🥰pdd上的整机为 啥这么便宜？
<2022-07-16 20:56:47.026> [INFO] [main] tid: 7926937893 最后回复时间戳: 1657976169 标题: 第一次买电脑，是买零件自己装还是买品牌机
<2022-07-16 20:56:47.027> [INFO] [main] tid: 7926958973 最后回复时间戳: 1657976205 标题:
<2022-07-16 20:56:47.027> [INFO] [main] tid: 7926962111 最后回复时间戳: 1657976156 标题: 有人买联想拯救者刃这款主机的么？质量咋样？求告知
<2022-07-16 20:56:47.028> [INFO] [main] tid: 7926477067 最后回复时间戳: 1657976152 标题: 这个信息是真的假的呀
<2022-07-16 20:56:47.029> [INFO] [main] tid: 7577926810 最后回复时间戳: 1657976151 标题: 显示屏一半暗一半亮怎么办
<2022-07-16 20:56:47.029> [INFO] [main] tid: 7926744414 最后回复时间戳: 1657976151 标题: 大佬们  这套配置加显示器卖我  2300亏吗？卖家说一年期配的
<2022-07-16 20:56:47.030> [INFO] [main] tid: 7926961884 最后回复时间戳: 1657976146 标题: 电脑视频线插独立显卡，显示检测不到信号线，插集成显卡屏幕黑屏！
<2022-07-16 20:56:47.031> [INFO] [main] tid: 7923574035 最后回复时间戳: 1657976143 标题: 卡诺基yyds
<2022-07-16 20:56:47.031> [INFO] [main] tid: 7925270056 最后回复时间戳: 1657976140 标题: 老哥们问个问题
<2022-07-16 20:56:47.032> [INFO] [main] tid: 7926056349 最后回复时间戳: 1657976140 标题: 新手第一次装机
<2022-07-16 20:56:47.033> [INFO] [main] tid: 7926912956 最后回复时间戳: 1657976137 标题: 8u们，这个配置最高能玩什么游戏。
<2022-07-16 20:56:47.034> [INFO] [main] tid: 7925518317 最后回复时间戳: 1657976132 标题: 救救孩子吧
```

## 案例3 多协程爬虫

复制下列代码并运行

```python
import asyncio
import time
from typing import List

import aiotieba as tb


async def crawler(fname: str):
    """
    获取贴吧名为fname的贴吧的前32页中浏览量最高的10个主题帖

    Args:
        fname (str): 贴吧名
    """

    start_time = time.perf_counter()
    tb.LOG.info("Spider start")

    # thread_list用来保存主题帖列表
    thread_list: List[tb.Thread] = []

    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as client:

        # asyncio.Queue是一个任务队列
        # maxsize=8意味着缓冲区长度为8
        # 当缓冲区被填满时，调用Queue.put的协程会被阻塞
        task_queue = asyncio.Queue(maxsize=8)
        # 当is_running被设为False后，消费者会在超时后退出
        is_running = True

        async def producer():
            """
            生产者协程
            """

            for pn in range(32, 0, -1):
                # 生产者使用Queue.put不断地将页码pn填入任务队列task_queue
                await task_queue.put(pn)
            # 这里需要nonlocal来允许对闭包外的变量的修改操作（类似于引用传递和值传递的区别）
            nonlocal is_running
            # 将is_running设置为False以允许各消费协程超时退出
            is_running = False

        async def worker(i: int):
            """
            消费者协程

            Args:
                i (int): 协程编号
            """

            while 1:
                try:
                    # 消费者协程不断地使用Queue.get从task_queue中拉取由生产者协程提供的页码pn作为任务
                    # asyncio.wait_for用于等待一个协程执行完毕直到超时
                    # timeout=1即把超时时间设为1秒
                    # 如果超过1秒未获取到新的页码pn，asyncio.wait_for将抛出asyncio.TimeoutError
                    pn = await asyncio.wait_for(task_queue.get(), timeout=1)
                    tb.LOG.debug(f"Worker#{i} handling pn:{pn}")
                except asyncio.TimeoutError:
                    # 捕获asyncio.TimeoutError以退出协程
                    if is_running is False:
                        # 如果is_running为False，意味着不需要再轮询task_queue获取新任务
                        tb.LOG.debug(f"Worker#{i} quit")
                        # 消费者协程通过return退出
                        return
                else:
                    # 执行被分派的任务，即爬取pn页的帖子列表
                    threads = await client.get_threads(fname, pn)
                    # 这里的nonlocal同样是为了修改闭包外的变量thread_list
                    nonlocal thread_list
                    thread_list += threads

        # 创建8个消费者协程
        workers = [worker(i) for i in range(8)]
        # 使用asyncio.gather并发执行
        # 需要注意这里*workers中的*意为将列表展开成多个参数
        # 因为asyncio.gather只接受协程作为参数，不接受协程列表
        await asyncio.gather(*workers, producer())

    tb.LOG.info(f"Spider complete. Time cost: {time.perf_counter()-start_time:.4f} secs")

    # 按主题帖浏览量降序排序
    thread_list.sort(key=lambda thread: thread.view_num, reverse=True)
    # 将浏览量最高的10个主题帖的信息打印到日志
    for i, thread in enumerate(thread_list[0:10], 1):
        tb.LOG.info(f"Rank#{i} view_num:{thread.view_num} title:{thread.title}")


# 执行协程crawler
asyncio.run(crawler("图拉丁"))
```

运行效果如下图所示

```log
<2022-07-16 20:57:29.227> [INFO] [crawler] Spider start
<2022-07-16 20:57:29.230> [DEBUG] [worker] Worker#0 handling pn:32
<2022-07-16 20:57:29.231> [DEBUG] [worker] Worker#1 handling pn:31
<2022-07-16 20:57:29.232> [DEBUG] [worker] Worker#2 handling pn:30
<2022-07-16 20:57:29.233> [DEBUG] [worker] Worker#3 handling pn:29
<2022-07-16 20:57:29.234> [DEBUG] [worker] Worker#4 handling pn:28
<2022-07-16 20:57:29.235> [DEBUG] [worker] Worker#5 handling pn:27
<2022-07-16 20:57:29.236> [DEBUG] [worker] Worker#6 handling pn:26
<2022-07-16 20:57:29.237> [DEBUG] [worker] Worker#7 handling pn:25
<2022-07-16 20:57:29.878> [DEBUG] [worker] Worker#4 handling pn:24
<2022-07-16 20:57:29.930> [DEBUG] [worker] Worker#3 handling pn:23
<2022-07-16 20:57:29.954> [DEBUG] [worker] Worker#2 handling pn:22
<2022-07-16 20:57:29.969> [DEBUG] [worker] Worker#7 handling pn:21
<2022-07-16 20:57:29.992> [DEBUG] [worker] Worker#1 handling pn:20
<2022-07-16 20:57:30.131> [DEBUG] [worker] Worker#6 handling pn:19
<2022-07-16 20:57:30.140> [DEBUG] [worker] Worker#5 handling pn:18
<2022-07-16 20:57:30.219> [DEBUG] [worker] Worker#0 handling pn:17
<2022-07-16 20:57:30.469> [DEBUG] [worker] Worker#3 handling pn:16
<2022-07-16 20:57:30.505> [DEBUG] [worker] Worker#1 handling pn:15
<2022-07-16 20:57:30.525> [DEBUG] [worker] Worker#4 handling pn:14
<2022-07-16 20:57:30.539> [DEBUG] [worker] Worker#2 handling pn:13
<2022-07-16 20:57:30.660> [DEBUG] [worker] Worker#6 handling pn:12
<2022-07-16 20:57:30.692> [DEBUG] [worker] Worker#0 handling pn:11
<2022-07-16 20:57:30.883> [DEBUG] [worker] Worker#5 handling pn:10
<2022-07-16 20:57:31.001> [DEBUG] [worker] Worker#1 handling pn:9
<2022-07-16 20:57:31.020> [DEBUG] [worker] Worker#3 handling pn:8
<2022-07-16 20:57:31.054> [DEBUG] [worker] Worker#4 handling pn:7
<2022-07-16 20:57:31.071> [DEBUG] [worker] Worker#7 handling pn:6
<2022-07-16 20:57:31.084> [DEBUG] [worker] Worker#2 handling pn:5
<2022-07-16 20:57:31.154> [DEBUG] [worker] Worker#0 handling pn:4
<2022-07-16 20:57:31.235> [DEBUG] [worker] Worker#6 handling pn:3
<2022-07-16 20:57:31.583> [DEBUG] [worker] Worker#5 handling pn:2
<2022-07-16 20:57:31.617> [DEBUG] [worker] Worker#4 handling pn:1
<2022-07-16 20:57:32.630> [DEBUG] [worker] Worker#2 quit
<2022-07-16 20:57:32.677> [DEBUG] [worker] Worker#7 quit
<2022-07-16 20:57:32.769> [DEBUG] [worker] Worker#0 quit
<2022-07-16 20:57:32.769> [DEBUG] [worker] Worker#1 quit
<2022-07-16 20:57:32.912> [DEBUG] [worker] Worker#3 quit
<2022-07-16 20:57:33.003> [DEBUG] [worker] Worker#6 quit
<2022-07-16 20:57:33.147> [DEBUG] [worker] Worker#5 quit
<2022-07-16 20:57:33.267> [DEBUG] [worker] Worker#4 quit
<2022-07-16 20:57:33.270> [INFO] [crawler] Spider complete. Time cost: 4.0417 secs
<2022-07-16 20:57:33.271> [INFO] [crawler] Rank#1 view_num:2527890 title:我真的想踹网线师傅
<2022-07-16 20:57:33.272> [INFO] [crawler] Rank#2 view_num:1677425 title:【重要更新】百度图拉丁吧吧规 20140329
<2022-07-16 20:57:33.272> [INFO] [crawler] Rank#3 view_num:649518 title:大佬们，这是真的吗？
<2022-07-16 20:57:33.273> [INFO] [crawler] Rank#4 view_num:363866 title:【圾佬乐园】图吧垃圾回收站(2021年冬季)
<2022-07-16 20:57:33.274> [INFO] [crawler] Rank#5 view_num:309239 title:第一次捡漏成功，拿着卡我就跑了
<2022-07-16 20:57:33.274> [INFO] [crawler] Rank#6 view_num:127988 title:刚签收的包装都没拆放衣服里直接洗了**
<2022-07-16 20:57:33.275> [INFO] [crawler] Rank#7 view_num:108095 title:pdd大事件 兄弟们加把劲
<2022-07-16 20:57:33.275> [INFO] [crawler] Rank#8 view_num:107064 title:一个同学帮我配的 要不要请他吃饭
<2022-07-16 20:57:33.276> [INFO] [crawler] Rank#9 view_num:91084 title:防坑指南之RX580
<2022-07-16 20:57:33.276> [INFO] [crawler] Rank#10 view_num:84287 title:350买的1660到啦
```

## 结语

使用异步请求相当于用更高的调度成本换取更低的时间成本，以克服客户端在同步IO上的速度瓶颈

想进一步了解如何使用`aiotieba`优雅地实现一些实用功能，请阅读[实用工具合集](many_utils.md)
