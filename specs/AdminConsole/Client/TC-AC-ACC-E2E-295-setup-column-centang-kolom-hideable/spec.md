---
id: TC-AC-ACC-E2E-295-setup-column-centang-kolom-hideable
title: "Setup Column Client List: Centang dan Hapus Centang Sepuluh Kolom Hideable, Simpan, dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-688
coverage:
  web: automated
---

# Setup Column Client List: Centang dan Hapus Centang Sepuluh Kolom Hideable, Simpan, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Tabel parameter kolom Hideable (dipakai langkah 1 sampai 9): Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, Last Updated.
- Kemampuan teknis: menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Centang dan hapus centang kolom Hideable (TC-AC-ACC-688)

1. Untuk setiap kolom pada tabel parameter: klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Hapus centang kolom itu
3. Verifikasi kolom itu masih tampil di tabel di balik modal sebelum [Save] (perubahan baru berlaku setelah [Save], D-065)
4. Klik `[Save]`
5. Verifikasi kolom itu hilang dari tabel
6. Tekan F5
7. Verifikasi kolom itu tetap hilang
8. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, centang kembali kolom itu, lalu klik `[Save]`
9. Verifikasi kolom itu tampil kembali di tabel

## Notes

- Langkah 1 sampai 9 diulang per kolom (10 iterasi). Spec melewati sekitar 35 langkah setelah ekspansi; alasan: satu TC dengan satu kelas harness dan dataset, iterasi tidak saling bergantung.
- Post Condition TC (`Konfigurasi kolom List kembali ke default lewat [Reset to Default] lalu [Save]`) dipenuhi oleh hook `after` lewat penghapusan preferensi (bagian 4); tiap iterasi sudah mengembalikan kolom ke tercentang.
- Keselarasan TC dan spec
  - TC-AC-ACC-688: TC sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065 (tabel di balik popup tidak berubah sampai [Save]); spec dan TC sama. langkah 3 mengasersi kolom masih tampil dan hilangnya kolom diasersi setelah [Save] (langkah 5). TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. Lihat juga Temuan di spec 294. Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation).
