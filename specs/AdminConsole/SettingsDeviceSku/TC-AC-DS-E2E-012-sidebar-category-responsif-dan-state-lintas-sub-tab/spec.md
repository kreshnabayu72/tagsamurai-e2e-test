---
id: TC-AC-DS-E2E-012-sidebar-category-responsif-dan-state-lintas-sub-tab
title: "Sidebar Category: Penutupan Otomatis di Bawah 1280 px dan Pilihan serta Search/Filter Lintas Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-45
  - TC-AC-DS-47
  - TC-AC-DS-48
coverage:
  web: automated
---

# Sidebar Category: Penutupan Otomatis di Bawah 1280 px dan Pilihan serta Search/Filter Lintas Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25, Device Name #26 (Device Name berkategori `Asset TAG`: `Asset TAG`, `Seed Tag`, `anggur sensor`, `Apel sensor`), SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Keadaan awal: panel Sidebar Category terbuka (preferensi tersimpan per user per halaman; spec lain yang menutupnya memulihkannya ke terbuka) dan viewport desktop berlebar 1440 px; spec memulihkan viewport ke 1440 px pada langkah 3.
- Kemampuan teknis: mengubah lebar viewport browser.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding.

## Test Steps

### TC-AC-DS-45: Penutupan otomatis di bawah 1280 px

1. Ubah lebar viewport menjadi 1100 px
2. Verifikasi panel Sidebar Category tersembunyi sementara
3. Ubah lebar viewport menjadi 1440 px
4. Verifikasi panel Sidebar Category tampil kembali sesuai preferensi tersimpan (terbuka)

### TC-AC-DS-47: Pilihan node dibagi lintas sub-tab

5. Klik tombol Expand/Collapse All pada Sidebar Category
6. Klik node `Asset TAG` pada Sidebar Category
7. Klik sub-tab `Device Name`
8. Verifikasi node `Asset TAG` tetap terpilih pada Sidebar Category
9. Verifikasi baris Device Name `Asset TAG` tampil pada tabel Device Name
10. Verifikasi setiap baris tabel Device Name berkategori `Asset TAG`
11. Klik sub-tab `Device SKU`
12. Verifikasi node `Asset TAG` tetap terpilih pada Sidebar Category
13. Verifikasi List tetap tersaring ke kategori `Asset TAG`
14. Klik node `Asset TAG` untuk membatalkan pilihan

### TC-AC-DS-48: Search disimpan terpisah per sub-tab

15. Ketik Search `HHR`, tekan Enter
16. Klik sub-tab `Device Name`
17. Ketik Search `Reader`, tekan Enter
18. Klik sub-tab `Device SKU`
19. Verifikasi kotak Search sub-tab Device SKU tetap berisi `HHR`
20. Verifikasi List tetap tersaring, baris `HHR-ARC-100` tampil
21. Verifikasi Search `Reader` pada sub-tab Device Name tidak memengaruhi List Device SKU, kotak Search sub-tab Device SKU tidak berisi `Reader`
22. Klik `(←)` pada kotak Search sub-tab Device SKU
23. Klik sub-tab `Device Name`
24. Klik `(←)` pada kotak Search sub-tab Device Name
25. Klik sub-tab `Device SKU`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-45, TC-47, TC-48.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 3 (mengubah viewport; langkah 3 memulihkan viewport, S-09), 5 sampai 7 dan 11 (membuka node dan berpindah sub-tab), 14 (membatalkan pilihan node, S-09), 15 sampai 18 (Search dan berpindah sub-tab), 22 sampai 25 (mengosongkan Search pada kedua sub-tab dan kembali ke sub-tab `Device SKU`, S-09).
- Langkah 5 membuka semua node agar node `Asset TAG` terlihat (TC-43 menyatakan klik Expand/Collapse All pertama membuka semua node).
- Langkah 10 didahului langkah 9 (baris `Asset TAG` tampil sebagai pembanding positif) sebelum asersi universal.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25, #26, dan #29 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #25/#26/#29/#30 di environment belum diverifikasi.
  - Judul TC-48 menyebut "Search dan Filter Panel disimpan terpisah", tetapi langkah dan Expected hanya memuat Search; spec tidak menambah langkah Filter Panel.
  - TC-48 Expected b ("tidak memengaruhi") tidak menyebut keadaan yang diamati; spec mengasersi isi kotak Search sub-tab Device SKU.
  - TC-45 langkah 2 mensyaratkan panel terbuka tanpa merinci cara menjamin; keadaan awal ditulis di Prerequisites.
  - TC-45 tidak menyebut tinggi viewport; hanya lebar diubah.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
