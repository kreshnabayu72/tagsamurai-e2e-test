---
id: TC-FA-TDC-E2E-011-aksesibilitas-fokus-ter-trap-dialog-d-09-d-10-dan-d-12
title: "Aksesibilitas Fokus Ter-trap Dialog D-09, D-10, dan D-12"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-293
coverage:
  web: automated
---

# Aksesibilitas Fokus Ter-trap Dialog D-09, D-10, dan D-12

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, dibersihkan di `after`; kunci `khsV1` dan `khsC1`): class `KHS-V1-{runId}-011` (satu versi, Used By 0) dan class `KHS-C1-{runId}-011` (memiliki versi Scheduled Effective From Jan 2027), di atas tujuh class seed bawaan sehingga tabel berisi 9 baris pada satu halaman (page size default 10), dan baris dicari tanpa Search. Nilai Useful Life baru untuk `KHS-V1-{runId}-011` ditetapkan fixture (TC tidak menyebut nilainya).
- Kemampuan teknis: seeding class dan versi Scheduled lewat API; mengosongkan tabel (seluruh class) lewat seeding API dan memulihkan tujuh class seed (`suite.md`); menekan `Tab` berulang dan `Esc`; mengamati posisi fokus; menutup Drawer dirty lewat `[×]` dan `[Leave]` (S-08).
- State global yang diubah: jam server dan browser, serta isi tabel (dikosongkan untuk D-12); dipulihkan di hook `after` (jam dipulihkan, tujuh class seed dipulihkan). Spec berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-293: Accessibility dialog D-09, D-10, dan D-12 — fokus ter-trap dan Esc menutup

1. Klik link Class Code `KHS-V1-{runId}-011`
2. Ubah Useful Life menjadi nilai berbeda dari nilai tersimpan
3. Klik `[Save]` sehingga dialog D-09 muncul
4. Tekan Tab berulang
5. Verifikasi D-09: fokus berputar di dalam dialog (Select Effective From, `[Cancel]`, `[Apply]`)
6. Tekan Esc
7. Verifikasi dialog D-09 tertutup
8. Klik `[×]` pada header Drawer
9. Verifikasi dialog `Unsaved Changes` tampil
10. Klik `[Leave]`
11. Klik link Class Code `KHS-C1-{runId}-011`
12. Klik `[Cancel scheduled version]` pada Alert sehingga dialog D-10 muncul
13. Tekan Tab berulang
14. Verifikasi D-10: fokus berputar di dalam dialog (`[Back]`, `[Cancel version]`)
15. Tekan Esc
16. Verifikasi dialog D-10 tertutup
17. Klik `[×]` pada header Drawer
18. Kosongkan tabel (seluruh class) lewat seeding API, lalu muat ulang halaman
19. Klik `Restore default classes` pada Empty State sehingga dialog D-12 muncul
20. Tekan Tab berulang
21. Verifikasi D-12: fokus berputar di dalam dialog (`[Cancel]`, `[Restore]`)
22. Tekan Esc
23. Verifikasi dialog D-12 tertutup

## Notes

- Langkah penghubung (S-03): langkah 8 sampai 10 dan 17 (menutup Drawer; S-08, langkah 17 tanpa dialog karena form tidak diubah), dan langkah 18 (mengosongkan tabel pada "sesi terpisah" sesuai precondition TC; dibuat lewat seeding API, tidak diasersi).
- Klausa "Esc menutup dialog" pada Expected a, b, dan c masing-masing satu `Verifikasi` (langkah 7, 16, 23); klausa fokus berputar satu `Verifikasi` per dialog (langkah 5, 14, 21).
- Tidak ada `Verifikasi` untuk D-09 yang menyatakan perubahan tidak tersimpan: TC tidak memintanya, dan form ditutup lewat `[Leave]` sehingga perubahan Useful Life dibuang.
- Temuan untuk QA:
  - TC-FA-TDC-293 langkah 1 tidak menyebut nilai Useful Life baru; nilai ditetapkan fixture (tidak ada nilai di TC).
  - Precondition d TC menyebut "untuk D-12 tabel dikosongkan pada sesi terpisah"; spec menjalankannya di akhir spec yang sama (langkah 18) karena D-12 hanya muncul pada tabel kosong.
  - Class Code `KHS-V1` dan `KHS-C1` ditulis tanpa suffix di TC; spec memakai `-{runId}-011` (S-12). Batas panjang Class Code tidak disebut TC.
  - Email akun Total Control tidak tertulis di TC.
