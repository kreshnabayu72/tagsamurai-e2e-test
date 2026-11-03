---
id: TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup
title: "User Detail: Foto Profil (Hover Avatar, Dialog Remove Photo dan Cancel, Upload, Ganti ke Recycle Bin, Berkas Korup Ditolak, Hapus dengan Klik Ganda, dan Hapus dengan Deleter Admin)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-335
  - TC-GS-USER-336
  - TC-GS-USER-337
  - TC-GS-USER-338
  - TC-GS-USER-340
  - TC-GS-USER-341
  - TC-GS-USER-343
  - TC-GS-USER-1017
  - TC-GS-USER-1041
coverage:
  web: automated
---

# User Detail: Foto Profil (Hover Avatar, Dialog Remove Photo dan Cancel, Upload, Ganti ke Recycle Bin, Berkas Korup Ditolak, Hapus dengan Klik Ganda, dan Hapus dengan Deleter Admin)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk menahan respons hapus foto pada TC-GS-USER-343).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup: tidak ada yang dibaca atau diubah; Division `Finance` (No. 23) dipakai user seed.
- Data Dinamis, di-seed lewat API di hook `before` (HK1), semuanya Activated, Division `Finance`, Access `Fixed Asset`, dan dibersihkan di hook `after`:
  - `Dewi Lestari {runId}-059`, Email `dewilestari+{runId}-059@qwertysystem.net`, tanpa foto (TC-GS-USER-335 dan 337).
  - `John Doe {runId}-059`, Email `johndoe+{runId}-059@qwertysystem.net`, dengan foto awal berkas `john-{runId}-059.png` (TC-GS-USER-336, 1017, 341, 338, 1041, dan 340).
  - `John Doe B {runId}-059`, Email `johndoeb+{runId}-059@qwertysystem.net`, dengan foto awal berkas `johnb-{runId}-059.png` (TC-GS-USER-343).
  - Berkas foto uji (fixture belum ada, disediakan tim FE): `dewi.png` dan `john3.png` (gambar valid), `corrupt.png` (berkas rusak), serta berkas foto awal kedua user John Doe.
- Kemampuan teknis, disediakan tim FE:
  - Memilih berkas pada input unggah foto dari fixture.
  - Intercept (`Spectra.intercept()`) menahan respons hapus foto pada TC-GS-USER-343 dan menghitung request hapus foto yang terkirim; nama endpoint ditentukan tim FE di tahap script (tidak disebut di TC dan PRD). Intercept dilepas segera setelah klik ganda.
  - Akses File Manager > Recycle Bin dengan akun aktor (Total Control).
- Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): lepas semua intercept, hapus tiga user seed di atas, dan hapus berkas foto uji yang tersisa di Recycle Bin milik user seed.
- State global yang diubah: tidak ada. Item Recycle Bin dan baris Changelog yang tercipta milik user seed.

## Test Steps

### Persiapan

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-335: Hover Avatar user tanpa foto hanya menampilkan [Edit]

2. Klik Name `Dewi Lestari {runId}-059` di User List
3. Hover Avatar header
4. Verifikasi Avatar menampilkan inisial
5. Verifikasi overlay Avatar hanya memuat `[Edit]` (tanpa `[Delete]`)

### TC-GS-USER-336: Hover Avatar user dengan foto menampilkan [Edit] dan [Delete]

6. Kembali ke User List dengan klik Back
7. Klik Name `John Doe {runId}-059` di User List
8. Hover Avatar header
9. Verifikasi overlay Avatar memuat `[Edit]` dan `[Delete]`

### TC-GS-USER-1017 dan TC-GS-USER-341: Screening dialog Remove Photo dan [Cancel] tidak mengubah foto

10. Hover Avatar header → klik `[Delete]`
11. Verifikasi Title dialog `Remove Photo`
12. Verifikasi body dialog `• John Doe {runId}-059` / `This will remove this user's profile photo. Are you sure you want to remove it?`
13. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
14. Klik `[Cancel]`
15. Verifikasi Avatar header tetap menampilkan foto (bukan inisial)

### TC-GS-USER-337: Upload foto dari Detail langsung tersimpan

16. Kembali ke User List dengan klik Back
17. Klik Name `Dewi Lestari {runId}-059` di User List
18. Hover Avatar header → klik `[Edit]`
19. Pilih berkas `dewi.png`
20. Verifikasi toast sukses: "Success, photo has been updated."
21. Verifikasi Avatar header menampilkan foto `dewi.png`
22. Kembali ke User List dengan klik Back
23. Verifikasi Avatar baris `Dewi Lestari {runId}-059` di User List menampilkan foto baru

### TC-GS-USER-338: Ganti foto dari Detail memindahkan foto lama ke Recycle Bin

24. Klik Name `John Doe {runId}-059` di User List
25. Hover Avatar header → klik `[Edit]`
26. Pilih berkas `john3.png`
27. Verifikasi toast sukses: "Success, photo has been updated."
28. Buka File Manager > Recycle Bin
29. Verifikasi foto lama `john-{runId}-059.png` ada di Recycle Bin
30. Catat jumlah item di Recycle Bin sebagai baseline

### TC-GS-USER-1041: Foto korup ditolak dengan toast error dan foto lama tidak berubah

