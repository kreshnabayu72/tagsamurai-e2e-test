---
id: TC-AC-ACC-E2E-293-sort-tujuh-kolom-hidden-default
title: "Sort Client List: Siklus Tiga State pada Tujuh Kolom Curated Setelah Di-unhide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-404
coverage:
  web: automated
---

# Sort Client List: Siklus Tiga State pada Tujuh Kolom Curated Setelah Di-unhide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 `PT Sortir Alfa`, C-LST-2 `PT Sortir Beta`, dan C-LST-3 `PT Sortir Gamma` tersedia dan hanya dibaca; spec memakai Search `Sortir` agar hanya ketiganya yang tersisa.
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Tabel parameter kolom Curated (dipakai langkah 4 sampai 10; urutan ascending, descending adalah kebalikannya): Company Email: `PT Sortir Beta` (admin@sortirbeta.qwertysystem.net), `PT Sortir Gamma` (halo@sortirgamma.qwertysystem.net), `PT Sortir Alfa` (kontak@sortiralfa.qwertysystem.net); PIC Email: `PT Sortir Beta` (bagas@sortirbeta.qwertysystem.net), `PT Sortir Alfa` (hendra@sortiralfa.qwertysystem.net), `PT Sortir Gamma` (sari@sortirgamma.qwertysystem.net); PIC Phone: `PT Sortir Beta` (081300000010), `PT Sortir Gamma` (081300000020), `PT Sortir Alfa` (081300000030); Industry: `PT Sortir Alfa` (Healthcare), `PT Sortir Gamma` (Manufacturing), `PT Sortir Beta` (Retail); Country: `PT Sortir Beta` (Indonesia), `PT Sortir Alfa` (Malaysia), `PT Sortir Gamma` (Singapore); State: `PT Sortir Gamma` (Central Region), `PT Sortir Beta` (Jawa Barat), `PT Sortir Alfa` (Selangor); City: `PT Sortir Beta` (Bandung), `PT Sortir Alfa` (Shah Alam), `PT Sortir Gamma` (Singapore).
- Kemampuan teknis: menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Sort tujuh kolom Hidden default (TC-AC-ACC-404)

1. Ketik Search `Sortir`, tekan Enter
2. Verifikasi `PT Sortir Alfa`, `PT Sortir Beta`, dan `PT Sortir Gamma` tersisa di tabel
3. Klik header kolom Actions `(⋯)` lalu centang Company Email, PIC Email, PIC Phone, Industry, Country, State, dan City
4. Untuk setiap baris tabel parameter kolom Curated: klik header kolom itu satu kali lalu baca urutan baris
5. Verifikasi urutan ascending sesuai tabel parameter
6. Klik header kolom itu untuk kedua kali lalu baca urutan baris
7. Verifikasi urutan descending adalah kebalikan tabel parameter
8. Klik header kolom itu untuk ketiga kali lalu baca urutan baris
9. Verifikasi indikator sort kolom itu nonaktif
10. Verifikasi urutan kembali ke default Company Name A-Z: `PT Sortir Alfa`, `PT Sortir Beta`, `PT Sortir Gamma`
11. Klik header kolom Actions `(⋯)` lalu hapus centang Company Email, PIC Email, PIC Phone, Industry, Country, State, dan City, lalu klik `(←)` pada kotak Search

## Notes

- Langkah 4 sampai 10 diulang per baris tabel parameter (7 iterasi). Spec melewati sekitar 35 langkah setelah ekspansi; alasan: satu TC, satu kelas harness dan dataset, dan iterasi tidak saling bergantung.
- Langkah penghubung (S-03): centang dan hapus centang tujuh kolom adalah Langkah 2 TC dan Post Condition TC.
- Temuan untuk QA
  - TC-AC-ACC-404: Data Uji menyebut `lihat tabel Tabel A3 (seluruh nilai terisi, tanpa sel kosong)`; spec menyalin nilai dari Tabel A3 C-LST-1 sampai C-LST-3.
