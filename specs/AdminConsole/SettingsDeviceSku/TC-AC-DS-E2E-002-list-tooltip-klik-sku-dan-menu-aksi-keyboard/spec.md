---
id: TC-AC-DS-E2E-002-list-tooltip-klik-sku-dan-menu-aksi-keyboard
title: "List: Tooltip Toolbar, Klik Kolom SKU Membuka Popup Detail, dan Menu Aksi Baris lewat Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-3
  - TC-AC-DS-5
  - TC-AC-DS-570
coverage:
  web: automated
---

# List: Tooltip Toolbar, Klik Kolom SKU Membuka Popup Detail, dan Menu Aksi Baris lewat Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30 (129 SKU Principal). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada). Popup Edit SKU dan dialog Delete hanya dibuka lalu ditutup dengan `Esc` tanpa mengubah data.
- Tabel "Ikon toolbar yang diuji":

| Ikon | Teks tooltip |
|---|---|
| Search | `Search` |
| Filter | `Filter` |
| Download | `Download` |
| Changelog | `Changelog` |
| Header kolom paling kanan (⋯) | `Column Visibility` |

- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Spec ini read-only: tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-3: Tooltip ikon toolbar dan header kolom Column Visibility

1. Untuk setiap baris tabel "Ikon toolbar yang diuji", lakukan langkah 2 sampai 5
2. Hover ikon pada baris tabel
3. Verifikasi tooltip dengan teks pada baris tabel tampil saat hover
4. Pindahkan fokus keyboard dengan Tab ke ikon yang sama
5. Verifikasi tooltip dengan teks pada baris tabel tampil saat fokus keyboard

### TC-AC-DS-5: Klik kolom SKU membuka popup Device SKU Detail

6. Klik teks SKU `HHR-ARC-100` pada baris pertama dengan kode itu
7. Verifikasi Popup `Device SKU Detail` tampil
8. Tutup popup dengan ikon close `[✕]`
9. Klik area sel Device Name baris `HHR-ARC-100`
10. Klik area sel Category baris `HHR-ARC-100`
11. Klik area sel Brand baris `HHR-ARC-100`
12. Klik area sel Model/Type baris `HHR-ARC-100`
13. Klik area sel Current Stock baris `HHR-ARC-100`
14. Klik area sel Last Modified baris `HHR-ARC-100`
15. Verifikasi tidak ada popup, dialog, atau halaman yang terbuka
16. Verifikasi halaman tidak berpindah
17. Verifikasi baris `HHR-ARC-100` tidak berubah menjadi terpilih

### TC-AC-DS-570: Menu aksi baris lewat keyboard

18. Pindahkan fokus keyboard dengan Tab ke tombol ⋯ pada baris `HHR-ARC-200`
19. Verifikasi tombol ⋯ baris `HHR-ARC-200` berfokus
20. Tekan Enter
21. Verifikasi menu aksi terbuka
22. Verifikasi menu memuat `Detail`, `Edit`, dan `Delete`
23. Pilih `Detail` memakai keyboard lalu tekan Enter
24. Verifikasi Popup `Device SKU Detail` tampil sama seperti pemilihan memakai mouse
25. Tekan Esc untuk menutup popup
26. Buka menu aksi baris `HHR-ARC-200` lewat keyboard lalu pilih `Edit` memakai keyboard dan tekan Enter
27. Verifikasi Popup `Edit SKU` tampil sama seperti pemilihan memakai mouse
28. Tekan Esc untuk menutup popup
29. Buka menu aksi baris `HHR-ARC-200` lewat keyboard lalu pilih `Delete` memakai keyboard dan tekan Enter
30. Verifikasi dialog `Delete SKU` tampil sama seperti pemilihan memakai mouse
31. Tekan Esc untuk menutup dialog

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-3, TC-5, TC-570.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 (perulangan), 2 dan 4 (hover dan fokus yang hasilnya diasersi pada langkah berikutnya), 6, 8, 9 sampai 14 (klik yang hasilnya diasersi pada langkah 15 sampai 17), 18, 20, 23, 25, 26, 28, 29, 31. Langkah 2 sampai 5 diulang untuk lima baris tabel "Ikon toolbar yang diuji" (8b butir 7).
- Spec melewati sekitar 35 langkah (ekspansi perulangan: 5 x 4 = 20 langkah ditambah 27 langkah lain = 47). Alasan pertahanan: seluruh blok berada di satu halaman List dalam kelas screening UI yang sama, tanpa seeding dan tanpa mengubah data; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 22 memuat tiga item menu dalam satu `Verifikasi` karena TC menyebutnya dalam satu butir (daftar item yang disebut utuh).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30 (`HHR-ARC-100`, `HHR-ARC-200`) karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29/#30 di environment belum diverifikasi.
  - TC-5 tidak merinci cara menutup popup selain `[✕]`; spec memakai `[✕]` sesuai TC.
  - TC-570 menyebut dialog bernama "Delete SKU" tanpa merinci isinya; spec hanya mengasersi dialog tampil.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila muncul menutupi layar, cara menyetel flag perlu disediakan tim FE.
