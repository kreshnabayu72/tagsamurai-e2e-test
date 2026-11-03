---
id: TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide
title: "Tab Users Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-669
  - TC-FA-GRP-670
  - TC-FA-GRP-671
  - TC-FA-GRP-672
coverage:
  web: automated
---

# Tab Users Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- N = jumlah user Warehouse A dari angka Total User Warehouse A pada Groups List, dicatat sebelum download.
- Kemampuan teknis (disediakan tim FE): membaca berkas yang terunduh (nama berkas, baris header, dan jumlah baris data) lewat penangkap unduhan browser. Isi sel berkas diasersi di spec 191.
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): `Fixture.groupsTabUsers.irisanKeyword` dan `Fixture.groupsTabUsers.irisanPosition` (beririsan pada sedikitnya satu baris dan kurang dari N baris).
- State yang diubah spec: kolom Email di-hide lalu di-unhide; dipulihkan lewat hook `after` (hapus preferensi kolom di browser).

## Test Steps

1. Catat angka Total User Warehouse A sebagai N
2. Klik angka Total User Warehouse A

### TC-669: Download seluruh data

3. Klik icon Download
4. Pilih Download as CSV
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Group-Users.csv` terunduh
7. Verifikasi berkas memuat seluruh baris (N baris data, semua halaman, bukan hanya halaman aktif)

### TC-670: Download dengan Search dan Filter aktif

8. Ketik Search `Fixture.groupsTabUsers.irisanKeyword`, tekan Enter
9. Klik icon Filter, pilih `Fixture.groupsTabUsers.irisanPosition` pada Position, klik [Apply]
10. Klik icon Download
11. Pilih Download as XLSX
12. Verifikasi tidak ada toast sukses
13. Verifikasi berkas `Group-Users.xlsx` terunduh
14. Verifikasi berkas hanya berisi baris yang match kondisi aktif (jumlah baris data sama dengan jumlah baris hasil tabel)
15. Buka Filter, klik [Clear Field], klik [Apply]
16. Klik `(←)` pada kotak Search

### TC-671: Kolom yang di-hide tidak ikut ter-export

17. Hide kolom Email via Column Visibility
18. Klik icon Download
19. Pilih Download as CSV
20. Verifikasi tidak ada toast atau peringatan tambahan
21. Verifikasi berkas tidak memuat kolom Email
22. Verifikasi kolom lain pada berkas sesuai urutan tampilan

### TC-672: Kolom yang di-unhide kembali ikut ter-export

23. Tampilkan kembali kolom Email via Column Visibility
24. Klik icon Download
25. Pilih Download as CSV
26. Verifikasi berkas kembali memuat kolom Email

## Notes

- Langkah penghubung (S-03): mencatat N, mengosongkan Filter dan Search setelah TC-670, dan menampilkan kembali kolom Email (TC-672 langkah 3 "Hide lalu tampilkan kembali": hide sudah dilakukan pada TC-671; spec menampilkan kembali saja).
- Asersi absence toast sukses diletakkan segera setelah pemicu pilihan format dan didahului `Verifikasi` berkas terunduh sebagai anchor positif pada langkah sesudahnya (8b butir 11).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-669 "seluruh baris" tidak menyebut cara mengetahui jumlah total; spec memakai angka Total User Warehouse A sebagai N. TC-672 langkah 3 mengulang Hide sebelum Unhide; spec mengikuti urutan state (Email sudah di-hide oleh TC-671).
