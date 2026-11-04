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
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); semuanya hanya dibaca. Target aksi tulis adalah replika milik spec di bawah.
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; seed di hook `before`, cleanup di hook `after`; S-06, S-12): `PT Sejahtera Abadi {runId}-007` (setara C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, FAMS, SAMS, SIEM Active) adalah target aksi tulis sesuai TC; efek: PIC Name diubah, Modified By menjadi `Andi Wijaya`, Last Updated berubah, dan Changelog replika bertambah satu baris `Edit`, hanya pada data milik spec ini. Client `PT Sejahtera Abadi` (C-01) tidak disentuh.
- Data uji: PIC Name 100 karakter `Bambang Hartono Wijayakusuma Pratama Santoso Nugroho Setiawan Mahendra Prasetyo Anggoro Saputra Joko`.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-18: Kolom Client Code dan PIC Name tampil sebagai teks biasa dengan nama panjang tidak dipotong

1. Ketik Search `PT Sejahtera Abadi {runId}-007`, tekan Enter
2. Buka `⋯` baris `PT Sejahtera Abadi {runId}-007`, lalu klik `Edit`
3. Ubah PIC Name menjadi `Bambang Hartono Wijayakusuma Pratama Santoso Nugroho Setiawan Mahendra Prasetyo Anggoro Saputra Joko`, lalu klik `[Save]`
4. Tunggu aksi `[Save]` selesai (popup Edit tertutup)
5. Muat ulang halaman, ketik Search `PT Sejahtera Abadi {runId}-007`, tekan Enter
6. Lihat sel PIC Name dan sel Client Code baris `PT Sejahtera Abadi {runId}-007`
7. Verifikasi PIC Name tampil utuh (tidak dipotong)
8. Verifikasi tidak ada tooltip pada PIC Name
9. Verifikasi kolom `PIC Name` melebar mengikuti konten
10. Verifikasi Client Code replika (nilai sesuai seed Fixture BE) tampil sebagai teks biasa tanpa link
11. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 4, 11. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: kolom PIC Name dan Client Code lain ada di spec 003 (isi sel) dan 001 (screening).
- Temuan untuk QA:
  - TC-AC-ACC-18: Post Condition (kembalikan PIC Name ke nilai semula lewat Edit) tidak dijalankan: target adalah replika milik spec yang dibersihkan hook `after`, sehingga langkah mencatat PIC Name awal dan memulihkannya tidak ada.
  - TC-AC-ACC-18 Expected b menyebut Client Code `SJA-001`, yaitu kode C-01 yang unik dan tidak dapat disalin ke replika; spec mengasersi Client Code replika (nilai dari seed Fixture BE) tampil sebagai teks biasa tanpa link dan tidak mengasersi nilai `SJA-001`.
  - TC-AC-ACC-18: Expected tidak menyebut toast hasil `[Save]`; spec tidak mengasersi toast dan memakai langkah penghubung "Tunggu aksi selesai" sebelum muat ulang.
