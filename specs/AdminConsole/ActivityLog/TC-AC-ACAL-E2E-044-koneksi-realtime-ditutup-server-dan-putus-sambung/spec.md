---
id: TC-AC-ACAL-E2E-044-koneksi-realtime-ditutup-server-dan-putus-sambung
title: "Koneksi Real-time: Ditutup Server dan Putus lalu Tersambung Kembali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-155
  - TC-AC-ACAL-161
  - TC-AC-ACAL-178
coverage:
  web: automated
---

# Koneksi Real-time: Ditutup Server dan Putus lalu Tersambung Kembali

## Prerequisites

- Mode: FE+BE.
- Kelas harness b ringan (resilience koneksi, bagian 3 prinsip 13): koneksi stream real-time ditutup server (TC-AC-ACAL-155, 161) dan diputus lalu disambung kembali di sisi klien (TC-AC-ACAL-178). Satu spec untuk kelas ini; tidak ada kelas harness lain.
- Suite serial (`parallel: false`); spec mengubah hubungan entitas (Reassign Partner) dan capability akun (Read Only); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md). Untuk akun Total Control Distributor Alfa dan Read Only Distributor Alfa dinamis, hook before/after spec ini menyetel dan memulihkan flag seen yang sama (kemampuan disediakan tim FE/BE).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)), urutan baris = urutan blok:

| Akun | Email | Env var password |
|---|---|---|
| Total Control (Principal), akun hook `before` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| Read Only (Distributor Alfa) dinamis `Staf RO Alfa {runId}-044` | `Fixture.activityLog.emailStafRoAlfa` (ditetapkan tim FE) | `Spectra.env.AC_DYN_PASSWORD` |

- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` memulihkan state yang diubah spec (di bawah) lalu mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`:
  - Client `Sejahtera {runId}-044` milik Principal (target ubah PIC Name TC-AC-ACAL-178; pengganti Client Sejahtera Pre-setup agar data Pre-setup tidak diubah, S-06).
  - Partner `Partner Uji {runId}-044` di jaringan Distributor Alfa dengan log awal (entri `Create` lewat sesi API); pengganti Partner Beta pada TC-AC-ACAL-161 agar data Pre-setup tidak diubah.
  - Staf `Staf RO Alfa {runId}-044` (Distributor Alfa) dengan capability Read Only Admin Console, dipakai pada TC-AC-ACAL-155.
- State global yang diubah dan dipulihkan: (1) Partner `Partner Uji {runId}-044` di-Reassign dari Distributor Alfa ke Distributor Gamma, dikembalikan di langkah 21; (2) capability Read Only `Staf RO Alfa {runId}-044` dicabut, dipulihkan di langkah 30. Hook `after` memulihkan keduanya lewat sesi API Principal bila masih berubah (walau spec gagal di tengah), lalu menghapus Client, Partner, dan staf dinamis bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Principal (ubah PIC Name Client, Reassign Partner, cabut dan pulihkan capability Read Only); inspeksi koneksi stream browser (status buka atau ditutup server); network offline lalu online pada konteks browser (TC-AC-ACAL-178: "koneksi stream dapat diputus"); baseline jumlah (S-12) tidak diperlukan karena nama bersuffix unik (baseline nol).
- Tidak ada pengaturan jam server atau jam browser.

## Test Steps

### TC-AC-ACAL-178: Koneksi real-time putus lalu tersambung kembali memuat snapshot terbaru

1. Klik tab "User Action"
2. Ketik Search `Sejahtera {runId}-044`, tekan Enter
3. Putuskan koneksi stream (network offline)
4. Pemicu API: Principal mengubah PIC Name Client `Sejahtera {runId}-044` menjadi `PIC 178 {runId}-044` hingga tersimpan
5. Pulihkan koneksi (network online)
6. Verifikasi baris `Edit` `Client` `Sejahtera {runId}-044` Field `PIC Name` New Value `PIC 178 {runId}-044` tampil tepat satu kali
7. Verifikasi tidak ada dialog yang tampil
8. Verifikasi isi kotak Search tetap `Sejahtera {runId}-044`, sehingga halaman tidak dimuat ulang
9. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-161: Koneksi real-time ditutup saat hubungan entitas berubah (Reassign)

