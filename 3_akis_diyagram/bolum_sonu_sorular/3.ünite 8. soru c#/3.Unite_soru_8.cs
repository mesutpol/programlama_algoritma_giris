namespace MyApplication;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("sayi giriniz : ");            //kullanıcından sayı istenir
        int Sayi = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("yuzde giriniz : ");           //kullanıcıdan yüzde istenir
        int v = Convert.ToInt32(Console.ReadLine());
        int Yuzde = v;
        int Sonuc = Sayi * Yuzde / 100;               //girilen sayının yüzdesi hesaplanır
        Console.WriteLine("Sonuc : " + Sonuc);        //Sonuç ekrana yazdırılır 

    }
}