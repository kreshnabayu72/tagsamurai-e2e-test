---
id: TC-FA-RP-E2E-077-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-1
title: "Eksklusivitas Manage user & role dan Manage global user & role (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1043
  - TC-FA-RP-1044
  - TC-FA-RP-1046
coverage:
  web: automated
---

# Eksklusivitas Manage user & role dan Manage global user & role (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18 (pohon Group Company Alpha), #6 (Hendra Wijaya, Global Role `Manage global user & role` aktif), #7 dan #33 (Gita Maharani, Group Role `Manage user & role` di `IT Infrastructure`), pool #15 (Budi Santoso sebagai kandidat pembanding TC-FA-RP-1044).
- State awal per blok (seed API, kemampuan disediakan tim FE/BE): blok TC-FA-RP-1043 dan TC-FA-RP-1044, Gita Maharani memegang Group Role `Manage user & role` di `IT Infrastructure`; blok TC-FA-RP-1046, Gita Maharani memegang Group Role `Manage user & role` di `IT Infrastructure` dan Global Role `Manage global user & role` berstatus inactive-retained. State dipasang di hook `before` untuk blok pertama dan sebagai langkah penghubung sebelum blok berikutnya.
- Kemampuan teknis: jumlah entri Changelog dibaca dari modal Changelog Detail Role (jumlah entri sebelum dan sesudah aksi sebagai baseline, S-12); halaman Settings > User > Detail Gita Maharani > Tab Role dibuka lewat navigasi UI.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Gita Maharani: Group Role `Manage user & role` di `IT Infrastructure`, Global Role `Manage global user & role` inactive-retained), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-1043: Assign Global Role Manage global user & role ke user yang punya penugasan grup Manage user & role

1. Klik Tab `System`, klik Role Name `Manage user & role` pada section Group Role
2. Klik `All Groups` di Sidebar Group Tree
3. Klik ikon Changelog di toolbar Detail Role `Manage user & role`, lalu catat jumlah entri sebagai baseline
4. Tutup modal Changelog
5. Klik Tab `System`, klik Role Name `Manage global user & role` pada section Global Role
6. Klik `[+ Assign]`, centang Gita Maharani, klik `[Assign]`
7. Verifikasi muncul toast sukses: `Success, Manage global user & role has been assigned.`
8. Verifikasi tidak ada dialog tambahan dan tidak ada dialog auto-revert Group Manager
9. Klik Tab `System`, klik Role Name `Manage user & role` pada section Group Role
10. Klik `All Groups` di Sidebar Group Tree
11. Verifikasi Detail Role `Manage user & role` termuat: judul Detail Role dan header tabel tampil
12. Verifikasi baris Gita Maharani di `IT Infrastructure` tidak ada di Detail Role `Manage user & role`
13. Klik ikon Changelog di toolbar Detail Role `Manage user & role`
14. Verifikasi entri `Remove` untuk Gita Maharani pada grup `IT Infrastructure` dengan pelaku `Siti R` tampil
15. Verifikasi jumlah entri Changelog bertambah tepat satu dibanding baseline (tanpa entri tambahan)
16. Tutup modal Changelog

### TC-FA-RP-1044: Popup Assign User Group Role Manage user & role menyaring user dengan Global Role Manage global user & role aktif

17. Pulihkan state lewat seed API: Gita Maharani kembali memegang Group Role `Manage user & role` di `IT Infrastructure` dan Global Role `Manage global user & role` tidak aktif lagi, lalu muat ulang halaman
18. Klik Tab `System`, klik Role Name `Manage user & role` pada section Group Role
19. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik `[+ Assign]`
20. Ketik Search `Budi Santoso`, tekan Enter
21. Verifikasi Budi Santoso ada di daftar picker
22. Ganti isi kotak search dengan `Hendra Wijaya`, tekan Enter
23. Verifikasi empty state `No results found` tampil sehingga Hendra Wijaya (Global Role `Manage global user & role` aktif) tidak ada di daftar picker
24. Tutup popup Assign
25. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
26. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik `[+ Assign]`
27. Ketik Search `Hendra Wijaya`, tekan Enter
28. Verifikasi Hendra Wijaya ada di daftar picker Group Role `Manage files`
29. Tutup popup Assign

### TC-FA-RP-1046: Switch Global Role Manage global user & role ON di Settings > User menghapus penugasan grup Manage user & role

30. Pulihkan state lewat seed API: Gita Maharani memegang Group Role `Manage user & role` di `IT Infrastructure` dan Global Role `Manage global user & role` inactive-retained, lalu muat ulang halaman
31. Buka Settings > User > Detail Gita Maharani > Tab Role sub-tab Global Role
32. Nyalakan switch `Manage global user & role`
33. Verifikasi switch `Manage global user & role` aktif
34. Verifikasi tidak ada dialog tambahan
35. Klik sub-tab Group Role
36. Verifikasi baris Group Role capability lain (mis. `Manage files`) tampil pada sub-tab Group Role
37. Verifikasi baris Group Role `Manage user & role` tidak dirender, termasuk `[Detail]` dan `[Assign Group]` baris itu
38. Buka Role & Permission > Tab System > Detail Role Group Role `Manage user & role`
39. Klik `All Groups` di Sidebar Group Tree
40. Verifikasi baris Gita Maharani tidak ada di Detail Role `Manage user & role`
41. Klik ikon Changelog di toolbar Detail Role
42. Verifikasi satu entri `Remove` per grup yang terlepas tercatat untuk Gita Maharani dengan pelaku `Siti R`
43. Tutup modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1043, TC-FA-RP-1044, TC-FA-RP-1046).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): membuka Tab System dan Detail Role; mencatat baseline Changelog dan menutup modal; pemulihan state seed antar blok (langkah 17 dan 30); menutup popup Assign. Asersi tambahan yang tidak ada di TC: `Verifikasi` Detail Role termuat (langkah 11) dan baris Group Role capability lain tampil (langkah 36) sebagai anchor positif untuk asersi absence baris (bagian 8b butir 2), dan `Verifikasi` jumlah entri bertambah tepat satu memakai baseline dari langkah 3 (S-12).
- Urutan pencarian pada TC-FA-RP-1044 dibalik terhadap TC (Budi Santoso lebih dulu, lalu Hendra Wijaya) supaya ada anchor positif pada picker yang sama sebelum asersi absence (bagian 8b butir 2); hasil pencarian Hendra Wijaya berupa empty state `No results found` yang menjadi anchor sah.
- Pelaku entri Changelog ditulis `Siti R` (format `[First Name] [Last Initial]`, R-14) untuk Total Control Siti Rahmawati.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-1043 dan TC-FA-RP-1046 tidak memuat langkah observasi dan tidak diasersi (S-01).
  - TC-FA-RP-1046 tidak menyebut cara menyiapkan Global Role `Manage global user & role` inactive-retained untuk Gita Maharani; spec memakai seed API yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
  - TC-FA-RP-1046 pada langkah uji ketiga: TC tidak menyebut apakah baris Group Role capability lain tetap dirender; spec memakai baris capability lain sebagai anchor berdasarkan TC-FA-RP-1048 yang menampilkan baris Group Role tanpa grup sebagai baris `—`.
- Spec ini 43 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (fungsional, Role Matrix tidak dipakai) pada permukaan yang sama, tiap blok berdiri sendiri dengan data seed sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
