---
id: TC-AC-DS-E2E-165-defense-injeksi-xss-sql-dan-karakter-invalid-sku
title: "Defense-in-Depth: Payload Script, Injeksi Basis Data, dan Karakter Invalid pada SKU lewat API"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-309
  - TC-AC-DS-526
  - TC-AC-DS-530
  - TC-AC-DS-531
  - TC-AC-DS-589
coverage:
  web: automated
---

# Defense-in-Depth: Payload Script, Injeksi Basis Data, dan Karakter Invalid pada SKU lewat API

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35).
- Data Dinamis: SKU `XSS-01` (Data Dinamis #33) dibuat TC 530; hook `before` menghapus sisa kode itu bila ada dan hook `after` menghapusnya. Payload TC 526 (SKU `ABC_123 #1`) tidak boleh tersimpan.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah entri Changelog Principal lewat BE sebelum dan sesudah Register TC 530 (audit trail permanen; S-12); klien HTTP untuk request langsung ke server dengan token akun #1 (sesi API aktor); ID record SKU dibaca lewat fixture BE. Sesi API aktor (login API password, tidak dihitung sesi web) disediakan tim BE/FE sesuai `suite.md`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-309: Search memperlakukan karakter khusus dan payload script sebagai teks biasa

1. Klik ikon Search, ketik Search `<script>alert(1)</script>`, tekan Enter
2. Verifikasi tidak ada script yang dijalankan (tidak ada dialog alert)
3. Verifikasi tabel tampil "No results found" untuk payload script
4. Kosongkan isi kotak search, ketik Search `%`, tekan Enter
5. Verifikasi `%` tidak berfungsi sebagai pola pencarian: tabel tampil "No results found"
6. Kosongkan isi kotak search, ketik Search `*`, tekan Enter
7. Verifikasi `*` tidak berfungsi sebagai pola pencarian: tabel tampil "No results found"

### TC-AC-DS-531: Payload injeksi basis data pada Search diperlakukan sebagai teks biasa

8. Ganti isi kotak search dengan `'; DROP TABLE x; --`, tekan Enter
9. Verifikasi tabel menampilkan "No results found" tanpa error
10. Hapus kata kunci lalu tekan Enter pada input kosong
11. Verifikasi setelah reset seluruh 129 SKU Principal tampil normal

### TC-AC-DS-526: Karakter invalid pada SKU lewat API ditolak dengan pesan SKU contains invalid characters

12. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `totalControlSku` dengan SKU `ABC_123 #1` (payload POST lengkap: `deviceNameId`, `brandId`, `sku`, `model`, `firstImage`, dan `defaultImage` terisi nilai valid kecuali field yang disebut)
13. Verifikasi respons ditolak dengan status 422 dan error pada field `sku` dengan pesan "SKU contains invalid characters"
14. Klik `(←)` pada kotak Search, klik ikon Search, ketik `ABC`, tekan Enter
15. Verifikasi Search `ABC` menampilkan "No results found" (tidak ada SKU baru)

### TC-AC-DS-589: Karakter invalid pada SKU lewat API PATCH ditolak dengan pesan SKU contains invalid characters

16. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-200` (stok 0) lewat klien HTTP dengan token `totalControlSku` dengan `sku` `ABC_123 #1` (formulir Edit lengkap: `sku`, `deviceNameId`, `brandId`, `model`, dan `defaultImage` berisi nilai tersimpan kecuali field yang disebut)
17. Verifikasi respons ditolak dengan status 422 dan error pada field `sku` dengan pesan "SKU contains invalid characters"
18. Klik `(←)` pada kotak Search, ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
19. Verifikasi field SKU tetap `HHR-ARC-200`
20. Verifikasi field Model/Type tetap `H200`
21. Tekan Esc lalu klik `(←)` pada kotak Search

### TC-AC-DS-530: Payload script pada Model/Type dirender sebagai teks pada List, Popup Detail, dan Changelog

22. Catat baseline jumlah entri Changelog Principal lewat kemampuan baca BE
23. Klik tombol `[+ SKU]` pada toolbar
24. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
25. Klik field Device Name lalu pilih `Asset TAG`
26. Klik field Brand lalu pilih `Arcturus`
27. Ketik `<script>alert(1)</script>` pada field Model/Type
28. Ketik `XSS-01` pada field SKU
29. Unggah `foto-a.jpg` pada field Photo
30. Klik `[Submit]`
31. Ketik Search `XSS-01`, tekan Enter
32. Verifikasi badge Model/Type pada baris `XSS-01` menampilkan teks `<script>alert(1)</script>` apa adanya dan tidak ada script yang dijalankan
33. Klik SKU `XSS-01`
34. Verifikasi Info Grid Popup Detail menampilkan teks `<script>alert(1)</script>` sebagai teks biasa
35. Tutup popup lalu buka modal Changelog dan cari entri `XSS-01`
36. Verifikasi jumlah entri Changelog Principal bertambah tepat 1 dari baseline langkah 22 (entri Create `XSS-01`)
37. Verifikasi Changelog menampilkan teks `<script>alert(1)</script>` apa adanya pada kolom yang memuat Model/Type

## Notes

- `K-1`: TC 526 dan 589 (kelas a, Expected respons API) tetap masuk spec FE+BE; langkah request langsung hanya mengasersi status respons, pesan error, dan state data (8b butir 1). TC 309, 530, dan 531 mengasersi perilaku FE atas payload di browser.
- Langkah penghubung tanpa `Verifikasi`: langkah 22 (baseline jumlah entri Changelog sebelum Register, S-12), pengosongan Search (R-16), Search `HHR-ARC-200` di langkah 18 (menemukan baris target), submit Register tanpa asersi (TC 530 tidak mengasersi toast), dan pembukaan Changelog dengan pencarian entri `XSS-01`.
- Spec berada di atas sekitar 35 langkah (35 langkah); alasan: semua blok satu kelas harness (a) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC 530 Expected butir c meminta Changelog menampilkan teks payload pada kolom yang memuat Model/Type, sedangkan PRD hanya mencatat Field `SKU` pada entri Create; spec tetap mengikuti TC (langkah 37) dan butir ini menunggu keputusan QA. Entri baru dibaca lewat selisih +1 dari baseline (langkah 22 dan 36).
  - TC 530 mengasersi Changelog tanpa langkah pencarian rinci ("cari entri XSS-01") dan TC 309 serta 531 menyebut hasil "No results found" tanpa kata kunci bantu; spec mengikuti TC. TC 531 Expected "129 SKU Principal tampil normal" memakai jumlah Pre-setup tetap, bukan total audit trail.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