10. Ganti akun: logout, lalu login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
11. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
12. Ketik Search `Partner Uji {runId}-044`, tekan Enter
13. Verifikasi baris Object `Partner` Name `Partner Uji {runId}-044` tampil
14. Pemicu API: Principal me-Reassign Partner `Partner Uji {runId}-044` dari Distributor Alfa ke Distributor Gamma hingga tersimpan
15. Verifikasi koneksi stream ditutup oleh server
16. Muat ulang halaman (F5)
17. Verifikasi Breadcrumb `Activity Log > User Action` tampil
18. Ketik Search `Partner Uji {runId}-044`, tekan Enter
19. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, sehingga log Partner `Partner Uji {runId}-044` tidak tampil lagi untuk Distributor Alfa
20. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
21. Pemicu API: Principal mengembalikan Partner `Partner Uji {runId}-044` ke Distributor Alfa hingga tersimpan

### TC-AC-ACAL-155: Aktor kehilangan akses saat koneksi real-time terbuka

22. Ganti akun: logout, lalu login sebagai Read Only (Distributor Alfa) `Staf RO Alfa {runId}-044` dengan `Spectra.env.AC_DYN_PASSWORD`
23. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
24. Pemicu API: Principal mencabut capability Read Only `Staf RO Alfa {runId}-044` hingga tersimpan
25. Verifikasi koneksi stream ditutup oleh server
26. Muat ulang halaman (F5)
27. Verifikasi toast error `You don't have permission to do this.` tampil
28. Verifikasi sedikitnya satu item menu lain tampil pada sidebar Admin Console
29. Verifikasi menu Activity Log Hidden pada sidebar Admin Console
30. Pemicu API: Principal memulihkan capability Read Only `Staf RO Alfa {runId}-044` hingga tersimpan

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-155, 161, 178).
- Urutan TC di spec berbeda dari urutan sumber: TC-AC-ACAL-178 lebih dulu karena memakai akun hook `before` (Principal), lalu TC-AC-ACAL-161 (Alfa), lalu TC-AC-ACAL-155 (Read Only Alfa) yang mencabut capability akun, sehingga ganti akun minimal.
- Pelaku kedua (Principal) memakai sesi API (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`): bukan konteks kedua, tanpa butir `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka tab dan menu (langkah 1, 11, 23), mengetik dan menutup Search (langkah 2, 9, 12, 18, 20), memutus dan memulihkan koneksi (langkah 3 dan 5), muat ulang halaman (langkah 16, 26), ganti akun (langkah 10, 22), dan pemulihan state (langkah 21 dan 30, hook `after` sebagai cadangan). Pemicu API pada langkah 4 menunggu hingga perubahan tersimpan, sehingga tidak ada langkah tunggu terpisah.
- Asersi tambahan di luar Expected TC (S-03): langkah 13 (log Partner tampil sebelum Reassign) dan langkah 17 serta 28 (Breadcrumb atau item menu lain sebagai anchor sesudah muat ulang, bagian 8b butir 2 dan R-21) menjadi anchor positif sebelum asersi absence pada langkah 19 dan 29. Langkah 8 membuktikan halaman tidak dimuat ulang lewat isi kotak Search yang bertahan. Langkah 27 mengasersi toast penolakan sebagai bagian dari Expected c TC-AC-ACAL-155 ("permintaan ditolak"). Langkah 19 mengasersi detail empty state (ilustrasi `No results found` dan deskripsi `Try adjusting your search or filter.`) di luar Expected c TC-AC-ACAL-161 ("Log Partner tidak tampil lagi untuk Alfa"); detail itu menjadi bukti bahwa hasil Search kosong (S-03).
- Temuan untuk QA:
  - TC-AC-ACAL-155 dan 161 Expected a berisi `-`; hanya Expected b dan c yang diasersi.
  - TC-AC-ACAL-155 tidak menyebut akun Read Only mana yang dicabut ("akun itu" = Read Only Distributor Alfa Pre-setup No 7); spec memakai staf Read Only dinamis milik spec supaya akun Pre-setup (dipakai spec 016) tidak dicabut. TC-AC-ACAL-161 memakai Partner Beta Pre-setup; spec memakai Partner dinamis di jaringan Alfa.
  - TC-AC-ACAL-155 Expected c ("Menu Activity Log Hidden dan permintaan ditolak") tidak menyebut apakah toast tampil sesudah Refresh; spec mengikuti pola direct URL TC-AC-ACAL-29.
  - TC-AC-ACAL-178 tidak menyebut cara memutus koneksi stream selain "network offline"; kemampuan disediakan tim FE/BE.
  - TC-AC-ACAL-161 dan 178 tidak menyebut field PIC Name tujuan; spec memakai nilai bersuffix. Email dan env akun memakai placeholder `{namaCompany}` dan password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
