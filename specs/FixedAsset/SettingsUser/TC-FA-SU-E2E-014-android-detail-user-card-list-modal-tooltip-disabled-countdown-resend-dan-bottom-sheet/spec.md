---
id: TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet
title: "Android: Detail User, Card List, Modal, Tooltip Disabled, Countdown Resend, dan Bottom Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-44
  - TC-FA-SU-45
  - TC-FA-SU-46
  - TC-FA-SU-47
  - TC-FA-SU-48
  - TC-FA-SU-49
coverage:
  mobile: automated
---

# Android: Detail User, Card List, Modal, Tooltip Disabled, Countdown Resend, dan Bottom Sheet

## Prerequisites

- Mode: FE+BE (backend nyata).
- Perangkat: perangkat atau emulator Android dengan aplikasi native TAG Samurai Mobile (FAMS) terpasang (disediakan tim FE). Perangkat dipakai bersama sehingga spec berjalan dengan `parallel: false`; gestur geser, bottom sheet, dan full-screen modal diamati di perangkat itu.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di aplikasi Android di hook `before` spec ini. Hook `beforeEach` suite membuka halaman web dan tidak berlaku untuk perangkat Android, sehingga halaman Settings > User dibuka oleh langkah 1.
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` dengan 25 pengguna (#20) dan pohon grup (#21); Changelog (#27), System Log (#28), dan Transaction Role (#39) Budi Santoso; Hana Kusuma (Pending Activation) dan Indra Wijaya (Pending Email Confirmation) dengan cooldown Resend yang belum berjalan (#37). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: gestur ketuk dan geser pada perangkat Android; pengaturan jam server dan jam perangkat bersama (countdown UI berjalan di jam klien, bagian 6 konvensi) untuk langkah 58, 60, dan 62 (T0 dibaca dari waktu terbit Resend, jam diset absolut ke T0 + 59 dan T0 + 60 detik, bagian 8b butir 3) serta pemulihannya pada langkah 69 dan di hook `after`; baseline cooldown Resend Hana Kusuma dan Indra Wijaya belum berjalan (dibaca lewat kemampuan tim FE/BE). Resend mengirim email sungguhan ke pengguna Pre-setup; efek email tidak diasersi.
- State global: jam server dan jam perangkat; cooldown Resend Hana Kusuma dan Indra Wijaya. Dipulihkan langkah 69 dan hook `after`. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Tab Detail User" (dipakai langkah 22 sampai 26): `Role`, `Responsibilities`, `Non-Login User`, `Changelog`, `System Log`, `Transaction Admin Log`, `User Log`.

## Test Steps

### TC-FA-SU-47: Android: ketuk kontrol Disabled menampilkan tooltip yang hilang otomatis dan bukan toast

1. Buka Settings > User di aplikasi Android
2. Ketuk sakelar Active kartu Ahmad Dahlan (Default User)
3. Verifikasi tooltip "Default User cannot be modified." tampil
4. Verifikasi tidak ada toast yang tampil
5. Verifikasi tooltip hilang otomatis

### TC-FA-SU-49: Android: dialog dan popup tampil sebagai bottom sheet atau full-screen modal sesuai jenisnya (bagian User List)

6. Ketuk label jumlah Role `4 roles` pada kartu Budi Santoso
7. Verifikasi Popup Role Count tampil sebagai bottom sheet
8. Tutup Popup Role Count

### TC-FA-SU-46: Android: Popup Detail Group Assignment, Combined Changelog, dan Changelog per sub-tab Role tampil sebagai full-screen modal (bagian User List)

9. Ketuk ikon Changelog di User List
10. Verifikasi Combined Changelog tampil sebagai full-screen modal
11. Verifikasi isi dan kolom Combined Changelog setara web dalam bentuk Card List
12. Tutup Combined Changelog lewat tombol close
13. Verifikasi Combined Changelog tertutup

### TC-FA-SU-44: Android: Detail User tersusun vertikal dengan tab dan sub-tab geser horizontal

14. Buka Detail Budi Santoso di Android
15. Verifikasi header (avatar, nama, badge status, sakelar Active, tombol Resend) tersusun vertikal
16. Verifikasi General Information satu kolom
17. Geser tab ke kanan
18. Verifikasi tab dan sub-tab Role, Responsibilities, Transaction Admin Log, dan User Log berupa navigasi horizontal yang dapat digeser jari
19. Ketuk tab Responsibilities
20. Geser sub-tab pada Tab Responsibilities
21. Verifikasi sub-tab Responsibilities bergeser horizontal

### TC-FA-SU-45: Android: tabel di Detail User menjadi Card List dan toolbar tab masuk bottom sheet

22. Untuk setiap baris tabel "Tab Detail User" (langkah 22 sampai 26): ketuk tab pada baris itu
23. Verifikasi tabel pada tab itu bertransformasi menjadi Card List
24. Ketuk `[⋯]` toolbar
25. Verifikasi Search, Filter, Download, dan Changelog tab atau sub-tab itu masuk ke bottom sheet `[⋯]` seperti User List
26. Tutup bottom sheet

### TC-FA-SU-46 dan TC-FA-SU-49: modal dan popup pada Tab Role Detail User

27. Ketuk tab Role
28. Ketuk ikon Changelog pada Sub-tab Global Role
29. Verifikasi Changelog sub-tab Global Role tampil sebagai full-screen modal
30. Verifikasi isi dan kolom Changelog sub-tab Global Role setara web dalam bentuk Card List
31. Tutup Changelog lewat tombol close
32. Verifikasi Changelog sub-tab Global Role tertutup
33. Ketuk sub-tab Group Role
34. Ketuk `[Detail]` pada Group Role
35. Verifikasi Popup Detail Group Assignment tampil sebagai full-screen modal
36. Verifikasi isi dan kolom Popup Detail Group Assignment setara web dalam bentuk Card List
37. Tutup Popup Detail Group Assignment lewat tombol close
38. Verifikasi Popup Detail Group Assignment tertutup
39. Ketuk `[Assign Group]` pada Group Role
40. Verifikasi popup Assign Group Role tampil sebagai bottom sheet
41. Ketuk `[+ Assign Group]`
42. Verifikasi Select Group tampil sebagai full-screen modal
43. Tutup Select Group
44. Tutup popup Assign Group Role
45. Ketuk sub-tab Transaction Role
46. Ketuk `[+ Assign]`
47. Verifikasi modal Assign Transaction Role tampil sebagai bottom sheet
48. Ketuk tombol Group pada modal Assign Transaction Role
49. Verifikasi popup tree Group pada modal Assign Transaction Role tampil sebagai full-screen modal
50. Tutup popup tree Group
51. Tutup modal Assign Transaction Role
52. Ketuk ikon edit Home Group pada General Information
53. Verifikasi Select Home Group tampil sebagai full-screen modal
54. Tutup Select Home Group

### TC-FA-SU-48: Android: hitung mundur cooldown Resend ditampilkan sebagai teks di tombol

55. Kembali ke User List
56. Buka Detail Hana Kusuma di Android
57. Ketuk Resend Activation Email
58. Baca T0 dari waktu terbit pengiriman Resend Hana Kusuma
59. Verifikasi tombol berlabel `Resend Activation Email (60s)`
60. Setel jam server dan jam perangkat ke T0 + 59 detik
61. Verifikasi tombol berlabel `Resend Activation Email (1s)` sesudah menghitung mundur dari `(60s)`
62. Setel jam server dan jam perangkat ke T0 + 60 detik
63. Verifikasi tombol kembali berlabel `Resend Activation Email` tanpa hitung mundur
64. Verifikasi tombol Enabled
65. Kembali ke User List
66. Buka Detail Indra Wijaya di Android
67. Ketuk Resend Confirmation Email
68. Verifikasi tombol berlabel pola `Resend Confirmation Email ([Seconds]s)`
69. Pulihkan jam server dan jam perangkat ke waktu semula

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Seluruh TC bertanda `Manual Only (b)` tetap masuk spec (bagian 2 konvensi); kebutuhan teknisnya ada di `## Prerequisites`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok di spec mengikuti posisi layar (User List, Detail Budi Santoso, lalu Detail Hana Kusuma dan Indra Wijaya) supaya navigasi tidak berulang (S-10): TC-FA-SU-47, bagian User List dari TC-FA-SU-49 dan TC-FA-SU-46, TC-FA-SU-44, TC-FA-SU-45, bagian Tab Role dari TC-FA-SU-46 dan TC-FA-SU-49, lalu TC-FA-SU-48.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 12 (menutup popup atau modal, S-09), langkah 26 (menutup bottom sheet), langkah 43, 44, 50, 51, dan 54 (menutup modal atau popup tanpa mengubah data; tidak ada form yang dirty), langkah 55 dan 65 (kembali ke User List), langkah 58 (membaca T0 dari waktu terbit Resend, bagian 8b butir 3), langkah 60 dan 62 (menyetel jam absolut), langkah 69 (memulihkan jam, S-09). Langkah 22 sampai 26 diulang untuk tujuh tab tabel parameter (ekspansi 35 langkah dari 5 langkah nominal, bagian 8b butir 7), sehingga bottom sheet `[⋯]` toolbar diasersi pada tiap tab.
- Langkah 4 (absence toast) diletakkan segera sesudah tooltip tampil (langkah 3) dan sebelum tooltip hilang (langkah 5) menurut bagian 8b butir 11; tooltip pada langkah 3 menjadi anchor positif.
- Langkah 60 dan 62: countdown UI berjalan di jam klien sehingga jam server dan jam perangkat diatur bersama (bagian 6 konvensi); langkah 61 membuktikan label menghitung mundur dari `(60s)` ke `(1s)`.
- Spec melewati sekitar 35 langkah (69 langkah nominal, 99 dengan ekspansi). Seluruhnya satu kelas (tampilan Android, satu perangkat, tanpa mengubah data bisnis; cooldown Resend adalah state yang dipulihkan), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: kartu User List, row action, toolbar, seleksi, dan drawer Group Tree (TC-FA-SU-39 sampai 43) ada di spec 013.
- Temuan untuk QA:
  - TC-FA-SU-49 Expected a menyebut dialog konfirmasi (termasuk Auto-Revert), dialog Downgrade, dan dialog Remove Transaction Role sebagai bottom sheet, dan Expected b menyebut popup Assign Group Transaction Role sebagai full-screen modal; Langkah Uji TC tidak memicu surface itu. Spec hanya mengasersi surface yang dipicu Langkah Uji (Popup Role Count, popup Assign Group Role, Select Group, modal Assign Transaction Role, popup tree Group, Select Home Group).
  - TC-FA-SU-46 Langkah Uji 1 ("Ketuk [Detail] pada Group Role") tidak menyebut posisi (Tab Role, sub-tab Group Role) dan baris Group Role mana; spec memakai Detail Budi Santoso yang memiliki Group Role (Manage group pada Finance & Accounting).
  - TC-FA-SU-48 Langkah Uji 3 ("Amati label tombol tiap beberapa detik") bergantung pada waktu nyata; spec memakai jam server dan jam perangkat yang diatur bersama (bagian 6) sehingga tidak ada menunggu nyata di atas 30 detik.
  - TC-FA-SU-48 Expected b hanya memberi pola `Resend Confirmation Email ([Seconds]s)` tanpa nilai; spec mengasersi pola sesudah Resend dan tidak mengasersi nilai detik.
  - TC-FA-SU-45 Expected a menyebut tujuh tab; Langkah Uji TC hanya membuka Tab Changelog dan Tab System Log. Spec membuka ketujuh tab dari tabel parameter.
