---
id: TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout
title: "Resilience Tulis User: Create, Edit, dan Delete Gagal 5xx dengan Form Dipertahankan, Tanpa Foto Yatim dan Tanpa Perubahan Foto Akibat Rollback, serta Retry Create setelah Timeout Tidak Menggandakan User"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-146
  - TC-GS-USER-147
  - TC-GS-USER-194
  - TC-GS-USER-208
  - TC-GS-USER-271
  - TC-GS-USER-987
coverage:
  web: automated
---

# Resilience Tulis User: Create, Edit, dan Delete Gagal 5xx dengan Form Dipertahankan, Tanpa Foto Yatim dan Tanpa Perubahan Foto Akibat Rollback, serta Retry Create setelah Timeout Tidak Menggandakan User

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness b: fault injection, bagian 3 prinsip 13 dan bagian 6 konvensi).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): Position `Staff` dan `Supervisor` (No. 22), Division `Finance` (No. 23), produk `Fixed Asset` (No. 26). Dewi Lestari (No. 12) dan John Doe (No. 18) diganti user seed milik spec karena menjadi target aksi tulis (S-06).
- Berkas foto uji (fixture berkas, disediakan tim FE): `budi.png` (TC-GS-USER-147) dan `john2.png` (TC-GS-USER-208).
- Data Dinamis, di-seed lewat API di hook `before` (HK1), semuanya Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Dewi Lestari {runId}-066`, Email `dewilestari+{runId}-066@qwertysystem.net`, Position `Staff` (target TC-GS-USER-194).
  - `John Doe {runId}-066`, Email `johndoe+{runId}-066@qwertysystem.net`, Position `Staff`, foto profil berkas `john-{runId}-066.png` (foto lama; target TC-GS-USER-208).
  - `Rudi Hakim {runId}-066`, Email `rudihakim+{runId}-066@qwertysystem.net`, Active (target TC-GS-USER-271).
- Data Dinamis yang dibuat lewat UI oleh spec: `Budi Santoso {runId}-066` (First Name `Budi`, Last Name `Santoso {runId}-066`, Email `budisantoso+{runId}-066@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`). Percobaan di TC-GS-USER-146 dan TC-GS-USER-147 digagalkan intercept sehingga tidak ada yang tersimpan; user ini tersimpan hanya oleh percobaan pertama di TC-GS-USER-987 dan dihapus di hook `after`.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD):
  - Respons Create user: jawab 5xx (500) tanpa meneruskan request ke backend (TC-GS-USER-146 dan TC-GS-USER-147). Dilepas segera setelah toast error tampil.
  - Respons Create user: request diteruskan ke backend nyata sehingga user tersimpan di server, tetapi respons ke browser ditahan sampai klien menyatakan timeout (TC-GS-USER-987). Dilepas segera setelah toast error tampil dan sebelum `[Submit]` kedua.
  - Respons Edit user: jawab 5xx (500) tanpa meneruskan request ke backend (TC-GS-USER-194).
  - Respons File Manager saat Save Edit user dengan foto baru: jawab 5xx (500) tanpa meneruskan request ke backend (TC-GS-USER-208).
  - Respons Delete user: jawab 5xx (500) tanpa meneruskan request ke backend (TC-GS-USER-271).
- Kemampuan teknis, disediakan tim FE/BE (tidak ada mekanisme di TC, PRD, atau LLD; endpoint tidak disebut):
  - Seeding user (termasuk foto profil berkas `john-{runId}-066.png`) lewat API.
  - Membaca sumber gambar avatar baris User List untuk dibandingkan dengan baseline.
  - Membaca jumlah file di Global Settings > File Manager dan di Recycle Bin File Manager.
  - Intercept yang meneruskan request ke backend lalu menahan respons ke browser sampai timeout klien.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah, tanpa mengandalkan setup berhasil penuh): lepas semua intercept; hapus lewat API `Dewi Lestari {runId}-066`, `John Doe {runId}-066`, `Rudi Hakim {runId}-066`, dan `Budi Santoso {runId}-066` bila ada; hapus berkas `john-{runId}-066.png` dari File Manager dan Recycle Bin bila masih ada; kembalikan sesi ke akun default suite.

## Test Steps

### Persiapan: baseline File Manager dan Recycle Bin, pembukaan layar

1. Buka Global Settings > File Manager
2. Catat jumlah file di File Manager sebagai baseline F0
3. Buka Global Settings > File Manager > Recycle Bin
4. Catat jumlah file di Recycle Bin sebagai baseline R0
5. Buka Global Settings > User > User List (sub-tab Login User)
6. Klik icon Search, ketik `{runId}-066`, tekan Enter

### TC-GS-USER-146: Create gagal 5xx, form tetap terbuka dengan input dipertahankan

7. Pasang intercept pada respons Create user: jawab 5xx
8. Klik `[+ User]` di Table Tools
9. Isi First Name `Budi`, Last Name `Santoso {runId}-066`, Division `Finance`, Email `budisantoso+{runId}-066@qwertysystem.net`, centang Access `Fixed Asset`
10. Klik `[Submit]`
11. Verifikasi toast error: "Error, failed to create user."
12. Lepas intercept respons Create user
13. Verifikasi popup Create tetap terbuka
14. Verifikasi input First Name, Last Name, Division, Email, dan Access utuh seperti yang diisi
15. Verifikasi tombol `[Submit]` enabled

### TC-GS-USER-147: Create gagal setelah foto dipilih, tidak ada file foto yatim

16. Pasang intercept pada respons Create user: jawab 5xx
17. Hover avatar Photo lalu klik `[Edit]`
18. Pilih file `budi.png`
19. Tunggu toast lama hilang otomatis
20. Klik `[Submit]`
21. Verifikasi toast error: "Error, failed to create user."
22. Lepas intercept respons Create user
23. Verifikasi popup Create tetap terbuka
24. Verifikasi input First Name, Last Name, Division, Email, dan Access utuh seperti yang diisi pada TC-GS-USER-146
25. Klik `✕` pada header Popup Create
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`
28. Buka Global Settings > File Manager
29. Verifikasi jumlah file di File Manager sama dengan baseline F0 (tidak ada file `budi.png` baru)

