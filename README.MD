# 说明
此目录下的python脚本是一些为解决“小需求”而创作的SublimeText插件，使用时将其放到SublimeText3/Data/Packages/User/目录下，然后在此目录下的Default.sublime-commands文件中写入菜单项，即可通过CommandPalette调用。

# 脚本的功能
## replace_duplines_to_dash.py
将除第一行之外的相邻的重复行替换为短线。如

	1
	1
	2
	2
	2

将被替换为

	1
	-
	2
	-
	-

## convert_timestamp_to_datetime.py
将选中的时间戳替换为yyyy-mm-dd H:M:I格式，支持10位、13位、10位+小数点+小数位的时间戳

## convert_datetime.py
将选中的-或/的日期、时间转换为时间戳。

## convert_timestamp.py
翻译关键词得到时间、时间戳

	now →	2018-06-12 12:34:18
	tsnow →	1528778060
	timestamp →	1528778063.12

将以下格式的数字翻译为形如2018-06-12 12:34:18的时间：

- 10位整数时间戳
- 13位整数时间戳
- 10位整数附加小数位的时间戳
- 20141220235959这样的时间字符串

## count_dublicates.py
统计重复行的行数

例如，统计

	a
	b
	c
	b
	c
	c

的结果为：

	a 1
	b 2
	c 3

## close_all_saved_file.py
关闭所有已经保存的文件。

## convert_fields_to_table.py
将特定字符分割的区域转换为html的table，分隔符可以在命令中指定。

例如：

	|标题1|标题2|标题3|
	|数据1|数据2|数据3|

将被转换为：

	<table>
		<tbody>
			<tr>
				<td>标题1</td>
				<td>标题2</td>
				<td>标题3</td>
			</tr>
			<tr>
				<td>数据1</td>
				<td>数据2</td>
				<td>数据3</td>
			</tr>
		</tbody>
	</table>

## html_table_to_text.py.py
convert_fields_to_table的逆操作，将table的html源码转换为竖线分割的文本表格，之后可以配合sublime的table editor整理对齐、编辑。

	<table>
		<tbody>
			<tr>
				<td>标题1</td>
				<td>标题2</td>
				<td>标题3</td>
			</tr>
			<tr>
				<td>数据1</td>
				<td>数据2</td>
				<td>数据3</td>
			</tr>
		</tbody>
	</table>

运行命令可以得到：

	| 标题1| 标题2| 标题3|
	| 数据1| 数据2| 数据3|

## remove_html_attrs.py
删除HTML源码中的标签属性。

## paste_lines_as_one.py
将在多个编辑点选中的内容粘贴为一行，当初是为了整理维基百科上一些表格内容写的。例如：

	第一行很长**很长的**内容
	第二行较长**较长的**内容
	第三行有点**长有点**长的内容

三个编辑点的星号之间的内容被选中后，运行命令可以得到：

	很长的/较长的/长有点/

## show_file_status.py
![image](https://raw.githubusercontent.com/qijianjun/sublime-text-small-plugins/master/images/sublime-text-file-status.png)
显示文件当前的状态，SAVED / UNSAVED / NONE / DEL 分别代表已保存、文件存在但未保存更改、文件不再盘上、文件之前在盘上但已被删除。详情参考：[在SublimeText编辑器中显示文件状态](https://vps123.top/show-file-status-in-sublime-text.html)。

## calculate_nums.py
![image](https://raw.githubusercontent.com/qijianjun/sublime-text-small-plugins/master/images/calnums.png)
状态栏显示全部选中区域的数字的数量、和、均值、最大值、最小值，取消选中区域后状态栏清除显示。

## sum_dublicates.py
计算全部行的出现次数，按从大到小排列。

## single_selection_keep_last_cursor.py
仅保留最后一个选区。
