---
id: TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate
title: "Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Efek ke Form User, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-156
  - TC-GS-UCF-157
  - TC-GS-UCF-158
  - TC-GS-UCF-159
  - TC-GS-UCF-160
  - TC-GS-UCF-163
  - TC-GS-UCF-345
coverage:
  web: automated
---

# Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Efek ke Form User, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah status Custom Field milik sendiri dan membaca Changelog yang dibagi suite.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah pertama blok tidak mengulang pembukaan layar kecuali sesudah berpindah halaman.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca, tidak diubah spec ini): 14 Custom Field di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada); `Cost Center` ditampilkan di form Create User sebagai anchor pembanding dan `Employee Grade` (nilai `Grade 5` pada Rahmat Hidayat) sebagai anchor pembanding di Detail User. User `Rahmat Hidayat` (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`, Pre-setup).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.toggleSingle040`; mekanisme seeding nilai Custom Field pada User disediakan tim FE/BE, lihat Temuan untuk QA):
  - `Toggle Probe {runId}-040`: Text; Active; nilai User Rahmat Hidayat = `Visible Text` (TC-GS-UCF-156, 157, 158, 159).
  - `Toggle Cancel {runId}-040`: Text; Active (TC-GS-UCF-160).
  - `Inactive Probe {runId}-040`: Text; Inactive (TC-GS-UCF-160).
  - `Toggle Dbl {runId}-040`: Text; Active (TC-GS-UCF-163).
  - `Toggle Dbl On {runId}-040`: Text; Inactive (TC-GS-UCF-345).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-040` yang masih ada dan nilai Custom Field milik spec pada Rahmat Hidayat.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: klik ganda cepat pada `[Deactivate]` dan `[Activate]` (TC-GS-UCF-163 dan 345); Search tabel Custom Field dan Changelog; menunggu toast sukses lama hilang otomatis (jeda pendek, ≤ 4 detik, TC-GS-UCF-489) pada langkah 50.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite).

## Test Steps

### TC-GS-UCF-160: Cancel dialog Deactivate atau Activate mengembalikan switch ke posisi semula

1. Ketik Search `Toggle Cancel {runId}-040`, tekan Enter
2. Matikan switch Active baris `Toggle Cancel {runId}-040`
3. Klik `[Cancel]`
4. Verifikasi tidak ada toast
5. Verifikasi dialog Deactivate tertutup
6. Verifikasi switch `Toggle Cancel {runId}-040` kembali On
7. Ganti isi kotak search dengan `Inactive Probe {runId}-040`, tekan Enter
8. Nyalakan switch Active baris `Inactive Probe {runId}-040`
9. Klik `[Cancel]`
10. Verifikasi tidak ada toast
11. Verifikasi dialog Activate tertutup
12. Verifikasi switch `Inactive Probe {runId}-040` tetap Off
13. Klik `(←)` pada kotak Search

### TC-GS-UCF-156 dan TC-GS-UCF-157: Dialog Deactivate single dan konfirmasi Deactivate

14. Ketik Search `Toggle Probe {runId}-040`, tekan Enter
15. Matikan switch Active baris `Toggle Probe {runId}-040`
16. Verifikasi dialog `Deactivate Custom Field` menampilkan bullet `Toggle Probe {runId}-040`, body "Deactivating this field will hide it and its data from all user forms. You can reactivate it later. Are you sure you want to deactivate it?", serta tombol `[Cancel]` dan `[Deactivate]`
17. Verifikasi tombol `[Deactivate]` bergaya danger (merah)
18. Verifikasi switch `Toggle Probe {runId}-040` belum berubah (masih On) selama dialog tampil
19. Klik `[Deactivate]`
20. Verifikasi muncul toast sukses: "Success, custom field has been deactivated."
21. Verifikasi switch `Toggle Probe {runId}-040` Off
22. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`, perhatikan section Custom Field dinamis
23. Verifikasi section Custom Field dinamis form Create User memuat field `Cost Center`
24. Verifikasi form Create User tidak memuat field `Toggle Probe {runId}-040`
25. Tutup popup lewat `[✕]`
26. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
27. Verifikasi Detail User Rahmat Hidayat menampilkan `Employee Grade` dengan nilai `Grade 5`
28. Verifikasi Detail User Rahmat Hidayat tidak menampilkan field `Toggle Probe {runId}-040`
29. Buka Global Settings > User > Custom Field

### TC-GS-UCF-158 dan TC-GS-UCF-159: Dialog Activate single dan konfirmasi Activate

