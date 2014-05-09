date: 2014-04-06 15:17:04
tag: css
---

#简介

##CSS概述

* CSS 指层叠样式表 (Cascading Style Sheets)​
* 解决内容与表现分离的问题
* 多个样式定义可层叠为一

##层叠次序
一般而言，所有的样式会根据下面的规则层叠于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。
1. 浏览器缺省设置
2. 外部样式表
3. 内部样式表（位于 <head> 标签内部）
4. 内联样式（在 HTML 元素内部）

#CSS基础语法

##CSS语法
CSS 规则由两个主要的部分构成：__选择器__，以及一条或多条__声明__。

    selector {declaration1; declaration2; ... declarationN }​



* __选择器__通常是您需要改变样式的 HTML 元素。

* 每条__声明__由一个属性和一个值组成。

* __属性__（property）是您希望设置的样式属性（style attribute）。每个属性有一个值。属性和值被冒号分开。
​CSS 语法

##值的不同写法和单位​

除了英文单词 red，我们还可以使用十六进制的颜色值 #ff0000：

    p { color: #ff0000; }

为了节约字节，我们可以使用 CSS 的缩写形式：

    p { color: #f00; }
我们还可以通过两种方法使用 RGB 值：

    p { color: rgb(255,0,0); }
    p { color: rgb(100%,0%,0%); }
​
请注意，当使用 RGB 百分比时，即使当值为 0 时也要写百分比符号。但是在其他的情况下就不需要这么做了。比如说，当尺寸为 0 像素时，0 之后不需要使用 px 单位，因为 0 就是 0，无论单位是什么。

####引号​

如果值为若干单词，则要给值加引号：

    ​p {font-family: "sans serif";}​
​

##多重声明
应当在每个生命后边加上__;__，同时每行只写一个声明增加可读性

```
p {
  text-align: center;
  color: black;
  font-family: arial;
}
```

##空格和大小写

* 增加空格以便美观
* css不会区分大小写，但是与HTML有关的id class需要大小写

#CSS高级语法

##选择器的分组

* 被分组的选择器就可以分享相同的声明。
* 用逗号将需要分组的选择器分开​。

```
h1,h2,h3,h4,h5,h6 {
  color: green;
  }
​
```

##继承及其问题

* 子元素从父元素继承属性。
* 子元素将继承最高级元素（在本例中是 body）所拥有的属性
* 有些浏览器不支持继承：IE6，Netscape4
* 如果不希望子类继承，则可以创建一个针对 p 的特殊规则，这样它就会摆脱父元素的规则

```
body {
     font-family: Verdana, sans-serif;
     }​
```
#CSS派生选择器

__派生选择器__：通过依据元素在其位置的上下文关系来定义样式，你可以使标记更加简洁。
就是有两个选择器～

```
li strong {
    font-style: italic;
    font-weight: normal;
  }​
```
​
#id选择器

##id选择器

* id 选择器可以为标有特定 id 的 HTML 元素指定特定的样式。
* id 选择器以 "#" 来定义。
* id 属性只能在每个 HTML 文档中出现一次

```
#red {color:red;}
#green {color:green;}​
```
##id 选择器和派生选择器

__在现代布局中，id 选择器常常用于建立派生选择器。​__

```
#sidebar p {
 font-style: italic;
 text-align: right;
 margin-top: 0.5em;
 }​
```
##一个选择器，多种用法

同派生器一样，可以对应id下多个选择

```
#sidebar p {
 font-style: italic;
 text-align: right;
 margin-top: 0.5em;
 }

#sidebar h2 {
 font-size: 1em;
 font-weight: normal;
 font-style: italic;
 margin: 0;
 line-height: 1.5;
 text-align: right;
 }
​
```

#CSS类选择器

##Class选择器

    .center {text-align: center}

​类名的第一个字符不能使用数字！它无法在 Mozilla 或 Firefox 中起作用。

​__和 id 一样，class 也可被用作派生选择器：​__

```
.fancy td {
 color: #f60;
 background: #666;
 }​
```
__元素也可以基于它们的类而被选择：​__

```
td.fancy {
 color: #f60;
 background: #666;
 }

​<td class="fancy">
```

#CSS属性选择器

可以为拥有指定属性的 HTML 元素设置样式，而不仅限于 class 和 id 属性。

##属性选择器

下面的例子为带有 title 属性的所有元素设置样式：

```
[title]
{
color:red;
}
​```

##属性和值选择器

下面的例子为 title="W3School" 的所有元素设置样式：

```
[title=W3School]
{
border:5px solid blue;
}
​```

##属性和值选择器 - 多个值

下面的例子为包含指定值的 title 属性的所有元素设置样式。适用于由空格分隔的属性值：

```
[title~=hello] { color:red; } //所有包含helo的title属性里 都有效
```

##参考手册


|选择器|                     描述|
|:--------------|:---------------------|
|[attribute] |用于选取带有指定属性的元素。|
|[attribute=value]| 用于选取带有指定属性和值的元素。|
|[attribute~=value]| 用于选取属性值中包含指定词汇的元素。|
|[attribute =value] |用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。|
|[attribute^=value] |匹配属性值以指定值开头的每个元素。|
|[attribute$=value] |匹配属性值以指定值结尾的每个元素。|
|[attribute*=value] |匹配属性值中包含指定值的每个元素。|
​
第4项中有个|，不知道怎么转义
#如何创建CSS

##如何插入样式表

当读到一个样式表时，浏览器会根据它来格式化 HTML 文档。插入样式表的方法有三种：​

###外部样式表

当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 <link> 标签链接到样式表。<link> 标签在（文档的）头部：

```
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css" />
</head>
```

浏览器会从文件 mystyle.css 中读到样式声明，并根据它来格式文档。​

```
hr {color: sienna;}
p {margin-left: 20px;}
body {background-image: url("images/back40.gif");}
```

.css扩展名，20px中间不能留空格！

###内部样式表

当单个文档需要特殊的样式时，就应该使用内部样式表。你可以使用 ```<style> ```标签在文档头部定义内部样式表，就像这样:

```
<head>
<style type="text/css">
hr {color: sienna;}
p {margin-left: 20px;}
body {background-image: url("images/back40.gif");}
</style>
</head>
​```

###内联样式

由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。请慎用这种方法，例如当样式仅需要在一个元素上应用一次时。

要使用内联样式，你需要在相关的标签内使用样式（style）属性。Style 属性可以包含任何 CSS 属性。本例展示如何改变段落的颜色和左外边距：

```
<p style="color: sienna; margin-left: 20px">
This is a paragraph
</p>
​```

##多重样式

如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来。

例如，外部样式表拥有针对 h3 选择器的三个属性：

```
h3 {
  color: red;
  text-align: left;
  font-size: 8pt;
  }
```

而内部样式表拥有针对 h3 选择器的两个属性：

```
h3 {
  text-align: right; 
  font-size: 20pt;
  }
```

假如拥有内部样式表的这个页面同时与外部样式表链接，那么 h3 得到的样式是：

```
color: red; 
text-align: right; 
font-size: 20pt;
​```
即颜色属性将被继承于外部样式表，而文字排列（text-alignment）和字体尺寸（font-size）会被内部样式表中的规则取代。

__和继承非常相似！！__​

