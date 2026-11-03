---
id: TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul
title: "Sinkron Lintas Modul: Rename Category, Brand, UoM, Label dan Blok Delete Master Data yang Dipakai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-589
  - TC-FA-FAAM-590
  - TC-FA-FAAM-591
  - TC-FA-FAAM-592
  - TC-FA-FAAM-594
  - TC-FA-FAAM-595
  - TC-FA-FAAM-596
coverage:
  web: automated
---

# Sinkron Lintas Modul: Rename Category, Brand, UoM, Label dan Blok Delete Master Data yang Dipakai

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) dengan akses ke modul sumber (Settings > Categories, Global Settings > Brand, Global Settings > Measurement, tab Labels). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (dibaca saja, tidak diubah): No. 10 (`Dell Latitude`, Category `IT Equipment`, Brand `Dell`, UoM `Unit`, Default Label `Finance`; hanya menjadi target Delete master data yang selalu diblokir guard, Last Updated tidak berubah).
- Data Dinamis, di-seed lewat API di hook `before` sebagai salinan fixture bersuffix `{runId}-220` (Tabel Data Uji Dinamis tidak memuat salinan untuk TC ini; lihat Temuan untuk QA):
  - `Rename Item 589 {runId}-220` (Code `RNI589`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0) ber-Category leaf `Rename Category 589 {runId}-220` (fixture No. 31).
  - `Rename Item 590 {runId}-220` (Code `RNI590`, Category `IT Equipment`, TAG `QR`, UoM `Unit`, Total Asset 0) ber-Brand `Rename Brand 590 {runId}-220` tanpa model ketikan (model `No Model`) (fixture No. 31b).
  - `Rename Item 591 {runId}-220` (Code `RNI591`, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, Total Asset 0) ber-UoM `Rename UoM 591 {runId}-220` (fixture No. 31c).
  - `Rename Label Item 592 {runId}-220` (Code `RLI592`, Category `IT Equipment`, TAG `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0) dengan Default Label `Rename Label 592 {runId}-220` (fixture No. 25c).
  - Hasil rename: `Rename Category 589 {runId}-220 Baru`, `Rename Brand 590 {runId}-220 Baru`, `Rename UoM 591 {runId}-220 Baru`, `Renamed Label 592 {runId}-220`.
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; mencatat entri Changelog sebelum aksi (TC-FA-FAAM-589).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini, termasuk Category, Brand, UoM, dan label bersuffix `{runId}-220`, lewat API.
- State global yang diubah: tidak ada selain master data bersuffix milik spec ini. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-589 sampai 596: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-220`, tekan Enter

### TC-FA-FAAM-589: Rename Category di Settings > Categories langsung terlihat di List dan Detail

2. Klik icon Changelog
3. Ketik Search `Rename Item 589 {runId}-220`, tekan Enter
4. Catat entri Changelog `Rename Item 589 {runId}-220` yang ada (baseline entri lama)
5. Tutup Modal Changelog
6. Buka Settings > Categories lalu rename `Rename Category 589 {runId}-220` menjadi `Rename Category 589 {runId}-220 Baru`
7. Buka tab Asset Name
8. Ketik Search `Rename Item 589 {runId}-220`, tekan Enter
9. Verifikasi kolom Category baris `Rename Item 589 {runId}-220` menampilkan `Rename Category 589 {runId}-220 Baru` tanpa memuat ulang halaman
10. Klik nama `Rename Item 589 {runId}-220` untuk membuka Popup Detail
11. Verifikasi Popup Detail menampilkan Category `Rename Category 589 {runId}-220 Baru` tanpa memuat ulang halaman
12. Tutup Popup Detail
13. Klik icon Changelog
14. Ketik Search `Rename Item 589 {runId}-220`, tekan Enter
15. Verifikasi entri Changelog lama `Rename Item 589 {runId}-220` sama dengan baseline pada langkah 4
16. Tutup Modal Changelog

### TC-FA-FAAM-590: Rename Brand di Global Settings langsung terlihat

17. Buka Global Settings > Brand lalu rename `Rename Brand 590 {runId}-220` menjadi `Rename Brand 590 {runId}-220 Baru`
18. Buka tab Asset Name
19. Ketik Search `Rename Item 590 {runId}-220`, tekan Enter
20. Verifikasi sel Brand baris `Rename Item 590 {runId}-220` menampilkan `Rename Brand 590 {runId}-220 Baru`
21. Klik nama `Rename Item 590 {runId}-220` untuk membuka Popup Detail
22. Verifikasi tabel Models per Brand pada Popup Detail menampilkan `Rename Brand 590 {runId}-220 Baru`
23. Tutup Popup Detail

### TC-FA-FAAM-591: Rename UoM di Global Settings langsung terlihat

24. Buka Global Settings > Measurement lalu rename Unit Name `Rename UoM 591 {runId}-220` menjadi `Rename UoM 591 {runId}-220 Baru`
25. Buka tab Asset Name
26. Ketik Search `Rename Item 591 {runId}-220`, tekan Enter
27. Verifikasi kolom UoM baris `Rename Item 591 {runId}-220` menampilkan `Rename UoM 591 {runId}-220 Baru`

### TC-FA-FAAM-592: Rename label di Labels langsung terlihat sebagai Default Label

28. Buka tab Labels lalu rename `Rename Label 592 {runId}-220` menjadi `Renamed Label 592 {runId}-220`
29. Buka tab Asset Name
30. Ketik Search `Rename Label Item 592 {runId}-220`, tekan Enter
31. Verifikasi badge Default Label baris `Rename Label Item 592 {runId}-220` menampilkan `Renamed Label 592 {runId}-220`

### TC-FA-FAAM-594: Delete Category yang dirujuk Asset Name diblokir dan List tidak berubah

32. Buka Settings > Categories lalu coba hapus `IT Equipment`
33. Verifikasi penghapusan diblokir oleh modul Categories (dialog in-use tampil)
34. Tutup dialog in-use
35. Buka tab Asset Name
36. Ketik Search `Dell Latitude`, tekan Enter
37. Verifikasi Asset Name `Dell Latitude` tetap menampilkan Category `IT Equipment`

### TC-FA-FAAM-595: Delete Brand yang dirujuk Asset Name diblokir

38. Buka Global Settings > Brand lalu coba hapus `Dell`
39. Verifikasi penghapusan diblokir
40. Tutup dialog blokir
41. Buka tab Asset Name
42. Verifikasi Brand `Dell` tetap tampil di Asset Name `Dell Latitude`

### TC-FA-FAAM-596: Delete UoM yang dipakai Asset Name diblokir

43. Buka Global Settings > Measurement lalu coba hapus `Unit`
44. Verifikasi penghapusan diblokir
45. Tutup dialog blokir
46. Buka tab Asset Name
47. Verifikasi UoM `Unit` tetap tampil di Asset Name `Dell Latitude`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search tabel utama), langkah 2, 3, 5, 13, 14, 16 (membuka, mencari, dan menutup Modal Changelog; S-12, S-14), langkah 4 (mencatat baseline), langkah 7, 18, 25, 29, 35, 41, 46 (pindah ke tab Asset Name), langkah 8, 19, 26, 30, 36 (Search untuk menemukan baris target), dan langkah 12, 23, 34, 40, 45 (menutup Popup Detail atau dialog).
- Di atas smell 35 langkah. Spec berisi 47 langkah, di atas ~35. Alasan: tujuh blok adalah sinkron lintas modul satu topik (master data yang dipakai Asset Name), tiap blok memakai seed sendiri dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-FA-FAAM-593 (Delete label yang dijadikan Default Label diblokir) ada di spec 216 karena memuat asersi tanpa baris log.
- Urutan: rename (TC-FA-FAAM-589 sampai 592) sebelum percobaan Delete yang diblokir (TC-FA-FAAM-594 sampai 596); blokir tidak mengubah data sehingga tidak ada aksi yang menghapus data.
- Temuan untuk QA:
  - Fixture 31, 31b, 31c, dan 25c dimutasi oleh rename; Tabel Data Uji Dinamis tidak memuat salinan bernama unik untuk TC-FA-FAAM-589 sampai 592. Spec men-seed salinan bersuffix `{runId}-220` sesuai S-06.
  - TC-FA-FAAM-594 sampai 596 menghapus `IT Equipment`, `Dell`, dan `Unit` pada data Pre-setup bersama; spec hanya mengasersi penolakan (data tidak berubah) dan tidak mengonfirmasi penghapusan.
  - TC-FA-FAAM-594 menyebut "dialog in-use" tanpa judul atau teksnya; spec mengasersi dialog tampil tanpa teks.
  - TC-FA-FAAM-589 butir b ("entri Changelog lama tidak berubah") tidak menyebut entri mana; spec membandingkan entri yang ada sebelum dan sesudah rename.
