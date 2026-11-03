---
id: TC-FA-FAAM-E2E-080-edit-dialog-default-addon-cancel-dan-hitungan-berubah
title: "Edit Ber-Aset: Cancel Dialog Default Addon Tunggal dan Hitungan Berubah Sebelum Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-728
  - TC-FA-FAAM-743
coverage:
  web: automated
---

# Edit Ber-Aset: Cancel Dialog Default Addon Tunggal dan Hitungan Berubah Sebelum Save

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog, System Log aktor (Detail User aktor > tab System Log), dan Activity Log FAMS sebelum aksi sebagai baseline dengan filter Search yang sama dengan pembandingan sesudah aksi (`Solo Addon Item`), agar jumlah dibandingkan pada cakupan yang sama; asersi memakai selisih terhadap baseline (S-12).
- Data Pre-setup #14p: `Solo Addon Item` (Total Asset 1: aset Active ter-pairing TAG `QR`, tanpa Default Addon; lisensi Tracking tersedia 5), hanya dibuka dan dibatalkan (TC-743). Data Pre-setup #30f: `Race Addon Item` (Total Asset 1: aset Active ter-pairing TAG `QR`, tanpa Default Addon; lisensi Tracking tersedia 5), disimpan oleh TC-728 dan dipulihkan lewat seed reset (disediakan tim FE/BE) di hook `before` dan `after` (S-06).
- State global yang diubah: lisensi Tracking tersedia diturunkan dari 5 menjadi 0 lewat seed API pada TC-728; hook `after` memulihkannya menjadi 5. Suite berjalan serial (`parallel: false`).
- Roster modul Tracking dibuka dalam mode baca; efek lintas modul pada roster itu (aset `Race Addon Item` berstatus `pending_quota`) tersisa sampai seed reset.

## Test Steps

### TC-FA-FAAM-743: Cancel pada dialog Change Default Addon sebagai dialog tunggal membatalkan penyimpanan

1. Ketik Search `Solo Addon Item`, tekan Enter
2. Buka Changelog, System Log aktor, dan Activity Log FAMS satu per satu, ketik Search `Solo Addon Item` pada masing-masing, catat jumlah entri hasil filter sebagai baseline, lalu tutup
3. Klik `⋯` baris `Solo Addon Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Tambahkan Default Addon `Tracking`
5. Klik `[Save]`
6. Klik `[Cancel]` pada dialog `Change Default Addon`
7. Verifikasi dialog tertutup
8. Verifikasi modal Edit tetap terbuka dengan chip `Tracking` dipertahankan
9. Klik `[✕]` pada modal Edit
10. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
11. Klik `[Leave]`
12. Buka Changelog (icon Changelog) dan cari entri `Solo Addon Item`
13. Verifikasi jumlah entri Changelog sama dengan baseline
14. Tutup Modal Changelog
15. Buka System Log (Detail User aktor > tab System Log) dan cari entri `Solo Addon Item`
16. Verifikasi jumlah entri System Log sama dengan baseline
17. Buka Activity Log FAMS dan cari entri `Solo Addon Item`
18. Verifikasi jumlah entri Activity Log sama dengan baseline
19. Buka roster Tracking dan cari aset pada `Solo Addon Item`
20. Verifikasi roster Tracking memuat aset milik Asset Name lain
21. Verifikasi roster Tracking tidak memuat aset pada `Solo Addon Item`

### TC-FA-FAAM-728: Hitungan berubah antara pratinjau D-10 dan Save: Save menghitung ulang tanpa dialog tambahan

22. Buka Fixed Asset > Settings > Asset Master > Asset Name lalu Ketik Search `Race Addon Item`, tekan Enter
23. Klik `⋯` baris `Race Addon Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
24. Tambahkan Default Addon `Tracking`
25. Klik `[Save]`
26. Verifikasi dialog `Change Default Addon` dengan tombol `[Cancel]` dan `[Save]` memuat `Adding Tracking:` dengan klausa `1 asset will be enrolled (5 available licenses).`
27. Turunkan lisensi Tracking tersedia dari 5 menjadi 0 lewat seed API sebelum dialog dikonfirmasi
28. Klik `[Save]` pada dialog
29. Verifikasi toast `Success, asset name has been updated.` tampil
30. Verifikasi modal Edit tertutup
31. Verifikasi tidak ada dialog tambahan
32. Buka roster Tracking (mode baca)
33. Verifikasi aset `Race Addon Item` berstatus `pending_quota`, bukan `enrolled_via_default` seperti angka pada dialog
34. Buka Fixed Asset > Settings > Asset Master > Asset Name, buka Changelog (icon Changelog), lalu ketik Search `Race Addon Item` pada Modal Changelog, tekan Enter
35. Verifikasi entri teratas Changelog: Field `Default Addon`, Old `—`, New `Tracking`
36. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 22, dan 34 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 9 (✕, dialog Unsaved Changes, `[Leave]`, S-08); penutupan Modal Changelog pada langkah 14 dan 36.
- Urutan TC: TC-FA-FAAM-743 (dibatalkan) lebih dulu, lalu TC-FA-FAAM-728 yang menyimpan (S-10). Ketiadaan entri log pada TC-FA-FAAM-743 diasersi sebagai selisih nol terhadap baseline atas aksi yang dibatalkan, bukan asersi absence kelas g; ketiadaan aset di roster didahului `Verifikasi` aset milik Asset Name lain sebagai anchor (bagian 8b butir 2).
- Langkah Uji TC-FA-FAAM-728 "Turunkan lisensi ... lewat seed API sebelum dialog dikonfirmasi" ditulis sebagai langkah pemicu pelaku kedua lewat sesi API aktor (R-20).
- Temuan untuk QA:
  - TC-FA-FAAM-728 Post Condition (roster Tracking menerima aset `pending_quota`) sudah punya langkah observasi pada Expected d; spec mengasersi di roster modul Tracking mode baca.
- Alasan melewati sekitar 35 langkah: dua blok mandiri; TC-FA-FAAM-743 memuat tiga surface log dan roster (pembacaan log menyumbang sekitar tujuh langkah) dan TC-FA-FAAM-728 memuat roster dan Changelog; kegagalan satu blok tidak membuat blok lain kehilangan makna.
