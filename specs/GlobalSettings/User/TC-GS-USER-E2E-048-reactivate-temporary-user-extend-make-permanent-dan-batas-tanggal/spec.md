---
id: TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal
title: "Reactivate Temporary User: Dialog, Cancel, Validasi Tanggal Kosong, Hari Ini, dan Kemarin, Extend Period, Make Permanent, dan Header Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-252
  - TC-GS-USER-253
  - TC-GS-USER-254
  - TC-GS-USER-255
  - TC-GS-USER-256
  - TC-GS-USER-257
  - TC-GS-USER-258
  - TC-GS-USER-1039
coverage:
  web: automated
---

# Reactivate Temporary User: Dialog, Cancel, Validasi Tanggal Kosong, Hari Ini, dan Kemarin, Extend Period, Make Permanent, dan Header Detail

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, termasuk Budi Hartono No. 16) tidak dipakai sebagai target aksi dan tidak diubah.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Temporary-expired (Temporary User, Temporary Until sudah terlewati), Inactive, Division `Finance`, Access `Fixed Asset`. Cara membuat Temporary Until yang sudah terlewati lewat seeding disediakan tim FE/BE (TC tidak menyebutnya):
  - B-1: Name `Budi Hartono {runId}-048`, email `budihartono+{runId}-048@qwertysystem.net` (TC-GS-USER-252, 255, 1039, 256, 257, 253).
  - B-2: Name `Budi Hartono Permanen {runId}-048`, email `budihartonopermanen+{runId}-048@qwertysystem.net` (TC-GS-USER-254).
  - B-3: Name `Budi Hartono Detail {runId}-048`, email `budihartonodetail+{runId}-048@qwertysystem.net` (TC-GS-USER-258).
- State yang diubah: konfigurasi kolom tabel User List akun aktor (kolom `Temporary User` dan `Temporary Until` ditampilkan, lalu dikembalikan ke default lewat `[Reset to Default]` pada langkah 53 sampai 56). Hook `after` mengembalikan konfigurasi kolom ke default sebagai cadangan.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus B-1, B-2, dan B-3 lewat API.
- Kemampuan teknis: mengisi date picker dengan tanggal hari ini, kemarin, dan hari ini + 7 hari dalam zona waktu client General Settings; membuka Popup Setup Column dari header Column Visibility (⋯).
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-048`, tekan Enter
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`
4. Centang kolom `Temporary User` dan `Temporary Until`
5. Klik `[Save]`
6. Tunggu aksi selesai (Popup Setup Column tertutup dan kolom `Temporary User` dan `Temporary Until` tampil di tabel)

### TC-GS-USER-252: Toggle ON user Temporary-expired memunculkan dialog Reactivate Temporary User

7. Klik switch Active baris `Budi Hartono {runId}-048` (OFF, Temporary-expired)
8. Verifikasi Title dialog `Reactivate Temporary User`
9. Verifikasi dialog memuat bullet `Budi Hartono {runId}-048`
10. Verifikasi dialog memuat `This user's active period has ended. Choose how to reactivate:`
11. Verifikasi Option A `Extend period`
12. Verifikasi Option A memuat date picker
13. Verifikasi Option B `Make permanent`
14. Verifikasi footer `[Cancel]` dan `[Reactivate]`
15. Verifikasi `[Reactivate]` disabled (belum ada opsi dipilih)

### TC-GS-USER-255: Reactivate Temporary, Cancel tanpa memilih membiarkan user Inactive

16. Klik `[Cancel]`
17. Verifikasi switch Active baris `Budi Hartono {runId}-048` tetap OFF
18. Verifikasi tidak ada toast

### TC-GS-USER-1039: Extend period tanpa tanggal menampilkan error inline

19. Klik switch Active baris `Budi Hartono {runId}-048`
20. Pilih `Extend period`, biarkan tanggal kosong
21. Verifikasi `[Reactivate]` enabled
22. Klik `[Reactivate]`
23. Verifikasi error inline di bawah field tanggal `Temporary until must not be empty`
24. Verifikasi dialog tetap terbuka
25. Klik `[Cancel]`
26. Verifikasi switch Active baris `Budi Hartono {runId}-048` tetap OFF

### TC-GS-USER-256: Extend period ke hari ini ditolak

27. Klik switch Active baris `Budi Hartono {runId}-048`
28. Pilih `Extend period`, isi date picker dengan tanggal hari ini
29. Klik `[Reactivate]`
30. Verifikasi error `Please select a future date.`
31. Klik `[Cancel]`
32. Verifikasi switch Active baris `Budi Hartono {runId}-048` tetap OFF

### TC-GS-USER-257: Extend period ke kemarin ditolak

33. Klik switch Active baris `Budi Hartono {runId}-048`
34. Pilih `Extend period`, isi date picker dengan tanggal kemarin
35. Klik `[Reactivate]`
36. Verifikasi error `Please select a future date.`
37. Klik `[Cancel]`
38. Verifikasi switch Active baris `Budi Hartono {runId}-048` tetap OFF

