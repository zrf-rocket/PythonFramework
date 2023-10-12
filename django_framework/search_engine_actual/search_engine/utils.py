import jieba

# 创建分词函数
def segmant_text(text):
    seg_list = jieba.cut(text)
    return " ".join(seg_list)

