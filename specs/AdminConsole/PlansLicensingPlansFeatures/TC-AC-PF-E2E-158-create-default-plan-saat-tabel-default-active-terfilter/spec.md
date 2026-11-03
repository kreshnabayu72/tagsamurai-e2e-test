---
id: TC-AC-PF-E2E-158-create-default-plan-saat-tabel-default-active-terfilter
title: Create Default Plan Baru Saat Tabel Default Active Masih Terfilter
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-334
coverage:
  web: automated
---

# Create Default Plan Baru Saat Tabel Default Active Masih Terfilter

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21) dengan SAMS kosong (tidak ada default plan SAMS), default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
- Data Dinamis: default plan SAMS Paid `Baru SAMS {runId}-158` (dibuat spec lewat `+ Default Plan`; nilai field wajib lain mengikuti isian bawaan form karena TC tidak menyebutnya); dihapus lewat fixture BE di hook `after`.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal dan menghapus default plan yang dibuat spec (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini menambah satu default plan dan memulihkannya di `after`; Last Updated dan entri Changelog Default yang timbul dari Create tidak dapat dihapus lewat UI dan dikembalikan oleh fixture BE.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Buka Filter Panel, pilih Product `FAMS`, klik `[Apply]`.
2. Verifikasi tabel menampilkan empat baris FAMS (`Starter`, `Growth`, `Professional`, `Enterprise`).
3. Buat default plan SAMS Paid `Baru SAMS {runId}-158` lewat `+ Default Plan`.
4. Kembali ke Plans & Licensing > Plans & Features > Default > Active.
5. Verifikasi baris `Starter` tampil di tabel.
6. Verifikasi tabel yang masih terfilter `FAMS` tidak menampilkan `Baru SAMS {runId}-158`.
7. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`.
8. Verifikasi `Baru SAMS {runId}-158` tampil di tabel.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 4 mengikuti Langkah Uji TC-AC-PF-334; langkah 7 menghapus filter sebagai bagian dari Expected TC ("setelah filter dihapus").
- Nama plan memakai suffix `{runId}-158` sesuai S-12; TC menulis `Baru SAMS`.
- Temuan untuk QA: (1) TC-AC-PF-334 langkah 2 hanya menulis "Buat default plan SAMS Paid `Baru SAMS` lewat `+ Default Plan`" tanpa isian field wajib lain (Template, fitur); spec memakai isian bawaan form. (2) Expected "Tabel yang masih terfilter `FAMS`" bertentangan dengan konvensi bagian 4 bila langkah 4 (kembali lewat sidebar) mereset Filter; langkah 5 mengasersi baris pembanding (`Starter`) alih-alih mengasumsikan filter masih aktif, sehingga langkah 6 tetap bermakna bila Filter tidak ter-reset. (3) Dataset Plan A dengan SAMS kosong dan "Dataset Plan S" (Pre-setup #31) memakai slot Free/Paid SAMS yang sama.
