---
id: TC-GS-FILEMGR-E2E-027-auto-transition-ganti-dan-hapus-foto-profil
title: "Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto Lama ke Recycle Bin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-106
  - TC-GS-FILEMGR-107
  - TC-GS-FILEMGR-239
  - TC-GS-FILEMGR-240
  - TC-GS-FILEMGR-265
coverage:
  web: automated
---

# Auto-Transition: Ganti dan Hapus Foto Profil (User, My Profile, Non-Login User) Memindahkan Foto Lama ke Recycle Bin

## Prerequisites

- Mode: FE+BE (alur lintas modul: File Manager, User, My Profile, Non-Login User).
- Akun aktor 1 (awal spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Dipakai untuk TC-GS-FILEMGR-106, 239, 107, 240.
- Akun aktor 2 (ganti akun di langkah 34 dan 35): Read Only Rina Pratiwi `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_RO_PASSWORD`. Dipakai untuk TC-GS-FILEMGR-265. Hook `after` mengembalikan sesi ke akun default suite (Total Control Sinta Maharani, `GS_TC_PASSWORD`) karena spec berakhir di Rina. Nama env `GS_TC_PASSWORD` dan `GS_RO_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run; pemilik adalah user klon milik spec dengan nama tampil seperti TC, disediakan tim FE agar user Pre-setup tidak diubah, S-06; email klon bersuffix `{runId}-027`):
  - TC-GS-FILEMGR-106: user klon `Budi Santoso` dengan foto aktif `budi-avatar-{runId}-027.jpg`; file pengganti `budi-new-{runId}-027.png`.
  - TC-GS-FILEMGR-107: user klon `Rudi Hartono` dengan foto aktif `rudi-hartono-{runId}-027.png`.
  - TC-GS-FILEMGR-239: foto profil aktif akun aktor Sinta Maharani `sinta-photo-{runId}-027.jpg` (Sinta tidak memiliki foto sebelum seeding; hook `after` menghapus foto yang di-seed dan hasil penggantian sehingga akun kembali tanpa foto, efek pada Last Updated akun Sinta dicatat); file pengganti `sinta-new-{runId}-027.png`.
  - TC-GS-FILEMGR-240: Non-Login User klon `Gita Permata` dengan foto aktif `gita-photo-{runId}-027.jpg`; file pengganti `gita-new-{runId}-027.png`.
  - TC-GS-FILEMGR-265 (D08): foto profil aktif akun Rina Pratiwi `rina-photo-{runId}-027.jpg` (JPG; Rina tidak memiliki foto sebelum seeding; sesudah spec foto kosong).
- Kemampuan teknis (disediakan tim FE/BE, mekanisme dan selektor tidak tercantum di TC; lihat Temuan untuk QA): seeding foto profil aktif untuk user klon, Non-Login User klon, dan akun aktor; langkah UI ganti/hapus foto profil di Global Settings > User > Detail User, My Profile, dan Global Settings > Non-Login User > Detail; file gambar fisik untuk foto pengganti; jam server dan jam browser sinkron (asersi Deleted Date, S-12); membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen seluruh file seed, hapus user dan Non-Login User klon, hapus foto profil akun Sinta dan Rina yang tersisa, kembalikan sesi ke akun default suite.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-106: Ganti foto di Global Settings > User

1. Buka Global Settings > User > Detail User Budi Santoso (klon milik spec)
2. Ganti foto profil dengan `budi-new-{runId}-027.png`, lalu klik [Save]
3. Verifikasi tidak ada toast terkait File Manager selain toast hasil Save modul User
4. Buka Global Settings > File Manager, lalu ketik Search `{runId}-027`, tekan Enter
5. Verifikasi tabel utama menampilkan `budi-new-{runId}-027.png`
6. Verifikasi tabel utama tidak lagi menampilkan `budi-avatar-{runId}-027.jpg`
7. Klik tombol Recycle Bin di toolbar, ketik Search `budi-avatar-{runId}-027`, tekan Enter
8. Verifikasi `budi-avatar-{runId}-027.jpg` tampil di Recycle Bin dengan Deleted By `System`
9. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-239: Ganti foto lewat My Profile

10. Buka My Profile
11. Ganti foto profil dengan `sinta-new-{runId}-027.png`, lalu klik [Save]
12. Buka Global Settings > File Manager, lalu ketik Search `sinta`, tekan Enter
13. Verifikasi tabel utama menampilkan `sinta-new-{runId}-027.png` sebagai foto aktif
14. Klik tombol Recycle Bin di toolbar, ketik Search `sinta-photo-{runId}-027`, tekan Enter
15. Verifikasi `sinta-photo-{runId}-027.jpg` tampil di Recycle Bin dengan Deleted By `System`
16. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-240: Ganti foto Non-Login User

17. Buka Global Settings > Non-Login User > Detail Gita Permata (klon milik spec)
18. Ganti foto dengan `gita-new-{runId}-027.png`, lalu klik [Save]
19. Buka Global Settings > File Manager, lalu ketik Search `{runId}-027`, tekan Enter
20. Verifikasi tabel utama menampilkan `gita-new-{runId}-027.png` sebagai foto aktif
21. Klik tombol Recycle Bin di toolbar, ketik Search `gita-photo-{runId}-027`, tekan Enter
22. Verifikasi `gita-photo-{runId}-027.jpg` tampil di Recycle Bin dengan Deleted By `System`
23. Tutup modal Recycle Bin dengan `✕` di header

### TC-GS-FILEMGR-107: Hapus foto profil tanpa pengganti

24. Buka Global Settings > User > Detail User Rudi Hartono (klon milik spec)
25. Hapus foto profil, lalu klik [Save]
26. Verifikasi tidak ada toast terkait File Manager selain toast hasil Save modul User
27. Buka Global Settings > File Manager, lalu ketik Search `rudi-hartono-{runId}-027`, tekan Enter
28. Verifikasi empty state "No results found" pada tabel utama (`rudi-hartono-{runId}-027.png` hilang dari tabel utama)
29. Klik tombol Recycle Bin di toolbar, ketik Search `rudi-hartono-{runId}-027`, tekan Enter
30. Verifikasi `rudi-hartono-{runId}-027.png` tampil di Recycle Bin dengan Deleted By `Sinta M`
31. Tutup modal Recycle Bin dengan `✕` di header
32. Buka Global Settings > User > Detail User Rudi Hartono (klon milik spec)
33. Verifikasi foto profil Rudi Hartono kosong

### Ganti akun ke Read Only

34. Logout dari Total Control Sinta Maharani
35. Login sebagai Read Only Rina Pratiwi

### TC-GS-FILEMGR-265: Pemilik menghapus foto sendiri lewat My Profile

36. Buka My Profile
37. Hapus foto profil sendiri, lalu konfirmasi
38. Buka Global Settings > File Manager, lalu ketik Search `rina-photo-{runId}-027`, tekan Enter
39. Verifikasi empty state "No results found" pada tabel utama (`rina-photo-{runId}-027.jpg` hilang dari tabel utama)
40. Klik tombol Recycle Bin di toolbar, ketik Search `rina-photo-{runId}-027`, tekan Enter
41. Verifikasi `rina-photo-{runId}-027.jpg` tampil di Recycle Bin dengan Deleted By `Rina P`
42. Tutup modal Recycle Bin dengan `✕` di header
43. Klik ikon Changelog di toolbar, ketik Search `rina-photo-{runId}-027`, tekan Enter
44. Verifikasi Changelog memuat tepat satu baris Action `Delete`, File Name `rina-photo-{runId}-027.jpg`, Field `File Name`, Old Value `rina-photo-{runId}-027.jpg`, New Value `—`, Modified By `Rina P`
45. Tutup modal Changelog dengan `✕` di header
46. Buka My Profile
47. Verifikasi foto profil Rina Pratiwi kosong

## Notes

- Mode: FE+BE (alur lintas modul). Subjudul `###` memetakan langkah ke id TC granular. Spec memakai dua akun dengan Step ganti akun eksplisit (langkah 34 dan 35); bagian Rina tetap bermakna walau bagian Sinta gagal.
- Spec melewati sekitar 35 langkah (47 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: semua blok satu topik (auto-transition foto profil lintas modul) dengan user klon dan file seed sendiri-sendiri; bagian akun Rina (Step ganti akun eksplisit, langkah 34 dan 35) tetap bermakna walau bagian Sinta gagal (bagian 3 pengecualian ganti akun eksplisit).
- Urutan TC pada spec: 106, 239, 240, 107, 265. Penggantian foto (tidak menghabisi file) lebih dulu, penghapusan foto tanpa pengganti sesudahnya, lalu bagian akun Rina di akhir (ganti akun, prinsip 3 dan 5).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 10, 17, 24, 36, 46 (navigasi ke modul asal), 4, 12, 19, 27, 38 (membuka File Manager dan Search untuk menemukan baris target), 9, 16, 23, 31, 42 (menutup modal Recycle Bin), 43 dan 45 (membuka dan menutup Changelog), 34 dan 35 (ganti akun).
- Asersi tambahan di luar Expected TC (S-03): langkah 28 dan 39 (empty state "No results found" sebagai anchor absence baris, Expected "hilang dari tabel utama"), langkah 32 dan 33 (TC-GS-FILEMGR-107 Expected c: foto profil Rudi Hartono kosong, dibaca di Detail User), 46 dan 47 (TC-GS-FILEMGR-265 Expected c).
- Temuan untuk QA:
  - Q-9: aksi ganti/hapus foto profil dilakukan di modul User, My Profile, dan Non-Login User; langkah UI dan selektor modul lain tidak didefinisikan di TC ini. Spec menulis langkah sebagai pemicu dan menandai selektor "disediakan tim FE".
  - Q-5: TC-GS-FILEMGR-239 dan 265 mengubah foto akun aktor Pre-setup (Sinta Maharani, Rina Pratiwi) yang juga akun login suite; TC menyebut foto aktif `sinta-photo.jpg` dan D08 `rina-photo.jpg` yang tidak ada di Tabel A1/A2. Spec men-seed foto bersuffix pada akun tersebut dan menghapusnya di hook `after`; efek pada Last Updated akun dicatat di Prerequisites. Alternatif akun klon belum bisa karena TC-GS-FILEMGR-239 dan 265 mensyaratkan login sebagai pemilik foto.
  - Q-5/Q-7: TC menargetkan baris Pre-setup F01 (`budi-avatar.jpg`) dan F05 (`rudi-hartono.png`) untuk diubah/dihapus, bertentangan dengan S-06; spec memakai file bersuffix dengan pemilik klon.
  - TC-GS-FILEMGR-106, 107 Expected a ("Tidak ada toast File Manager terpisah") ambigu: toast Save modul User kemungkinan tetap tampil; langkah 3 dan 26 mengasersi hanya tidak adanya toast terkait File Manager. Perlu klarifikasi teks toast yang dimaksud.
  - TC-GS-FILEMGR-265: akun Read Only membuka Recycle Bin dan Changelog di File Manager; matriks role (spec `TC-GS-FILEMGR-E2E-006`) menentukan apakah kontrol itu tersedia untuk Read Only. TC tidak merujuk TC role; spec mengikuti TC.
  - TC-GS-FILEMGR-106 Post Condition butir b ("entri log Delete aktor System tercatat di Changelog File Manager; penempatan di log lain menunggu OI-01") tidak memiliki langkah observasi di TC; dicakup oleh spec `TC-GS-FILEMGR-E2E-057` (TC-GS-FILEMGR-228 s.d. 230).
