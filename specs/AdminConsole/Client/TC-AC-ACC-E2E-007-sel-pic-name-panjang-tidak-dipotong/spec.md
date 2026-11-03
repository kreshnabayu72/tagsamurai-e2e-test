---
id: TC-AC-ACC-E2E-007-sel-pic-name-panjang-tidak-dipotong
title: "Sel PIC Name 100 Karakter Tampil Utuh dan Client Code Teks Biasa pada List Client"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-18
coverage:
  web: automated
---

# Sel PIC Name 100 Karakter Tampil Utuh dan Client Code Teks Biasa pada List Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Client `PT Sejahtera Abadi` (C-01, Pre-setup) adalah target aksi tulis sesuai TC (S-06: TC mensyaratkan Client ini, Client Code `SJA-001`); efek: PIC Name diubah lalu dipulihkan, Modified By menjadi `Andi Wijaya`, Last Updated berubah, dan Changelog Client bertambah dua baris `Edit`. Pemulihan nilai awal dilakukan langkah spec dan hook `after` lewat Fixture BE bila spec gagal di tengah.
- Data uji: PIC Name 100 karakter `Bambang Hartono Wijayakusuma Pratama Santoso Nugroho Setiawan Mahendra Prasetyo Anggoro Saputra Joko`.
- PIC Name awal `PT Sejahtera Abadi` dicatat langkah spec sebelum diubah sebagai nilai pemulihan (setara Old Value baris Changelog `Edit` yang disebut Post Condition TC).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-18: Kolom Client Code dan PIC Name tampil sebagai teks biasa dengan nama panjang tidak dipotong

1. Ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Catat PIC Name awal baris `PT Sejahtera Abadi` (nilai pemulihan)
3. Buka `⋯` baris `PT Sejahtera Abadi`, lalu klik `Edit`
4. Ubah PIC Name menjadi `Bambang Hartono Wijayakusuma Pratama Santoso Nugroho Setiawan Mahendra Prasetyo Anggoro Saputra Joko`, lalu klik `[Save]`
5. Tunggu aksi `[Save]` selesai (popup Edit tertutup)
6. Muat ulang halaman, ketik Search `PT Sejahtera Abadi`, tekan Enter
7. Lihat sel PIC Name dan sel Client Code baris `PT Sejahtera Abadi`
8. Verifikasi PIC Name tampil utuh (tidak dipotong)
9. Verifikasi tidak ada tooltip pada PIC Name
10. Verifikasi kolom `PIC Name` melebar mengikuti konten
11. Verifikasi Client Code `SJA-001` tampil sebagai teks biasa tanpa link
12. Buka `⋯` baris `PT Sejahtera Abadi`, klik `Edit`, kembalikan PIC Name ke nilai awal yang dicatat, klik `[Save]`, lalu tunggu popup Edit tertutup
13. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 12, 13. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: kolom PIC Name dan Client Code lain ada di spec 003 (isi sel) dan 001 (screening).
- Temuan untuk QA:
  - TC-AC-ACC-18: Post Condition merujuk "Old Value baris Changelog `Edit` hasil langkah 3" untuk nilai pemulihan, tetapi tidak ada langkah membuka Changelog; spec mencatat PIC Name awal langsung dari sel tabel sebelum Edit sebagai nilai pemulihan (hasil sama).
  - TC-AC-ACC-18: Expected tidak menyebut toast hasil `[Save]`; spec tidak mengasersi toast dan memakai langkah penghubung "Tunggu aksi selesai" sebelum muat ulang.
