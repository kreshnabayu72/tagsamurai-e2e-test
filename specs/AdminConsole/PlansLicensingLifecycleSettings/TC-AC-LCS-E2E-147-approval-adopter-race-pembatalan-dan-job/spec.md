---
id: TC-AC-LCS-E2E-147-approval-adopter-race-pembatalan-dan-job
title: "Approval Settings Konsumen: Pembatalan Manual Bersamaan dengan Job Timeout"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-518
coverage:
  web: automated
---

# Approval Settings Konsumen: Pembatalan Manual Bersamaan dengan Job Timeout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Mode multi-konteks (kelas c): dua sesi, yaitu sesi requester (UI, konteks browser kedua) dan job timeout yang ditunda lewat Fixture BE; TC-AC-LCS-518 bertanda Manual Only (dua sesi pengguna paralel) dan tetap ditulis sebagai spec.
- Akun requester pengajuan Device Allocation disediakan tim FE (tidak tertulis di Pre-setup TC); login requester dilakukan di konteks browser kedua pada langkah spec.
- Data: Device Allocation berstatus `Waiting for Approval` yang tepat mencapai batas timeout, diseed lewat Fixture BE di langkah pertama (dipakai sebagai precondition TC, tidak diasersi).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan menunda dan melepaskan job Timeout Auto-Cancel.
- Pemulihan: jam, penundaan job, dan data pengajuan dipulihkan lewat Fixture BE di hook `after`; konteks browser kedua ditutup dan sesinya dihapus di langkah terakhir (S-09). Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-518: Pembatalan manual oleh requester bersamaan dengan job timeout: transaksi pertama menang, yang kedua no-op

1. Atur lewat Fixture BE: Device Allocation berstatus `Waiting for Approval` yang tepat mencapai batas timeout dan job Timeout Auto-Cancel ditunda
2. Buka konteks browser kedua dan login sebagai requester pengajuan tersebut
3. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE pada sesi requester, tekan Enter
4. Buka pengajuan Device Allocation tersebut pada sesi requester
5. Klik Cancel Request pada pengajuan pada sesi requester
6. Lepaskan penundaan job Timeout Auto-Cancel lewat Fixture BE tanpa jeda dari langkah sebelumnya
7. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
8. Buka status akhir dan log pengajuan
9. Verifikasi status akhir pengajuan `Canceled` tepat satu kali
10. Verifikasi log pengajuan memuat tepat satu catatan pembatalan (transaksi kedua no-op)
11. Tutup konteks browser kedua dan hapus sesi login requester

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ...", "Buka konteks browser kedua ...", "Buka pengajuan ...", "Ketik Search nomor pengajuan ..., tekan Enter" (langkah 3, 7) sebelum membuka pengajuan (R-16, R-23), dan "Tutup konteks browser kedua ..." (S-03, S-09). Nomor pengajuan Device Allocation uji tidak tertulis di Pre-setup TC; spec memakai nomor hasil seeding Fixture BE.
- Temuan untuk QA: TC tidak menyebut cara membuat dua aksi terjadi "pada saat yang sama"; spec menulis dua langkah berurutan tanpa jeda dan keserentakan ditentukan tahap script. Akun requester dan cara membaca log pengajuan tidak didefinisikan di TC (S-11, S-13). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
