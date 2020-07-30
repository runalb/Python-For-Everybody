# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

fzero = text.find("0")
text_len=len(text)

num = text[fzero:text_len]
f_num=float(num)
print(f_num)
