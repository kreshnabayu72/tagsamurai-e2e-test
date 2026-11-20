---
id: TC-FA-TDC-E2E-093-job-j-02-class-inactive-dan-job-gagal-dicoba-lagi
title: "Job J-02: Class Inactive dan Job Gagal Dicoba Lagi"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-347
  - TC-FA-TDC-348
sourceRules: ["FATDC-LOGIC-04o", "F-FATDC-10.k1", "F-FATDC-10.k3a", "§4.1.6#r5", "R-12"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04o": 3
  "F-FATDC-10.k1": [3, 16]
  "F-FATDC-10.k3a": [7, 10]
  "§4.1.6#r5": 10
  "R-12": 16
coverage:
  web: automated
---

# Job J-02: Class Inactive dan Job Gagal Dicoba Lagi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00). Job J-02 dijalankan oleh scheduler harian; tick scheduler J-02 dijalankan eksplisit di langkah (kemampuan penahanan dan penjalanan job disediakan tim FE/BE, `suite.md`).
- Kendali jam sistem (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut yang tertulis di langkah (batas Jan 2027 menurut Time Zone entitas adalah 31 Des 2026 17:00:00 UTC); jam dipulihkan di hook `after`.
- Kemampuan teknis: fault injection sisi server pada job J-02 (disediakan tim FE/BE; TC menyebutnya tanpa mekanisme, S-13).
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API dengan urutan seperti tertulis, dihapus di hook `after`):

| TC | Class / data (bersuffix) | Isi |
|---|---|---|
| TC-347 | `KHS-J4-{runId}-093` | Inactive; Current tanpa Effective From (Useful Life 8); Scheduled Jan 2027 (Useful Life 10) |
| TC-348 | `KHS-J1-{runId}-093` | Active, Used By 0; Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance); Scheduled Jan 2027 (Useful Life 10, Straight Line dan Declining Balance) |

- Tabel berisi tujuh class seed bawaan dan kedua class di atas; baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-347: Versi Scheduled pada class Inactive tetap menjadi Current

1. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC lalu jalankan tick scheduler J-02
2. Muat ulang halaman; baca baris `KHS-J4-{runId}-093`
3. Verifikasi baris `KHS-J4-{runId}-093`: Active = Off; Useful Life (years) "10"; Effective From "Jan 2027"

### TC-FA-TDC-348: Job J-02 gagal, versi tetap Scheduled lalu dicoba lagi

4. Aktifkan fault injection job J-02 (pembentuk precondition e, tidak diasersi)
5. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC lalu jalankan tick scheduler J-02 (gagal)
6. Muat ulang halaman; baca baris `KHS-J1-{runId}-093`
7. Verifikasi baris `KHS-J1-{runId}-093`: Effective From "—", Useful Life "8"
8. Klik link Class Code `KHS-J1-{runId}-093` pada tabel
9. Klik tautan View versions
10. Verifikasi versi "Jan 2027" masih berstatus "Scheduled"
11. Tutup modal Versions
12. Klik `[×]` pada header Drawer
13. Hapus fault injection job J-02
14. Atur jam server dan jam browser ke 1 Jan 2027 17:00:00 UTC (2 Jan 2027 00:00 WIB) lalu jalankan tick scheduler J-02
15. Muat ulang halaman; baca baris `KHS-J1-{runId}-093`
16. Verifikasi baris `KHS-J1-{runId}-093`: Effective From "Jan 2027", Useful Life "10"

## Notes

- Pengecualian P-2: fault injection job J-02 (TC-348) hanya berfungsi sebagai pemicu state (versi tetap Scheduled lalu dicoba pada putaran berikutnya); objek uji adalah perilaku J-02 dan hasil di tabel, sehingga TC-348 tidak dipindah ke spec kelas b. TC-348 bertanda Manual Only (b) di TC karena kegagalan job di server tidak dapat dipicu dari klien; kebutuhan itu ditulis di Prerequisites.
- Langkah penghubung (S-03): langkah 4 dan 13 (mengatur fault injection), langkah 11 (menutup modal), langkah 12 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`). Langkah 2, 6, dan 15 menggabungkan muat ulang dengan "baca" seperti langkah TC.
- Langkah 10 mengamati "versi 'Jan 2027' masih Scheduled" lewat modal Versions (TC hanya menyebut hasil di baris tabel dan menamainya "masih Scheduled").
- `KHS-J1` pada TC-348 dan `KHS-J4` pada TC-347 adalah class milik spec dengan Class Code berbeda.
- Post Condition TC-348 ("satu entri L-08 setelah retry; tidak ada entri L-08 dari percobaan gagal") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-08 ada di spec 096.
- Temuan untuk QA:
  - TC-348 Expected a menyebut versi "Jan 2027" masih Scheduled tanpa tempat mengamati; spec memakai modal Versions (langkah 10).
  - Post Condition TC-348 tanpa langkah observasi di TC.
  - TC-347 dan TC-348 memakai `KHS-J4` dan `KHS-J1` tanpa suffix di TC; spec memakai `-{runId}-093` (S-12).
  - TC-347 tidak menyebut tanggal sistem uji; spec memakai jam absolut dari langkah.
  - Email akun Total Control tidak tertulis di TC.
