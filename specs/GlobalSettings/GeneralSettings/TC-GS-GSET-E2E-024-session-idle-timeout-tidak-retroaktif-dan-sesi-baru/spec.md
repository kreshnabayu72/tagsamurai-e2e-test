---
id: TC-GS-GSET-E2E-024-session-idle-timeout-tidak-retroaktif-dan-sesi-baru
title: "Session Idle Timeout: Tidak Retroaktif pada Sesi Berjalan dan Berlaku pada Sesi Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-57
  - TC-GS-GSET-58
coverage:
  web: automated
---

# Session Idle Timeout: Tidak Retroaktif pada Sesi Berjalan dan Berlaku pada Sesi Baru

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Sesi A (UI, login di hook `before`) dan sesi baru (UI, login di langkah 8) | Total Control Client A, Budi Santoso (`Budi S`) | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1) | `GS_TC_PASSWORD` |
  | Admin B (hanya sesi API, memicu Save di langkah 1) | Total Control Client A, Andi Wijaya (`Andi W`) | `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 2) | `GS_TCB_PASSWORD` |

  Admin B hanya memicu perubahan state, sehingga memakai sesi API; sesi UI kedua tidak dibuka (P-2, bagian 3 konvensi). Akun Budi Santoso adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal sesi A: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD` (nama baru, pola `<APP>_<ROLE>_PASSWORD`, belum terdaftar di `spectra.config.ts` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`). Langkah 1 mengubah Session Idle Timeout menjadi `1 hour` (dipakai TC-GS-GSET-58 sebagai precondition); hook `after` suite memulihkan baseline.
- Kemampuan teknis (TC-GS-GSET-57 dan 58 berstatus Manual Only di TC; disediakan tim FE/BE tanpa endpoint karangan):
  - Mengatur jam server secara absolut dan jam browser (klien) bersama ke waktu tertentu, lalu memulihkannya. Jam diatur bersama karena batas idle dievaluasi di server dan Dialog Session Expired diamati di browser; jam server saja tidak cukup untuk sisi UI (bagian 6 konvensi).
  - Membaca waktu terbit sesi dan waktu aktivitas terakhir sebuah sesi dari sisi server (T0), dipakai sebagai acuan jam absolut (bagian 8b butir 3).
  - Klien HTTP dengan sesi API Admin B untuk PUT `/v2/enterprise-management/general-settings` (`currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `60`).
- Cara hitung batas dan margin: idle 31 menit terhadap batas 30 menit (TC-GS-GSET-57) dan 61 menit terhadap batas 60 menit (TC-GS-GSET-58) bermargin 1 menit, kurang dari 5 menit. Karena itu jam server diatur absolut ke `T0 + 31 menit` (langkah 4 dan 10) dan `T0 + 61 menit` (langkah 14), dengan T0 dibaca dari server (waktu aktivitas terakhir sesi A pada langkah 3, waktu terbit sesi baru pada langkah 9, waktu aktivitas langkah 11 pada langkah 13), bukan digeser relatif dari jam sekarang. Nilai 31 dan 61 menit adalah titik uji sesudah batas, bukan batas eksak yang diuji.
- State global yang diubah: jam server dan jam browser (diatur di langkah 4, 10, 14; dipulihkan di langkah 7 dan 17; hook `after` memulihkan walau spec gagal di tengah) dan record Client A. Suite berjalan serial (`parallel: false`, lihat `suite.md`); tidak ada spec lain yang berjalan bersamaan.
- Data Uji: Session Idle Timeout `1 hour` (`sessionIdleTimeout` 60); idle 31 menit lalu 61 menit. Tidak ada Data Dinamis yang dibuat; Save Admin B menghasilkan baris Changelog yang tidak dihapus (audit trail permanen).
- TC-GS-GSET-57: Total Control (Budi Santoso, sesi A aktif dengan batas 30 menit); Admin B Total Control pada sesi terpisah; record baseline. TC-GS-GSET-58: Total Control (Budi Santoso) dengan Session Idle Timeout tersimpan `1 hour` (dari langkah 1).

## Test Steps

### TC-GS-GSET-57: Save tidak memutus sesi yang sedang berjalan