### TC-GS-USER-253: Extend period mengaktifkan user tetap sebagai Temporary

39. Klik switch Active baris `Budi Hartono {runId}-048`
40. Pilih `Extend period`, isi date picker dengan tanggal hari ini + 7 hari
41. Klik `[Reactivate]`
42. Verifikasi toast sukses "Success, user has been activated."
43. Verifikasi switch Active baris `Budi Hartono {runId}-048` ON
44. Verifikasi kolom Temporary User baris `Budi Hartono {runId}-048` `Yes`
45. Verifikasi kolom Temporary Until baris `Budi Hartono {runId}-048` tanggal hari ini + 7 hari

### TC-GS-USER-254: Make permanent menghapus status Temporary

46. Klik switch Active baris `Budi Hartono Permanen {runId}-048`
47. Pilih `Make permanent`
48. Klik `[Reactivate]`
49. Verifikasi toast sukses "Success, user has been activated."
50. Verifikasi switch Active baris `Budi Hartono Permanen {runId}-048` ON
51. Verifikasi kolom Temporary User baris `Budi Hartono Permanen {runId}-048` `No`
52. Verifikasi kolom Temporary Until baris `Budi Hartono Permanen {runId}-048` `—`
53. Klik header kolom Column Visibility (⋯)
54. Klik `[Setup Column]`
55. Klik `[Reset to Default]`
56. Klik `[Save]`

### TC-GS-USER-258: Reactivate Temporary dari header User Detail

57. Buka Detail `Budi Hartono Detail {runId}-048` dengan klik Name
58. Klik switch Active header
59. Verifikasi dialog `Reactivate Temporary User` muncul
60. Verifikasi dialog memuat Option A `Extend period` dan Option B `Make permanent` (bukan dialog Activate biasa)
61. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (61 langkah) karena delapan TC Reactivate Temporary berada di satu kelas harness (fungsional), satu dialog, dan satu dataset user Temporary-expired milik spec. Validasi yang diblokir, Cancel, dan aksi sukses berdiri sendiri pada user seed sendiri atau dialog yang dibuka ulang, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah: screening (TC-GS-USER-252) dan Cancel (TC-GS-USER-255) di awal, lalu validasi yang diblokir (TC-GS-USER-1039, 256, 257), lalu aksi sukses (TC-GS-USER-253 pada B-1 dan TC-GS-USER-254 pada B-2, bagian 3 prinsip 3), lalu TC-GS-USER-258 paling akhir karena pindah ke halaman Detail. Pemulihan konfigurasi kolom (langkah 53 sampai 56) ditaruh sebelum TC-GS-USER-258 karena langkah itu membutuhkan layar User List.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 sampai 6 (Search dan menampilkan kolom `Temporary User` dan `Temporary Until`, yang tersembunyi secara default), 16, 25, 31, 37, 61 (menutup dialog dengan `[Cancel]`), 53 sampai 56 (mengembalikan konfigurasi kolom), 57 (membuka Detail).
- Asersi tambahan: langkah 17, 26, 32, dan 38 (switch tetap OFF sesudah `[Cancel]`) adalah cara mengamati "User tetap Inactive" TC-GS-USER-1039, 256, dan 257 dengan dialog ditutup lebih dulu; langkah 60 membedakan dialog Reactivate Temporary dari dialog Activate biasa (Expected TC-GS-USER-258).
- Dialog ditutup dengan `[Cancel]` (dialog konfirmasi), bukan `✕`; tidak ada form Create atau Edit yang dibuka.
- Temuan untuk QA:
  - TC-GS-USER-252 butir b menyebut "date picker tanggal depan" tanpa menjelaskan apakah date picker menonaktifkan tanggal lampau; TC-GS-USER-256 dan TC-GS-USER-257 memilih hari ini dan kemarin lewat date picker yang sama, sehingga date picker harus mengizinkan tanggal itu. Spec mengisi date picker dengan tanggal tersebut.
  - TC-GS-USER-253 butir c ("Temporary Until tanggal baru") dan TC-GS-USER-253 sampai 254 mengasersi kolom `Temporary User` dan `Temporary Until` yang tersembunyi secara default; TC tidak menyebut langkah menampilkannya. Spec menampilkannya lewat Setup Column dan mengembalikannya.
  - TC-GS-USER-256 dan TC-GS-USER-257 tidak menyebut letak error (inline di bawah field atau toast); spec hanya mengasersi teks `Please select a future date.`
  - TC-GS-USER-255 bertipe Negative padahal Cancel tanpa aksi; spec mengikuti Expected TC.
  - TC memakai Budi Hartono (Pre-setup No. 16) sebagai target aksi tulis; spec memakai seed milik spec (B-1, B-2, B-3) dan TC tidak menyebut cara membuat user Temporary-expired lewat seeding.
  - TC-GS-USER-258 tidak menyatakan cara menutup dialog; spec menutup dengan `[Cancel]`.
