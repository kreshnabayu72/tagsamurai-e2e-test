---
id: TC-AC-DS-E2E-141-usage-download-cakupan-baris-nol-baris-dan-kolom-tampil
title: "Download Usage: Nama File, Ekstensi, Cakupan Baris, Nol Baris, dan Mengikuti Kolom Tampil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-463
  - TC-AC-DS-466
  - TC-AC-DS-598
coverage:
  web: automated
---

# Download Usage: Nama File, Ekstensi, Cakupan Baris, Nol Baris, dan Mengikuti Kolom Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris dengan tiga baris Entity Type `Client` (`PT Delta Retail`, `PT Mitra Lintas Nusa`, `PT Surya Logistik`) (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Berkas unduhan disimpan di folder unduhan runner dan tidak dihapus oleh spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca isi berkas CSV dan XLSX yang diunduh (nama berkas, baris header, jumlah baris data); menghapus preferensi kolom Setup Column popup Usage di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil

### TC-AC-DS-463: Download Usage by Company: nama file, ekstensi, dan cakupan baris

3. Klik ikon Download pada popup
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi file bernama `SKU-HHR-ARC-100-Usage-by-Company.csv` berisi 5 baris
7. Verifikasi file CSV memuat header `Company`, `Entity Type`, dan `Total Stock`
8. Klik ikon Filter pada popup
9. Pada field Entity Type pilih `Client`
10. Klik `[Apply]` pada Filter Panel popup
11. Klik ikon Download lalu `Download as XLSX`
12. Verifikasi file bernama `SKU-HHR-ARC-100-Usage-by-Company.xlsx` berisi 3 baris Entity Type `Client`

### Pemulihan state antar TC

13. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-DS-466: Download Usage dengan hasil nol baris menghasilkan file berisi header saja

14. Klik ikon Search pada popup, ketik Search `tidak-ada-company`, tekan Enter
15. Klik ikon Download lalu `Download as CSV`
16. Verifikasi tidak ada toast
17. Verifikasi file terunduh berisi hanya header `Company`, `Entity Type`, dan `Total Stock`

### Pemulihan state antar TC

18. Klik `(←)` pada kotak Search

### TC-AC-DS-598: Download Usage by Company mengikuti kolom yang tampil: kolom Hidden tidak ikut dan kembali setelah unhide

19. Klik header kolom Actions (⋯) pada popup, hilangkan centang `Entity Type`
20. Verifikasi kolom `Entity Type` hilang dari tabel Usage
21. Klik ikon Download pada popup lalu `Download as CSV`
22. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
23. Verifikasi file pertama `SKU-HHR-ARC-100-Usage-by-Company.csv` memuat kolom `Company` dan `Total Stock` tanpa kolom `Entity Type`
24. Centang kembali kolom `Entity Type`
25. Klik ikon Download pada popup lalu `Download as CSV`
26. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
27. Verifikasi file kedua memuat kembali ketiga kolom `Company`, `Entity Type`, dan `Total Stock`

### Pemulihan state akhir

28. Tutup popup `Device SKU Detail` dengan ikon close `[✕]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 13, 18, dan 28 (S-03, S-09). Langkah 13 mengklik `[Clear Field]` tepat setelah `[Apply]` mengikuti pola TC-AC-DS-448 (Filter Panel diasumsikan masih terbuka).
- Absence toast (langkah 5, 16, 22, 26) diletakkan segera setelah pemicu unduh dan sebelum asersi berkas (8b butir 11); pemicu dan berkas pada langkah berikutnya menjadi anchor positif. Expected 598 butir c ditulis satu `Verifikasi` per unduhan (tidak ada toast dan tidak ada peringatan atas pemicu yang sama).
- Temuan untuk QA:
  - TC 598 tidak menyebut nama dan format berkas kedua selain CSV; nama berkas kedua tidak diasersi.
  - S-15: TC tidak menyatakan apakah Filter Panel tertutup sesudah `[Apply]`; spec mengikuti TC.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