1. Admin B menyimpan Session Idle Timeout `1 hour` lewat sesi API hingga tersimpan
2. Verifikasi sesi A tidak diputus dan tidak di-reset: halaman General Settings tetap tampil di sesi A tanpa Dialog Session Expired
3. Baca waktu aktivitas terakhir sesi A dari server sebagai `{T0A}`
4. Atur jam server (absolut) dan jam browser bersama ke `{T0A}` + 31 menit
5. Pada sesi A, klik menu Global Settings > General Settings
6. Verifikasi sesi A berakhir: Dialog Session Expired tampil (sesi A memakai batas 30 menit)
7. Pulihkan jam server dan jam browser ke waktu nyata

### TC-GS-GSET-58: Sesi baru memakai batas yang baru

8. Logout, lalu login kembali sebagai Budi Santoso (`Spectra.env.GS_TC_PASSWORD`, sesi baru)
9. Baca waktu terbit sesi baru dari server sebagai `{T0B}`
10. Atur jam server (absolut) dan jam browser bersama ke `{T0B}` + 31 menit
11. Pada sesi baru, klik menu Global Settings > General Settings
12. Verifikasi sesi baru tetap aktif: halaman General Settings tampil tanpa Dialog Session Expired (idle 31 menit)
13. Baca waktu aktivitas terakhir sesi baru (aksi langkah 11) dari server sebagai `{T0C}`
14. Atur jam server (absolut) dan jam browser bersama ke `{T0C}` + 61 menit
15. Pada sesi baru, klik menu Global Settings > General Settings
16. Verifikasi sesi baru berakhir: Dialog Session Expired tampil (melewati 60 menit idle)
17. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Kelas harness eksternal (prinsip 13d): objek uji adalah batas waktu idle sebagai fungsi jam; jam server dan jam browser dimanipulasi.
- TC-GS-GSET-57 dan TC-GS-GSET-58 berstatus Manual Only di TC; tetap spec (konvensi bagian 2), kebutuhannya ada di Prerequisites. TC-GS-GSET-58 menyebut TC-GS-GSET-36 dan TC-GS-GSET-57 sebagai dependensi; langkah 1 menyalin penyimpanan `1 hour` sebagai precondition (S-04), dan blok TC-GS-GSET-58 dijalankan sesudah sesi A berakhir di blok TC-GS-GSET-57.
- Pemetaan Expected: TC-GS-GSET-57 a ke langkah 2, b ke 6; TC-GS-GSET-58 a ke langkah 12, b ke 16.
- Jam dipulihkan secara eksplisit (langkah 7 dan 17) sebelum tindakan berikutnya dan sebelum akun aktor membuka Activity Log atau Changelog (S-09). Baseline log tidak diasersi di spec ini.
- Langkah penghubung: langkah 3, 9, 13 (membaca T0 dari server); langkah 4, 10, 14 (mengatur jam); langkah 7 dan 17 (memulihkan jam). Langkah 5, 11, dan 15 adalah "aksi apa pun" pada TC; spec memilih klik menu Global Settings > General Settings.
- Temuan untuk QA:
  - TC-GS-GSET-57: "Admin B ... klik `[Save]`" tidak mengasersi hasil di sesi Admin B; spec memicunya lewat sesi API (P-2) dan tidak mengasersi toast Admin B.
  - TC-GS-GSET-57 dan 58: TC tidak menyebut tombol atau tindakan pada Dialog Session Expired dan "Logout lalu login kembali" pada langkah 1 TC-GS-GSET-58 dilakukan sesudah sesi A berakhir; spec menulis Logout lalu login tanpa merinci tombol dialog.
  - TC-GS-GSET-58: langkah 4 TC ("idle hingga 61 menit") tidak menyebut apakah 61 menit dihitung dari aksi langkah 3 atau dari login; spec menghitung dari aktivitas terakhir (langkah 13).
  - TC-GS-GSET-57 dan 58: cara membaca waktu terbit dan aktivitas terakhir sesi serta mengatur jam server tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
  - TC-GS-GSET-57 Expected a "tidak di-reset" tidak punya cara observasi; spec hanya mengasersi sesi tidak diputus.
