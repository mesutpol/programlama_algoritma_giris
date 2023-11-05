//Kodu geliştiren Oğuzhan Demirbaş
//Geliştirilme tarihi 5.11.2023
//Geliştirilme amacı :6 Dilde aynı algoritmayı çalıştırarak arasıdnaki farkları görmek

#include <iostream>// kullanıcıdan veri girişi almak ve program sonuçlarını ekrana yazdırmak gibi giriş/çıkış işlemlerini kolaylaştırmak için kullanılır.

int main() {
    int Satır_yıldız, Sutun_yıldız;//int(tam sayı) veri tipi içinde 2 değişken tanımlıyoruz

    std::cout << "Satır sayısını girin: ";//"Kullanıcıdan satır sayısını alınır
    std::cin >> Satır_yıldız;//">>" operatörü kullanılarak kullanıcıdan giriş alınır ve Satır_yıldız değişkenine atanır

    std::cout << "Sütun sayısını girin: ";//"Kullanıcıdan sütun sayısını alınır
    std::cin >> Sutun_yıldız;

    for (int i = 0; i < Satır_yıldız; i++) {//i'yi "0"dan başlat değeri Satır_yıldız değeri i den küçük olana kadar değeri döndür 
        for (int j = 0; j < Sutun_yıldız; j++) {//j'yi "0"dan başlat değeri Sutun_yıldız değeri j den küçük olana kadar değeri döndür 

            std::cout << "*";//Ekrana "*" yazdır
        }
        std::cout << std::endl; // Her satırın sonunda yeni bir satıra geç
    }

    return 0;//return 0; ifadesi, programın herhangi bir hata olmadan çalıştığını ve sona erdiğini ifade eder.
}