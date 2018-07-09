# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!
def decompress(text):
  i=0
  start=0
  end=0

  while i!=len(text):
    if text[i]=="]":
      end=i;

      start=end
      while start!=0:
        if text[start]=="[":
          break
        else:
          start = start -1
      if start==0:
        return "No Counter!!!"

      if text[start-1].isnumeric():
        count = int(text[start-1])
      else:
        return "Invalid counter!!"

      text = text.replace(text[start-1:end+1],text[start+1:end]*count)

      i=start-1;
    else:
      i=i+1

  return text

ex1= "1[1[1[1[1[1[2[1[1[1[2[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
ex2= "0[abc]"
ex3="a[]b"

print(decompress(ex1))
print(decompress(ex2))
print(decompress(ex3))
