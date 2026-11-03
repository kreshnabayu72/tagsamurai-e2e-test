---
id: TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal
title: "Bulk Action Bar sub-tab Active: Screening, Counter, Checkbox Header, Menu Campuran, Cancel Bulk Suspend, dan Seleksi Dibersihkan Setelah Aksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-202
  - TC-AC-ACC-203
  - TC-AC-ACC-204
  - TC-AC-ACC-210
  - TC-AC-ACC-216
  - TC-AC-ACC-217
coverage:
  web: automated
---

# Bulk Action Bar sub-tab Active: Screening, Counter, Checkbox Header, Menu Campuran, Cancel Bulk Suspend, dan Seleksi Dibersihkan Setelah Aksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup: C-01 `PT Sejahtera Abadi` (Active) dan C-06 `PT Maju Bersama` (Active, Derived) hanya dibaca; C-07 `PT Cahaya Baru` (FAMS Waiting for Approval) dan C-08 `PT Mulai Esok` (FAMS Pending), keduanya Active, disuspend lewat Bulk Suspend (TC-AC-ACC-217) lalu dipulihkan dengan Bulk Unsuspend (S-06; TC tidak menyebut Client untuk TC-AC-ACC-216 dan 217, lihat Temuan). Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated kedua Client bertambah.
- Sub-tab Active memuat lebih dari satu halaman baris (populasi Tabel A2/A3), sehingga {N} pada `Select All ({N} records)` berupa angka.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-202: Screening Bulk Action Bar sub-tab Active

1. Klik sub-tab Active, ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Centang baris `PT Sejahtera Abadi`
3. Verifikasi Bulk Action Bar memuat berurutan: `Bulk Action` (dropdown trigger), "1 client selected", `Select All ({N} records)`, dan ikon (X)
4. Klik `Bulk Action`
5. Verifikasi menu hanya memuat `Suspend`
6. Verifikasi `Unsuspend` disembunyikan (semua terpilih Active)
7. Tutup menu Bulk Action, lalu klik ikon (X) pada Bulk Action Bar

### TC-AC-ACC-203: Counter bulk realtime dan dismiss lewat (X)

8. Klik `(←)` pada kotak Search untuk menampilkan seluruh baris sub-tab Active
9. Centang dua baris pertama
10. Verifikasi Bulk Action Bar menampilkan "2 clients selected"
11. Uncheck satu baris
12. Verifikasi Bulk Action Bar menampilkan "1 client selected"
13. Klik ikon (X)
14. Verifikasi seleksi dibatalkan (tidak ada baris tercentang)
15. Verifikasi Bulk Action Bar tertutup

### TC-AC-ACC-204: Checkbox header: Select All halaman dan state indeterminate

16. Klik checkbox header
17. Verifikasi semua baris halaman checked
18. Uncheck satu baris
19. Verifikasi checkbox header berstatus Indeterminate
20. Uncheck semua baris yang tersisa
21. Verifikasi Bulk Action Bar hilang

### TC-AC-ACC-210: Bulk campuran Active + Client Derived di sub-tab Active menampilkan Suspend dan tidak menampilkan Unsuspend

22. Ketik Search `PT Sejahtera Abadi`, tekan Enter
23. Centang baris `PT Sejahtera Abadi`
24. Ganti isi Search dengan `PT Maju Bersama`, tekan Enter
25. Centang baris `PT Maju Bersama` (Derived)
26. Klik `Bulk Action`
27. Verifikasi menu Bulk Action memuat `Suspend`
28. Verifikasi `Unsuspend` tidak ada di menu (disembunyikan di sub-tab Active)
29. Tutup menu Bulk Action, lalu klik ikon (X) pada Bulk Action Bar

### TC-AC-ACC-216: Cancel dialog Bulk Suspend

30. Ganti isi Search dengan `PT Cahaya Baru`, tekan Enter, lalu centang barisnya
31. Ganti isi Search dengan `PT Mulai Esok`, tekan Enter, lalu centang barisnya
32. Klik `Bulk Action` → pilih `Suspend`
33. Klik `[Cancel]` pada dialog
34. Verifikasi dialog tertutup
35. Verifikasi seleksi dipertahankan: Bulk Action Bar menampilkan "2 clients selected"
36. Verifikasi baris `PT Mulai Esok` tetap tercentang di sub-tab Active
37. Ganti isi Search dengan `PT Cahaya Baru`, tekan Enter
38. Verifikasi baris `PT Cahaya Baru` tetap tercentang dan berstatus Active di sub-tab Active

### TC-AC-ACC-217: Seleksi bulk setelah aksi selesai

39. Klik `Bulk Action` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog
40. Tunggu aksi selesai (dialog tertutup)
41. Verifikasi Bulk Action Bar tertutup
42. Verifikasi tidak ada baris tercentang
43. Klik sub-tab Suspended, ketik Search `PT Cahaya Baru`, tekan Enter, lalu centang barisnya
44. Ganti isi Search dengan `PT Mulai Esok`, tekan Enter, lalu centang barisnya
45. Klik `Bulk Action` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas enam TC satu topik (Bulk Action Bar sub-tab Active), satu akun; blok tanpa perubahan data (TC-AC-ACC-202, 203, 204, 210, 216) mendahului blok yang mengubah status (TC-AC-ACC-217, di akhir); tiap blok memakai seleksi sendiri sehingga tetap bermakna walau blok sebelumnya gagal.
- Seleksi TC-AC-ACC-216 dipertahankan dan dipakai TC-AC-ACC-217 (dialog Bulk Suspend dibuka ulang dari seleksi yang sama; pembukaan dialog baru tetap satu per kejadian).
- Langkah penghubung (tanpa awalan Verifikasi): menutup menu Bulk Action dan klik (X) (langkah 7, 29), klik `(←)` pada Search untuk menampilkan seluruh baris (langkah 8), "Tunggu aksi selesai" (langkah 40), dan pemulihan Bulk Unsuspend (langkah 43 sampai 45; langkah di akhir TC-AC-ACC-217). Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-202, 203, 204, 210, 216, 217: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-203 dan 204 menyebut "2 baris" dan "baris halaman" tanpa Client dan tanpa Search; spec memakai dua baris pertama sub-tab Active dan baris halaman saat ini. TC-AC-ACC-216 dan 217 ("Pilih 2 baris", "Bulk Suspend 2 baris sukses") tidak menyebut Client; spec memakai C-07 `PT Cahaya Baru` dan C-08 `PT Mulai Esok`.
  - TC-AC-ACC-217 Expected tidak menyebut toast sukses; spec tidak mengasersi toast.
  - TC-AC-ACC-203 dan 204 berlabel `FE Test: UI Only` dan 216/217 `Need API`; semua dijalankan di atas backend nyata dalam spec ini.
