# CampusHub AI — Nihai Model Kararı (T11)

## 1. Amaç

CampusHub uygulamasındaki etkinlik açıklamalarını otomatik olarak altı kategoriden birine sınıflandırmak.

Bu görev için önceden eğitilmiş, Türkçe metinleri destekleyen bir zero-shot classification modeli kullanılacaktır. Proje kapsamında model yeniden eğitilmeyecektir.

## 2. Seçilen Model

- **Model ID:** `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`
- **Hugging Face Revision (Commit SHA):** `8adb042d524ecd5c26d3e3ba0e3fbcf7e2d0864c`
- **Yöntem:** Zero-shot text classification
- **Çalışma ortamı:** CPU
- **Dil:** Türkçe
- **Çıktı:** Tek kategori ve güven skoru

Modelin farklı tarihlerde değişen sürümlerinden etkilenmemek için entegrasyonda model adıyla birlikte yukarıdaki revision kullanılacaktır.

## 3. Sabit Kategoriler ve Açıklamaları

Son değerlendirmelerde kullanılan V5 kategori açıklamaları seçilmiştir.

| Kategori | Modelde Kullanılacak Açıklama |
|---|---|
| TECHNOLOGY | teknoloji ve yazılım |
| SPORT | spor |
| ART | sanat, müzik ve kültür |
| CAREER | kariyer ve iş hayatı |
| SOCIAL | sosyal buluşma ve gönüllülük |
| OTHER | sağlık, güvenlik ve genel bilgilendirme |

Kategori açıklamalarının kaynak dosyası:

`data/evaluation/CampusHub_Kategori_Aciklamalari_v5.json`

Modelde kullanılacak hypothesis template:

`Bu etkinlik {} ile ilgilidir.`

## 4. Sınıflandırma Kuralları

1. Her etkinlik yalnızca **bir kategoriye** atanacaktır.
2. `multi_label=False` kullanılacaktır.
3. Modelin en yüksek skoru verdiği kategori seçilecektir.
4. `OTHER`, diğer kategoriler gibi normal bir aday kategoridir.
5. Şimdilik ayrıca bir confidence threshold kullanılmayacaktır.
6. Modelin döndürdüğü skor, kalibre edilmiş bir doğruluk olasılığı olarak yorumlanmayacaktır.

## 5. Model Karşılaştırma Sonuçları

Aynı 42 geliştirme örneği üzerinde yapılan değerlendirmeler:

| Model | Doğru / Toplam | Accuracy |
|---|---|---|
| MiniLM | 22/42 | %52,38 |
| mDeBERTa V5 | 33/42 | %78,57 |
| mDeBERTa 2mil7 V5 | 31/42 | %73,81 |

CPU benchmark sonuçları:

| Metrik | MiniLM | mDeBERTa V5 | mDeBERTa 2mil7 V5 |
|---|---:|---:|---:|
| Model yükleme (sn) | 1,597 | 1,554 | 2,093 |
| Ortalama inference (ms) | 26,36 | 621,51 | 607,38 |
| P95 inference (ms) | 27,91 | 723,40 | 710,52 |
| Ölçülen peak RAM (MB) | 817,12 | 750,42 | 871,88 |

Bu değerler yerel benchmark koşullarına aittir; farklı cihazlarda aynı performans garanti edilmez.

## 6. Ek Geliştirme Testleri

Seçilen mDeBERTa V5 modeliyle yapılan ek testler:

- İlk 42 geliştirme örneği: 33/42 — %78,57
- Yeni 18 etkinlik: 13/18 — %72,22
- Yeni 24 etkinlik: 18/24 — %75,00
- Tüm bu geliştirme testleri birlikte: 64/84 — %76,19

Bu 18 ve 24 yeni etkinlik, ayrı tutulan **18 final holdout etkinliğiyle aynı değildir.**

Yeni 24 etkinlikte özellikle `OTHER` sınıfında hatalar gözlenmiştir. Bu, modelin bilinen bir sınırlılığıdır.

## 7. Nihai Modelin Seçilme Nedeni

mDeBERTa V5 modeli, karşılaştırılan modeller arasında 42 örneklik geliştirme setinde en yüksek doğruluğu göstermiştir.

MiniLM daha hızlı olmasına rağmen sınıflandırma doğruluğu belirgin şekilde daha düşüktür.

Bu nedenle doğruluk ve CPU üzerinde çalışabilirlik birlikte değerlendirilerek `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` seçilmiştir.

## 8. Final Holdout Testi — T29

Final test için başlangıçtan beri ayrı tutulan **18 etkinlik** kullanılacaktır.

Final test yapılmadan önce şu kararlar sabitlenmiştir:

- Model ID ve revision
- Altı kategori
- V5 kategori açıklamaları
- Hypothesis template
- `multi_label=False`
- En yüksek skorlu kategoriyi seçme kuralı
- Ek confidence threshold kullanılmaması

**Önceden belirlenen kabul ölçütü:** 18 final etkinliğin en az 13'ünün doğru sınıflandırılması (**13/18 = %72,22**).

Final değerlendirme tek bir sabit model yapılandırmasıyla yapılacaktır. Sonuçlar görüldükten sonra holdout setine göre model veya kategori açıklamaları ayarlanmayacaktır.

Kabul ölçütü sağlanmazsa sonuç başarısız olarak raporlanacak; sonraki iyileştirmeler için ayrı bir değerlendirme süreci oluşturulacaktır.

**Final holdout durumu:** Henüz çalıştırılmadı.

## 9. Sonraki Adımlar

- **T29:** 18 final holdout etkinliğini değerlendirmek ve sonucu raporlamak.
- **T12:** Seçilen modeli `app/models/classifier.py` içerisine entegre etmek.
- Model entegrasyonundan sonra mevcut API kontratı ve testlerle uyumluluğu doğrulamak.

**Karar:** T11 kapsamında mDeBERTa V5 modeli ve yukarıdaki sınıflandırma ayarları sabitlenmiştir.