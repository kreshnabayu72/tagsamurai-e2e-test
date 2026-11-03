---
id: TC-FA-RP-E2E-151-tab-total-control-download-1
title: "Tab Total Control: Download (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-519
  - TC-FA-RP-520
  - TC-FA-RP-521
coverage:
  web: automated
---

# Tab Total Control: Download (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Division `Finance` untuk Fitri Handayani dan Rudi Hartono) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembaca berkas unduhan (CSV dan XLSX) untuk langkah "Buka file", disediakan tim FE. Asersi hanya nama berkas, nama kolom, dan baris yang ada; isi sel tidak diasersi.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

## Test Steps

### Download tanpa Search atau Filter (TC 519)

1. Klik ikon Download.
2. Klik `Download as CSV`.
3. Verifikasi tidak ada toast sukses.
4. Verifikasi berkas `Role-Permission-Total-Control.csv` terunduh.
5. Buka file.
6. Verifikasi berkas memuat kolom Name, Position, Division, Status, Modified By, Last Updated untuk seluruh baris (sembilan baris Pre-setup #36).

### Download dengan Search dan Filter aktif (TC 520)

7. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
8. Klik ikon Search, ketik Search `Fina`, tekan Enter.
9. Klik ikon Filter, pilih opsi `Finance` pada field Division, lalu klik `[Apply]`.
10. Klik ikon Download, lalu klik `Download as XLSX`.
11. Verifikasi berkas `Role-Permission-Total-Control.xlsx` terunduh.
12. Buka file.
13. Verifikasi berkas hanya memuat baris Fitri Handayani dan Rudi Hartono.
14. Klik `✕` pada Search, tekan Enter.
15. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`.

### Kolom yang disembunyikan tidak ikut diekspor (TC 521)

16. Sembunyikan kolom `Division` lewat Setup Column, lalu klik `[Save]`.
17. Klik ikon Download, lalu klik `Download as CSV`.
18. Buka file.
19. Verifikasi berkas memuat kolom yang sedang tampil: Name, Position, Status, Modified By, Last Updated.
20. Verifikasi berkas tidak memuat kolom `Division`.
21. Tampilkan kembali kolom `Division` lewat Setup Column, lalu klik `[Save]`.

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Langkah penghubung (S-03): langkah 1, 2, 5, 8, 9, 10, 12, 14 sampai 18, dan 21. Langkah 14, 15, dan 21 membersihkan Search, filter, dan kolom sebelum TC berikutnya (S-09). Langkah 3 mengikuti 8b butir 11: absence toast sukses diletakkan segera sesudah pemicu (langkah 2) dengan berkas terunduh (langkah 4) sebagai anchor positif.
- Langkah 7 adalah pembanding positif untuk asersi universal langkah 13; langkah 19 adalah pembanding positif untuk asersi absence langkah 20.
- Temuan untuk QA:
  - Isi sel berkas (BOM, escape, sel kosong) tidak diasersi di spec ini.
