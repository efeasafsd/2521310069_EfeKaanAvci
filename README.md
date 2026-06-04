# BVA5108 - Yapay Zeka Destekli Siber Güvenlik Aracı

## Proje Bilgileri

Ad Soyad: Efe Kaan Avcı
Öğrenci No: 2521310069
Tarih: 2026
Seçilen Modül: M6 Banner Grabbing

---

## Proje Amacı

Bu proje Kali Linux üzerinde çalışan, ağ güvenlik analizi yapan ve yapay zeka destekli raporlama üreten bir Python aracıdır.

Sistem:
- Port taraması yapar
- Servis ve versiyon bilgisi toplar
- Banner grabbing yapar
- AI ile risk analizi üretir
- HTML rapor oluşturur

---

## Sistem Akışı

Kullanıcı IP girer  
→ M1 Nmap taraması yapılır  
→ M6 Banner Grabbing çalışır  
→ AI API analiz yapar  
→ HTML rapor oluşturulur  

---

## M1 Port Tarama Modülü

Nmap ile hedef sistem taranır.

Özellikler:
- SYN scan
- Açık port tespiti
- Servis ve versiyon bilgisi
- XML çıktısının Python ile parse edilmesi

Örnek çıktı:

---

## M6 Banner Grabbing Modülü

Socket kullanılarak açık portlardan banner bilgisi çekilir.

Örnek çıktı:

---

## AI ENTEGRASYONU

Bu projede gerçek AI API kullanılmıştır.

Kullanılan API:
- Gemini / Groq / Cohere / Ollama / OpenAI

Görev:
- Açık portları analiz etmek
- Riskleri açıklamak
- Güvenlik önerileri sunmak

Örnek prompt:
Aşağıdaki ağ tarama sonuçlarını analiz et:
8000/tcp open http SimpleHTTP/0.6 Python/3.13.12

Örnek AI çıktısı:
RİSK ANALİZİ:
- HTTP servisi saldırı yüzeyi oluşturur
- Eski versiyonlar risklidir
- Gereksiz servisler kapatılmalıdır
- Firewall ile erişim sınırlandırılmalıdır

---

## HTML RAPOR (report.html)

HTML rapor aşağıdaki bilgileri içerir:

- M1 port tarama sonuçları
- M6 banner bilgileri
- AI analiz sonucu

HTML içerik:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Güvenlik Raporu</title>
</head>
<body>

<h1>AI Destekli Siber Güvenlik Raporu</h1>

<h2>M1 Port Tarama</h2>
<pre>
8000/tcp open http SimpleHTTP/0.6 Python/3.13.12
</pre>

<h2>M6 Banner Grabbing</h2>
<pre>
8000 -> HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.13.12
</pre>

<h2>AI Risk Analizi</h2>
<pre>
RİSK ANALİZİ:
- HTTP servisi saldırı yüzeyi oluşturur
- Eski versiyonlar risklidir
- Gereksiz servisler kapatılmalıdır
</pre>

</body>
</html>
