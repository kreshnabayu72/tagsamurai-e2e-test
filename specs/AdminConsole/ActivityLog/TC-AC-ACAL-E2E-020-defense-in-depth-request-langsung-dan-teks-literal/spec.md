---
id: TC-AC-ACAL-E2E-020-defense-in-depth-request-langsung-dan-teks-literal
title: "Defense-in-depth: Request Langsung ke Endpoint Log dan Teks Literal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-150
  - TC-AC-ACAL-151
  - TC-AC-ACAL-152
  - TC-AC-ACAL-153
  - TC-AC-ACAL-156
coverage:
  web: automated
---

# Defense-in-depth: Request Langsung ke Endpoint Log dan Teks Literal

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth, bagian 3 prinsip 13): request langsung ke server tanpa browser (TC-AC-ACAL-150 sampai 153) dan render teks literal (TC-AC-ACAL-156).
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md); empat akun lain di bawah hanya dipakai lewat sesi API dan tidak membuka halaman.
- Klien HTTP (kemampuan disediakan tim FE/BE): mengirim request langsung List Session, List User Action, Export, dan membuka koneksi stream Activity Log dengan token sesi API akun yang disebut tiap langkah (token bukan sesi web). Endpoint dan header mengikuti kontrak API modul Activity Log yang dipegang tim BE; spec ini tidak menetapkannya.
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Principal), akun UI hook `before` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Capability Client Full CRUD (staf Principal, tanpa access level) | `fullCrudClient_automated_{namaCompany}@qwertysystem.net` (No 5) | `Spectra.env.AC_FULLCRUD_PASSWORD` |
| Group Manager | `groupManagerAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 4) | `Spectra.env.AC_GM_PASSWORD` |
| Total Control Global Settings tanpa Total Control/Read Only Admin Console | `totalControlGlobalSettingsOnly_automated_{namaCompany}@qwertysystem.net` (No 6) | `Spectra.env.AC_GSONLY_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |

