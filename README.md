Python Flask订餐系统
=====================

#### 介绍

- 此项目是一个微信小程序订餐系统，用户可以进行订餐一系列的操作，并且可以在后台的界面进行更多的操作。

#### 模块

- 后台管理

- 前台(小程序)

#### 启动

- `export ops_config=local|production && python manage.py runserver`

    - windows下运行参考下面的配置栏目

#### flask-sqlacodegen快速生成model

- 为了快速的生成数据库的model，使用如下的命令即可(第一条是全部生成，第二条是只生成指定table)

    - `flask-sqlacodegen 'mysql://root:123456@127.0.0.1/orders' --outfile "common/models/Model.py"  --flask`
    - `flask-sqlacodegen 'mysql://root:123456@127.0.0.1/orders' --tables user --outfile "common/models/User.py"  --flask`

#### 运行

- 此项目依赖于mysql5.7, python3.6

    - 服务器部署还需要uwsgi, nginx

        - 根目录下`uwsgi.ini`是uwsgi配置文件

    - [介绍](https://www.cnblogs.com/knarfeh/p/5616515.html)

- 下载此项目, 然后执行pip install -r requirements.txt进行依赖环境的安装

- 安装完成后, 打开`food_db.sql`将里面的sql语句在数据库中执行, 然后执行`python manager.py runserver`运行起来((用户:roux 密码:roux))

    - `python manager.py runjob`这条命令的具体解释还有参数可以在`jobs`目录的`launcher.py`里面查看

    - 配置文件(config目录)

        - `base_setting`: 基础配置

        - `local_setting`: 本地配置

            - 在windows下需要将本配置文件的代码全部拷贝到`base_setting`里面，并且注释掉`application.py`里面关于`local_setting`的配置信息

        - `production_setting`: 上线开配置(目前还无)

#### 目录分析

- common
    - libs：后台处理的通用方法
    - models：数据库模型

- config：配置文件

- docs：说明文档

- jobs：job相关处理

- mina：微信小程序

- tmp：临时文件

- web
    - controllers：后台控制
    - interceptors：权限拦截器
    - static：静态资源
    - templates：模板文件

- 根目录
    - application.py：对app和db进行封装
    - manager.py：入口文件
    - www\\.py：蓝图注册


#### ueditor编辑器

- 配置:(代码文件无需关心)
    ```
    <script src="{{ build_static_url('/plugins/ueditor/ueditor.config.js') }}"></script>
    <script src="{{ build_static_url('/plugins/ueditor/ueditor.all.min.js') }}"></script>
    <script src="{{ build_static_url('/plugins/ueditor/lang/zh-cn/zh-cn.js') }}"></script>

    UE.getEditor('editor',{
       toolbars: [
            [ 'undo', 'redo', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall',  '|','rowspacingtop', 'rowspacingbottom', 'lineheight'],
            [ 'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                'directionalityltr', 'directionalityrtl', 'indent', '|',
                'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                'link', 'unlink'],
            [ 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                'insertimage', 'insertvideo', '|',
                'horizontal', 'spechars','|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols' ]

        ],
        enableAutoSave:true,
        saveInterval:60000,
        elementPathEnabled:false,
        zIndex:4,
        serverUrl:common_ops.build_url(  '/upload/ueditor' )
    });
    ```
