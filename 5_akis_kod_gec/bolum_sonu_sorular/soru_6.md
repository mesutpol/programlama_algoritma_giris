#Veri tiplerinin sınırları değiştirilebilir mi?Tip sıfatlarını yazınız.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
İlkel veri tiplerinin sınırları değiştirilemez. Bunlar, bunları programlama dili tarafından kaydedilen sabit değerlerdir.

Ancak veri yapılarını ve öğelerini kullanarak daha büyük parçalar ve veri bütünlüklerini görebilirsiniz. Bu nedenle, örneğin bir intdeğişkenin 2 milyardan fazla tutamayacağı, longdeğişkeni kullanarak bu kadar genişleyebilir.

Bu şekilde değiştirilemez olsa da, programlama yoluyla bunları aşabileceğiniz çok daha büyük ve karmaşık verilere sahip yapılara sahip olabilirsiniz.
  

int int_variable = 2000000000; // This will give an error because the value is out of range for an int variable
long long_variable = 2000000000L; // This will work correctly


Bu örnekte, intdeğişkenin değeri, intdeğişken tarafından temsil edilebilecek en büyük sayıdan daha büyük olduğu için hata verir. Bununla birlikte longdeğişkenlik gösterebilir.
