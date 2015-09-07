# -*- encoding:utf-8 -*-
import lxml.etree as etree

content = '   <table width="100%" border="1" cellspacing="0" cellpadding="0">     <thead>         <tr>             <th>                 商品id             </th>             <th>                 商品名称             </th>             <th>                 商品分类             </th>             <th>                 商品状态             </th>             <th>                 颜色             </th>             <th>                 尺码             </th>             <th>                 仓库名称             </th>             <th>                 可销售库存             </th>             <th>                 参与促销             </th> 	        <th> 				操作 	        </th>         </tr>     </thead>   	 				<tr> 					<td> 						1 					</td> 					<td> 						1 					</td> 					<td> 						 							测试1 						 					</td> 					<td> 						 							已下架 						 					</td> 					<td> 						 							 								黑色 							 						 							 						 					</td> 					<td> 						 							 						 							 								165/88A 							 						 					</td> 					<td> 		 					</td> 					<td>  					</td> 					<td> 						 							 								 									<a href="http://promo.dangdang.com/2100591201" target="_blank">满额减621 ( 2013-01-11 00:00:00 - 2020-12-12 00:00:00)</a></br> 								 							 						 					</td> 					<td><a href="http://product.dangdang.com/product.aspx?product_id=1" target="_blank">单品页</a></td>				 			</tr> 	   </table> '
content = content.replace('\t', '').replace('<br>', '<br/>').replace('</br>', '<br/>')
doc = etree.fromstring(content)

# print content

heads_etree = doc.xpath('//table/thead/tr/th')

heads_list = list()
for head in heads_etree:
    heads_list.append(head.text.strip())
# print columns
# print columns[0]

rows_etree = doc.xpath('//table/tr')
result = list()
length = len(heads_list)

for row in rows_etree:
    row_dict = dict()
    for index in range(length):
        if row[index].text == '' or row[index].text is None:
            row_dict[heads_list[index]] = ''
        else:
            row_dict[heads_list[index]] = row[index].text.strip()
    result.append(row_dict)

print result