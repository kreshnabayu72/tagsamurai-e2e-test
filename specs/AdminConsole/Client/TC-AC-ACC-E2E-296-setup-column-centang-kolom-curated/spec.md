---
id: TC-AC-ACC-E2E-296-setup-column-centang-kolom-curated
title: "Setup Column Client List: Centang dan Hapus Centang Tujuh Kolom Curated, Simpan, dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-689
coverage:
  web: automated
---

# Setup Column Client List: Centang dan Hapus Centang Tujuh Kolom Curated, Simpan, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Tabel parameter kolom Curated (dipakai langkah 1 sampai 10): Company Email, PIC Email, PIC Phone, Industry, Country, State, City.
- Kemampuan teknis: menghapus preferensi Setup Column di browser (disediakan tim FE). Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Centang dan hapus centang kolom Curated (TC-AC-ACC-689)

1. Untuk setiap kolom pada tabel parameter: klik header kolom Actions `(⋯)` lalu klik `Setup Column...`
2. Verifikasi kolom itu belum tampil di tabel sebelum dicentang
3. Centang kolom itu
4. Verifikasi kolom itu masih belum tampil di tabel di balik modal sebelum [Save] (perubahan baru berlaku setelah [Save], D-065)
5. Klik `[Save]`
6. Verifikasi kolom itu tampil di tabel
7. Tekan F5
8. Verifikasi kolom itu tetap tampil
9. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, hapus centang kolom itu, lalu klik `[Save]`
10. Verifikasi kolom itu hilang kembali dari tabel

## Notes

- Langkah 1 sampai 10 diulang per kolom (7 iterasi). Spec melewati sekitar 35 langkah setelah ekspansi; alasan: satu TC dengan satu kelas harness dan dataset, iterasi tidak saling bergantung.
- Post Condition TC dipenuhi tiap iterasi (kolom dikembalikan Hidden) dan hook `after`.
- Keselarasan TC dan spec
  - TC-AC-ACC-689: TC sudah diselaraskan pada 2026-11-03 sesuai `docs/spec-decisions.md` D-065 (tabel di balik popup tidak berubah sampai [Save]); spec dan TC sama. langkah 4 mengasersi kolom masih belum tampil dan tampilnya kolom diasersi setelah [Save] (langkah 6). TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. Sisa konflik hanya `prd-conventions.md` §9.3 (di luar scope suite, dilaporkan ke pemilik foundation).
