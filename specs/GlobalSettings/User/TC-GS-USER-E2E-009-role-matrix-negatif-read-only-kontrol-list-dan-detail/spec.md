---
id: TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail
title: "Role Matrix Negatif: Kontrol User List dan User Detail untuk Read Only (Create, Checkbox, Aksi Tulis, Header, dan Tab Role Tidak Tersedia)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-47
  - TC-GS-USER-48
  - TC-GS-USER-81
  - TC-GS-USER-1000
  - TC-GS-USER-1002
  - TC-GS-USER-1071
coverage:
  web: automated
---

# Role Matrix Negatif: Kontrol User List dan User Detail untuk Read Only (Create, Checkbox, Aksi Tulis, Header, dan Tab Role Tidak Tersedia)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (satu role; seluruh TC sumber berprecondition Read Only):

| Role | Akun | Nama user | Env var password |
|---|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | Yudi Pratomo (Tabel Pre-setup No. 3) | `Spectra.env.GS_RO_PASSWORD` |

- Login akun Read Only dilakukan di hook `before` (aktor pertama dan satu-satunya spec); tidak ada langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_RO_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Dewi Lestari (No. 12, Normal, Activated, Active ON, Custom Field Blood Type), Ahmad Fauzi (No. 13, holder Manage user and role), John Doe (No. 18, Activated, punya foto). Data Dinamis: tidak ada.
- Kemampuan teknis: hover elemen (switch, checkbox, avatar) dan membaca tooltip; membaca state disabled elemen; menekan Esc.
- State global yang diubah: tidak ada.

## Test Steps

### Persiapan tabel

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-47: Kontrol List untuk Read Only: tanpa Create, checkbox, dan aksi tulis

2. Verifikasi baris Dewi Lestari tampil di tabel
3. Verifikasi Table Tools memuat `Search | Filter | Download | Changelog`
4. Verifikasi `[+ User]` tidak tampil
5. Verifikasi kolom checkbox tidak dirender (header dan body)
6. Verifikasi Search, Filter, Sort, Pagination, dan header Column Visibility tampil dan aktif
7. Klik (⋯) pada baris Dewi Lestari
8. Verifikasi overlay row action memuat opsi `Detail`
9. Verifikasi opsi `Edit` dan `Delete` tidak tampil di overlay
10. Tutup overlay dengan menekan Esc
11. Arahkan kursor ke switch Active baris Dewi Lestari
12. Verifikasi switch Active baris Dewi Lestari tampil namun disabled
13. Verifikasi tooltip `Read Only access cannot modify data.`

### TC-GS-USER-48: Bulk bar tidak muncul untuk Read Only

14. Klik sel Email pada baris Dewi Lestari (mencoba memilih baris)
15. Verifikasi tidak ada checkbox untuk dipilih di area kiri baris Table Tools dan baris tabel
16. Verifikasi Bulk Action Bar tidak tampil

### TC-GS-USER-81: Kontrol header dan section User Detail target Normal untuk Read Only

17. Klik Name `Dewi Lestari` di User List
18. Arahkan kursor ke switch Active header
19. Verifikasi switch Active header tampil namun disabled
20. Verifikasi tooltip `Read Only access cannot modify data.`
21. Verifikasi sub-section User TAG dan Authenticator (MFA) tampil
22. Verifikasi `Scan TAG`, `Unpair`, `Reset Authenticator`, dan `Resend ... Email` tidak tampil
23. Verifikasi Section Custom Fields tampil dengan field Blood Type
24. Verifikasi icon inline edit Custom Field tidak tampil
25. Coba temukan menu `[⋯]` pada header
26. Verifikasi menu `[⋯]` header tidak dirender
27. Klik Tab `Role`
28. Verifikasi Tab `Role` terbuka
29. Arahkan kursor ke switch Active baris `Manage TAG`
30. Verifikasi switch Active baris `Manage TAG` tampil namun disabled
31. Verifikasi tooltip `Read Only access cannot modify data.`
32. Arahkan kursor ke checkbox Update baris `Manage TAG`
33. Verifikasi checkbox Update baris `Manage TAG` tampil namun disabled
34. Verifikasi tooltip `Read Only access cannot modify data.`
35. Klik Tab `Responsibilities`
36. Verifikasi Tab `Responsibilities` terbuka
37. Klik Tab `Non-Login User`
38. Verifikasi Tab `Non-Login User` terbuka
39. Klik Tab `Changelog`
40. Verifikasi Tab `Changelog` terbuka
41. Klik Tab `System Log`
42. Verifikasi Tab `System Log` terbuka
43. Klik Tab `User Log`
44. Verifikasi Tab `User Log` terbuka

### TC-GS-USER-1002: Menu [⋯] header User Detail Hidden untuk Read Only

45. Verifikasi menu `[⋯]` tidak dirender pada header
46. Verifikasi avatar, nama, badge, dan Product Selector tetap tampil pada header

### TC-GS-USER-1000: Tab Role untuk Read Only: switch Active dan checkbox Disabled dengan tooltip permission

