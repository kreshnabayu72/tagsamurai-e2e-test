---
id: TC-AC-ACAL-E2E-041-download-threshold-5000-5001-baris-loading-screen-dan-gagal
title: "Download: Threshold 5.000 dan 5.001 Baris, Loading Screen, dan Gagal di Atas Threshold"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-129
  - TC-AC-ACAL-130
  - TC-AC-ACAL-164
coverage:
  web: automated
---

# Download: Threshold 5.000 dan 5.001 Baris, Loading Screen, dan Gagal di Atas Threshold

## Prerequisites

- Mode: FE+BE (intercept parsial respons export di atas backend nyata pada TC-AC-ACAL-164; tidak seluruh API di-mock).
- Akun aktor: Total Control entitas Volume khusus spec ini (`Fixture.activityLog.akunVolume041`, disediakan tim FE; email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), kredensial `Spectra.env.AC_VOLUME_TC_PASSWORD` (nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Entitas ini dipakai hanya oleh spec ini karena seed volume tidak dapat dihapus dan akan mengubah jumlah baris di spec lain. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook `before`/`after` spec ini menyetel dan memulihkan flag seen untuk akun `akunVolume041` dan halaman Admin Console > Activity Log (kemampuan disediakan tim FE/BE).
- Data volume (kelas volume data, bagian 3 prinsip 13e), disediakan lewat seed BE di entitas Volume sebelum run (mekanisme seeding log tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE), jumlah dihitung pada saat langkah dijalankan termasuk baris sesi akun aktor hook `before`:
  - Tab User Action: tepat 5.000 entri dalam scope (TC-AC-ACAL-129).
  - Tab Session: tepat 5.001 entri dalam scope (TC-AC-ACAL-130 dan TC-AC-ACAL-164).
  - Pembersihan: baris log tidak dapat dihapus lewat UI atau API modul ini; entitas Volume direset oleh tim BE di luar spec.
- Jendela pengamatan absence notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 9) adalah pilihan spec (bagian 6 konvensi); TC tidak menyatakan durasinya dan PRD tidak menyebut nilainya.
- Kemampuan teknis (disediakan tim FE/BE):
  - Menangkap berkas unduhan browser ke direktori bersih per unduhan dan memeriksa nama berkas serta ada atau tidaknya berkas. Berkas unduhan dihapus di hook `after`.
  - Mengamati loading screen penuh secara tepat waktu: muncul atau tidak muncul antara klik pilihan format dan berkas terunduh, memakai auto-wait tanpa intercept (TC-AC-ACAL-129 dan TC-AC-ACAL-130).
  - Mengamati ada atau tidaknya toast dan notifikasi in-app.
  - Intercept respons export Session: `POST /v2/analytics-reporting/session-logs/export` (path dari `tc-activity-log-backend.md`) mengembalikan 5xx setelah ditunda sehingga loading screen teramati (TC-AC-ACAL-164). Intercept dilepas segera setelah pemicu selesai (langkah 18); hook `after` melepasnya sebagai cadangan.
- State yang diubah dan dipulihkan: intercept export (langkah 18). Spec tidak mengubah Search, Filter, Sort, atau Setup Column. Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-129: Download tepat 5.000 baris langsung terunduh

1. Klik tab "User Action", klik icon Download, lalu klik `Download as CSV`
2. Verifikasi tidak ada loading screen penuh
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `Activity-Log-User-Action.csv` langsung terunduh

### TC-AC-ACAL-130: Download 5.001 baris memakai loading screen lalu langsung terunduh

5. Klik tab "Session", klik icon Download, lalu klik `Download as XLSX`
6. Verifikasi loading screen tampil sampai berkas siap
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Activity-Log-Session.xlsx` langsung terunduh
9. Tunggu 5 detik tanpa memuat ulang halaman
10. Verifikasi tidak ada notifikasi in-app

### TC-AC-ACAL-164: Download di atas threshold gagal, loading screen hilang dan toast error

11. Pasang intercept pada respons `POST /v2/analytics-reporting/session-logs/export` agar mengembalikan 5xx setelah ditunda
12. Klik icon Download pada tab Session, lalu klik `Download as CSV`
13. Verifikasi loading screen tampil
14. Tunggu sampai proses gagal
15. Verifikasi loading screen hilang
16. Verifikasi toast error `"Error, failed to download Activity-Log-Session."` tampil
17. Verifikasi tidak ada berkas terunduh
18. Lepas intercept respons export

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 129, 130, 164 (kasus berhasil lebih dulu, kasus gagal dengan intercept terakhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE. Kolom Automation TC-AC-ACAL-129, 130, dan 164 bernilai Manual Only di TC; itu bukan alasan keluar spec, kebutuhan teknisnya ada di Prerequisites.
- Absence state sementara (bagian 8b butir 11 dan 5): loading screen dan toast diasersi segera setelah pemicu (klik pilihan format) dan sebelum asersi berkas terunduh (langkah 2 sampai 4 dan 6 sampai 8); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas. Pengecualian notifikasi in-app (bagian 6 dan 8b butir 11): asersi absence notifikasi in-app (langkah 10) ditulis sesudah anchor positif berkas terunduh (langkah 8) dan langkah penghubung "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 9). Langkah 17 (tidak ada berkas) memakai langkah 16 (toast error tampil) sebagai anchor positif bahwa respons gagal sudah diproses.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 ("Tunggu 5 detik tanpa memuat ulang halaman" sebelum absence notifikasi in-app, jendela pilihan spec yang dinyatakan di Prerequisites; S-03), langkah 11 (memasang intercept sebagai pemicu), langkah 14 ("Tunggu sampai proses gagal" menurut Langkah Uji TC-AC-ACAL-164; tanpa durasi, menunggu toast), langkah 18 (melepas intercept, S-09).
- `P-5` butir (b): TC-AC-ACAL-164 adalah satu TC objek-uji ringan kelas b (satu kegagalan 5xx pada export) tanpa harness eksternal dan tanpa state berat sendiri; ia berada di spec volume Download karena permukaannya sama (unduhan di atas threshold 5.000 baris) dan memakai seed 5.001 baris yang sama dengan TC-AC-ACAL-130.
- Label menu Download: TC-AC-ACAL-129, 130, dan 164 menulis `Download > CSV|XLSX`, label UI adalah `Download as CSV|XLSX` (PRD §4.2); spec memakai label UI.
- Temuan untuk QA:
  - TC-AC-ACAL-129, 130, dan 164 menyebut jumlah entri dalam scope tanpa menyebut akun atau entitas; entitas Volume dan akunnya tidak ada di Pre-setup TC (Pre-setup No 11 hanya menyebut volume seed BE). Mekanisme seed 5.000 dan 5.001 entri tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-AC-ACAL-129 dan 130 tidak menyebut nama berkas; spec memakai nama berkas menurut PRD §4.2 (`Activity-Log-User-Action`, `Activity-Log-Session`) dan format yang diklik di Langkah Uji.
  - TC-AC-ACAL-129 mengizinkan "indikator loading biasa boleh tampil sebentar"; spec hanya mengasersi tidak ada loading screen penuh.
  - TC-AC-ACAL-130 dan 164 menulis "Tunggu sampai berkas siap" dan "Tunggu sampai proses gagal" tanpa durasi; spec memakai auto-wait.
  - TC-AC-ACAL-164 menyebut "endpoint export Session gagal 5xx setelah diproses" tanpa menyebut kode 5xx dan endpoint; spec memakai endpoint export Session dari `tc-activity-log-backend.md` dan menunda respons supaya loading screen teramati.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