30. Ketik Search `Toggle Probe {runId}-040`, tekan Enter
31. Nyalakan switch Active baris `Toggle Probe {runId}-040`
32. Verifikasi dialog `Activate Custom Field` menampilkan bullet `Toggle Probe {runId}-040`, body "Activating this field will make it and its data visible in all user forms. Are you sure you want to activate it?", serta tombol `[Cancel]` dan `[Activate]`
33. Verifikasi tombol `[Activate]` bergaya primary, bukan danger (merah)
34. Klik `[Activate]`
35. Verifikasi muncul toast sukses: "Success, custom field has been activated."
36. Verifikasi switch `Toggle Probe {runId}-040` On
37. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`, perhatikan section Custom Field dinamis
38. Verifikasi form Create User memuat kembali field `Toggle Probe {runId}-040`
39. Tutup popup lewat `[✕]`
40. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
41. Verifikasi Detail User Rahmat Hidayat menampilkan `Toggle Probe {runId}-040` dengan nilai `Visible Text`
42. Buka Global Settings > User > Custom Field

### TC-GS-UCF-163: Klik ganda [Deactivate] hanya memproses satu perubahan

43. Ketik Search `Toggle Dbl {runId}-040`, tekan Enter
44. Matikan switch Active baris `Toggle Dbl {runId}-040`
45. Klik `[Deactivate]` dua kali cepat
46. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been deactivated."
47. Klik icon Changelog, Search `Toggle Dbl {runId}-040`, tekan Enter
48. Verifikasi Changelog memuat tepat 1 entri Deactivate untuk `Toggle Dbl {runId}-040`
49. Tutup modal Changelog dengan `[✕]`

### TC-GS-UCF-345: Klik ganda [Activate] hanya memproses satu perubahan

50. Tunggu toast dari langkah 46 hilang otomatis
51. Ganti isi kotak search dengan `Toggle Dbl On {runId}-040`, tekan Enter
52. Nyalakan switch Active baris `Toggle Dbl On {runId}-040`
53. Klik `[Activate]` dua kali cepat
54. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been activated."
55. Klik icon Changelog, Search `Toggle Dbl On {runId}-040`, tekan Enter
56. Verifikasi Changelog memuat tepat 1 entri Activate untuk `Toggle Dbl On {runId}-040`
57. Tutup modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (57 langkah). Seluruhnya satu kelas (Toggle Active single), satu dataset milik spec; tiap blok memakai field milik sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; blok TC-GS-UCF-156 dan 157 serta 158 dan 159 membentuk rantai pada `Toggle Probe` (Activate hanya bermakna sesudah Deactivate berhasil), sedangkan blok lain berdiri sendiri.
- Urutan TC dalam spec: 160 (tanpa mutasi), 156 dan 157 (dialog yang dibuka pada langkah 15 dipakai bersama), 158 dan 159, 163, 345. Urutan menyimpang dari urutan TC sumber karena TC-GS-UCF-158 membutuhkan `Toggle Probe` Inactive dari TC-GS-UCF-157 dan kasus tanpa mutasi didahulukan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 14, 30, 43, 51 (Search agar baris target tampil), langkah 13 (menutup input Search lewat `(←)`), langkah 25, 29, 39, 42, 49, 57 (menutup popup atau modal dan kembali ke tab Custom Field), dan langkah 50 (menunggu toast sukses lama hilang otomatis supaya hitungan toast pada langkah 54 hanya memuat toast hasil klik ganda).
- Asersi tambahan di luar Expected TC (S-03): langkah 23 (anchor pembanding `Cost Center` untuk absence di form Create User) dan langkah 27 (anchor pembanding `Employee Grade` untuk absence di Detail User).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-157 dan 159 ("efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import"; hanya form Create User dan Detail User yang punya Expected) dan "nilai User tersimpan" TC-GS-UCF-157.
  - TC-GS-UCF-160 mencantumkan Dependensi `TC-GS-UCF-133` (Edit field Inactive) yang tidak berhubungan dengan skenario Cancel Toggle; field `Inactive Probe` pada Precondition dan Data Uji TC-GS-UCF-160 tidak punya ID Data Dinamis `D-nn`. Spec men-seed `Inactive Probe {runId}-040` sebagai field Text Inactive.
  - TC-GS-UCF-156 sampai 163 dan 345 memakai nama field tanpa suffix; spec memakai versi bersuffix `{runId}-040`.
  - Mekanisme seeding nilai Custom Field pada User (`Visible Text`) tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
  - TC-GS-UCF-157 dan 159 menyebut Detail User Rahmat Hidayat tanpa cara mencari user; spec menulis "Buka ... Detail Rahmat Hidayat" sesuai TC.
