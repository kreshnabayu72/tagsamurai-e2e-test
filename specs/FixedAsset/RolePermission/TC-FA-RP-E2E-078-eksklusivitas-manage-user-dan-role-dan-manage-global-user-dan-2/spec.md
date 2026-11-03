---
id: TC-FA-RP-E2E-078-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-2
title: "Eksklusivitas Manage user & role dan Manage global user & role (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1047
  - TC-FA-RP-1048
  - TC-FA-RP-1049
coverage:
  web: automated
---

# Eksklusivitas Manage user & role dan Manage global user & role (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18 (pohon Group Company Alpha), #6 (Hendra Wijaya), #7 dan #33 (Gita Maharani, Group Role `Manage user & role` di `IT Infrastructure`).
- State awal per blok (seed API, kemampuan disediakan tim FE/BE): blok TC-FA-RP-1047, Gita Maharani memegang Group Role `Manage user & role` di `IT Infrastructure` tanpa tingkat akses; blok TC-FA-RP-1048, Gita Maharani baru ditugaskan Global Role `Manage global user & role` sehingga penugasan grup `Manage user & role` terhapus; blok TC-FA-RP-1049, Gita Maharani memegang Group Role `Manage user & role` dan `Manage files` di `IT Infrastructure` serta Group Manager di `Data Center`. State dipasang di hook `before` untuk blok pertama dan sebagai langkah penghubung sebelum blok berikutnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Gita Maharani (Group Role, Group Manager, Global Role `Manage global user & role`, dan tingkat akses)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-1047: Assign Total Control ke user yang punya penugasan grup Manage user & role

1. Klik Tab `Total Control`, lalu klik `[+ Assign]`
2. Centang Gita Maharani, klik `[Assign]`
3. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
4. Klik Tab `System`, klik Role Name `Manage user & role` pada section Group Role
5. Klik `All Groups` di Sidebar Group Tree
6. Verifikasi Detail Role `Manage user & role` termuat: judul Detail Role dan header tabel tampil
7. Verifikasi baris Gita Maharani tidak ada di Detail Role `Manage user & role`

### TC-FA-RP-1048: Global Role Manage global user & role kembali inactive tidak mengembalikan penugasan grup

8. Pulihkan state lewat seed API: Gita Maharani memegang Global Role `Manage global user & role` tanpa penugasan grup `Manage user & role` dan tanpa tingkat akses, lalu muat ulang halaman
9. Klik Tab `System`, klik Role Name `Manage global user & role` pada section Global Role
10. Klik `[⋯]` baris Gita Maharani lalu `Remove`, klik `[Remove]`
11. Tunggu aksi selesai: dialog Remove tertutup dan baris Gita Maharani hilang dari tabel
12. Buka Settings > User > Detail Gita Maharani > Tab Role sub-tab Group Role
13. Verifikasi baris Group Role `Manage user & role` tampil dengan Group `—`
14. Verifikasi baris Group Role `Manage user & role` tidak aktif
15. Buka Role & Permission > Tab System > Detail Role Group Role `Manage user & role`
16. Klik `All Groups` di Sidebar Group Tree
17. Verifikasi Detail Role `Manage user & role` termuat: judul Detail Role dan header tabel tampil
18. Verifikasi penugasan grup `IT Infrastructure` tidak kembali: baris Gita Maharani tidak ada
19. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik `[+ Assign]`
20. Ketik Search `Gita Maharani`, tekan Enter
21. Verifikasi Gita Maharani muncul kembali sebagai kandidat popup Assign Group Role `Manage user & role`
22. Tutup popup Assign

### TC-FA-RP-1049: Eksklusivitas hanya untuk Manage user & role

23. Pulihkan state lewat seed API: Gita Maharani memegang Group Role `Manage user & role` dan `Manage files` di `IT Infrastructure` serta Group Manager di `Data Center` tanpa Global Role `Manage global user & role`, lalu muat ulang halaman
24. Klik Tab `System`, klik Role Name `Manage global user & role` pada section Global Role
25. Klik `[+ Assign]`, centang Gita Maharani, klik `[Assign]`
26. Tunggu aksi selesai: popup Assign tertutup dan baris Gita Maharani tampil di Detail Role `Manage global user & role`
27. Klik Tab `Group Manager`
28. Verifikasi baris Gita Maharani di `Data Center` tetap ada di Tab Group Manager
29. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
30. Klik node `IT Infrastructure` di Sidebar Group Tree
31. Verifikasi baris Gita Maharani pada `Manage files` di `IT Infrastructure` tetap ada

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1047, TC-FA-RP-1048, TC-FA-RP-1049).
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; pemulihan state seed antar blok (langkah 8 dan 23); "Tunggu aksi selesai" pada langkah 11 dan 26 karena langkah berikutnya berpindah surface dan hasilnya tidak diasersi langsung (bagian 8b butir 8); menutup popup Assign; mencari Gita Maharani di picker untuk menemukan baris target (R-16).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` Detail Role termuat (langkah 6 dan 17) sebagai anchor positif untuk asersi absence baris (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-1048 tidak menyebut apakah ada penugasan Group Role lain pada Detail Role `Manage user & role` yang dapat menjadi anchor; spec memakai Detail Role termuat sebagai anchor permukaan.
  - TC-FA-RP-1047 menyebut penyebab penghapusan penugasan grup (Global Role aktif lewat cascade Total Control) dalam kurung; penyebab itu tidak teramati terpisah di UI sehingga hanya hasilnya (baris tidak ada) yang diasersi.
  - TC-FA-RP-1048 pada langkah uji keempat menyebut kandidat popup Assign tanpa menyebut group yang dipilih; spec memilih node `IT Infrastructure` sesuai penugasan awal Gita Maharani.
