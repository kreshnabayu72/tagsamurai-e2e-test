---
id: TC-AC-ACC-E2E-298-setup-column-pin-kolom-membeku-saat-scroll
title: "Setup Column Client List: Pin dan Unpin Kolom Hideable dan Curated Membekukan Kolom Saat Scroll Horizontal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-692
  - TC-AC-ACC-693
coverage:
  web: automated
---

# Setup Column Client List: Pin dan Unpin Kolom Hideable dan Curated Membekukan Kolom Saat Scroll Horizontal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Tabel parameter kolom Hideable (langkah 1 sampai 8): Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated. Tabel parameter kolom Curated (langkah 9 sampai 16): Company Email, PIC Email, PIC Phone, Industry, Country, State, City.
- Kemampuan teknis: mengubah ukuran jendela browser (viewport) hingga tabel memiliki scroll horizontal dan memulihkannya; menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Pin kolom Hideable (TC-AC-ACC-692)

1. Untuk setiap kolom pada tabel parameter Hideable: klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik ikon Pin pada kolom itu, lalu klik `[Save]`
2. Perkecil lebar jendela hingga tabel memiliki scroll horizontal, lalu scroll tabel ke kanan
3. Verifikasi kolom itu tetap terlihat di sisi kiri tabel (setelah kolom Checkbox) saat tabel di-scroll ke kanan
4. Tekan F5 lalu scroll tabel ke kanan
5. Verifikasi kolom itu tetap terlihat di sisi kiri tabel setelah F5
6. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik ikon Pin pada kolom itu (unpin), lalu klik `[Save]`
7. Scroll tabel ke kanan
8. Verifikasi kolom itu ikut bergeser bersama kolom lain setelah di-unpin

### Pin kolom Curated (TC-AC-ACC-693)

9. Untuk setiap kolom pada tabel parameter Curated: klik header kolom Actions `(⋯)`, klik `Setup Column...`, centang kolom itu, klik ikon Pin pada kolom itu, lalu klik `[Save]`
10. Perkecil lebar jendela hingga tabel memiliki scroll horizontal, lalu scroll tabel ke kanan
11. Verifikasi kolom itu tetap terlihat di sisi kiri tabel (setelah kolom Checkbox) saat tabel di-scroll ke kanan
12. Tekan F5 lalu scroll tabel ke kanan
13. Verifikasi kolom itu tetap terlihat di sisi kiri tabel setelah F5
14. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, unpin kolom itu, hapus centang kolom itu, lalu klik `[Save]`
15. Scroll tabel ke kanan
16. Verifikasi kolom itu hilang dari tabel

### Pemulihan viewport

17. Pulihkan lebar jendela browser ke ukuran semula

## Notes

- Langkah 1 sampai 8 (10 iterasi) dan 9 sampai 16 (7 iterasi) diulang per kolom. Spec melewati sekitar 35 langkah setelah ekspansi; alasan: semua blok satu kelas harness dan dataset (Setup Column List/pin), iterasi tidak saling bergantung.
- Expected TC-AC-ACC-692 `setelah di-unpin ikut bergeser bersama kolom lain` dan TC-AC-ACC-693 `setelah di-unpin dan dilepas centangnya kolom hilang dari tabel` masing-masing satu `Verifikasi`. Langkah `Pulihkan lebar jendela` adalah langkah penghubung (S-03, S-09).
- Temuan untuk QA
  - TC-AC-ACC-692, 693: ukuran jendela `diperkecil` tidak punya nilai piksel; spec membiarkan tim FE menetapkan lebar yang memunculkan scroll horizontal (Prerequisites).
