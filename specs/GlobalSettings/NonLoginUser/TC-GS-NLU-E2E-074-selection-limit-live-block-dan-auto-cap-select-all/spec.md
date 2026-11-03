---
id: TC-GS-NLU-E2E-074-selection-limit-live-block-dan-auto-cap-select-all
title: "Selection Limit: Live-Block dan Auto-Cap Select All"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-218
  - TC-GS-NLU-219
coverage:
  web: automated
---

# Selection Limit: Live-Block dan Auto-Cap Select All

## Prerequisites

- Mode: FE+BE (backend nyata). Spec memakai limit Selection Limit yang diturunkan dan 120 record.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): 120 Non-Login User `Seleksi Uji 001 {runId}-074` sampai `Seleksi Uji 120 {runId}-074`. Search `{runId}-074` menyaring tepat 120 baris (N = 120 dari seeding). Pengganti fixture Seleksi Uji 001 sampai 120 Pre-setup No. 11 agar Search tidak bercampur dengan record Pre-setup.
- State global: Selection Limit diturunkan ke 100 (nilai minimum) di Lifecycle Settings > System Limits oleh hook `before`; nilai awal dicatat dan dipulihkan hook `after`. Akun pelaku perubahan limit dan mekanisme pemulihannya tidak disebut TC, PRD, atau LLD sehingga disediakan tim FE (S-13). Suite berjalan serial (`parallel: false`).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).

## Test Steps


### TC-GS-NLU-218: Selection Limit live-block pada seleksi manual

1. Ketik Search `{runId}-074`, tekan Enter
2. Ubah page size menjadi 100
3. Centang checkbox header (Select All halaman ini)
4. Verifikasi 100 baris pada halaman 1 tercentang
5. Verifikasi Bulk Action Bar aktif
6. Pindah ke halaman 2
7. Coba centang satu baris
8. Verifikasi checkbox baris disabled
9. Hover checkbox baris yang disabled
10. Verifikasi tooltip `You've reached the maximum selection of 100 rows.`

### TC-GS-NLU-219: Selection Limit auto-cap pada Select All lintas halaman

11. Klik icon `(X)` untuk membatalkan seleksi dan kembali ke halaman 1
12. Centang satu baris agar button Select All tampil
13. Klik button `Select All (120 records)`
14. Verifikasi seleksi dipotong otomatis ke 100 baris pertama (`100 Non-Login Users selected`)
15. Verifikasi toast error persisten: `Error, only the first 100 of 120 rows were selected. Narrow your filter to include the rest.`
16. Verifikasi Bulk Action Bar tetap muncul untuk 100 baris

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 2, 11, 12.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- TC-218 dan TC-219 berbagi state global yang sama (Selection Limit 100); keduanya satu kelas volume data (e).
- Temuan untuk QA:
  - TC-219 Langkah Uji langsung mengklik `Select All (120 records)` tanpa menyebut seleksi awal, sedangkan button itu hanya tampil setelah ada baris tercentang; spec menambah langkah penghubung memusatkan satu baris.
  - TC-218 Langkah 4 "coba centang satu baris" lalu Expected b menyebut tooltip pada checkbox disabled tanpa menyebut hover; spec menambah hover.
  - TC-218 menyebut Search "120 baris" sebagai pengamatan tanpa Expected; spec tidak mengasersinya.
  - Akun dan mekanisme menurunkan Selection Limit tidak disebut di TC, PRD, atau LLD; disediakan tim FE.
