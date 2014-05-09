title: Node.js基础
date: 2014-04-09 20:16:57
category: Node.js
tag: node
---
#第一章 简介

##1.1Node.js 是什么 

###CommonJS 规范

一个单独的文件就是一个模块。加载模块使用require方法，该方法读取一个文件并执行，最后返回文件内部的exports对象。

```
console.log("evaluating example.js");

var invisible = function () {
  console.log("invisible");
}

exports.message = "hi";

exports.say = function () {
  console.log(message);
}
```

使用require方法，加载example.js。

```
var example = require('./example.js');
```

这时，变量example就对应模块中的exports对象，于是就可以通过这个变量，使用模块提供的各个方法。

```
{
  message: "hi",
  say: [Function]
}
```

require方法默认读取js文件，所以可以省略js后缀名。

```
var example = require('./example');
```

js文件名前面需要加上路径，可以是相对路径（相对于使用require方法的文件），也可以是绝对路径。如果省略路径，node.js会认为，你要加载一个核心模块，或者已经安装在本地 node_modules 目录中的模块。如果加载的是一个目录，node.js会首先寻找该目录中的 package.json 文件，加载该文件 main 属性提到的模块，否则就寻找该目录下的 index.js 文件。

下面的例子是使用一行语句，定义一个最简单的模块。

```
// addition.js
exports.do = function(a, b){ return a + b };
```

上面的语句定义了一个加法模块，做法就是在exports对象上定义一个do方法，那就是供外部调用的方法。使用的时候，只要用require函数调用即可。

```
var add = require('./addition');

add.do(1,2)
// 3
```

再看一个复杂一点的例子。

```
// foobar.js

function foobar(){
        this.foo = function(){
                console.log('Hello foo');
        }

        this.bar = function(){
                console.log('Hello bar');
        }
}
exports.foobar = foobar;
```

调用该模块的方法如下：

```
var foobar = require('./foobar').foobar,
    test   = new foobar();
 
test.bar(); // 'Hello bar'
```

有时，不需要exports返回一个对象，只需要它返回一个函数。这时，就要写成module.exports。

```
module.exports = function () {
  console.log("hello world")
}
```

##1.2Node能做什么？

* 具有复杂逻辑的网站； 
* 基于社交网络的大规模 Web 应用； 
* Web Socket 服务器； 
* TCP/UDP 套接字应用程序； * 
* 命令行工具； 
* 交互式终端程序； 
* 带有图形用户界面的本地应用程序； 
* 单元测试工具； 
* 客户端 JavaScript 编译器。

##1.3异步式 I/O 与事件驱动

* 异步式 I/O: 跳过I/O直接运行下一步，不再等待I/O处理结果
* 事件驱动:事件队列，程序执行的时候进入事件循环来执行下一个事件

##1.4Node.js性能

比PHP性能要高很多

##1.5JavaScript简史


#第二章 安装和配置Node.js


#第三章 快速入门

* node helloworld.js:执行js脚本

* node 的 REPL 模式（同Python的Shell交互模式）

##3.1创建Http服务器

```
//app.js 

var http = require('http'); 

 
http.createServer(function(req, res) { 

 res.writeHead(200, {'Content-Type': 'text/html'}); 

 res.write('<h1>Node.js</h1>'); 

 res.end('<p>Hello World</p>'); 

}).listen(3000); 

console.log("HTTP server is listening at port 3000.");
```

##3.2使用supervisor

* 安装

    $ npm install -g supervisor 

* 使用

    $ supervisor app.js 

* 作用：开发时修改代码后会自动终止脚本，然后重新启动，方便调试。

##3.3异步式 I/O 与事件式编程

* 异步I/O
 * 优点：单线程减少开销
 * 缺点：编程思维独特，难以适应
* 回调函数：不鼓励用同步I/O
* 事件循环机制：Node.js 程序由事件循环开始，到事件循环结束，所有的逻辑都是事件的回调函数，所以 Node.js 始终在事件循环中，程序入口就是事件循环第一个事件的回调函数。事件的回调函数在执行的过程中，可能会发出 I/O 请求或直接发射（emit）事件，执行完毕后再返回事件循环，事件循环会检查事件队列中有没有未处理的事件，直到程序结束。

##3.4模块和包

* 两者没有本质区别
* 文件和模块一一对应，一个Node.js文件就是一个模块

###加载：

* require 用于从外部获取一个模块的接口，即所获取模块的 exports 对象。 
* exports 是模块公开的接口

例子：

```
//module.js 

var name; 

exports.setName = function(thyName) { 
 name = thyName; 
}; 

exports.sayHello = function() { 
 console.log('Hello ' + name); 
}; 
```

