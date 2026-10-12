---
id: TC-GS-BRAND-E2E-045-used-by-items-angka-besar-1250
title: "Angka Besar Used By (Items) Tampil Apa Adanya dan Terurut Numerik"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-279
coverage:
  web: automated
---

# Angka Besar Used By (Items) Tampil Apa Adanya dan Terurut Numerik

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi); password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` (seedSession).
- Data Pre-setup (tetap di environment): 12 brand Client A; Vertex Labs memiliki Used By `5`.
- Data Dinamis (di-seed lewat API di hook `before`, fixture belum ada; tim FE menyiapkan):
  - D-39: brand `Ten Co {runId}-045` dipakai 10 Asset Name FAMS.
  - D-40: brand `Big Co {runId}-045` dipakai 1250 Asset Name FAMS (fixture backend).
  - Pembersihan di hook `after`: hapus Asset Name FAMS fixture, lalu hapus kedua brand; tidak berasumsi seeding berhasil penuh.
- Total tabel pada spec ini 14 brand (12 Pre-setup + Ten Co + Big Co).
- State global: tidak ada yang diubah. Page size dan sort tabel (preferensi UI) dikembalikan ke default (10 per halaman, urutan default) di hook `after`.
- Hook `beforeEach`: kembali ke layar Global Settings > Master Reference > Brand.
- Kemampuan teknis: seeding 1250 Asset Name FAMS lewat API/fixture backend dalam waktu wajar.

## Test Steps

1. Buka layar Global Settings > Master Reference > Brand

### TC-GS-BRAND-279: Angka besar pada Used By (Items) tampil apa adanya tanpa pemisah ribuan dan terurut numerik

2. Search `Big Co {runId}-045`, tekan Enter
3. Perhatikan Used By (Items) baris Big Co {runId}-045
4. Verifikasi Used By (Items) Big Co {runId}-045 bernilai `1250` (tanpa pemisah ribuan, tidak terpotong)
5. Hapus keyword Search, tekan Enter
6. Ubah page size 25 agar seluruh brand tampil dalam satu halaman
7. Klik header Used By (Items) sekali (ascending)
8. Amati posisi Big Co {runId}-045 terhadap Ten Co {runId}-045 (`10`) dan Vertex Labs (`5`)
9. Verifikasi ascending: Big Co {runId}-045 berada setelah Ten Co {runId}-045 dan Vertex Labs (urutan numerik, bukan leksikografis)
10. Klik angka `1250` pada baris Big Co {runId}-045
11. Verifikasi Total Item di Modal Brand Detail Big Co {runId}-045 bernilai `1250`

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Dependensi "Disiapkan sebelum TC-GS-BRAND-279" dipenuhi oleh seeding Ten Co dan Big Co di hook `before` spec ini. Nama Ten Co memakai nomor spec (`{runId}-045`) karena nama yang sama dipakai spec `TC-GS-BRAND-E2E-038-sort-brand-name-used-by-dan-last-updated`.
- Langkah penghubung: langkah 2 (Search untuk menemukan baris Big Co) dan langkah 5 (menghapus keyword Search supaya seluruh brand tampil pada sort Used By (Items)).
