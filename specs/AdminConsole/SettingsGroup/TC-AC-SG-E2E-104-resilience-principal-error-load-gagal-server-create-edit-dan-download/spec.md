---
id: TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download
title: "Resilience Principal: Error Load Tabel, Gagal Server pada Create dan Edit, serta Download Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-11
  - TC-AC-SG-105
  - TC-AC-SG-127
  - TC-AC-SG-239
coverage:
  web: automated
---

# Resilience Principal: Error Load Tabel, Gagal Server pada Create dan Edit, serta Download Gagal

## Prerequisites

- Mode: FE+BE. Kegagalan dipaksa dengan intercept parsial di atas backend nyata (bagian 6 konvensi); seluruh state lain nyata.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data Pre-setup: Pohon Uji Utama entitas Principal, 14 group (Pre-setup #16 dan #17), dibaca saja oleh TC-AC-SG-11 dan TC-AC-SG-239. Total record pada TC-AC-SG-11 dicatat (langkah 1) sesudah seeding data milik spec di hook `before`, sehingga total yang diasersi pada langkah 8 sama dengan total yang dicatat.
- Data milik spec: `Region B {runId}-104` (level 1, tanpa entitas) untuk TC-AC-SG-127, di-seed lewat Fixture BE di hook `before` (sebelum langkah 1) dan dihapus hook `after`. Data yang dibuat langkah spec: `Region Gagal {runId}-104` (TC-AC-SG-105), dihapus hook `after`.
- Failure injection (Pre-setup #38; disediakan tim FE): respons 5xx pada pengambilan data Group (list), pada Create Group, dan pada Edit Group, serta Download gagal. Tiap injeksi dinyalakan sebelum aksi pemicu dan dimatikan segera sesudahnya (S-09); hook `after` memastikan semua injeksi mati.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan; disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-11: Error load tabel menampilkan pesan dan tombol Try Again

1. Catat total record pada label root sidebar `All Groups ([N])` sebelum failure injection
2. Aktifkan failure injection: respons 5xx pada pengambilan data Group
3. Buka halaman Settings > Group lewat sidebar
4. Verifikasi area tabel menampilkan "Unable to load this data." dan tombol `[Try Again]`
5. Verifikasi area tabel bukan empty state
6. Nonaktifkan failure injection
7. Klik `[Try Again]`
8. Verifikasi tabel menampilkan data group dengan total record sama dengan total yang dicatat pada langkah 1
9. Verifikasi pesan error "Unable to load this data." hilang
10. Buka halaman Settings > Group lewat sidebar

### TC-AC-SG-105: Gagal server saat Create: popup tetap terbuka dan input dipertahankan

11. Aktifkan failure injection: respons 5xx pada Create Group
12. Klik `[+] Group` di Sidebar Group Tree
13. Ketik `Region Gagal {runId}-104` lalu klik `[Submit]`
14. Verifikasi toast error (persist): "Error, failed to create group."
15. Verifikasi popup New Group tetap terbuka
16. Verifikasi input menampilkan `Region Gagal {runId}-104`
17. Verifikasi `[Submit]` kembali enabled
18. Nonaktifkan failure injection
19. Tutup toast error persisten
20. Klik `[Submit]` lagi
21. Verifikasi toast sukses: "Success, group has been created."
22. Verifikasi hanya satu group `Region Gagal {runId}-104` yang dibuat (satu baris pada tabel dan satu node pada Sidebar Group Tree)

### TC-AC-SG-127: Gagal server saat Edit: popup tetap terbuka dan input dipertahankan

23. Ketik Search `{runId}-104`, tekan Enter
24. Aktifkan failure injection: respons 5xx pada Edit Group
25. Klik ikon `⋯` pada baris `Region B {runId}-104` lalu `Edit`
26. Ubah nama menjadi `Region B Gagal {runId}-104` lalu klik `[Save]`
27. Verifikasi toast error: "Error, failed to update group."
28. Verifikasi popup Edit Group tetap terbuka dengan input `Region B Gagal {runId}-104`
29. Verifikasi `[Save]` enabled
30. Verifikasi nama baris di tabel tetap `Region B {runId}-104`
31. Nonaktifkan failure injection
32. Tutup popup Edit Group dengan `✕`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`
35. Tutup toast error

### TC-AC-SG-239: Download gagal menampilkan toast error

36. Aktifkan failure injection: Download gagal
37. Klik ikon Download pada toolbar
38. Klik "Download as CSV"
39. Verifikasi toast error (persist): "Error, failed to download Groups."
40. Verifikasi tidak ada file terunduh
41. Nonaktifkan failure injection
42. Tutup toast error persisten

## Notes

- Kelas b (fault injection). Pada seluruh blok, pemicu kegagalan adalah objek uji; tidak ada TC kelas lain dalam spec ini.
- Langkah penghubung (S-03, tanpa `Verifikasi`): menyalakan dan mematikan failure injection, pencatatan total record sebelum injeksi (langkah 1), membuka kembali Settings > Group (langkah 10), menutup toast persisten (langkah 19, 35, dan 42; R-12), dan Search `{runId}-104` untuk menemukan baris target (langkah 23; R-16).
- Absence pada langkah 40 (tidak ada file terunduh) didahului `Verifikasi` toast error (langkah 39) sebagai anchor positif; langkah 30 (nama tidak berubah) didahului toast error pada langkah 27.
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (kelas b) dan berdiri sendiri; tiap blok memakai satu injeksi kegagalan pada satu aksi sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Penutupan popup dirty (S-08) dan penutupan toast persisten (R-12) menambah panjang spec.
- Temuan untuk QA:
  - TC-AC-SG-127 menyebut `Region B` Pre-setup dan nama `Region B Gagal`; spec memakai node milik spec `Region B {runId}-104` (S-06).
  - TC-AC-SG-105 Langkah Uji tidak menyebut penutupan toast error (persist) sebelum Submit ulang; spec menambah langkah penghubung agar toast sukses dan toast error tidak tertukar (R-12).
  - TC-AC-SG-239 Expected "tidak ada file terunduh" tidak menyebut cara mengamati unduhan; spec mengasersi tidak ada berkas terunduh pada pengamatan unduhan browser (kemampuan disediakan tim FE).
