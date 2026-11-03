---
id: TC-AC-ACC-E2E-287-filter-chip-dan-checkbox-sinkron
title: "Filter Client List: Sinkronisasi Chip dan Centang Opsi pada Dropdown Multi-select"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-714
  - TC-AC-ACC-715
coverage:
  web: automated
---

# Filter Client List: Sinkronisasi Chip dan Centang Opsi pada Dropdown Multi-select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 sampai C-LST-3 tersedia dan hanya dibaca.
- Tabel parameter field (dipakai langkah 2 sampai 9 dan 10 sampai 14): Partner (`CV Mitra Sejati`, `CV Mitra Lestari`); Distributor (`PT Distribusi Nusantara`, `PT Distribusi Timur`); FAMS (`Active`, `Grace`); SAMS (`Active`, `Grace`); SIEM (`Active`, `Grace`); Industry (`Healthcare`, `Retail`); Country (`Indonesia`, `Malaysia`); State (`Jawa Barat`, `Selangor`); City (`Bandung`, `Shah Alam`). Opsi pertama dan opsi kedua dipilih berurutan pada field itu.
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Hapus chip lewat tombol silang (TC-AC-ACC-714)

1. Klik Filter
2. Untuk setiap baris tabel parameter field: pilih opsi pertama lalu opsi kedua pada field itu
3. Klik tombol silang pada chip opsi pertama
4. Verifikasi chip opsi pertama hilang dari field
5. Verifikasi chip opsi kedua tetap ada
6. Buka dropdown field itu
7. Verifikasi opsi pertama tidak tercentang di dalam dropdown
8. Verifikasi opsi kedua tetap tercentang di dalam dropdown
9. Tutup dropdown lalu klik [Clear Field] (mengosongkan seluruh field Filter agar pilihan putaran sebelumnya tidak mempersempit opsi State dan City)

### Hapus centang opsi menghapus chip (TC-AC-ACC-715)

10. Untuk setiap baris tabel parameter field: pilih opsi pertama lalu opsi kedua pada field itu
11. Buka dropdown field itu dan hapus centang opsi pertama
12. Verifikasi chip opsi pertama hilang dari field
13. Verifikasi chip opsi kedua tetap ada
14. Tutup dropdown lalu klik [Clear Field], dan setelah iterasi terakhir klik ikon Filter untuk menutup panel

## Notes

- Langkah 2 sampai 9 dan 10 sampai 14 diulang per baris tabel parameter (9 iterasi tiap blok). Spec melewati sekitar 35 langkah setelah ekspansi; alasan: satu kelas harness dan satu dataset (dropdown Filter), kedua blok berurutan tanpa state bersama, kegagalan satu field tidak membuat field lain kehilangan makna.
- Langkah penghubung (S-03): [Clear Field] antar iterasi sesuai Langkah 5 TC (agar pilihan Country/State tidak mempersempit opsi State dan City).
- [Apply] tidak diklik di spec ini karena TC tidak meminta aksi Apply.
