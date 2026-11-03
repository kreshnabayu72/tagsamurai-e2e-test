---
id: TC-FA-RP-E2E-152-tab-total-control-download-2
title: "Tab Total Control: Download (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-522
  - TC-FA-RP-524
  - TC-FA-RP-526
coverage:
  web: automated
---

# Tab Total Control: Download (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`. Keyword `zzzz` untuk TC 526 tidak cocok dengan baris mana pun pada Pre-setup #36.
- Kemampuan teknis: pembaca berkas unduhan (CSV dan XLSX) untuk langkah "Buka file", disediakan tim FE. Asersi hanya nama berkas, nama kolom, dan baris yang ada; isi sel tidak diasersi.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Kolom yang ditampilkan kembali ikut diekspor (TC 522)

1. Sembunyikan kolom `Division` lewat Setup Column, lalu klik `[Save]`.
2. Tampilkan kembali kolom `Division` lewat Setup Column, lalu klik `[Save]`.
3. Klik ikon Download, lalu klik `Download as CSV`.
4. Buka file.
5. Verifikasi berkas memuat kembali kolom `Division` yang tadi disembunyikan.

### Extension berkas mengikuti pilihan format (TC 524)

6. Klik ikon Download, lalu klik `Download as CSV`.
7. Verifikasi berkas `Role-Permission-Total-Control.csv` terunduh untuk pilihan CSV.
8. Klik ikon Download, lalu klik `Download as XLSX`.
9. Verifikasi berkas `Role-Permission-Total-Control.xlsx` terunduh untuk pilihan XLSX.

### Download dengan nol baris (TC 526)

10. Klik ikon Search, ketik Search `zzzz`, tekan Enter.
11. Verifikasi tabel menampilkan empty state `No results found`.
12. Verifikasi tombol Download tetap aktif.
13. Klik ikon Download, lalu klik `Download as CSV`.
14. Buka file.
15. Verifikasi berkas hanya memuat baris header kolom.
16. Klik `✕` pada Search, tekan Enter.

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 3, 4, 6, 8, 10, 13, 14, dan 16. Langkah 1 dan 2 adalah aksi TC 522 (sembunyikan lalu tampilkan kembali); langkah 16 mengosongkan Search (S-09).
- Langkah 11 memakai empty state `No results found` sebagai anchor positif bahwa pencarian selesai sebelum asersi tombol Download dan isi berkas.
- Temuan untuk QA:
  - TC 522 bergantung pada TC 521 (kolom `Division` sudah tersembunyi); spec ini menjalankan sembunyikan lalu tampilkan sendiri dari state awal Pre-setup (kolom `Division` tampil), sehingga tidak bergantung pada spec lain (S-06).
  - TC 526 mengasersi berkas CSV "hanya memuat baris header kolom"; nama kolom yang diharapkan tidak dirinci di TC (kolom yang sedang tampil: Name, Position, Division, Status, Modified By, Last Updated menurut TC 519).
