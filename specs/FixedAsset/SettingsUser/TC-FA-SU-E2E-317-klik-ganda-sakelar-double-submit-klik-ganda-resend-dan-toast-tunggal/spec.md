---
id: TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal
title: "Klik Ganda Sakelar, Double-submit, Klik Ganda Resend, dan Toast Tunggal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1017
  - TC-FA-SU-1018
  - TC-FA-SU-1019
  - TC-FA-SU-1024
coverage:
  web: automated
---

# Klik Ganda Sakelar, Double-submit, Klik Ganda Resend, dan Toast Tunggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), layanan terkendali (#37: Hana Kusuma Pending Activation). Target: Gita Permata dan Doni Prasetyo (Inactive), Wawan Setiawan (Group Role Manage files; Branch Surabaya), dan Hana Kusuma.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): `Spectra.intercept()` atas respons HTTP (network error tanpa respons) yang dilepas segera setelah pemicu (S-09), serta pencatat request jaringan halaman untuk menghitung request Save, Submit, dan Select yang terkirim (langkah 22, 29, 36); kegagalan dipicu di atas backend nyata sehingga spec tetap FE+BE (bagian 6).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): jumlah entri pada Tab Changelog target, Tab System Log aktor, dan Activity Log dibaca sebelum aksi (baseline, S-12) dan sesudah aksi; audit trail permanen sehingga asersi memakai selisih terhadap baseline. Log yang eventual dibaca ulang (muat ulang surface) sampai batas tunggu 2 menit.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan status aktif, penugasan peran, dan Home Group pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC; dijalankan sebagai langkah penghubung dan di hook `after` (cadangan).
- Mail-catcher dengan baseline jumlah email per alamat (R-11, S-12) untuk Hana Kusuma (disediakan tim FE). Precondition cooldown Resend Hana Kusuma belum berjalan dipenuhi di hook `before` dengan jam server dan jam browser; hook `after` memajukan jam 61 detik lalu memulihkannya supaya cooldown yang dimulai blok TC-FA-SU-1019 tidak terbawa ke spec lain (R-10).
- State global dan pemulihan: intercept penundaan dilepas sesudah respons selesai; data Pre-setup dipulihkan lewat seed API pada langkah penghubung dan di hook `after`; jam server dan jam browser dimajukan di hook `after` lalu dipulihkan. Efek pada Pre-setup: Last Updated dan Modified By Gita Permata, Doni Prasetyo, dan Wawan Setiawan berubah, satu email Resend terkirim ke Hana Kusuma, dan entri log permanen bertambah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1024: Toast baru menggantikan toast lama pada slot tunggal

1. Tunggu toast lama hilang otomatis
2. Klik sakelar Active baris Gita Permata, lalu klik `[Deactivate]`
3. Segera klik sakelar Active baris Doni Prasetyo, lalu konfirmasi Activate
4. Verifikasi hanya satu toast tampil pada satu waktu
5. Verifikasi toast kedua menggantikan toast pertama
6. Verifikasi toast tampil di kanan bawah
7. Pulihkan Gita Permata (Active) dan Doni Prasetyo (Inactive) lewat seed API

### TC-FA-SU-1017: Klik sakelar Active dua kali beruntun

8. Catat jumlah entri `Deactivate` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline
9. Klik dua kali dengan cepat sakelar Active baris Gita Permata
10. Verifikasi hanya satu dialog `Deactivate User` tampil dan klik kedua tidak membuka dialog kedua
11. Klik `[Deactivate]`
12. Verifikasi jumlah entri `Deactivate` bertambah tepat satu pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
13. Pulihkan Gita Permata (Active) lewat seed API

### TC-FA-SU-1018: Tombol konfirmasi Save atau Submit Disabled saat request berjalan