47. Klik menu User di sidebar Global Settings
48. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
49. Klik Name `Ahmad Fauzi`
50. Klik Tab `Role`
51. Arahkan kursor ke switch Active baris `Manage TAG`
52. Verifikasi switch Active baris `Manage TAG` tampil namun disabled
53. Verifikasi tooltip `Read Only access cannot modify data.`
54. Arahkan kursor ke checkbox Update baris `Manage TAG`
55. Verifikasi checkbox Update baris `Manage TAG` tampil namun disabled
56. Verifikasi tooltip `Read Only access cannot modify data.`

### TC-GS-USER-1071: Hover Avatar header tidak menampilkan [Edit]/[Delete] untuk Read Only

57. Klik menu User di sidebar Global Settings
58. Klik icon Search, ketik `John Doe`, tekan Enter
59. Klik Name `John Doe`
60. Verifikasi avatar John Doe (foto) tampil pada header
61. Arahkan kursor ke Avatar header
62. Verifikasi overlay `[Edit]` dan `[Delete]` tidak dirender
63. Verifikasi Avatar dan nama tetap tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi) dengan satu role (Read Only); kontrol yang tidak tersedia pada List dan Detail. Spec melewati sekitar 35 langkah (63 langkah) karena semua blok berada di satu kelas (Role Matrix negatif Read Only, fungsional baca saja tanpa aksi yang mengubah data), satu akun, dan berbagi satu pembukaan List dan satu pembukaan Detail Dewi Lestari; tiap blok TC berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Enam pasang langkah buka dan verifikasi tab (langkah 27 sampai 44) berasal dari satu Expected TC-GS-USER-81 butir f.
- Urutan TC sumber diubah: TC-GS-USER-1002 berada tepat setelah TC-GS-USER-81 karena keduanya mengamati header User Detail Dewi Lestari yang sama (header tetap tampil di semua tab), sehingga tidak perlu membuka Detail ulang; TC-GS-USER-1000 dan TC-GS-USER-1071 membuka user lain dan berada sesudahnya.
- Langkah buka layar User List tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (memilih 100 baris per halaman), 10 (menutup overlay), 14 (klik sel Email sebagai percobaan memilih baris, langkah 2 TC-GS-USER-48), 25 (mencari menu `[⋯]`), 47 dan 48, 57 dan 58 (kembali ke User List dan mencari user; Search dipakai karena tampilan 100 baris per halaman belum tentu dipertahankan).
- Langkah anchor positif untuk asersi absence (bukan Expected TC; konvensi 8b butir 2): langkah 2 (baris Dewi Lestari tampil) untuk langkah 4, 5, dan 9; langkah 8 untuk langkah 9; langkah 21 dan 23 untuk langkah 22 dan 24; langkah 60 untuk langkah 62.
- Langkah 6 mengasersi "aktif" sebagai tampil dan enabled; interaksi tiap kontrol (mengetik, memfilter, mengurutkan) tidak termasuk Expected TC-GS-USER-47.
- Temuan untuk QA:
  - TC-GS-USER-81 langkah 3 menyebut "Klik menu `[⋯]` header" padahal Expected d menyatakan menu Hidden; spec mencoba menemukan menu (langkah 25) dan mengasersi menu tidak dirender.
  - TC-GS-USER-81 langkah 5 menyebut "Hover elemen yang disabled" tanpa menunjuk elemen selain switch Active header dan checkbox Tab Role; spec memakai switch Active header dan, pada Tab Role, switch Active serta checkbox Update baris `Manage TAG` (sama dengan TC-GS-USER-1000).
  - TC-GS-USER-81 Expected b menyebut `Resend ... Email`, `Scan TAG`, dan `Unpair` Hidden; untuk Dewi Lestari (Activated, tanpa email pending) `Resend Activation Email` dan `Resend Confirmation Email` tidak tampil terlepas dari role, dan `Unpair` hanya tampil bila TAG terpasang, sehingga sebagian asersi tidak membedakan Read Only dari role lain. Kondisi TAG Dewi Lestari tidak disebut di Tabel Pre-setup No. 12.
  - TC-GS-USER-81 Expected e dan TC-GS-USER-1000 menguji kondisi yang sama (switch Active dan checkbox Tab Role disabled dengan tooltip permission) pada user berbeda.
  - TC-GS-USER-81 Expected f ("dapat dibuka") tanpa penanda isi tab; spec mengasersi tab terbuka.
  - TC-GS-USER-47 Expected e menyebut Search, Filter, Sort, Pagination, dan Column Visibility "aktif" tanpa definisi; spec mengasersi tampil dan enabled.
  - TC-GS-USER-48 langkah 2 "Coba pilih baris (tidak ada checkbox)" tanpa aksi pasti; spec mengklik sel Email baris Dewi Lestari.
  - Seluruh TC sumber spec ini (termasuk TC-GS-USER-1000 dan TC-GS-USER-1071) berprecondition Read Only; kontrol List holder Manage user and role (Read-Only role) diverifikasi di spec 013 (TC-GS-USER-66 dan TC-GS-USER-1004).
