---
id: TC-AC-DS-E2E-129-detail-usage-by-company-principal-total-stock-dan-empty
title: "Usage by Company Principal: Seluruh Baris, Total Stock per Peran, Dua Badge, Kuota Alokasi, Empty State, dan Pembaruan Stok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-430
  - TC-AC-DS-431
  - TC-AC-DS-432
  - TC-AC-DS-433
  - TC-AC-DS-434
  - TC-AC-DS-435
  - TC-AC-DS-438
  - TC-AC-DS-441
  - TC-AC-DS-442
coverage:
  web: automated
---

# Usage by Company Principal: Seluruh Baris, Total Stock per Peran, Dua Badge, Kuota Alokasi, Empty State, dan Pembaruan Stok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `HHR-ARC-100` (Current Stock 120), `HHR-ARC-200` (stok 0), `SFR-VEL-4P` serta seed (#29, #30); data Usage by Company dan jaringan entitas (#32, #24); kuota alokasi Category `Portal Reader` untuk `PT Cakra Distribusi` pada Device Allocation (#40); General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35); modul stok Hardware Stock (#39). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): stok `HHR-ARC-100` untuk `PT Cakra Distribusi` bertambah 2 unit lewat Add Stock pada TC-AC-DS-442 (Total Stock Cakra 25 menjadi 27, Current Stock `HHR-ARC-100` 120 menjadi 122). Data ini Pre-setup bersama karena TC menetapkannya; pemulihan ke 25 dan 120 dijamin fixture BE yang disediakan tim FE/BE di hook `before` dan `after`. Efek: Last Modified `HHR-ARC-100` dan entri audit trail stok.
- Kemampuan teknis (disediakan tim FE/BE): Add Stock `HHR-ARC-100` 2 unit untuk `PT Cakra Distribusi` (lewat modul Hardware Stock atau fixture BE; TC menyebut "Add Stock" tanpa menyebut mekanisme), seeding dan pemulihan Pre-setup di atas.
- State global: tidak ada selain stok di atas. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-430, TC-AC-DS-432, TC-AC-DS-433, TC-AC-DS-434: Usage `HHR-ARC-100`

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil
3. Verifikasi lima baris berurutan Company A-Z: `PT Arunika Prima` (Principal) 55, `PT Cakra Distribusi` (Distributor) 25, `PT Delta Retail` (Client) 5, `PT Mitra Lintas Nusa` (Distributor dan Client) 20, `PT Surya Logistik` (Client) 15
4. Verifikasi jumlah Total Stock seluruh baris 120 sama dengan Current Stock `HHR-ARC-100`
5. Verifikasi `PT Nusantara Mitra` (0 unit) dan Partner murni `CV Karya Mandiri` tidak tampil
6. Verifikasi baris `PT Mitra Lintas Nusa` tampil satu kali dengan dua badge Entity Type: `Distributor` dan `Client`
7. Verifikasi Total Stock baris `PT Mitra Lintas Nusa` `20` sama dengan jumlah unit tercatat company itu dan tidak dijumlahkan antar relasi
8. Verifikasi baris `PT Cakra Distribusi` dengan Entity Type `Distributor` menampilkan Total Stock `25` (unit tercatat Distributor untuk SKU Principal hasil Device Allocation)
9. Verifikasi baris `PT Surya Logistik` dengan Entity Type `Client` menampilkan Total Stock `15`
10. Verifikasi unit tanpa SKU (BYO) `PT Surya Logistik` sebanyak 7 unit tidak ikut dihitung (Total Stock tetap `15`)

### Pemulihan state antar TC

11. Tutup popup dengan ikon close `[✕]`

### TC-AC-DS-431, TC-AC-DS-435: Usage `SFR-VEL-4P`