### TC-GS-USER-194: Edit gagal 5xx, form tetap terbuka dengan perubahan dipertahankan

30. Buka Global Settings > User > User List (sub-tab Login User)
31. Klik icon Search, ketik `{runId}-066`, tekan Enter
32. Pasang intercept pada respons Edit user: jawab 5xx
33. Klik (⋯) baris `Dewi Lestari {runId}-066` → `Edit`
34. Ubah Position ke `Supervisor`
35. Klik `[Save]`
36. Verifikasi toast error: "Error, failed to update user."
37. Lepas intercept respons Edit user
38. Verifikasi popup Edit tetap terbuka
39. Verifikasi Position tetap `Supervisor`
40. Verifikasi tombol `[Save]` enabled
41. Klik `✕` pada header Popup Edit
42. Verifikasi dialog `Unsaved Changes` tampil
43. Klik `[Leave]`

### TC-GS-USER-208: Edit dengan foto, kegagalan simpan foto me-rollback seluruh perubahan

44. Catat sumber gambar avatar baris `John Doe {runId}-066` sebagai baseline avatar
45. Pasang intercept pada respons File Manager saat Save Edit user: jawab 5xx
46. Klik (⋯) baris `John Doe {runId}-066` → `Edit`
47. Hover avatar lalu klik `[Edit]`
48. Pilih file `john2.png`
49. Ubah Position ke `Supervisor`
50. Klik `[Save]`
51. Verifikasi toast error: "Error, failed to update user."
52. Lepas intercept respons File Manager
53. Klik `✕` pada header Popup Edit
54. Verifikasi dialog `Unsaved Changes` tampil
55. Klik `[Leave]`
56. Verifikasi kolom Position baris `John Doe {runId}-066` tetap `Staff`
57. Verifikasi sumber gambar avatar baris `John Doe {runId}-066` sama dengan baseline avatar (foto tidak berubah)
58. Buka Global Settings > File Manager > Recycle Bin
59. Verifikasi jumlah file di Recycle Bin sama dengan baseline R0 (foto lama `john-{runId}-066.png` tidak masuk Recycle Bin)

### TC-GS-USER-271: Delete gagal 5xx, user tetap ada

60. Buka Global Settings > User > User List (sub-tab Login User)
61. Klik icon Search, ketik `{runId}-066`, tekan Enter
62. Pasang intercept pada respons Delete user: jawab 5xx
63. Klik (⋯) baris `Rudi Hakim {runId}-066` → `Delete`
64. Klik `[Delete]` pada dialog konfirmasi
65. Verifikasi toast error: "Error, failed to delete user."
66. Lepas intercept respons Delete user
67. Verifikasi baris `Rudi Hakim {runId}-066` tetap ada di User List
68. Verifikasi dialog Delete tetap terbuka
69. Verifikasi tombol `[Delete]` enabled
70. Klik `[Cancel]` pada dialog Delete

### TC-GS-USER-987: Retry Create setelah timeout tidak menggandakan user

71. Pasang intercept pada respons Create user: request diteruskan ke backend, respons ke browser ditahan sampai timeout
72. Klik `[+ User]` di Table Tools
73. Isi First Name `Budi`, Last Name `Santoso {runId}-066`, Division `Finance`, Email `budisantoso+{runId}-066@qwertysystem.net`, centang Access `Fixed Asset`
74. Klik `[Submit]`
75. Verifikasi toast error: "Connection problem. Please try again."
76. Lepas intercept respons Create user
77. Tunggu toast lama hilang otomatis
78. Klik `[Submit]` lagi
79. Verifikasi inline error `Email already exists` pada field Email
80. Klik `✕` pada header Popup Create
81. Verifikasi dialog `Unsaved Changes` tampil
82. Klik `[Leave]`
83. Ganti isi kotak search dengan `Budi Santoso {runId}-066`, tekan Enter
84. Verifikasi tabel memuat tepat 1 baris `Budi Santoso {runId}-066`

