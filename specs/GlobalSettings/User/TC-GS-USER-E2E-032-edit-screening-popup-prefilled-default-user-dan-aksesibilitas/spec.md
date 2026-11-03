---
id: TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas
title: "Edit User: Screening Popup Pre-filled, Default User (Access Disabled dan Edit Position), Access Otomatis Produk Baru, dan Aksesibilitas Popup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-160
  - TC-GS-USER-161
  - TC-GS-USER-162
  - TC-GS-USER-163
  - TC-GS-USER-240
coverage:
  web: automated
---

# Edit User: Screening Popup Pre-filled, Default User (Access Disabled dan Edit Position), Access Otomatis Produk Baru, dan Aksesibilitas Popup

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca kecuali Default User): John Doe (No. 18; `EMP-0001`, Position `Staff`, TAG `TAG-4F7K2XQ9` terpasang, foto, MFA Enrolled, Temporary dinonaktifkan), Dewi Lestari (No. 12; dibuka lalu ditutup tanpa perubahan pada TC-GS-USER-240), dan Hendra Gunawan (Default User, No. 1).
- Default User (Pre-setup No. 1) adalah target TC-GS-USER-162 dan tidak bisa diganti data seed milik spec (hanya Default User yang memiliki Access otomatis semua produk dan kunci Access). Spec mengubahnya dan memulihkannya:
  - Hook `before` membaca dan mencatat Position awal Default User (nilai ini disebut "Position awal" di langkah). Position awal bukan `Finance Manager` (kondisi ini disediakan tim FE pada entitas uji; bila sama, Save TC-GS-USER-162 menjadi No-Op).
  - Pemulihan: langkah 45 sampai 48 mengembalikan Position ke Position awal; hook `after` memulihkan Position awal lewat API sebagai cadangan (kemampuan disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD).
  - Efek yang tidak bisa dipulihkan: Modified By Default User berisi `Siti N` (bukan `System` seperti pada seed), Last Update diperbarui, dan Changelog Default User bertambah dua entri Edit. Spec TC-GS-USER-1043 dan TC-GS-USER-1044 (Default User seed belum pernah diedit) berjalan sebelum spec ini; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Kondisi entitas uji (TC-GS-USER-163): Client menambah subscription produk baru `Supply Asset` setelah Default User dibuat, sehingga Access Default User memuat `Supply Asset` secara otomatis. Kondisi ini disediakan tim FE/BE pada entitas uji (TC tidak memberi cara menambah subscription); spec tidak mengubah subscription.
- Data Dinamis: tidak ada; spec tidak membuat user, sehingga tidak ada seeding atau cleanup selain pemulihan Default User di atas.
- Kemampuan teknis: hover kontrol Access yang disabled untuk membaca tooltip; menekan Tab berulang dan membaca elemen yang sedang fokus; menekan Esc; mendeteksi muncul tidaknya dialog.
- State global yang diubah: hanya Default User (lihat di atas); tidak ada jam, plan, atau konfigurasi lain.

## Test Steps

### TC-GS-USER-160: Screening Popup Edit User pre-filled

1. Klik icon Search, ketik `John Doe`, tekan Enter
2. Buka row action baris `John Doe` lalu klik `Edit`
3. Verifikasi Header: Title `Edit User`
4. Verifikasi Header: icon `[✕]`
5. Verifikasi Body: Avatar menampilkan foto John Doe
6. Verifikasi Body: First Name `John`
7. Verifikasi Body: Last Name `Doe`
8. Verifikasi Body: Position `Staff`
9. Verifikasi Body: Division terisi sesuai sel Division baris John Doe di tabel
10. Verifikasi Body: Employee ID `EMP-0001`
11. Verifikasi Body: Email terisi sesuai sel Email baris John Doe di tabel
12. Verifikasi Body: kontrol Access (multi dropdown, placeholder `Select access`) menampilkan produk terpilih sesuai isi sel Access baris John Doe di tabel
13. Verifikasi Body: User TAG langsung menampilkan badge `Verified` (success)
14. Verifikasi Body: User TAG menampilkan `TAG-4F7K2XQ9`
15. Verifikasi Body: User TAG menampilkan tombol `Scan TAG` dan `Unpair`
16. Verifikasi Body: User TAG tanpa state sebelum scan
17. Verifikasi Body: `Set as Temporary User` unchecked
18. Verifikasi Body: Custom Field terisi (pre-filled) sesuai data John Doe
19. Verifikasi Footer: tombol `[Clear Field]` lalu `[Save]` berurutan
20. Verifikasi Footer: tidak ada checkbox `Stay on this form after submitting`
21. Klik `[✕]`

