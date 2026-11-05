---
id: TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate
title: "Konkurensi Form Allocate: Client Dihapus, Gate Station Storage, dan App Ganda"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-461
  - TC-AC-LA-462
  - TC-AC-LA-463
  - TC-AC-LA-464
coverage:
  web: automated
---

# Konkurensi Form Allocate: Client Dihapus, Gate Station Storage, dan App Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Klinik Harapan Bunda (#24, FAMS Professional dan SAMS Growth Paid Active) dan Bengkel Cahaya Motor (#23, belum punya Asset Control App) sebagai target perubahan sesi lain, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation OFF (#39). Perubahan sesi lain atas #23 dan #24 (Cancel Subscription, alokasi App) dipulihkan oleh fixture backend yang disediakan tim FE/BE di langkah penghubung antar blok dan hook `after` (S-06, pengecualian 2026-10-30).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): satu Client bersuffix `PT Sejahtera {runId}-080` binaan Distributor PT Maju Bersama dengan term FAMS Professional Paid Active (bentuk PT Sejahtera #19, dihapus oleh blok TC-AC-LA-461 sehingga tidak memakai baris Pre-setup bersama). Nilai nama dan ID Subscription dibaca dari hasil seeding.
- Pelaku kedua: sesi API aktor yang disediakan tim FE (TC tidak menyebut akun pelaku, lihat Temuan untuk QA). Login API tidak dihitung sebagai sesi web; kemampuan dinyatakan sekali di `suite.md`.
- Tabel parameter blok Station dan Storage (dipakai langkah 15 sampai 22):

| Type | Additional Quantity | Pesan gate |
|---|---|---|
| `Asset Control Station` | `2` | `Asset Control Station requires at least one active paid subscription.` |
| `Storage` | `50` | `Storage requires at least one active paid subscription.` |

- State global yang diubah: status Subscription Klinik Harapan Bunda dan Bengkel Cahaya Motor, serta penghapusan Client seed. Dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-461: Client dihapus sesi lain, V-03 mengosongkan Client dan mereset Target dan Type

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera {runId}-080`
3. Pilih Target term FAMS Professional Client itu
4. Pilih Type `Concurrent User`
5. Isi Additional Quantity `3`
6. Pelaku kedua (sesi API) menghapus Client `PT Sejahtera {runId}-080` hingga tersimpan
7. Tunggu aksi selesai
8. Klik `[Submit]`
9. Verifikasi pesan `This client no longer exists. Please select another.`
10. Verifikasi Client dikosongkan
11. Verifikasi opsi Client dimuat ulang
12. Verifikasi Target dan Type ikut di-reset
13. Verifikasi Additional Quantity `3` dipertahankan
14. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-462 dan TC-AC-LA-463: Gate Paid Active gugur sesi lain (Station V-09, Storage V-11)

Untuk setiap baris tabel parameter (langkah 15 sampai 24):

15. Klik `[+ Allocation]`, pilih Client `Klinik Harapan Bunda`, Target `Client-wide`, Type dari tabel, dan isi Additional Quantity dari tabel
16. Pelaku kedua (sesi API) meng-Cancel semua Subscription Paid Active Klinik Harapan Bunda hingga tersimpan
17. Tunggu aksi selesai
18. Klik `[Submit]`
19. Verifikasi pesan gate dari tabel
20. Verifikasi Target dikosongkan
21. Verifikasi Type di-reset
22. Verifikasi Client `Klinik Harapan Bunda` dan Additional Quantity dari tabel dipertahankan
23. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
24. Pulihkan Subscription Klinik Harapan Bunda lewat fixture backend hingga tersimpan

### TC-AC-LA-464: Asset Control App ganda saat Submit serentak

25. Klik `[+ Allocation]`
26. Pilih Client `Bengkel Cahaya Motor`
27. Pilih Target Subscription tanpa App, Type `Asset Control App`, dan isi field wajib lain
28. Pelaku kedua (sesi API) mengalokasikan Asset Control App ke Subscription yang sama hingga tersimpan
29. Tunggu aksi selesai
30. Catat jumlah baris tab Current sebagai baseline (Search tidak aktif)
31. Klik `[Submit]` di sesi pertama
32. Verifikasi pesan `Asset Control App is already active for this subscription.`
33. Verifikasi alokasi tidak dibuat oleh sesi pertama (jumlah baris tab Current sama dengan baseline)
34. Verifikasi field lain dipertahankan
35. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
36. Pulihkan Subscription Bengkel Cahaya Motor lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-462 dan TC-AC-LA-463 memakai langkah yang sama (8b butir 7); langkah 15 sampai 23 diulang dua kali (satu kali per baris tabel parameter) dengan parameter pada tabel Prerequisites.
- Langkah penghubung (S-03): langkah 30 (Catat baseline jumlah baris tab Current tanpa Search, sesudah alokasi pelaku kedua tersimpan dan sebelum `[Submit]` sesi pertama, S-12), langkah 7, 17, 29 (menunggu aksi selesai karena langkah berikutnya berganti sesi, 8b butir 8), 24 dan 36 (memulihkan data Pre-setup lewat fixture backend), langkah dialog `Unsaved Changes` (S-08).
- Penyimpangan data (S-06): TC-AC-LA-461 menghapus PT Sejahtera (Pre-setup #19); spec memakai Client seed milik spec dengan bentuk yang sama agar Pre-setup bersama tidak berubah.
- Langkah 16, 28 (pelaku kedua sesi API) tidak memakai butir `P-2` (sesi API bukan konteks kedua, bagian 3).
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (multi-konteks dengan pelaku kedua sesi API) dan satu pola alur (form Allocate terbuka lalu sesi lain mengubah state); langkah blok 462 dan 463 diulang per baris tabel (8b butir 7).
- Temuan untuk QA:
  - TC-AC-LA-461 sampai 464 tidak menyebut akun dan mekanisme pelaku "sesi lain" (hapus Client, Cancel Subscription, alokasi App); disediakan tim FE.
  - TC-AC-LA-461 Langkah 1 menyebut "Target, Type" tanpa nilai pada TC-AC-LA-462 sampai 464; spec memakai Target dan Type yang dapat dipilih Client itu.
  - TC-AC-LA-464 Expected a menyebut kode S-08 dan V-12 pada judul tetapi Expected hanya memuat pesan V-12; hanya pesan itu yang diasersi. Post Condition "Satu App Active" tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-AC-LA-464 Precondition tidak menyebut Target Subscription Bengkel Cahaya Motor yang dipilih; spec memakai Subscription Paid Active yang belum punya App.
