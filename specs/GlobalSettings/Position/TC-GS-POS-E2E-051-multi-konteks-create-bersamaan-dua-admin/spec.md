---
id: TC-GS-POS-E2E-051-multi-konteks-create-bersamaan-dua-admin
title: "Multi-Konteks: Create Position Bersamaan oleh Dua Admin dengan Nama Sama dan pada Slot Limit Terakhir"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-269
  - TC-GS-POS-270
coverage:
  web: automated
---

# Multi-Konteks: Create Position Bersamaan oleh Dua Admin dengan Nama Sama dan pada Slot Limit Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun Sesi A (Admin A): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B): Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`.
- Akun Super Admin Admin Console `superAdminAdminConsole_automated_{namaPrincipal}@qwertysystem.net`, kredensial `Spectra.env.AC_TC_PASSWORD`, dipakai untuk mengubah Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` dan berada di Global Settings > User > Position pada entitas yang sama. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat oleh langkah spec, bersuffix per run): `Business Development Lead {runId}-051` (TC-GS-POS-269), `Audit Lead {runId}-051` dan `Audit Officer {runId}-051` (TC-GS-POS-270; salah satunya tersimpan, yang lain ditolak).
- Hook `before` mencatat nilai awal Master Data Count Limit entitas dan memastikan tiga nama di atas belum ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Sesi A dan Sesi B) dan hook `after` memulihkannya; lihat `suite.md`.
- Nilai N (TC-GS-POS-270): hook `before` membaca jumlah total Position entitas lewat API (`totalRecords` pada respons `POST /v2/iam/positions/list`, openapi.yaml:38; pembacaan oleh hook disediakan tim FE/BE) dan mencatatnya sebagai T. TC-GS-POS-269 menambah tepat satu record (Sesi A), sehingga pada langkah 14 jumlah total N = T + 1; Master Data Count Limit diubah menjadi N + 1 sehingga sisa kuota tinggal 1.
- State global yang diubah: Master Data Count Limit entitas (langkah 14). Hook `after` memulihkan ke nilai awal yang dicatat di `before`, walau spec gagal di tengah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `Business Development Lead {runId}-051`, `Audit Lead {runId}-051`, dan `Audit Officer {runId}-051` bila ada; pulihkan Master Data Count Limit; tutup konteks Sesi B; kembalikan sesi ke akun default suite.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Position; layar awal dibuka di hook ini sehingga `## Test Steps` tidak mengulang langkah buka.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; dua klik `[Submit]` dikirim hampir bersamaan (paralel) pada langkah 21; perubahan System Limits oleh akun Super Admin Admin Console dijalankan lewat kemampuan yang disediakan tim FE/BE; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.

## Test Steps

### TC-GS-POS-269: Create bersamaan dengan nama sama oleh 2 admin

1. [Sesi A] Klik `[+ Position]`
2. [Sesi B] Klik `[+ Position]`
3. [Sesi A] Ketik `Business Development Lead {runId}-051` pada field Position Name
4. [Sesi B] Ketik `Business Development Lead {runId}-051` pada field Position Name
5. [Sesi A dan Sesi B] Tunggu ±500 ms (debounce pengecekan keunikan)
6. [Sesi A] Klik `[Submit]`
7. [Sesi A] Verifikasi toast sukses: "Success, position has been created."
8. [Sesi B] Klik `[Submit]`
9. [Sesi B] Verifikasi error inline "Position Name already exists" pada field Position Name
10. [Sesi B] Verifikasi Popup Create Position tetap terbuka
11. [Sesi B] Klik `✕` di header Popup Create Position
12. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
13. [Sesi B] Klik `[Leave]`

### TC-GS-POS-270: Create bersamaan pada slot Master Data Count Limit terakhir