### TC-GS-USER-240: Accessibility Popup Edit User, fokus terkunci dan Esc

22. Ganti isi kotak search dengan `Dewi Lestari`, tekan Enter
23. Buka row action baris `Dewi Lestari` (Name persis tanpa suffix `{runId}`) lalu klik `Edit`
24. Tekan Tab berulang melewati seluruh elemen di Popup Edit
25. Verifikasi fokus berputar di dalam Popup (tidak keluar dari Popup)
26. Tekan Esc tanpa perubahan
27. Verifikasi Popup Edit tertutup
28. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-USER-163 dan TC-GS-USER-161: Access Default User otomatis dan Popup Edit Default User

29. Ganti isi kotak search dengan `Hendra Gunawan`, tekan Enter
30. Verifikasi sel Access baris `Hendra Gunawan` memuat `Supply Asset`
31. Catat isi sel Access baris `Hendra Gunawan` (acuan TC-GS-USER-162)
32. Buka row action baris `Hendra Gunawan` lalu klik `Edit`
33. Verifikasi `Supply Asset` terpilih di kontrol Access Popup Edit
34. Verifikasi kontrol Access di Popup Edit disabled
35. Verifikasi seluruh produk Access terpilih
36. Verifikasi seluruh produk Access tetap tampil namun kontrol Access disabled
37. Hover kontrol Access
38. Verifikasi tooltip `Default User cannot be modified.`
39. Verifikasi field First Name, Last Name, Position, Division, Employee ID, dan Email enabled

### TC-GS-USER-162: Edit info dasar Default User oleh Total Control

40. Ubah Position ke `Finance Manager`
41. Klik `[Save]`
42. Verifikasi toast sukses: `Success, user has been updated.`
43. Verifikasi sel Position baris `Hendra Gunawan` `Finance Manager`
44. Verifikasi sel Access baris `Hendra Gunawan` tidak berubah (sama dengan yang dicatat pada langkah 32)

### Pemulihan Default User

45. Buka row action baris `Hendra Gunawan` lalu klik `Edit`
46. Ubah Position ke Position awal
47. Klik `[Save]`
48. Tunggu aksi selesai

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md` (TC-GS-USER-160, 161, 162, 163, 240). Mode FE+BE; kelas harness: screening Popup Edit dan satu aksi tulis pada Default User.
- Urutan TC di spec: 160, 240, 163, 161, 162, lalu pemulihan. Urutan sumber (160, 161, 162, 163, 240) diubah karena TC-GS-USER-162 mengubah Default User dan dijalankan paling akhir (bagian 3 butir 5, S-10); TC-GS-USER-163 dan TC-GS-USER-161 berbagi satu pembukaan Edit Hendra Gunawan (langkah 32 sampai 39), dan langkah 32 juga menjadi langkah 1 TC-GS-USER-162; langkah 40 sampai 44 melanjutkan form yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi` yang bukan langkah TC): langkah 21 (menutup form bersih lewat `[✕]`), 31 (mencatat acuan Access), 45 sampai 48 (pemulihan Default User; hasilnya tidak diasersi, hook `after` sebagai cadangan).
- Pembagian TC lintas spec: TC-GS-USER-160 sampai 163 dan 240 diverifikasi seluruhnya di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-160 butir b.v ("Access tercentang sesuai data"), b.iii-iv (Division dan Email "terisi"), dan b.viii (Custom Field "pre-filled") tidak menyebut nilai; spec membandingkan dengan sel tabel baris John Doe dan hanya mengasersi bahwa Custom Field terisi.
  - TC-GS-USER-162 tidak menyebut Position awal Default User, dan Tabel Data Uji Pre-setup No. 1 tidak memuatnya; pemulihan bergantung pada nilai yang dicatat hook `before`. Bila Position awal kosong, pemulihan lewat UI tidak jelas (Position kosong belum tentu bisa disimpan lewat Popup Edit); hook `after` lewat API menjadi satu-satunya jalur.
  - TC-GS-USER-163 tidak menyebut cara menambah subscription `Supply Asset` setelah Default User dibuat dan precondition-nya bergantung pada entitas uji; kondisi disediakan tim FE/BE.
  - TC-GS-USER-240 langkah 2 ("Tab berulang") tidak menyebut jumlah penekanan Tab; spec menafsirkan satu putaran penuh dan lebih.
- Spec melewati sekitar 35 langkah (48 langkah) karena memuat satu kelas (screening Popup Edit dan satu edit Default User), semuanya pada satu layar Edit User dengan pembukaan form dipakai bersama, dan tiap blok TC berdiri sendiri (kegagalan blok screening John Doe tidak membuat blok Default User kehilangan makna).
