---
id: TC-GS-ACTLOG-E2E-009-role-matrix-visibilitas-dan-download-total-control-dan-read-only
title: "Role Matrix: Visibilitas, Masking, dan Download Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-28
  - TC-GS-ACTLOG-29
  - TC-GS-ACTLOG-37
  - TC-GS-ACTLOG-139
coverage:
  web: automated
---

# Role Matrix: Visibilitas, Masking, dan Download Read Only

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Spec Role Matrix (bagian 3a konvensi): langkah visibilitas dan masking identik untuk semua role, hanya akun login yang berbeda. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (Client A), urutan baris = urutan iterasi:

| Role | Email | Env var password |
|---|---|---|
| Total Control | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Read Only | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |

- Login Total Control di hook `before`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Data Pre-setup (tetap di environment): hanya dua akun pada tabel di atas.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor:
  - User `John Doe {runId}-009` (First Name `John`, Last Name `Doe {runId}-009`), Employee ID `EMP001-{runId}-009`, Position `Staff {runId}-009`, Division `Marketing {runId}-009`. Nilai bersuffix dipakai sebagai pengganti `John Doe`, `EMP001`, `Staff`, dan `Marketing` di TC agar tidak bentrok dengan spec lain. Password user `Spectra.env.ACTLOG_PASSWORD`.
  - Entri Session Login `Failed` milik `John Doe {runId}-009` dengan Note `Incorrect password` dan IP Address `192.0.2.10`, dihasilkan lewat alur Login Auth dengan password salah `Spectra.env.LP_PASSWORD_WRONG`.
  - Entri Tab User Action hasil aksi Create User, Create Position, dan Create Division pada seeding di atas; cukup untuk precondition "data log tersedia pada kedua tab" TC-GS-ACTLOG-139.
- Kemampuan teknis (disediakan tim FE/BE): (a) request Login dikirim dari alamat sumber `192.0.2.10`, atau entri Session setara di-seed BE, karena IP ditentukan jaringan penguji dan TC tidak memberi mekanismenya; (b) penangkapan berkas unduhan browser untuk langkah Download.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `John Doe {runId}-009`, Position `Staff {runId}-009`, dan Division `Marketing {runId}-009` bila masih ada.

## Test Steps

### TC-GS-ACTLOG-28, TC-GS-ACTLOG-29, dan TC-GS-ACTLOG-37: Matriks visibilitas dan tidak ada masking field, per role

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 15): logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
2. Verifikasi menu Activity Log tampil (Show) pada menu Global Settings di sidebar
3. Buka menu Activity Log
4. Verifikasi Tab `Session` tampil pada tab Session
5. Verifikasi Tab `User Action` tampil pada tab Session
6. Verifikasi Search, Filter, dan Download tampil pada tab Session
7. Verifikasi Search, Filter, dan Download aktif pada tab Session
8. Klik Tab `User Action`
9. Verifikasi Tab `Session` tampil pada tab User Action
10. Verifikasi Tab `User Action` tampil pada tab User Action
11. Verifikasi Search, Filter, dan Download tampil pada tab User Action
12. Verifikasi Search, Filter, dan Download aktif pada tab User Action
13. Verifikasi tidak ada elemen berstatus Disabled pada toolbar dan tabel kedua tab: elemen yang tampil aktif
14. Klik Tab `Session`, ketik Search `John Doe {runId}-009`, tekan Enter
15. Verifikasi baris `John Doe {runId}-009` pada role baris tabel menampilkan IP Address `192.0.2.10`, Note `Incorrect password`, Employee ID `EMP001-{runId}-009`, Position `Staff {runId}-009`, dan Division `Marketing {runId}-009` penuh tanpa bagian yang disamarkan
16. Verifikasi tampilan Read Only identik dengan Total Control pada matriks visibilitas (menu, tab, Search, Filter, Download tanpa elemen Hidden atau Disabled)
17. Verifikasi nilai IP Address, Note, Employee ID, Position, dan Division baris `John Doe {runId}-009` pada Read Only identik dengan Total Control, tanpa bagian yang disamarkan