31. Buka Global Settings > User > User List (sub-tab Login User)
32. Klik Name `John Doe {runId}-059` di User List
33. Buka Tab `Changelog`
34. Verifikasi Tab Changelog memuat baris `Edit | Photo` dari penggantian foto di TC-GS-USER-338
35. Catat jumlah baris `Edit | Photo` di Tab Changelog sebagai baseline
36. Hover Avatar header → klik `[Edit]`
37. Pilih berkas `corrupt.png`
38. Verifikasi toast error: "Error, failed to upload photo."
39. Verifikasi Avatar header tetap menampilkan foto `john3.png`
40. Verifikasi jumlah baris `Edit | Photo` di Tab Changelog sama dengan baseline (tidak ada baris baru)
41. Buka File Manager > Recycle Bin
42. Verifikasi foto lama `john-{runId}-059.png` masih ada di Recycle Bin
43. Verifikasi jumlah item di Recycle Bin sama dengan baseline (tidak ada foto baru)

### TC-GS-USER-343: Hapus foto dari Detail, tombol loading selama request

44. Pasang intercept pada respons hapus foto: tahan respons
45. Buka Global Settings > User > User List (sub-tab Login User)
46. Klik Name `John Doe B {runId}-059` di User List
47. Tunggu toast lama hilang otomatis
48. Hover Avatar header → klik `[Delete]` → klik `[Remove]`
49. Verifikasi tombol `[Remove]` dalam state loading
50. Verifikasi tombol `[Remove]` disabled
51. Klik `[Remove]` lagi saat loading
52. Lepas intercept respons hapus foto sehingga respons diteruskan
53. Tunggu aksi selesai (dialog tertutup)
54. Verifikasi hanya 1 request hapus foto yang terkirim
55. Verifikasi hanya 1 toast tampil

### TC-GS-USER-340: Delete foto dari Detail, dialog lalu foto dihapus

56. Kembali ke User List dengan klik Back
57. Klik Name `John Doe {runId}-059` di User List
58. Hover Avatar header → klik `[Delete]`
59. Verifikasi body dialog `• John Doe {runId}-059` / `This will remove this user's profile photo. Are you sure you want to remove it?`
60. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
61. Klik `[Remove]`
62. Verifikasi toast sukses: "Success, photo has been removed."
63. Verifikasi Avatar header kembali menampilkan inisial
64. Buka File Manager > Recycle Bin
65. Verifikasi foto lama `john3.png` ada di Recycle Bin dengan deleter `Siti Nurhaliza` (bukan System)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (65 langkah). Alasan: seluruh blok satu kelas (fungsional) dan satu layar (Avatar di User Detail); tiap blok memakai user seed sendiri (atau urutan state foto yang dibangun berurutan pada `John Doe {runId}-059`), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pembukaan Detail berulang tidak dihitung sebagai alur uji.
- Urutan TC sumber diubah: screening hover (TC-GS-USER-335, 336) dan dialog (TC-GS-USER-1017) di awal; TC-GS-USER-1017 dan 341 digabung pada satu pembukaan dialog Remove Photo (dialog dibuka satu kali, diasersi, lalu `[Cancel]`); TC-GS-USER-1041 sesudah TC-GS-USER-338 (bukan sebelum aksi sukses) karena asersi tidak ada baris `Edit | Photo` baru dan tidak ada foto baru di Recycle Bin membutuhkan anchor positif di surface yang sama (baris `Edit | Photo` dan foto lama dari TC-GS-USER-338); aksi hapus (TC-GS-USER-343, lalu TC-GS-USER-340) di akhir.
- P-1 (S-05): Expected c TC-GS-USER-1041 ("tidak ada baris log `Edit | Photo` baru dan tidak ada foto baru di Recycle Bin") diasersi di spec ini dengan baseline jumlah baris `Edit | Photo` dan jumlah item Recycle Bin, karena konteksnya (foto yang baru diganti pada `John Doe {runId}-059`) dibangun TC-GS-USER-338 di spec ini dan tidak ada spec absence yang memuat aksi nyata untuk TC itu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Back ke User List, buka ulang Detail, buka Tab `Changelog`, buka File Manager > Recycle Bin, mencatat baseline, pasang dan lepas intercept, dan "Tunggu aksi selesai". Langkah "Tunggu toast lama hilang otomatis" (sebelum klik `[Remove]` pada TC-GS-USER-343) menjaga hitungan "hanya 1 toast" tidak tercampur toast sebelumnya. Asersi jumlah Recycle Bin dan jumlah baris `Edit | Photo` sama dengan baseline adalah asersi jumlah, bukan asersi absence kelas g.
- Nama bersuffix mengganti `John Doe` dan `Dewi Lestari` pada bullet dialog dan pada pencarian baris di User List.
- Temuan untuk QA:
  - TC-GS-USER-1041: Expected c tidak menyebut surface log (Modal Changelog User, Tab Changelog Detail, System Log, atau Activity Log); spec memakai Tab Changelog Detail John Doe.
  - TC-GS-USER-338: Expected b ("foto lama ada di Recycle Bin") tidak menyebut nama berkas, deleter, atau cara mengenali foto lama; spec mengenalinya lewat nama berkas foto awal user seed.
  - TC-GS-USER-340: deleter foto di Recycle Bin diasersi `Siti Nurhaliza`; TC-GS-USER-338 tidak menyebut deleter foto lama yang diganti.
  - TC-GS-USER-343: Expected b ("hanya 1 request dan 1 toast") tidak menyebut cara menghitung request; spec memakai intercept yang menghitung request hapus foto. Teks toast tidak disebut; spec hanya mengasersi jumlah toast.
  - TC-GS-USER-343: precondition "Response hapus foto ditahan" tidak menyebut cara menahan respons; disediakan tim FE lewat intercept.
  - TC-GS-USER-337: Expected b ("Avatar di User List menampilkan foto baru") tidak menyebut cara mengenali foto baru; spec membandingkan Avatar dengan keadaan inisial sebelumnya.
