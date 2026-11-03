---
id: TC-AC-DC-E2E-005-pencarian-tree-dan-expand-collapse
title: "Sidebar Category: State Loading Tree, Toggle Expand/Collapse All, Pencarian Tree, dan Pencarian Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-12
  - TC-AC-DC-14
  - TC-AC-DC-15
  - TC-AC-DC-16
coverage:
  web: automated
---

# Sidebar Category: State Loading Tree, Toggle Expand/Collapse All, Pencarian Tree, dan Pencarian Tanpa Hasil

## Prerequisites

- Mode: FE+BE (penundaan respons memakai `Spectra.intercept()` parsial di atas backend nyata; hanya untuk mengamati state Loading, bukan kegagalan).
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) hanya dibaca; spec tidak membuat, mengubah, atau menghapus node. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons endpoint pemuat tree Category selama 5 detik (nama endpoint ditunjuk tim FE dari LLD modul; tidak dikarang di spec ini); intercept dilepas segera setelah respons diterima (S-09).
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-12: State Loading tree saat data kategori sedang dimuat

1. Pasang penundaan 5 detik pada respons endpoint pemuat tree Category
2. Muat ulang halaman dengan F5
3. Verifikasi area tree menampilkan komponen Loading selama data belum diterima
4. Verifikasi komponen Loading hilang setelah respons diterima
5. Verifikasi tree `Hardware` dan `TAG` tampil
6. Lepas penundaan respons

### TC-AC-DC-15: Tombol toggle Expand/Collapse All pada header sidebar

7. Verifikasi `Hardware` dan `TAG` tampil collapsed pada kondisi awal
8. Klik tombol toggle Expand/Collapse All pada baris 2 header sidebar
9. Verifikasi seluruh node tree ter-expand
10. Klik tombol toggle Expand/Collapse All yang sama sekali lagi
11. Verifikasi seluruh node tree collapse kembali ke kondisi awal

### TC-AC-DC-14: Pencarian node pada tree dengan kolom pencarian sidebar

12. Ketik Search `Rugged` pada kolom pencarian tree, tekan Enter
13. Verifikasi hanya node yang cocok (`Rugged Scanner`, `Rugged`, `Rugged Kit`) tampil beserta induknya yang otomatis ter-expand
14. Verifikasi node yang tidak cocok tidak tampil
15. Ganti isi kotak pencarian tree dengan `rugged`, tekan Enter
16. Verifikasi pencarian huruf kecil menampilkan hasil yang sama
17. Klik `[×]` pada kotak pencarian tree, tekan Enter
18. Verifikasi tree kembali ke kondisi awal (`Hardware` dan `TAG` collapsed)
19. Verifikasi placeholder kolom pencarian tree yang kosong berisi "Search categories..."

### TC-AC-DC-16: Pencarian tree tanpa hasil menampilkan empty state tidak ada hasil

20. Ketik Search `zzzz` pada kolom pencarian tree, tekan Enter
21. Verifikasi baris `All Categories` tetap tampil
22. Verifikasi area tree di bawah `All Categories` menampilkan empty state dengan ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
23. Klik `[×]` pada kotak pencarian tree, tekan Enter
24. Verifikasi tree kembali ke kondisi awal (`Hardware` dan `TAG` collapsed)

## Notes

- Urutan TC dalam spec: TC-AC-DC-12, 15, 14, 16. TC-AC-DC-12 dijalankan pertama karena membutuhkan muat ulang; TC-AC-DC-15 membutuhkan kondisi awal (collapsed) sebelum pencarian (S-10).
- Langkah penghubung (S-03): langkah 1 dan 6 memasang dan melepas penundaan respons; langkah 2 memuat ulang halaman supaya respons tertunda terpakai.
- TC-AC-DC-14 Expected a menyebut pencarian "dijalankan setelah Enter"; langkah TC selalu mengetik lalu menekan Enter, sehingga keadaan sebelum Enter tidak diasersi.
- Temuan untuk QA: (1) TC-AC-DC-12 menyebut "Respons endpoint tree Category ditunda 5 detik" tanpa nama endpoint; nama endpoint disediakan tim FE dari LLD. (2) Kegagalan fetch tree (TC-AC-DC-13) ada di spec ketahanan terhadap kegagalan server, bukan di spec ini.
