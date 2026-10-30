---
id: TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses
title: "Siklus Aktivasi dan Login: Status Activated, Link Kedaluwarsa, Effective Active, dan Deactivate Memutus Login"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-988
  - TC-GS-USER-989
  - TC-GS-USER-990
  - TC-GS-USER-991
coverage:
  web: automated
---

# Siklus Aktivasi dan Login: Status Activated, Link Kedaluwarsa, Effective Active, dan Deactivate Memutus Login

## Prerequisites

- Mode: FE+BE. Kelas harness d: mail-catcher dan modul Auth (halaman aktivasi dan login), manipulasi jam server dan jam browser.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun yang diuji (spec memakai tiga akun dan berganti akun secara eksplisit; user uji dibuat spec lewat API sehingga tidak ada di Tabel Pre-setup):

  | Urutan | Peran dalam spec | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control (Siti Nurhaliza), Tabel Data Uji Pre-setup No. 2 | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | Joko Susilo uji (TC-GS-USER-990) | `jokosusilo+{runId}-157@qwertysystem.net` | `USER_PASSWORD` |
  | 3 | Dewi Lestari uji (TC-GS-USER-991) | `dewilestari+{runId}-157@qwertysystem.net` | `USER_PASSWORD` |

  Lukman Hakim (TC-GS-USER-988) mengaktifkan akunnya sendiri dengan `Spectra.env.USER_PASSWORD` pada langkah 4. Login akun 1 di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (akun 1). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`.
- Data Pre-setup tidak dipakai dan tidak diubah; spec memakai user milik sendiri (S-06).
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun 1 (kemampuan seeding Login User, status Pending Activation, toggle per-produk, dan nilai field wajib lain user lewat API; fixture `fixtures/user.json` belum ada, disediakan tim FE):
  - Login User `Lukman Hakim {runId}-157` (First Name `Lukman`, Last Name `Hakim {runId}-157`), email `lukmanhakim+{runId}-157@qwertysystem.net`, Pending Activation, Access `Fixed Asset` (TC-GS-USER-988).
  - Login User `Lukman Hakim Dua {runId}-157` (First Name `Lukman`, Last Name `Hakim Dua {runId}-157`), email `lukmanhakimdua+{runId}-157@qwertysystem.net`, Pending Activation, Access `Fixed Asset`, link aktivasi dibiarkan tidak dibuka sampai kedaluwarsa (TC-GS-USER-989).
  - Login User `Joko Susilo {runId}-157`, email `jokosusilo+{runId}-157@qwertysystem.net`, Activated, password `Spectra.env.USER_PASSWORD`, Global Active ON, Access `Fixed Asset` dan `Supply Asset`, toggle per-produk `Supply Asset` OFF dan `Fixed Asset` ON (setara Joko Susilo Tabel Pre-setup No. 19; TC-GS-USER-990).
  - Login User `Dewi Lestari {runId}-157`, email `dewilestari+{runId}-157@qwertysystem.net`, Activated, Active, password `Spectra.env.USER_PASSWORD`, Access `Fixed Asset` (setara Dewi Lestari Tabel Pre-setup No. 12; TC-GS-USER-991).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak memberi cara):
  - Mail-catcher: membaca email per alamat (waktu terbit dan tautan di badan email) dan membuka tautan aktivasi; spec hanya membaca email aktivasi terbaru dan tidak mengasersi jumlah email.
  - Manipulasi jam: jam server dan jam browser diatur bersama ke waktu absolut dan dipulihkan ke waktu nyata (TC-GS-USER-989). `T_N` = waktu terbit email aktivasi `Lukman Hakim Dua {runId}-157`, dibaca dari mail-catcher; jam diatur ke `T_N` + 25 jam. Masa berlaku link aktivasi 24 jam (Auth, TC-AUTH-ACT-86 dan 124), sehingga margin terhadap batas 1 jam (lebih dari 5 menit).
  - Membaca jumlah notifikasi in-app user dari BE (TC-GS-USER-991 Expected b).
  - Jendela privat browser untuk konteks tanpa sesi login (Lukman, Dewi).
- State global yang diubah: jam server dan jam browser (langkah 32 sampai 36). Pemulihan jam ditulis sebagai langkah aksi (langkah 36) sebelum akun aktor membuka User List (S-09); hook `after` memulihkan jam sebagai cadangan dan tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan jam; hapus lewat API Login User `lukmanhakim+{runId}-157@qwertysystem.net`, `lukmanhakimdua+{runId}-157@qwertysystem.net`, `jokosusilo+{runId}-157@qwertysystem.net`, dan `dewilestari+{runId}-157@qwertysystem.net`; kembalikan sesi ke akun 1.

## Test Steps

### TC-GS-USER-988: Login user Activated mengubah status Pending Activation menjadi Activated

1. Klik icon Search, ketik `{runId}-157`, tekan Enter pada tabel User List
2. Baca tautan aktivasi dari email aktivasi terbaru di mail-catcher untuk alamat `lukmanhakim+{runId}-157@qwertysystem.net`
3. Buka jendela privat baru (tanpa sesi login), lalu buka tautan aktivasi Lukman Hakim sehingga halaman Set Password tampil
4. Ketik `Spectra.env.USER_PASSWORD` di field Password dan field Confirm Password
5. Klik button "Set Password"
6. Tunggu aksi selesai (halaman Activation Success tampil)
7. Tutup jendela privat
8. Muat ulang halaman User List
9. Klik icon Search, ketik `{runId}-157`, tekan Enter
10. Verifikasi badge `Pending Activation` baris `Lukman Hakim Dua {runId}-157` tampil
11. Verifikasi badge `Pending Activation` baris `Lukman Hakim {runId}-157` hilang
12. Verifikasi kolom Activation Status baris `Lukman Hakim {runId}-157` `Activated`
13. Klik `⋯` pada baris `Lukman Hakim {runId}-157`
14. Verifikasi opsi `Edit` tampil di overlay (⋯) baris `Lukman Hakim {runId}-157`
15. Verifikasi opsi `Resend Activation Email` tidak ada di overlay (⋯) baris `Lukman Hakim {runId}-157`
16. Tekan Esc untuk menutup overlay (⋯)

### TC-GS-USER-990: Effective Active, Global ON tetapi toggle per-produk OFF tidak dapat beraksi di produk itu

17. Ganti akun: logout, lalu login sebagai Joko Susilo (`jokosusilo+{runId}-157@qwertysystem.net`) dengan `Spectra.env.USER_PASSWORD`
18. Buka Supply Asset
19. Verifikasi Joko Susilo tidak dapat beraksi di Supply Asset
20. Buka Fixed Asset
21. Verifikasi Joko Susilo dapat memakai Fixed Asset

### TC-GS-USER-991: Deactivate memutus akses login

22. Ganti akun: logout, lalu login sebagai Total Control (`totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`) dengan `Spectra.env.GS_TC_PASSWORD`, lalu buka Global Settings > User > User List
23. Catat jumlah notifikasi in-app `Dewi Lestari {runId}-157` dari BE sebagai baseline `{n0}`
24. Klik icon Search, ketik `Dewi Lestari {runId}-157`, tekan Enter
25. Matikan switch Active baris `Dewi Lestari {runId}-157`, klik `[Deactivate]` pada dialog
26. Tunggu aksi selesai
27. Buka jendela privat baru (tanpa sesi login), buka Auth > Login, isi email `dewilestari+{runId}-157@qwertysystem.net` dan password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, lalu klik `[Log in]`
28. Verifikasi dialog `Account Deactivated` milik Auth tampil dan login diblok
29. Verifikasi jumlah notifikasi in-app `Dewi Lestari {runId}-157` dari BE sama dengan `{n0}` (tidak ada notifikasi Deactivate)
30. Tutup jendela privat

### TC-GS-USER-989: Link aktivasi kedaluwarsa ditangani modul Auth

31. Baca tautan aktivasi dan waktu terbit `T_N` dari email aktivasi terbaru di mail-catcher untuk alamat `lukmanhakimdua+{runId}-157@qwertysystem.net`
32. Atur jam server dan jam browser bersama ke `T_N` + 25 jam
33. Buka jendela privat baru (tanpa sesi login), lalu buka tautan aktivasi `Lukman Hakim Dua {runId}-157`
34. Verifikasi halaman link kedaluwarsa milik Auth tampil dengan Title "Activation Link Expired"
35. Tutup jendela privat
36. Pulihkan jam server dan jam browser ke waktu nyata
37. Muat ulang halaman User List
38. Klik icon Search, ketik `{runId}-157`, tekan Enter
39. Verifikasi badge `Pending Activation` baris `Lukman Hakim Dua {runId}-157` tetap tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness d (prinsip 13d): TC-GS-USER-988, 989, 990, 991 membuka halaman Auth (aktivasi dan login) dan mail-catcher; TC-GS-USER-989 mengatur jam.
- Spec melewati sekitar 35 langkah (39 langkah) karena empat blok TC berada di satu kelas harness (kelas d: halaman Auth, mail-catcher, jam). Tiap blok memakai user seed dan jendela privatnya sendiri, ditutup di akhir blok, dan hanya TC-GS-USER-989 mengubah state global (jam) sehingga diletakkan paling akhir; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-989 paling akhir karena mengatur jam server dan jam browser (state global); jam dipulihkan lewat langkah 36 sebelum akun aktor membuka User List (S-09). TC-GS-USER-990 dan 991 berurutan dengan ganti akun eksplisit (langkah 17 dan 22); TC-GS-USER-991 (Deactivate) sesudah TC-GS-USER-990.
- Tiap jendela privat (langkah 3, 27, 33) ditutup di akhir blok TC-nya (langkah 7, 30, 35; S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 9, 24, 37, 38 (Search dan muat ulang); langkah 2, 31 (membaca email di mail-catcher); langkah 3 sampai 7 (Lukman membuka tautan dan set password, aksi TC-GS-USER-988); langkah 6 dan 26 (menunggu aksi selesai); langkah 13 dan 16 (membuka dan menutup overlay (⋯)); langkah 18 dan 20 (membuka produk); langkah 23 (baseline); langkah 32 dan 36 (mengatur dan memulihkan jam).
- Asersi tambahan di luar Expected TC: langkah 10 adalah anchor positif untuk `Verifikasi` badge hilang (langkah 11; bagian 8b butir 2); langkah 14 adalah anchor positif untuk `Verifikasi` opsi `Resend Activation Email` tidak ada (langkah 15). Expected b TC-GS-USER-991 diasersi sebagai jumlah notifikasi in-app sama dengan baseline (asersi jumlah, bukan absence kelas g).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-988, 989, 990, 991: kolom Automation bernilai Manual Only; spec memasukkannya (bagian 2 konvensi) dengan mail-catcher, jam, dan jendela privat yang disediakan tim FE/BE.
  - TC-GS-USER-989: TC tidak menyebut masa berlaku link dan cara membuatnya kedaluwarsa; spec memakai masa berlaku 24 jam dari modul Auth dan jam absolut `T_N` + 25 jam. TC menyebut "halaman link kedaluwarsa milik Auth" tanpa teks; spec mengasersi Title "Activation Link Expired" dari spec Auth Account Activation. Status "tetap Pending Activation" diasersi lewat badge di User List.
  - TC-GS-USER-990: TC tidak menyebut bentuk tampilan "tidak dapat beraksi di Supply Asset" (halaman ditolak atau kontrol tulis disabled) dan cara mengatur toggle per-produk OFF; spec men-seed toggle lewat API dan bentuk asersi ditentukan bersama tim FE di tahap script.
  - TC-GS-USER-991: Expected b ("Tidak ada notifikasi in-app Deactivate") tidak menyebut penerima dan lokasi notifikasi; spec membaca jumlah notifikasi in-app Dewi dari BE sebelum dan sesudah Deactivate. TC juga tidak menyebut teks dialog `Account Deactivated`; spec mengasersi judul dialog.
  - TC-GS-USER-988: TC tidak menyebut password yang diset Lukman dan Activation Status pada kolom mana; spec memakai `Spectra.env.USER_PASSWORD` dan kolom Activation Status User List.