在同一目录下创建 getmodule.js，内容是： 

```
//getmodule.js 
var myModule = require('./module'); 
myModule.setName('BYVoid'); 
myModule.sayHello(); 

```

运行node getmodule.js，结果是： 

```
Hello BYVoid
```

###单次加载

这点和对象不一样，无论调用多少次 require，获得的模块都是同一个

```
//loadmodule.js 
var hello1 = require('./module'); 
hello1.setName('BYVoid'); 
var hello2 = require('./module'); 
hello2.setName('BYVoid 2'); 
hello1.sayHello();
```
输出结果：

    Hello BYVoid 2

结果被后者覆盖了。

###覆盖exports

```
//singleobject.js 
function Hello() { 
 var name; 
 this.setName = function (thyName) { 
 name = thyName; 
 }; 
this.sayHello = function () { 
 console.log('Hello ' + name); 
 }; 
}; 
exports.Hello = Hello; 

//简化后：module.exports = Hello; 
```

简化前：

    require('./singleobject').Hello

简化后可以直接获取对象：

```
//gethello.js 
var Hello = require('./hello'); 
hello = new Hello(); 
hello.setName('BYVoid'); 
hello.sayHello(); 
```
__exports__本是就是一个空对象，本质上是通过闭包来建立一个有限的的访问接口。（很简单却想了很久～）

##创建包

commonJS规范如下：

* package.json 必须在包的顶层目录下； 
* 二进制文件应该在 bin 目录下； 
* JavaScript 代码应该在 lib 目录下； 
* 文档应该在 doc 目录下； 
* 单元测试应该在 test 目录下。

###package.jason

Node.js 在调用某个包时，会首先检查包中 package.json 文件的 main 字段，将其作为包的接口模块，如果 package.json 或 
main 字段不存在，会尝试寻找 index.js 或 index.node 作为包的接口。

* name：包的名称，必须是唯一的，由小写英文字母、数字和下划线组成，不能包含空格。 
* description：包的简要说明。 
* version：符合语义化版本识别①规范的版本字符串。 
* keywords：关键字数组，通常用于搜索。 
* maintainers：维护者数组，每个元素要包含 name、email （可选）、web （可选）字段。 
* contributors：贡献者数组，格式与maintainers相同。包的作者应该是贡献者数组的第一个元素。 
* bugs：提交bug的地址，可以是网址或者电子邮件地址。 
* licenses：许可证数组，每个元素要包含 type （许可证的名称）和 url （链接到许可证文本的地址）字段。 
* repositories：仓库托管地址数组，每个元素要包含 type （仓库的类型，如 git ）、url （仓库的地址）和 path （相对于
仓库的路径，可选）字段。 
*  dependencies：包的依赖，一个关联数组，由包名称和版本号组成。

例子：
```
{ 
 "name": "mypackage", 
 "description": "Sample package for CommonJS. This package demonstrates the required 
elements of a CommonJS package.", 
 "version": "0.7.0", 
 "keywords": [ 
 "package", 
 "example" 
 ], 
 "maintainers": [ 
 { 
 "name": "Bill Smith", 
 "email": "bills@example.com", 
 } 
 ], 
 "contributors": [ 
 { 
 "name": "BYVoid", 
 "web": "http://www.byvoid.com/" 
 } 
 ], 
 "bugs": { 
 "mail": "dev@example.com", 
 "web": "http://www.example.com/bugs" 
 }, 
 "licenses": [ 
 { 
 "type": "GPLv2", 
 "url": "http://www.example.org/licenses/gpl.html" 
 } 
 ], 
 "repositories": [ 
 { 
 "type": "git", 
 "url": "http://github.com/BYVoid/mypackage.git" 
 } 
 ], 
 "dependencies": { 
 "webkit": "1.2", 
 "ssl": { 
 "gnutls": ["1.0", "2.0"], 
 "openssl": "0.9.8" 
 } 
 } 
} 
```

###包管理

npm：

    npm [install/i] [package_name]

* 本地模式：默认方法，存放当前目录下
* 全局模式：减少重复副本

    npm [install/i] -g [package_name] 
* 创建全局链接：把全局包当成本地包来用

    $ npm link express 
    ./node_modules/express -> /usr/local/lib/node_modules/express 

###使用 node-inspector 调试 Node.js 

    npm install -g node-inspector //安装insepctor
    node --debug-brk=5858 debug.js //链接服务器
    $ node-inspector//启动
     http://127.0.0.1:8080/debug?port=5858 //浏览器中打开！


