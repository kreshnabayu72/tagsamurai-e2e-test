---
id: TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi
title: "Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-274
  - TC-GS-USER-275
  - TC-GS-USER-276
  - TC-GS-USER-277
  - TC-GS-USER-278
  - TC-GS-USER-279
  - TC-GS-USER-280
  - TC-GS-USER-281
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE. Spec hanya memilih baris dan tidak menekan aksi di dropdown `Bulk Action`; tidak ada data diubah atau dihapus.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 1 dan 10-22) dibaca saja; Default User `Hendra Gunawan` (No. 1) dan baris akun aktor `Siti Nurhaliza` (No. 2) dipakai pada TC-GS-USER-277 untuk mengamati checkbox disabled. Total baris User List (Login User) pada saat spec berjalan tidak lebih dari 100.
- Data Dinamis, populasi 15 user milik spec, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Active, Division `Finance`, Access `Fixed Asset`, email `<name tanpa spasi huruf kecil>+{runId}-051@qwertysystem.net`:
  - `Dewi Lestari {runId}-051`, `Jane Smith {runId}-051`, `John Doe {runId}-051`
  - `Uji Massal 01 {runId}-051` sampai `Uji Massal 12 {runId}-051` (12 user)
  - Dengan urutan default Name A-Z dan Search `{runId}-051`, halaman 1 (10 baris) memuat tiga user pertama dan `Uji Massal 01` sampai `Uji Massal 07`; halaman 2 memuat `Uji Massal 08` sampai `Uji Massal 12` (5 baris); `Select All` menampilkan 15 records.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus 15 user seed lewat API, bersihkan seleksi, kosongkan Search, kembalikan ukuran halaman dan sort ke default dengan memuat ulang User List.