12. Ketik Search `SFR-VEL-4P`, tekan Enter
13. Klik SKU `SFR-VEL-4P`
14. Verifikasi Popup `Device SKU Detail` tampil
15. Verifikasi baris `PT Arunika Prima` dengan Entity Type `Principal` menampilkan Total Stock `20` (unit tercatat Principal untuk `SFR-VEL-4P`)
16. Verifikasi Total Stock `20` bukan kuota alokasi
17. Verifikasi baris dan Total Stock tidak berubah walau Category `Portal Reader` memiliki kuota alokasi untuk `PT Cakra Distribusi` di Device Allocation: `PT Arunika Prima` 20 dan `PT Cakra Distribusi` 16

### Pemulihan state antar TC

18. Tutup popup dengan ikon close `[✕]`
19. Klik `(←)` pada kotak Search

### TC-AC-DS-438: Empty state Usage by Company

20. Klik SKU `HHR-ARC-200`
21. Verifikasi area tabel menampilkan ilustrasi dengan judul "No usage data yet" dan deskripsi "Company usage details will appear here."
22. Verifikasi toolbar popup tetap tampil

### Pemulihan state antar TC

23. Tutup popup dengan ikon close `[✕]`

### TC-AC-DS-441: Popup Detail tanpa kolom tanggal

24. Klik SKU `HHR-ARC-100`
25. Verifikasi Popup `Device SKU Detail` tampil
26. Verifikasi Info Grid dan tabel Usage tidak memuat kolom atau label bertanggal sehingga format General Settings tidak relevan pada surface ini

### Pemulihan state antar TC

27. Tutup popup dengan ikon close `[✕]`

### TC-AC-DS-442: Total Stock Usage mengikuti perubahan stok setelah popup dibuka kembali

28. Tambahkan 2 unit `HHR-ARC-100` untuk `PT Cakra Distribusi` lewat Add Stock hingga perubahan stok tersimpan
29. Klik SKU `HHR-ARC-100`
30. Verifikasi baris `PT Cakra Distribusi` menampilkan Total Stock `27`
31. Tutup popup dengan ikon close `[✕]`
32. Verifikasi Current Stock `HHR-ARC-100` pada List `122`

## Notes

- Pengelompokan: TC-AC-DS-430, 432, 433, 434 memakai popup `HHR-ARC-100` yang dibuka sekali (langkah 1) karena membaca tabel Usage yang sama; TC-AC-DS-431 dan 435 memakai popup `SFR-VEL-4P`. Urutan TC-AC-DS-442 di akhir karena menulis data stok (S-10).
- Langkah penghubung tanpa `Verifikasi`: langkah 11, 18, 23, 27, dan 31 (menutup popup, S-03), langkah 12 (Search untuk menemukan baris `SFR-VEL-4P`, R-16), dan langkah 19 (menutup Search agar baris `HHR-ARC-200` tampil kembali); langkah 28 adalah pemicu aksi tulis TC-AC-DS-442 dengan "hingga ... tersimpan" (R-20).
- Langkah 1, 20, 24, 29 membuka baris dari List yang dibuka hook `beforeEach` tanpa Search (baris tampil di halaman pertama pada urutan bawaan); `SFR-VEL-4P` berada di sekitar baris ke-124 sehingga ditemukan lewat Search (langkah 12) sebelum diklik (langkah 13).
- Temuan untuk QA:
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100` dan `HHR-ARC-200`; spec mengandalkan keduanya tampil di halaman pertama List. TC 431 dan 435 juga tidak menyebut Search untuk `SFR-VEL-4P` (bukan di halaman 1); spec menambah langkah penghubung Search.
  - S-15: TC 442 menyebut Add Stock tanpa menyebut modul/jalur UI; List Current Stock `122` pada langkah 32 mungkin membutuhkan muat ulang; TC tidak menyatakannya. Pemulihan stok disebut hanya sebagai kegiatan automation baseline.
  - S-15: Expected TC 433 butir b ("7 unit BYO tidak ikut dihitung") tidak punya langkah observasi selain nilai Total Stock; langkah 10 mengasersi `15` bukan `22`.
  - Fixture rancangan Pre-setup #32, #24, #40 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