- Login akun UI (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log dibuka hook `beforeEach` suite. Langkah 1 sampai 28 tidak memakai browser; hanya langkah 29 sampai 37 memakai halaman (langkah 37 menutup Search). Hook `after` tidak perlu memulihkan sesi (akun UI adalah akun default suite).
- Data Pre-setup (tetap di environment): data log Session (No 9) dan entri Name `<b>PT Uji</b>` serta `PT 100%_Test` (No 13; seed BE; seeding idempotent, nama literal karena asersi bergantung pada teks literal dan tidak dihapus).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password staf `Spectra.env.AC_DYN_PASSWORD`: staf `Staf Alfa {runId}-020` (Distributor Alfa) dan `Staf Gamma {runId}-020` (Distributor Gamma), masing-masing membuka lalu menutup Admin Console sehingga punya baris Session. ID staf Gamma tersedia sebagai `Fixture.activityLog.idStafGamma` (fixture activityLog baru, nilai ditetapkan tim FE). Dihapus lewat API di hook `after` bila masih ada.
- Tidak ada state global yang diubah. Spec ini hanya mengasersi status respons dan isi respons atau berkas (state data); tidak ada pengalihan halaman, toast, atau tampilan yang diasersi pada langkah request langsung (bagian 8b butir 1).

## Test Steps

### TC-AC-ACAL-150: Permintaan langsung oleh aktor tanpa Total Control/Read Only ditolak

1. Kirim permintaan langsung List Session sebagai Capability Client Full CRUD
2. Verifikasi respons List Session berstatus `403 Forbidden`
3. Kirim permintaan langsung List User Action sebagai Capability Client Full CRUD
4. Verifikasi respons List User Action berstatus `403 Forbidden`
5. Kirim permintaan langsung Export sebagai Capability Client Full CRUD
6. Verifikasi respons Export berstatus `403 Forbidden`
7. Verifikasi ketiga respons tidak memuat data log

### TC-AC-ACAL-151: Permintaan langsung oleh Group Manager ditolak

8. Kirim permintaan langsung List Session sebagai Group Manager
9. Verifikasi respons List Session berstatus `403 Forbidden`
10. Kirim permintaan langsung List User Action sebagai Group Manager
11. Verifikasi respons List User Action berstatus `403 Forbidden`
12. Kirim permintaan langsung Export sebagai Group Manager
13. Verifikasi respons Export berstatus `403 Forbidden`
14. Buka koneksi stream langsung sebagai Group Manager
15. Verifikasi koneksi stream ditolak
16. Verifikasi seluruh respons dan koneksi tidak memuat data log

### TC-AC-ACAL-152: Permintaan langsung oleh pemegang akses Global Settings tanpa level AC

17. Kirim permintaan langsung List User Action sebagai Total Control Global Settings tanpa Total Control/Read Only Admin Console
18. Verifikasi respons List User Action berstatus `403 Forbidden`
19. Verifikasi respons tidak memuat data log

### TC-AC-ACAL-153: Penyaringan scope di server tidak bisa ditembus lewat parameter

20. Kirim permintaan langsung List Session sebagai Total Control (Distributor Alfa) tanpa filter
21. Verifikasi respons List Session memuat sedikitnya satu baris sesi `Staf Alfa {runId}-020`
22. Kirim permintaan langsung List Session sebagai Total Control (Distributor Alfa) dengan filter User berisi `Fixture.activityLog.idStafGamma`
23. Verifikasi respons List Session memuat 0 baris
24. Verifikasi respons List Session tidak memuat data staf Distributor Gamma
25. Kirim permintaan langsung Export Session sebagai Total Control (Distributor Alfa) tanpa filter
26. Verifikasi berkas hasil Export memuat sedikitnya satu baris sesi `Staf Alfa {runId}-020`
27. Verifikasi berkas hasil Export hanya berisi scope Distributor Alfa
28. Verifikasi berkas hasil Export tidak memuat baris sesi `Staf Gamma {runId}-020`

### TC-AC-ACAL-156: Kata kunci dan isi sel ditampilkan sebagai teks literal

29. Klik tab "User Action"
30. Ketik Search `<b>`, tekan Enter
31. Verifikasi baris Name `<b>PT Uji</b>` ditemukan
32. Verifikasi sel Name menampilkan `<b>PT Uji</b>` apa adanya
33. Verifikasi sel Name tidak dirender tebal (bold)
34. Ganti isi kotak search dengan `100%_`, tekan Enter
35. Verifikasi baris Name `PT 100%_Test` tampil
36. Verifikasi hasil Search hanya memuat baris `PT 100%_Test`: footer `Showing 1–1 of 1 entries` (karakter khusus tidak diinterpretasi)
37. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-150, 151, 152, 153, 156).
- Spec ini 37 langkah (di atas 35 langkah): dua langkah muncul karena S-01 memecah dua Verifikasi yang menggabung klausa. TC-AC-ACAL-150 sampai 153 dan 156 memakai satu dataset dan satu sesi kelas harness yang sama (K-1); memecahnya akan mengulang seeding dan login tanpa mengurangi langkah, sehingga tetap satu spec (bagian 3 konvensi).
- K-1 (bagian 2 konvensi, `[KEPUTUSAN 2026-10-30]`): TC-AC-ACAL-150 sampai 153 adalah TC defense-in-depth kelas a dengan Expected respons API (status respons dan state data) yang tumpang tindih dengan `tc-activity-log-backend.md`; tetap masuk spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec. Asersi hanya status respons dan isi respons atau berkas (bagian 8b butir 1); perilaku FE untuk respons yang sama diasersi di spec jalur UI (spec 013).
- Pemicu bukan objek uji: spec ini tidak memuat asersi absence log (kelas g); frasa "tidak ada data log" pada respons 403 diasersi sebagai isi respons.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengirim request (langkah 1, 3, 5, 8, 10, 12, 14, 17, 20, 22, 25), membuka tab (langkah 29), mengetik dan mengganti isi Search (langkah 30, 34), dan menutup Search (langkah 37, supaya Search `100%_` tidak tetap aktif di akhir spec; S-03).
- Asersi tambahan di luar Expected TC (S-03): langkah 21 dan 26 membuktikan data pembanding (baris sesi staf Alfa) ada pada respons yang sama sebelum asersi 0 baris dan ketiadaan data Gamma (bagian 8b butir 2).
- Urutan langkah TC-AC-ACAL-156 berbeda dari Langkah Uji TC: kata kunci `<b>` diketik lebih dulu untuk menemukan baris `<b>PT Uji</b>` di antara entri lain, lalu sel diamati.
- TC-AC-ACAL-153 klausa b (isi berkas Export) dibaca dari respons Export langsung (bukan berkas unduhan browser), sehingga tidak memakai kelas f.
- Temuan untuk QA:
  - TC-AC-ACAL-150 sampai 153 tidak menyebut endpoint, metode, dan header; spec menyerahkannya ke kontrak API modul (S-13).
  - TC-AC-ACAL-153 tidak menyebut ID staf Gamma dan cara mendapatkannya; spec memakai fixture hasil seeding. Klausa "Berkas hanya berisi scope Alfa" tidak menyebut format berkas (CSV atau XLSX); spec membaca respons Export Session apa adanya.
  - TC-AC-ACAL-151 "buka stream" tidak menyebut endpoint stream; kemampuan membuka stream langsung disediakan tim FE/BE.
  - TC-AC-ACAL-156 Expected c ("Hanya baris `PT 100%_Test`") menyatakan keunikan hasil; spec mengasersinya lewat footer `Showing 1–1 of 1 entries`, mengandalkan seeding literal idempotent yang hanya memuat satu baris itu.
  - Email Pre-setup memakai placeholder `{namaCompany}`; password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_FULLCRUD_PASSWORD`, `AC_GM_PASSWORD`, `AC_GSONLY_PASSWORD`, `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
