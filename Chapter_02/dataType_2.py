d1=np.datetime64('2024-02-14')
d2=np.datetime64('1999-12-02')
diff=d1-d2
print(diff)
print(type(diff))
print(diff.dtype)

"""print(type(diff)) ifadesinin çıktısı, diff değişkeninin türünü gösterir. Bu durumda, diff değişkeni bir numpy.timedelta64 nesnesidir. numpy.timedelta64, iki tarih veya zaman damgası arasındaki farkı temsil etmek için kullanılan özel bir veri tipidir.

print(diff.dtype) ifadesinin çıktısı ise diff değişkeninin veri tipini gösterir. Bu durumda, diff değişkeninin veri tipi timedelta64[D] şeklindedir. [D] ifadesi, farkın gün cinsinden temsil edildiğini gösterir. timedelta64 veri tipi, zaman farklarını toplama, çıkarma ve karşılaştırma gibi çeşitli işlemleri gerçekleştirmenizi sağlar."""

dt=np.datetime64('2023-07-06 12:30:00')
print(type(dt))

mix_ar=np.array([1,3,4,False,[1,2,3],'jafri'],dtype=object)
print(mix_ar)
print(type(mix_ar))
print(mix_ar.dtype)