14. Super Admin Admin Console mengubah Master Data Count Limit entitas menjadi N + 1 (N dari Prerequisites) sehingga sisa kuota tinggal 1
15. Tunggu aksi selesai (limit tersimpan)
16. [Sesi A] Klik `[+ Position]`
17. [Sesi B] Klik `[+ Position]`
18. [Sesi A] Ketik `Audit Lead {runId}-051` pada field Position Name
19. [Sesi B] Ketik `Audit Officer {runId}-051` pada field Position Name
20. [Sesi A dan Sesi B] Tunggu ±500 ms (debounce pengecekan keunikan)
21. [Sesi A dan Sesi B] Klik `[Submit]` hampir bersamaan
22. Tetapkan peran hasil: sesi yang menerima toast sukses disebut Sesi pemenang, sesi lainnya Sesi penolak
23. [Sesi pemenang] Verifikasi toast sukses: "Success, position has been created."
24. [Sesi penolak] Verifikasi dialog `Limit Reached` tampil dengan body "You've reached the position limit for this workspace." dan tombol `[OK]`
25. [Sesi penolak] Verifikasi tidak ada error inline "Position Name already exists" pada field Position Name
26. [Sesi penolak] Klik `[OK]`
27. [Sesi penolak] Verifikasi Popup Create Position tetap terbuka
28. [Sesi penolak] Klik `✕` di header Popup Create Position
29. [Sesi penolak] Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
30. [Sesi penolak] Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c. Spec serial karena mengubah Master Data Count Limit (state global); batas kuota Position baru yang diuji ada di TC-GS-POS-270.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: TC-GS-POS-269 lebih dulu karena tidak mengubah state global, TC-GS-POS-270 sesudahnya karena mengubah Master Data Count Limit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 20 (menunggu debounce supaya kedua form belum menampilkan error sebelum `[Submit]`); langkah 11, 13, 28, dan 30 (aksi `✕` dan `[Leave]`) serta langkah 12 dan 29 (`Verifikasi` dialog `Unsaved Changes` tambahan agar penutupan form Create yang dirty deterministik, S-08; teks dialog dari PRD §4.2d Dialog 5, diasersi sebagai satu elemen dengan judul, body, dan tombol disebut utuh); langkah 14 (mengubah kuota) dan langkah 15 (menunggu aksi selesai: limit tersimpan, sebelum Sesi A membuka form); langkah 22 (penetapan peran hasil).
- Langkah 22 bukan langkah bersyarat: kedua sesi mengirim `[Submit]` bersamaan dan TC menyatakan "satu sesi" mendapat toast sukses tanpa menyebut sesi mana; harness menetapkan perannya dari hasil. Langkah 23 sampai 30 dijalankan pada sesi berperan itu.
- Jumlah pembukaan form: empat (langkah 1, 2, 16, 17); kejadian menutup form: dua lewat `✕` (langkah 11 sampai 13 dan 28 sampai 30) dan dua lewat submit yang berhasil (Sesi A pada TC-GS-POS-269 dan Sesi pemenang pada TC-GS-POS-270); tertutupnya form setelah submit sukses tidak diasersi (tidak ada di Expected TC).
- Dialog `Limit Reached` dan body-nya mengikuti PRD §4.2d Dialog 6; `[OK]` ditambahkan karena dialog memakai Single Dismiss Rule. Verifikasi "form tetap terbuka" (langkah 27) dilakukan sesudah `[OK]` karena dialog menutupi form selama tampil.
- P-2 (pemicu bukan objek uji): kuota Master Data Count Limit pada TC-GS-POS-270 (langkah 14) hanya memicu state "sisa kuota tinggal 1"; objek uji spec ini adalah race dua sesi admin (kelas c), bukan volume data (kelas e). Perubahan kuota dilakukan oleh akun Super Admin Admin Console lewat kemampuan yang disediakan tim FE/BE dan tidak diasersi di UI Admin Console; kuota dipulihkan di hook `after`.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-269 ("Hanya 1 record `Business Development Lead`") dan TC-GS-POS-270 ("Tepat 1 record baru") tidak punya langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-270 tidak menyebut sesi mana yang mendapat toast sukses; spec memakai penetapan peran dari hasil (langkah 22).
  - TC-GS-POS-270 butir b menyebut "form tetap terbuka" bersamaan dengan Dialog Limit Reached; spec mengasersinya sesudah `[OK]` (langkah 27).
  - Cara mengubah Master Data Count Limit dan memulihkannya (UI Admin Console atau seeding API) tidak didefinisikan di TC; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE tanpa menyebut endpoint.
