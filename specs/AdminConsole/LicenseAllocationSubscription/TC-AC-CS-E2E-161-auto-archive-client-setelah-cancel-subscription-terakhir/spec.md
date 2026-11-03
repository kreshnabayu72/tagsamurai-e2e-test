---
id: TC-AC-CS-E2E-161-auto-archive-client-setelah-cancel-subscription-terakhir
title: "Modul Konsumen: Auto-Archive Client setelah Cancel Subscription Terakhir"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-480
coverage:
  web: automated
---

# Modul Konsumen: Auto-Archive Client setelah Cancel Subscription Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12), keduanya binaan langsung Principal dan bersuffix `+{runId}-161`: Client A `Client Auto Archive A+{runId}-161` dengan satu-satunya term Active (FAMS), dan Client B `Client Auto Archive B+{runId}-161` dengan dua term Active (FAMS dan SAMS). Endpoint pembuatan data tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE (S-13).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-480: Cancel Subscription terakhir memicu evaluasi Auto-Archive Client

1. Ketik Search `Client Auto Archive A+{runId}-161`, tekan Enter
2. Klik ikon `⋯` pada term Active Client A
3. Klik `Cancel Subscription`
4. Klik `[Cancel Subscription]` pada dialog konfirmasi
5. Tunggu aksi selesai (dialog/modal tertutup)
6. Klik tab `History`
7. Verifikasi term Client A berstatus Archive
8. Klik tab `Current`
9. Ganti isi kotak search dengan `Client Auto Archive B+{runId}-161`, tekan Enter
10. Klik ikon `⋯` pada term FAMS Client B
11. Klik `Cancel Subscription`
12. Klik `[Cancel Subscription]` pada dialog konfirmasi
13. Tunggu aksi selesai (dialog/modal tertutup)
14. Klik tab `History`
15. Verifikasi term FAMS Client B berstatus Archive
16. Klik menu `Client` di sidebar
17. Ketik Search `Client Auto Archive A+{runId}-161`, tekan Enter
18. Verifikasi Client A dievaluasi untuk Auto-Archive karena tidak punya subscription live lain
19. Ganti isi kotak search dengan `Client Auto Archive B+{runId}-161`, tekan Enter
20. Verifikasi Client B tidak ter-Archive karena masih punya term live lain

## Notes

- Langkah penghubung (S-03): langkah 1, 9, 17, 19 (Search untuk menemukan baris target, R-16), langkah 6, 8, 14 (pindah tab), langkah 16 (pindah halaman), langkah 5 dan 13 (menunggu aksi konfirmasi Cancel Subscription selesai sebelum pindah tab, 8b.8).
- Langkah 18 dan 20 memakai hasil langkah 7 dan 15 (status term Archive pada tab `History`, sesudah langkah Tunggu aksi selesai, menandai respons server selesai dan daftar sudah disegarkan; spec ini tidak memakai toast sebagai anchor karena TC tidak menyebutnya) sebagai anchor sebelum membaca status Client (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-480 langkah 1 hanya menyebut Cancel Subscription satu term; asersi b ("Client yang masih punya term live lain tidak ter-Archive") tidak menyebut Client atau term mana yang di-Cancel; spec men-Cancel satu dari dua term Client B.
  - TC-AC-CS-480 langkah 2 ("Buka daftar Client") dan Expected a tidak menyebut wujud "dievaluasi untuk Auto-Archive" di UI (status Client apa yang tampil); label menu `Client` dan nilai status perlu dilengkapi QA (S-02).
  - Auto-Archive dapat berjalan sebagai proses latar; TC tidak menyebut batas waktu tunggu (tanpa jam atau job di TC).