- Selection Limit entitas tidak diubah dan lebih besar dari jumlah baris yang dipilih (default entitas).
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-051`, tekan Enter

### TC-GS-USER-274: Screening Bulk Action Bar saat 1 baris dicentang

2. Centang baris `Dewi Lestari {runId}-051`
3. Verifikasi urutan elemen bar di kiri Table Tools: Button `Bulk Action`, teks `1 User selected`, Button `Select All (15 records)`, icon `×`

### TC-GS-USER-278: Checkbox header indeterminate saat sebagian baris dicentang (diamati dari seleksi satu baris di langkah 2)

4. Verifikasi checkbox header tampil indeterminate `[-]`

### TC-GS-USER-275: Counter bulk bertambah dan berkurang realtime

5. Verifikasi teks `1 User selected`
6. Centang baris `Jane Smith {runId}-051`
7. Verifikasi teks `2 Users selected`
8. Uncheck baris `Jane Smith {runId}-051`
9. Verifikasi teks `1 User selected`

### TC-GS-USER-276: Icon × menutup bar dan membersihkan seluruh seleksi

10. Centang baris `Jane Smith {runId}-051`
11. Klik icon `×`
12. Verifikasi semua checkbox ter-uncheck
13. Verifikasi bulk bar hilang

### TC-GS-USER-279: Select All memilih seluruh baris lintas halaman lalu berubah jadi Unselect All

14. Centang baris `Dewi Lestari {runId}-051`
15. Klik `Select All (15 records)`
16. Verifikasi counter `15 Users selected`
17. Verifikasi button berganti `Unselect All`
18. Pindah ke halaman 2
19. Verifikasi baris di halaman 2 tetap tercentang
20. Klik `Unselect All`
21. Verifikasi seluruh seleksi hilang
22. Verifikasi bar tertutup

### TC-GS-USER-280: Uncheck satu baris dari kondisi 100% terselect mengembalikan button Select All

23. Pindah ke halaman 1
24. Centang baris `Dewi Lestari {runId}-051`
25. Klik `Select All (15 records)`
26. Uncheck baris `Jane Smith {runId}-051`
27. Verifikasi counter `14 Users selected`
28. Verifikasi button kembali `Select All (15 records)`
29. Verifikasi bar tetap tampil
30. Klik icon `×`

### TC-GS-USER-281: Seleksi bertahan saat pindah halaman, ubah search/filter, dan ubah sort

31. Centang baris `Dewi Lestari {runId}-051`
32. Pindah ke halaman 2
33. Pindah kembali ke halaman 1
34. Verifikasi baris `Dewi Lestari {runId}-051` tetap tercentang
35. Verifikasi counter `1 User selected`
36. Atur ukuran halaman menjadi 100 baris
37. Ganti isi kotak search dengan `John`, tekan Enter
38. Verifikasi counter `1 User selected`
39. Kosongkan Search lewat `(✕)`, tekan Enter
40. Verifikasi baris `Dewi Lestari {runId}-051` tetap tercentang
41. Verifikasi counter `1 User selected`
42. Klik header kolom Email (sort ascending)
43. Verifikasi baris `Dewi Lestari {runId}-051` tetap tercentang
44. Verifikasi counter `1 User selected`

### TC-GS-USER-277: Checkbox header memilih seluruh baris halaman aktif kecuali baris disabled

45. Klik icon `×`
46. Klik checkbox header
47. Verifikasi semua baris halaman aktif tercentang kecuali baris `Hendra Gunawan` dan `Siti Nurhaliza`
48. Verifikasi baris `Hendra Gunawan` (Default User) unchecked dan disabled
49. Verifikasi baris `Siti Nurhaliza` (baris sendiri) unchecked dan disabled
50. Uncheck checkbox header
51. Verifikasi semua baris unchecked
52. Verifikasi bar hilang

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (52 langkah) karena delapan TC Bulk Action Bar berada di satu kelas harness (fungsional, hanya memilih baris), satu layar, dan satu populasi 15 user milik spec. Blok memakai kembali populasi dan Search yang sama; memisahkannya mengulang login, seeding 15 user, dan pembentukan Search. Tidak ada aksi yang mengubah atau menghapus data.
- Urutan TC sumber diubah: TC-GS-USER-278 diamati dari seleksi satu baris yang sama dengan TC-GS-USER-274 (langkah 2); TC-GS-USER-275 melanjutkan seleksi `Dewi Lestari {runId}-051` dari TC-GS-USER-274 (langkah "Centang Dewi Lestari" TC-275 sumber dipenuhi langkah 2); TC-GS-USER-277 paling akhir karena memerlukan ukuran halaman 100 dan Search kosong supaya baris Default User dan baris sendiri berada di halaman aktif, sedangkan TC lain memerlukan Search `{runId}-051` dan dua halaman.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search), 23 (kembali ke halaman 1), 30 dan 45 (membersihkan seleksi dengan icon `×`), 36 (mengatur ukuran halaman 100 baris agar Search yang dikosongkan menampilkan baris `Dewi Lestari {runId}-051` pada halaman yang sama), 18 dan 32 sampai 33 (pindah halaman).
- Asersi tambahan: langkah 5 (counter `1 User selected` sebagai awal urutan Expected TC-GS-USER-275) diamati dari seleksi langkah 2; langkah 38 mengasersi counter saat Search `John` karena baris `Dewi Lestari {runId}-051` tidak cocok dengan Search itu dan tidak tampil.
- Pembagian TC: opsi dropdown `Bulk Action` per kombinasi seleksi diverifikasi di spec 052, Selection Limit di spec 053, dan dialog serta hasil Bulk Activate, Deactivate, dan Delete di spec 054 dan 055.
- Temuan untuk QA:
  - TC-GS-USER-274 menyebut `{N}` = total baris cocok filter tanpa baris disabled tanpa menyebut nilainya; spec menyaring dengan Search `{runId}-051` sehingga N = 15.
  - TC-GS-USER-277 tidak menyebut ukuran halaman atau Search; baris Default User dan baris sendiri hanya berada di halaman aktif bila ukuran halaman cukup besar. Spec memakai 100 baris dan Search kosong.
  - TC-GS-USER-280 langkah 1 menekan `Select All ({N} records)` tanpa langkah yang memunculkan bar; spec mencentang satu baris lebih dulu.
  - TC-GS-USER-281 butir a ("Dewi Lestari tetap tercentang di setiap langkah") tidak dapat diamati pada langkah Search `John` karena baris Dewi tidak tampil; spec mengasersi counter pada langkah itu dan baris Dewi sesudah Search dikosongkan.
  - TC-GS-USER-275, 276, 278, 279, dan 280 tidak menyebut baris yang dicentang; spec memakai seed bernama.
  - TC-GS-USER-274 sampai 281 tanpa Post Condition.
