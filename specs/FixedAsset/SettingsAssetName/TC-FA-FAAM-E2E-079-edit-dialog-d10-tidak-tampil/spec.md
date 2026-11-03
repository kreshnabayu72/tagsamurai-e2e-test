---
id: TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil
title: "Edit Ber-Aset: Dialog D-10 Tidak Tampil dan Judul Removing Tanpa Klausa"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-707
  - TC-FA-FAAM-708
  - TC-FA-FAAM-709
  - TC-FA-FAAM-710
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog D-10 Tidak Tampil dan Judul Removing Tanpa Klausa

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup (fixture kecil, tidak dapat digandakan): #14r `Zero Addon Item` (Total Asset 1: aset Draft, TAG Type `QR`, tanpa Default Addon; lisensi Tracking tersedia 5; TC-707), #14s `Pending Only Item` (Total Asset 2: Default Addon `Tracking`, dua aset Active berstatus `pending_quota` dan `pending_tag`, tanpa aset `enrolled_via_default` dan tanpa transaksi aktif; TC-708), #14u `Zero Mixed Item` (Total Asset 1: aset Draft, TAG Type `QR`, Category `IT Equipment`, tanpa Default Addon; lisensi Tracking tersedia 5; TC-709), dan #14t `Multi Remove Item` (Total Asset 3: Default Addon `Audit` dan `Tracking`; `Audit` `enrolled_via_default` pada 2 aset tanpa transaksi aktif, aset Tracking semuanya `pending_quota`; hanya dibatalkan, TC-710). TC-707, 708, dan 709 menyimpan; tiap fixture dipulihkan lewat seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri Changelog bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Pohon kategori Pre-setup #22: leaf `Office Equipment`.
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-710: Judul Removing addon tanpa klausa ikut dihilangkan sedangkan addon lain tetap tampil

1. Ketik Search `Multi Remove Item`, tekan Enter
2. Klik `⋯` baris `Multi Remove Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas Default Addon `Audit` dan `Tracking`
4. Klik `[Save]`
5. Verifikasi dialog `Change Default Addon` memuat `Removing Audit:` dengan klausa `2 assets will be unenrolled.`
6. Verifikasi judul `Removing Tracking:` tidak tampil
7. Verifikasi kalimat penutup `Are you sure you want to save this change?` tetap tampil
8. Klik `[Cancel]` pada dialog
9. Tambahkan kembali Default Addon `Audit` dan `Tracking` (kembali ke nilai tersimpan)
10. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-707: Tambah Default Addon tanpa aset Active: D-10 tidak tampil dan Save langsung berjalan

11. Ganti isi kotak search dengan `Zero Addon Item`, tekan Enter
12. Klik `⋯` baris `Zero Addon Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
13. Tambahkan Default Addon `Tracking`
14. Klik `[Save]`
15. Verifikasi toast `Success, asset name has been updated.` tampil
16. Verifikasi modal Edit tertutup
17. Verifikasi dialog `Change Default Addon` tidak tampil karena seluruh klausanya bernilai 0
18. Buka Changelog (icon Changelog) dan ketik Search `Zero Addon Item`, tekan Enter
19. Verifikasi entri teratas Changelog: Field `Default Addon`, Old `—`, New `Tracking`
20. Tutup Modal Changelog

### TC-FA-FAAM-708: Hapus Default Addon yang hanya menyisakan pending_quota dan pending_tag: D-10 tidak tampil

21. Pulihkan `Zero Addon Item` ke keadaan Pre-setup #14r lewat seed reset, lalu Ganti isi kotak search dengan `Pending Only Item`, tekan Enter
22. Klik `⋯` baris `Pending Only Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
23. Lepas Default Addon `Tracking`
24. Klik `[Save]`
25. Verifikasi toast `Success, asset name has been updated.` tampil
26. Verifikasi modal Edit tertutup
27. Verifikasi dialog `Change Default Addon` tidak tampil karena seluruh klausanya bernilai 0
28. Buka Changelog (icon Changelog) dan ketik Search `Pending Only Item`, tekan Enter
29. Verifikasi entri teratas Changelog: Field `Default Addon`, Old `Tracking`, New `—`
30. Tutup Modal Changelog

### TC-FA-FAAM-709: D-10 tidak tampil sedangkan dialog dampak lain tetap tampil menurut urutan

31. Pulihkan `Pending Only Item` ke keadaan Pre-setup #14s lewat seed reset, lalu Ganti isi kotak search dengan `Zero Mixed Item`, tekan Enter
32. Klik `⋯` baris `Zero Mixed Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
33. Ganti Category ke `Office Equipment` dan tambahkan Default Addon `Tracking`
34. Klik `[Save]`
35. Verifikasi dialog `Change Category` dengan teks `1 asset will be moved to Office Equipment. Are you sure you want to save this change?`
36. Klik `[Save]` pada dialog
37. Verifikasi toast `Success, asset name has been updated.` tampil
38. Verifikasi dialog `Change Default Addon` tidak tampil
39. Buka Changelog (icon Changelog) dan ketik Search `Zero Mixed Item`, tekan Enter
40. Verifikasi Changelog memuat baris Edit Field `Category`
41. Verifikasi Changelog memuat baris Edit Field `Default Addon`
42. Tutup Modal Changelog
43. Pulihkan `Zero Mixed Item` ke keadaan Pre-setup #14u lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 11, dan 21 serta 31 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 8; pengembalian addon ke nilai tersimpan pada langkah 9 dan penutupan modal bersih pada langkah 10; penutupan Modal Changelog pada langkah 20, 30, dan 42; pemulihan fixture pada langkah 21, 31, dan 43 (antar-blok, S-09).
- Urutan TC: TC-FA-FAAM-710 (dibatalkan) lebih dulu, lalu TC-FA-FAAM-707, 708, dan 709 yang menyimpan (S-10). Ketiadaan dialog pada TC-FA-FAAM-707, 708, dan 709 diasersi sesudah toast sukses yang menjadi anchor (bagian 8b butir 2); "entri teratas" Changelog dibaca lewat Search nama fixture (urutan Date menurun, suite serial).
- Verifikasi isi dialog TC-FA-FAAM-710 menjadi anchor bagi asersi judul `Removing Tracking:` tidak tampil.
- Temuan untuk QA:
  - TC-FA-FAAM-707, 708, dan 709 menyimpan perubahan pada fixture Pre-setup #14r, #14s, dan #14u langsung; Tabel Data Dinamis tidak memuat salinannya. Fixture dipulihkan seed reset (S-06, pengecualian 2026-10-30), dan pernyataan ini belum tercantum di `suite.md`.
- Alasan melewati sekitar 35 langkah: empat blok satu topik (D-10 tidak tampil) dengan fixture kecil masing-masing yang dipulihkan seed reset antar-blok; kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembacaan Changelog (buka, cari, tutup) per blok dan pemulihan fixture menyumbang sekitar sepertiga langkah.
