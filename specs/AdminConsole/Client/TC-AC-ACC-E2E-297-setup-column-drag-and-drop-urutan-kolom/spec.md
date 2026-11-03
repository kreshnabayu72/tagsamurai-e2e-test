---
id: TC-AC-ACC-E2E-297-setup-column-drag-and-drop-urutan-kolom
title: "Setup Column Client List: Drag and Drop Urutan Kolom Hideable dan Curated, Simpan, dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-690
  - TC-AC-ACC-691
coverage:
  web: automated
---

# Setup Column Client List: Drag and Drop Urutan Kolom Hideable dan Curated, Simpan, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Tabel parameter drag Hideable (dipakai langkah 2 sampai 4, diseret berurutan ke posisi pertama): Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated, Company Name.
- Tabel parameter drag Curated (dipakai langkah 10 sampai 12, diseret berurutan ke posisi pertama): City, State, Country, Industry, PIC Phone, PIC Email, Company Email.
- Kemampuan teknis: drag and drop pada modal Setup Column; menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Drag and drop kolom Hideable (TC-AC-ACC-690)

1. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Untuk setiap kolom pada tabel parameter drag Hideable: seret kolom itu ke posisi pertama daftar kolom
3. Verifikasi kolom itu berada di posisi pertama pada daftar kolom modal
4. Verifikasi urutan header tabel di balik modal belum berubah dari sebelum seretan (urutan baru berlaku setelah [Save], D-065)
5. Klik `[Save]`, lalu tekan F5
6. Verifikasi urutan header tersimpan: Company Name, Last Updated, Modified By, SIEM, SAMS, FAMS, Group, Managed By, PIC Name, Client Code
7. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]` (pemulihan urutan)

### Drag and drop kolom Curated (TC-AC-ACC-691)

8. Klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
9. Centang Company Email, PIC Email, PIC Phone, Industry, Country, State, dan City
10. Untuk setiap kolom pada tabel parameter drag Curated: seret kolom itu ke posisi pertama daftar kolom
11. Verifikasi kolom itu berada di posisi pertama pada daftar kolom modal
12. Verifikasi urutan header tabel di balik modal belum berubah dari sebelum seretan (urutan baru berlaku setelah [Save], D-065)
13. Klik `[Save]`, lalu tekan F5
14. Verifikasi urutan header tersimpan: Company Email, PIC Email, PIC Phone, Industry, Country, State, City, Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated
15. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]` (pemulihan urutan dan visibilitas)

## Notes

- Langkah 2 sampai 4 (10 iterasi) dan 10 sampai 12 (7 iterasi) diulang per kolom. Spec melewati sekitar 35 langkah setelah ekspansi; alasan: semua blok satu kelas harness dan dataset (Setup Column List); blok kedua memulai dari konfigurasi default hasil pemulihan blok pertama dan kegagalan blok pertama tidak membuat blok kedua kehilangan makna.
- Langkah penghubung (S-03): `[Reset to Default]` lalu `[Save]` memulihkan urutan sesuai Post Condition TC.
- Keselarasan TC dan spec
  - TC-AC-ACC-690 (Expected a sampai j) dan TC-AC-ACC-691 (Expected a sampai g) sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065; spec dan TC sama: untuk tiap kolom yang diseret, kolom berada di posisi pertama pada daftar kolom modal (langkah 3 dan 11) dan urutan header tabel di balik modal belum berubah sebelum [Save] (langkah 4 dan 12); urutan baru diasersi setelah [Save] dan F5 (langkah 6 dan 14). Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation). Lihat juga catatan di spec 294.