### TC-GS-ACTLOG-139: Read Only dapat mengunduh log kedua tab

18. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
19. Klik icon Download, pilih `Download as CSV`
20. Verifikasi berkas `Activity-Log-Session.csv` terunduh
21. Klik Tab `User Action`
22. Klik icon Download, pilih `Download as CSV`
23. Verifikasi berkas `Activity-Log-User-Action.csv` terunduh

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-28, 29, 37, 139).
- Pengulangan (K-9): langkah 1 sampai 15 diulang untuk tiap baris tabel Role yang diuji (Total Control, lalu Read Only). Langkah 16 dan 17 dinilai sesudah kedua iterasi selesai; langkah 18 sampai 23 berjalan pada sesi Read Only, iterasi terakhir.
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-ACTLOG-37 digabung ke dalam perulangan TC-GS-ACTLOG-28 dan TC-GS-ACTLOG-29 karena langkahnya identik per role, dan TC-GS-ACTLOG-139 ditaruh terakhir karena memakai sesi Read Only.
- Spec 38 langkah setelah ekspansi (langkah 1 sampai 15 dikali 2 role ditambah 8 langkah lain), di atas smell 35 langkah. Alasan: seluruh blok satu topik (matriks role pada halaman baca) dan satu kelas harness; langkah tiap role identik, sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas dan aksi baca per role; `caseType` Positive mengikuti seluruh TC sumber. Download hanya diuji untuk Read Only (TC-GS-ACTLOG-139); Download Total Control diuji TC lain. Role yang tidak berhak (tanpa akses menu, URL langsung) diuji di spec `TC-GS-ACTLOG-E2E-010-role-matrix-tanpa-akses-menu-dan-direct-url`.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (ganti akun; pada iterasi Total Control mengulang login akun hook `before` supaya langkah perulangan tidak bersyarat), membuka menu dan tab (langkah 3, 8, 14, 21), serta mengetik Search `John Doe {runId}-009` untuk menemukan baris subjek (langkah 14). Langkah 18 menutup Search dan mereset tabel sebelum Download (pemulihan state antar TC).
- Isi berkas unduhan tidak diasersi (hanya nama berkas yang terunduh sesuai Expected TC-GS-ACTLOG-139).
- Langkah 16 dan 17 adalah kesimpulan dari Expected d TC-GS-ACTLOG-29 dan Expected b TC-GS-ACTLOG-37 ("identik dengan Total Control"); keduanya dinilai terhadap hasil langkah 2 sampai 15 pada iterasi Total Control dan Read Only.
- Temuan untuk QA:
  - TC-GS-ACTLOG-28 Expected b menulis "tampil pada kedua tab" untuk Tab `Session` dan `User Action`; spec memverifikasi keduanya dari masing-masing tab (langkah 4, 5, 9, 10).
  - TC-GS-ACTLOG-28 Expected d ("elemen yang tidak tampil tidak ada") tidak punya objek yang dapat diamati; spec hanya memverifikasi tidak ada elemen Disabled (langkah 13).
  - TC-GS-ACTLOG-37 tidak menyebut Activity dan Status baris `John Doe` yang punya Note `Incorrect password`; spec memakai Login `Failed` (padanan Note itu di TC-GS-ACTLOG-41). Mekanisme membuat IP `192.0.2.10` tidak ditentukan di TC.
  - TC-GS-ACTLOG-37 memakai `EMP001`, `Staff`, `Marketing` literal; spec memakai nilai bersuffix; QA konfirmasi format Employee ID yang diizinkan.
  - Hook suite Guided Tooltip menyetel flag untuk akun aktor suite; akun Read Only pada tabel Role yang diuji perlu tercakup oleh hook yang sama (flag untuk akun itu ditetapkan tim FE/BE).
  - Nama env baru `ACTLOG_PASSWORD` perlu didaftarkan tim FE.