14. Catat jumlah entri penugasan Group Role, penugasan Transaction Role, dan Edit Home Group pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
15. Ketik Search `Wawan`, tekan Enter, klik nama Wawan Setiawan, lalu buka Tab Role > Sub-tab Group Role
16. Pasang `Spectra.intercept()` yang menunda respons request Save Group Role 3 detik
17. Buka popup Assign Group Role Manage files dan ubah Delete pada Branch Surabaya
18. Klik `[Save]` dua kali beruntun
19. Verifikasi `[Save]` popup Assign Group Role Disabled dengan indikator loading selama respons ditunda
20. Verifikasi kontrol lain pada popup Assign Group Role dibekukan selama respons ditunda
21. Tunggu respons tertunda selesai lalu lepas intercept
22. Verifikasi hanya satu request Save terkirim (klik kedua tidak mengirim request kedua)
23. Verifikasi jumlah entri penugasan Group Role bertambah tepat satu pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log
24. Buka Sub-tab Transaction Role, klik `[+ Assign]`, dan isi Transfer × Asset Admin pada Finance & Accounting
25. Pasang `Spectra.intercept()` yang menunda respons request Submit Transaction Role 3 detik
26. Klik `[Submit]` dua kali beruntun
27. Verifikasi `[Submit]` modal Assign Transaction Role Disabled dengan indikator loading selama respons ditunda
28. Tunggu respons tertunda selesai lalu lepas intercept
29. Verifikasi hanya satu request Submit terkirim (klik kedua tidak mengirim request kedua)
30. Verifikasi jumlah entri penugasan Transaction Role bertambah tepat satu pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log
31. Kembali ke User List, Ketik Search `Wawan Setiawan`, tekan Enter, klik `⋯` pada baris Wawan Setiawan, klik `Edit Home Group`, dan pilih IT Infrastructure
32. Pasang `Spectra.intercept()` yang menunda respons request Select Edit Home Group 3 detik
33. Klik `[Select]` dua kali beruntun
34. Verifikasi `[Select]` popup Home Group Disabled dengan indikator loading selama respons ditunda
35. Tunggu respons tertunda selesai lalu lepas intercept
36. Verifikasi hanya satu request Select terkirim (klik kedua tidak mengirim request kedua)
37. Verifikasi jumlah entri Edit Home Group bertambah tepat satu pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log
38. Pulihkan Group Role, Transaction Role, dan Home Group Wawan Setiawan ke Pre-setup lewat seed API

### TC-FA-SU-1019: Klik ganda Resend Activation Email

39. Catat jumlah entri `Resend Activation Email` pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log serta jumlah email yang diterima Hana Kusuma di mail-catcher sebagai baseline
40. Klik dua kali dengan cepat Resend Activation Email pada baris Hana Kusuma
41. Verifikasi tombol Resend menampilkan hitung mundur tooltip segera setelah klik pertama
42. Verifikasi klik kedua tidak mengirim email kedua: jumlah email yang diterima Hana Kusuma bertambah tepat satu dari baseline
43. Verifikasi jumlah entri `Resend Activation Email` bertambah tepat satu pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah (TC-FA-SU-1024, 1017, 1018, 1019): TC-FA-SU-1024 dan 1017 sama-sama memakai Gita Permata sehingga Gita dipulihkan di antaranya (S-09); TC-FA-SU-1018 berpindah ke Detail Wawan Setiawan dan TC-FA-SU-1019 kembali ke User List.
- Hitungan toast pada TC-FA-SU-1024 didahului "Tunggu toast lama hilang otomatis" (R-12). Expected "hanya satu entri log" pada TC-FA-SU-1017, 1018, dan 1019 adalah asersi jumlah dengan baseline (bagian 3), bukan kelas g.
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 7, 8, 13, 14, 15, 21, 28, 35, 38, 39. Langkah 15 dan 31 juga Search untuk menemukan baris target Wawan Setiawan di luar halaman 1 (R-16).
- Spec ini 43 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu topik (perlindungan klik ganda dan double-submit) dan berdiri sendiri dengan target sendiri; ekspansi berasal dari Expected c TC-FA-SU-1018 yang menuntut hal yang sama pada tiga tombol (`[Save]`, `[Submit]`, `[Select]`).
- Temuan untuk QA:
  - TC-FA-SU-1018 Expected c ("Hal yang sama berlaku pada `[Submit]` modal Assign Transaction Role dan `[Select]` popup Home Group") tidak punya Langkah Uji; spec menambah dua blok dengan target Wawan Setiawan (Transfer × Asset Admin pada Finance & Accounting dan Home Group IT Infrastructure) dan mencatatnya di sini (S-03, S-15).
  - TC-FA-SU-1019 Expected b menyebut "hitung mundur tooltip" tanpa nilai awal; spec mengasersi hitung mundur tampil tanpa nilai.
  - TC-FA-SU-1024 tidak menyebut dialog Activate untuk Doni Prasetyo; spec menulis "lalu konfirmasi Activate" mengikuti pola dialog Deactivate.
