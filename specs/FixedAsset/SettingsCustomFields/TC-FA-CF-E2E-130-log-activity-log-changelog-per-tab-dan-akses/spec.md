---
id: TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses
title: "Log: Activity Log, Changelog Per Tab, Entri Ganda, dan Akses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-510
  - TC-FA-CF-511
  - TC-FA-CF-512
  - TC-FA-CF-513
coverage:
  web: automated
---

# Log: Activity Log, Changelog Per Tab, Entri Ganda, dan Akses

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha, pengguna Sarah Johnson (Modified By `Sarah J`) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha (Pre-setup #1). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun Master-Crud Company Alpha (Pre-setup #8; Manage asset master data: Create, Read, Update, Delete) `masterCrud_automated_{namaCompany}@qwertysystem.net`, dipakai lewat ganti akun eksplisit (login UI dengan `Spectra.env.FA_MCRUD_PASSWORD`).
- Data Pre-setup: Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`. Data Dinamis: field `AL Check {runId}-130` (tab General) dan `Purchasing Log {runId}-130` (tab Purchasing, Text, Scope General). `Asset Serial Tag` (Required Yes) diedit pada TC-FA-CF-512.
- Kemampuan teknis (disediakan tim FE/BE): interception respons yang menunda respons Save selama 3 detik (Pre-setup #26), hanya untuk mengamati hasil klik ganda (bukan fault injection) dan dilepas segera sesudah klik (langkah 21); membaca jumlah dan isi entri Changelog tab General, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- State global: tidak ada yang diubah.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-510: Activity Log menampilkan Object Custom Fields dan Name field

1. Klik `[+ Custom Field]`, isi Field Name `AL Check {runId}-130`, pilih Data Type `Text` dan Scope `General`, lalu klik `[Submit]`
2. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
3. Buka Reports & Logs > Activity Log > Tab User Action
4. Buka filter Object
5. Verifikasi opsi filter Object memuat `Custom Fields`
6. Pilih opsi `Custom Fields` pada filter Object dan terapkan filter
7. Verifikasi baris `AL Check {runId}-130` bertanda Object `Custom Fields` dan Name `AL Check {runId}-130`

### TC-FA-CF-511: Changelog tiap tab hanya memuat entri grup field tab itu

8. Klik tab `Purchasing`
9. Klik `[+ Custom Field]`, isi Field Name `Purchasing Log {runId}-130`, pilih Data Type `Text` dan Scope `General`, lalu klik `[Submit]`
10. Tunggu aksi selesai (dialog tertutup dan tabel dimuat ulang)
11. Buka Modal Changelog dari tab Purchasing dan temukan baris `Purchasing Log {runId}-130`
12. Verifikasi entri field `Purchasing Log {runId}-130` tampil di Modal Changelog tab Purchasing
13. Tutup Modal Changelog dan klik tab `General`
14. Buka Modal Changelog dari tab General
15. Verifikasi Modal Changelog tab General memuat sedikitnya satu baris
16. Verifikasi entri field `Purchasing Log {runId}-130` tidak tampil di Modal Changelog tab General

### TC-FA-CF-512: Satu aksi tidak menghasilkan entri log ganda atau entri untuk record lain

17. Catat jumlah entri total Changelog tab General, ketik Search `Asset Serial Tag` dan catat jumlah baris hasilnya, sebagai baseline, lalu tutup Modal Changelog
18. Klik row action `⋯` > `Edit` pada baris `Asset Serial Tag`, lalu ubah toggle Required ke No
19. Tunda respons Save 3 detik
20. Klik `[Save]` dua kali cepat
21. Lepas tahanan respons Save
22. Tunggu aksi selesai (modal Edit tertutup dan tabel dimuat ulang)
23. Buka Modal Changelog tab General, ketik Search `Asset Serial Tag`, tekan Enter
24. Verifikasi hasil Search `Asset Serial Tag` bertambah tepat satu baris dibanding baseline, yaitu satu baris baru Edit properti `Required` untuk `Asset Serial Tag` (bukan dua)
25. Klik `(←)` pada kotak Search
26. Verifikasi jumlah entri total Changelog tab General bertambah tepat satu dibanding baseline (tidak ada baris baru untuk field lain)

### TC-FA-CF-513: Activity Log hanya dapat dibuka oleh Total Control dan Read Only

27. Ganti akun: logout, lalu login sebagai pemegang Manage asset master data CRUD `Master-Crud` (Pre-setup #8)
28. Perhatikan menu sidebar dan coba buka Reports & Logs > Activity Log
29. Verifikasi sidebar menampilkan sedikitnya satu menu lain
30. Verifikasi menu Activity Log tidak tersedia bagi pemegang Manage asset master data (Create, Read, Update, Delete)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 510, 511, 512, 513. TC-FA-CF-513 berjalan terakhir karena ganti akun ke `Master-Crud`; hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 27 (ganti akun eksplisit), langkah 19 dan 21 (menunda dan melepas tahanan respons Save; Pre-setup #26; baseline langkah 17 dicatat sebelum penundaan sesuai TC-FA-CF-512), langkah tutup Modal Changelog dan klik tab, "Tunggu aksi selesai" sebelum surface log atau Modal Changelog dibuka (8b butir 8), klik `(←)` pada kotak Search sebelum membaca jumlah entri total, serta pencatatan baseline (S-12).
- TC-FA-CF-512: "tepat satu baris" ditulis sebagai selisih satu baris terhadap baseline jumlah baris hasil Search `Asset Serial Tag` (langkah 24) dan selisih satu entri terhadap baseline jumlah entri total (langkah 26), karena `Asset Serial Tag` adalah field Pre-setup yang entri Changelog-nya tidak unik (S-12).
- Temuan untuk QA:
  - TC-FA-CF-513 Expected klausa kedua ("akses penuh hanya Total Control dan Read Only") tidak punya langkah untuk Total Control dan Read Only; spec hanya mengasersi menu Activity Log tidak tersedia bagi pemegang `Master-Crud`, dan akses Total Control teramati lewat langkah 3 sampai 7 TC-FA-CF-510 di spec ini. Akses Read Only tidak diuji.
  - TC-FA-CF-510 tidak menyebut label tombol terapkan filter Activity Log; spec menulis "terapkan filter".
  - TC-FA-CF-512 tidak menyebut field dan nilai Required yang diubah; spec memakai `Asset Serial Tag` (Required Yes) menjadi No.
  - TC-FA-CF-511 tidak menyebut Scope dan Data Type field Purchasing; spec memakai Text dan Scope `General`.
  - Email akun Master-Crud mengikuti pola Pre-setup #8; env var `FA_MCRUD_PASSWORD` disediakan tim FE.