## Notes

- Mode: FE+BE (intercept parsial, kelas harness b: fault injection; bagian 6 konvensi). Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (84 langkah). Alasan: keenam TC berada di satu kelas harness (b, kegagalan atau timeout aksi tulis pada User List), satu akun, dan satu layar; tiap blok TC berdiri sendiri (intercept dan user seed sendiri, intercept dilepas di dalam blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah penutupan form dirty deterministik (S-08), navigasi ke File Manager dan Recycle Bin, dan pencarian ulang setelah berpindah layar.
- Urutan TC sumber diubah: TC-GS-USER-147 ditaruh tepat sesudah TC-GS-USER-146 dan memakai Popup Create yang sama (input TC-GS-USER-146 dipertahankan setelah kegagalan, lalu foto `budi.png` dipilih), sehingga hanya satu pembukaan dan satu penutupan form untuk keduanya; TC-GS-USER-194 dan TC-GS-USER-208 mengikuti. TC-GS-USER-271 tidak menghapus data karena digagalkan intercept, sehingga tidak ditaruh paling akhir; TC-GS-USER-987 berada paling akhir karena membuat satu user yang tersimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Tunggu toast lama hilang otomatis` sebelum `[Submit]` kedua pada teks toast sama (langkah 19 dan 77; toast error "Error, failed to create user." dan "Connection problem. Please try again." dari percobaan sebelumnya harus hilang agar asersi toast berikutnya tidak lolos oleh toast lama), langkah persiapan (membuka File Manager dan Recycle Bin, mencatat baseline F0, R0, dan sumber gambar avatar), membuka User List dan Search `{runId}-066`, memasang dan melepas intercept, `Klik ✕` dan `[Leave]` pada penutupan form dirty (S-08), `[Cancel]` yang menutup dialog Delete, dan Search ulang di akhir TC-GS-USER-987. Verifikasi dialog `Unsaved Changes` adalah bagian penutupan deterministik S-08 dan tidak ada di Expected TC.
- Asersi "tidak ada file foto yatim" (TC-GS-USER-147) dan "Recycle Bin tidak memuat foto lama" (TC-GS-USER-208) ditulis sebagai jumlah file sama dengan baseline (F0 dan R0), bukan sebagai asersi ketiadaan nama berkas, karena `budi.png` adalah berkas fixture dengan nama yang sama di setiap run. Jumlah file yang sama membuktikan tidak ada file baru dan tidak ada foto lama yang berpindah.
- Pembagian TC lintas spec: Create sukses diverifikasi di spec 024, Edit sukses di spec 035, ganti foto Edit di spec 038, dan Delete sukses di spec 050; spec ini hanya memuat jalur kegagalan.
- Temuan untuk QA:
  - TC-GS-USER-146, 194, 208, 147, dan 271 menulis precondition "dibuat gagal 5xx (mock/proxy)" tanpa nama endpoint; spec memicu lewat `Spectra.intercept()` di atas backend nyata dan nama endpoint ditentukan tim FE di tahap script.
  - TC-GS-USER-146, 147, dan 987 memakai Last Name `Santoso` dan Email `budisantoso@qwertysystem.net` tanpa suffix; spec memakai nilai bersuffix `{runId}-066`.
  - TC-GS-USER-147 menyebut berkas `budi.png` dan "cari `budi.png`" di File Manager tanpa baseline; nama berkas fixture sama di setiap run sehingga spec membandingkan jumlah file dengan baseline F0.
  - TC-GS-USER-208 tidak menyebut nama berkas foto lama, nilai Position baru, dan lokasi Recycle Bin; spec memakai berkas seed `john-{runId}-066.png`, Position baru `Supervisor`, dan Recycle Bin di Global Settings > File Manager (PRD F-USER-12 menyebut Recycle Bin File Manager). Expected b ("Foto dan Position tidak berubah") diasersi lewat kolom Position dan sumber gambar avatar di User List.
  - TC-GS-USER-208 tidak menyebut apakah Popup Edit tetap terbuka setelah kegagalan; spec menutupnya lewat `✕` dan `[Leave]` karena form dirty.
    - TC-GS-USER-987 menyebut "toast error" tanpa teks dan tidak menyebut cara menahan respons; spec mengasersi teks `Connection problem. Please try again.` dari error-handling-convention bagian 2 (Timeout / Network) dan memakai intercept yang meneruskan request ke backend lalu menahan respons. Expected "ditolak `Email already exists`" tidak menyebut inline atau dialog; spec memakai inline error di field Email sesuai NC-05 dan V-07.
  - Mekanisme seeding user dengan foto profil, pembacaan jumlah file File Manager dan Recycle Bin, dan intercept yang meneruskan lalu menahan respons tidak punya sumber di TC, PRD, atau LLD; disediakan tim FE/BE.
