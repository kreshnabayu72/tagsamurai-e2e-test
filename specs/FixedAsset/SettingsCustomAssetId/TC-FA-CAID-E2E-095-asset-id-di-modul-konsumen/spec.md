---
id: TC-FA-CAID-E2E-095-asset-id-di-modul-konsumen
title: "Asset ID di Daftar Modul Konsumen: Available, Borrow, Damaged, Missing, Disposal, Assignment, Transfer"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-297
coverage:
  web: automated
---

# Asset ID di Daftar Modul Konsumen: Available, Borrow, Damaged, Missing, Disposal, Assignment, Transfer

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Consumers (Pre-setup No 31; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_CONSUMERS_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di tab itu.
- Data Pre-setup: Company Consumers (No 31), di-seed hook `before`: aset C1 Available, C2 Borrowed, C3 Damaged, C4 Missing, C5 pada laporan Disposal, C6 pada Assignment, C7 pada tiket Transfer dengan Asset ID `JKT/LAP/T490/0926/1` sampai `JKT/LAP/T490/0926/7`, dengan Separator Slash.
- Surface yang diuji (urutan langkah 3 sampai 22):

| Aset | Surface | Asset ID baru |
|---|---|---|
| C1 | Fixed Asset > Available | `JKT-LAP-T490-0926-1` |
| C2 | Fixed Asset > Borrow | `JKT-LAP-T490-0926-2` |
| C3 | Fixed Asset > Damaged | `JKT-LAP-T490-0926-3` |
| C4 | Fixed Asset > Missing | `JKT-LAP-T490-0926-4` |
| C5 | Fixed Asset > Transactions > Disposal | `JKT-LAP-T490-0926-5` |
| C6 | Fixed Asset > Transactions > Assignment | `JKT-LAP-T490-0926-6` |
| C7 | Fixed Asset > Transactions > Transfer (tabel aset tiket) | `JKT-LAP-T490-0926-7` |

- Data Dinamis: tidak ada; Separator Company Consumers diubah ke `- (Dash)` dan dipulihkan hook `after`.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: konfigurasi singleton Company Consumers (Separator) diubah; hook `after` memulihkan Company Consumers ke seed awal dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih Separator `- (Dash)` lalu klik `[Save]`
2. Tunggu aksi selesai
3. Buka Fixed Asset > Available
4. Ketik Search `JKT-LAP-T490-0926-1`, tekan Enter
5. Verifikasi Available menampilkan Asset ID `JKT-LAP-T490-0926-1` untuk C1
6. Buka Fixed Asset > Borrow
7. Ketik Search `JKT-LAP-T490-0926-2`, tekan Enter
8. Verifikasi Borrow menampilkan Asset ID `JKT-LAP-T490-0926-2` untuk C2
9. Buka Fixed Asset > Damaged
10. Ketik Search `JKT-LAP-T490-0926-3`, tekan Enter
11. Verifikasi Damaged menampilkan Asset ID `JKT-LAP-T490-0926-3` untuk C3
12. Buka Fixed Asset > Missing
13. Ketik Search `JKT-LAP-T490-0926-4`, tekan Enter
14. Verifikasi Missing menampilkan Asset ID `JKT-LAP-T490-0926-4` untuk C4
15. Buka Fixed Asset > Transactions > Disposal
16. Ketik Search `JKT-LAP-T490-0926-5`, tekan Enter
17. Verifikasi Disposal menampilkan Asset ID `JKT-LAP-T490-0926-5` untuk C5
18. Buka Fixed Asset > Transactions > Assignment
19. Ketik Search `JKT-LAP-T490-0926-6`, tekan Enter
20. Verifikasi Assignment menampilkan Asset ID `JKT-LAP-T490-0926-6` untuk C6
21. Buka Fixed Asset > Transactions > Transfer dan perhatikan tabel aset tiket C7
22. Verifikasi Transfer menampilkan Asset ID `JKT-LAP-T490-0926-7` untuk C7

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Langkah 3 sampai 22 mengulang pola buka surface, cari aset, lalu verifikasi untuk tujuh surface pada tabel "Surface yang diuji"; parameter tiap iterasi ada di tabel itu.
- Langkah penghubung: langkah 2 (tunggu aksi selesai sebelum pindah surface), 4, 7, 10, 13, 16, 19 (Search untuk menemukan baris target, R-16), 21 (perhatikan).
- Temuan untuk QA:
  - TC-FA-CAID-297 menulis "cari C1" sampai "cari C6" tanpa kata kunci pencarian; spec memakai Asset ID baru sebagai kata kunci Search.
  - Email akun Total Control Company Consumers tidak tertulis di Pre-setup TC.
  - TC-FA-CAID-297 tidak menyebut Expected toast `[Save]`; hasil Save teramati lewat Asset ID di tiap surface.
