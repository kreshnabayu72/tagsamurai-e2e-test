---
id: TC-GS-DIV-E2E-002-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca Tab Division: Loading, Error Load, dan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-5
  - TC-GS-DIV-8
  - TC-GS-DIV-9
coverage:
  web: automated
---

# Resilience Baca Tab Division: Loading, Error Load, dan Try Again

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Division (6 Division, data environment tetap; hanya dibaca): Finance, Human Resources, Legal, Operations, Compliance, Treasury. Spec tidak membuat atau mengubah data backend.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script:
  - Respons daftar Division: tahan 3 detik lalu jawab normal (langkah 1 sampai 7, TC-GS-DIV-5); jawab 500 (langkah 8 sampai 12, TC-GS-DIV-8). Intercept 500 yang sama dilepas di langkah 13 sebelum `[Try Again]` (TC-GS-DIV-9); tidak dibutuhkan intercept "500 sekali" terpisah.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-division` lalu menyetelnya ke true; hook `after` memulihkan nilai awal. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah, dan flag Guided Tooltip dipulihkan.
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### TC-GS-DIV-5: Tampilan Loading saat data tabel diambil

1. Pasang intercept pada respons daftar Division: tahan 3 detik lalu jawab normal
2. Buka Global Settings > User > Tab Division
3. Verifikasi Skeleton loader / Loading component tampil pada area tabel selama menunggu
4. Tunggu respons diterima
5. Verifikasi data tabel Division tampil
6. Verifikasi Skeleton loader hilang
7. Lepas intercept respons daftar Division

### TC-GS-DIV-8: Error Load tabel saat pengambilan data gagal

8. Pasang intercept pada respons daftar Division: jawab 500
9. Buka Tab Division (muat ulang Global Settings > User > Tab Division)
10. Verifikasi tabel menampilkan teks `Unable to load this data.`
11. Verifikasi tombol `[Try Again]` tampil
12. Verifikasi tampilan bukan empty state `No division yet`

### TC-GS-DIV-9: Klik Try Again memuat ulang data setelah Error Load

13. Pulihkan respons normal pada respons daftar Division (lepas intercept 500 dari TC-GS-DIV-8)
14. Klik `[Try Again]`
15. Verifikasi data tabel Division dimuat ulang dan tampil
16. Verifikasi teks `Unable to load this data.` hilang
17. Verifikasi tombol `[Try Again]` hilang

## Notes

- Mode: FE+BE (intercept parsial, kelas harness fault injection; bagian 6 konvensi). Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-DIV-9 berdependensi TC-GS-DIV-8, dan langkah 1 sampai 2 TC-GS-DIV-9 (paksa 500, buka Tab Division dan tunggu `Unable to load this data.`) identik dengan langkah 8 sampai 10 spec ini; spec melanjutkan state Error Load dari TC-GS-DIV-8 tanpa membuka ulang tab, lalu memulihkan respons di langkah 13 sebelum `[Try Again]`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 (menunggu respons) dan 7 (lepas intercept).
- Nama endpoint tidak disebut di TC sumber; kebutuhan ini sudah dicatat di Prerequisites.
- Temuan untuk QA:
  - TC-GS-DIV-5 tidak menyebut apakah delay hanya diterapkan pada kunjungan pertama; spec menahan respons pada pembukaan tab di langkah 2 dan melepas intercept di langkah 7.
