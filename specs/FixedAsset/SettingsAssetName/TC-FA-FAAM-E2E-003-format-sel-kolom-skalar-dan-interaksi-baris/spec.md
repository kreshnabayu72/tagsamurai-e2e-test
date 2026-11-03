---
id: TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris
title: "Format Sel Kolom Skalar, Header Tanpa Wrap, Hover Nama, dan Menu Aksi Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-10
  - TC-FA-FAAM-11
  - TC-FA-FAAM-12
  - TC-FA-FAAM-13
  - TC-FA-FAAM-14
  - TC-FA-FAAM-15
  - TC-FA-FAAM-16
  - TC-FA-FAAM-17
  - TC-FA-FAAM-26
  - TC-FA-FAAM-29
  - TC-FA-FAAM-30
  - TC-FA-FAAM-31
coverage:
  web: automated
---

# Format Sel Kolom Skalar, Header Tanpa Wrap, Hover Nama, dan Menu Aksi Baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10: Code `DLAT`, Category `IT Equipment`, TAG `RFID`+`QR`, UoM `Unit`, Total Asset 42, Modified By Sarah Johnson) dan `Warehouse Pallet` (#13: TAG `Non-TAG`, Total Asset 0). Baris ditemukan lewat Search karena katalog lebih dari satu halaman.
- General Settings client utama memakai Date Format dan Time Format baseline (tidak diubah spec); nilai konkretnya tidak ditulis di TC (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Viewport diperkecil pada langkah 30 dan dipulihkan pada langkah 34. Suite berjalan serial (`parallel: false`).

## Test Steps

### Penghubung: menemukan baris target

1. Ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-10: Sel kolom Asset Name di tabel utama tampil sesuai format

2. Verifikasi sel kolom Asset Name baris `Dell Latitude` berupa teks link primary identifier
3. Verifikasi sel kolom Asset Name baris `Dell Latitude` tidak terpotong

### TC-FA-FAAM-11: Sel kolom Code di tabel utama tampil sesuai format

4. Verifikasi kolom Code baris `Dell Latitude` berupa teks biasa `DLAT`

### TC-FA-FAAM-12: Sel kolom Category di tabel utama tampil sesuai format

5. Verifikasi kolom Category baris `Dell Latitude` berupa Badge Primary berisi nama kategori `IT Equipment`

### TC-FA-FAAM-13: Sel kolom TAG Type di tabel utama tampil sesuai format

6. Verifikasi kolom TAG Type: icon aktif tampil berurutan RFID, NFC, QR, BLE, GPS tanpa `+N more`
7. Verifikasi baris `Dell Latitude` menampilkan icon RFID dan QR

### TC-FA-FAAM-14: Sel kolom UoM di tabel utama tampil sesuai format

8. Verifikasi kolom UoM baris `Dell Latitude` berupa teks `Unit` (Unit Name, bukan Symbol)

### TC-FA-FAAM-15: Sel kolom Total Asset di tabel utama tampil sesuai format

9. Verifikasi kolom Total Asset baris `Dell Latitude` berupa angka bulat rata kanan `42`

### TC-FA-FAAM-16: Sel kolom Modified By di tabel utama tampil sesuai format

10. Verifikasi kolom Modified By baris `Dell Latitude` berupa plain text `Sarah J` (format `[First Name] [Last Initial]`)
11. Hover sel Modified By baris `Dell Latitude`
12. Verifikasi tooltip nama lengkap `Sarah Johnson` tampil

### TC-FA-FAAM-17: Sel kolom Last Updated di tabel utama tampil sesuai format

13. Verifikasi kolom Last Updated baris `Dell Latitude` menampilkan tanggal sesuai Date Format General Settings
14. Verifikasi kolom Last Updated baris `Dell Latitude` menampilkan jam sesuai Time Format General Settings

### TC-FA-FAAM-29: Primary identifier Asset Name berwarna netral dan berubah biru tanpa underline saat hover

15. Verifikasi teks nama `Dell Latitude` berwarna default netral seperti teks body
16. Hover nama `Dell Latitude`
17. Verifikasi warna teks nama berubah menjadi warna primary FAMS (biru)
18. Verifikasi teks nama tidak ber-underline saat hover

### TC-FA-FAAM-30: Klik area baris di luar nama, checkbox, dan menu aksi tidak melakukan aksi apa pun

19. Klik sel kolom Code baris `Dell Latitude`
20. Verifikasi tidak ada popup atau navigasi terbuka

### TC-FA-FAAM-31: Menu aksi baris untuk Total Control berisi Detail, Edit, Delete berurutan

21. Klik icon `⋯` baris `Dell Latitude`
22. Verifikasi overlay row action memuat `Detail`, `Edit`, `Delete` berurutan
23. Verifikasi `Delete` bersifat danger (merah)
24. Verifikasi `Delete` berada paling akhir
25. Tekan Esc untuk menutup overlay row action

### TC-FA-FAAM-13 dan TC-FA-FAAM-15: baris `Warehouse Pallet`

26. Ganti isi kotak search dengan `Warehouse Pallet`, tekan Enter
27. Verifikasi baris `Warehouse Pallet` pada kolom TAG Type menampilkan teks `Non-TAG`
28. Verifikasi baris `Warehouse Pallet` pada kolom TAG Type tanpa badge
29. Verifikasi kolom Total Asset baris `Warehouse Pallet` berupa `0` (bukan `—`)

### TC-FA-FAAM-26: Header kolom tidak pernah wrap ke dua baris

30. Perkecil lebar viewport sampai kolom sempit
31. Verifikasi label header kolom `Default Addon` tetap satu baris
32. Verifikasi label header kolom `Default Label` tetap satu baris
33. Verifikasi tinggi header tetap
34. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: kelompok `Dell Latitude` (TC-10, 11, 12, 13 bagian a dan b, 14, 15 bagian `42`, 16, 17, 29, 30, 31) memakai satu Search; TC-13 bagian c dan TC-15 bagian `0` memakai baris `Warehouse Pallet` sehingga ditaruh bersama setelah ganti Search; TC-26 (mengubah viewport) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 dan 26 (Search untuk menemukan baris target, R-16), langkah 25 (menutup overlay), langkah 34 (memulihkan viewport, S-09). Langkah "Perhatikan sel ..." pada Langkah uji TC-10 sampai TC-17 dilebur ke langkah `Verifikasi` karena tidak mengubah state.
- Langkah 12 asersi tooltip nama lengkap dan langkah 10 format `[First Name] [Last Initial]` mengikuti R-14.
- Langkah 28 dan 20 (absence) memakai baris yang baru diasersi atau tabel yang tampil sebagai anchor permukaan (8b butir 2).
- Temuan untuk QA:
  - TC-17 Expected "tanggal dan jam mengikuti Date Format dan Time Format General Settings" tidak menyebut nilai format konkret; spec tidak menulis string tanggal literal dan mengasersi kesesuaian dengan General Settings client utama.
  - TC-10 sampai TC-17 Langkah 1 "pada baris Pre-setup #10 s.d. #14" tidak menyebut baris untuk tiap kolom; spec memakai `Dell Latitude` (#10) dan `Warehouse Pallet` (#13) sesuai nilai Expected yang disebut.
  - TC-13 a menyebut kelima icon "tanpa `+N more`" sebagai aturan kolom, bukan pada satu baris; spec mengasersinya pada kolom TAG Type baris `Dell Latitude`.
