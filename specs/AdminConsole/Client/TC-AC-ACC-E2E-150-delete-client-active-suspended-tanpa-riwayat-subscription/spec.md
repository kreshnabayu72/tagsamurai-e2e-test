---
id: TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription
title: "Delete Client Active dan Suspended: Hidden bila Pernah Berlangganan, Tampil bila Tanpa Riwayat atau Hanya Rejected/Canceled, dan Delete Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-224
  - TC-AC-ACC-656
  - TC-AC-ACC-657
  - TC-AC-ACC-1027
  - TC-AC-ACC-466
  - TC-AC-ACC-652
  - TC-AC-ACC-223
  - TC-AC-ACC-606
coverage:
  web: automated
---

# Delete Client Active dan Suspended: Hidden bila Pernah Berlangganan, Tampil bila Tanpa Riwayat atau Hanya Rejected/Canceled, dan Delete Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):

| Blok | Role | Akun | Env password | TC |
|---|---|---|---|---|
| 1 | Active-Full A-15 | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_FULL_PASSWORD` | 224 |
| 2 | Active-Delete-Only A-07 (Manage active client: Delete + Read, exact-match Area Jakarta dan Cabang Menteng) | `activeDeleteJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_DELETE_PASSWORD` | 656, 657, 1027, 466, 652, 223 |
| 3 | Group Manager A-03 (scope Area Jakarta + seluruh descendant) | `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_GM_PASSWORD` | 606 |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup/A3 (kelas Dikonsumsi untuk yang dihapus; Fixture BE yang disediakan tim FE/BE, idempotent, men-seed ulang tanpa syarat di hook `before` dan `after`): C-01 `PT Sejahtera Abadi` dan C-03 `PT Wahana Nusantara` (pernah berlangganan; hanya dibaca); C-ROL-13 `PT Direct Jakarta` (Direct, Group Area Jakarta, tanpa riwayat subscription; hanya dibaca sebagai pembanding); C-07 `PT Cahaya Baru` (FAMS Waiting for Approval) dan C-08 `PT Mulai Esok` (FAMS Pending), hanya dibaca; C-LIF-1 `PT Pengajuan Ditolak` (FAMS Rejected dan SAMS Canceled; hanya dibaca, dibatalkan di dialog); C-FX18-5 `PT Trial Dibatalkan Saja` (Active, SAMS Trial Canceled satu-satunya term; hanya dibaca); C-LIF-3 `PT Hanya Ditolak` (FAMS satu-satunya term Rejected, tanpa user ber-App Access; dihapus); C-LIF-4 `PT Suspend Tanpa Riwayat` (Suspended, tanpa riwayat subscription; dihapus); C-09 `PT Baru Daftar` (Active, belum pernah berlangganan, Default User Not Yet Activated, Group Cabang Menteng; dihapus); C-ROL-18 `PT Menteng Hapus` (Direct, Cabang Menteng, tanpa riwayat subscription, tanpa user ber-App Access; dihapus).
- Efek Delete: Client soft-delete; relasi Client–Partner `transferred` dan relasi Group dilepas; Default User dihapus dari Global Settings karena tanpa peran di entitas lain; baris Changelog `Delete` ditulis.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Full

#### TC-AC-ACC-224: Delete Hidden untuk Client Active/Suspended yang pernah memiliki subscription

1. Klik sub-tab Active, ketik Search `PT Sejahtera Abadi`, tekan Enter
2. Klik `[⋯]` pada baris `PT Sejahtera Abadi`
3. Verifikasi `Delete` Hidden pada menu `[⋯]` `PT Sejahtera Abadi`
4. Klik sub-tab Suspended, ketik Search `PT Wahana Nusantara`, tekan Enter
5. Klik `[⋯]` pada baris `PT Wahana Nusantara`
6. Verifikasi `Delete` Hidden pada menu `[⋯]` `PT Wahana Nusantara`

### Blok 2: Active-Delete-Only

7. Ganti akun: logout lalu login sebagai Active-Delete-Only A-07

#### TC-AC-ACC-656: Delete Hidden pada Client Active dengan term Waiting for Approval atau Pending

8. Klik sub-tab Active, ketik Search `PT Direct Jakarta`, tekan Enter
9. Klik `[⋯]` pada baris `PT Direct Jakarta`
10. Verifikasi menu `[⋯]` `PT Direct Jakarta` memuat `Detail` dan `Delete`
11. Ganti isi Search dengan `PT Cahaya Baru`, tekan Enter
12. Klik `[⋯]` pada baris `PT Cahaya Baru`
13. Verifikasi menu `[⋯]` `PT Cahaya Baru` hanya memuat `Detail`
14. Verifikasi `Delete` Hidden pada menu `[⋯]` `PT Cahaya Baru`
15. Ganti isi Search dengan `PT Mulai Esok`, tekan Enter
16. Klik `[⋯]` pada baris `PT Mulai Esok`
17. Verifikasi menu `[⋯]` `PT Mulai Esok` hanya memuat `Detail`
18. Verifikasi `Delete` Hidden pada menu `[⋯]` `PT Mulai Esok`

#### TC-AC-ACC-657: Client Active dengan term hanya Rejected dan Canceled: Delete tampil dan dialog D-05 terbuka tanpa blok

19. Ganti isi Search dengan `PT Pengajuan Ditolak`, tekan Enter
20. Klik `[⋯]` pada baris `PT Pengajuan Ditolak`
21. Verifikasi menu `[⋯]` `PT Pengajuan Ditolak` memuat `Detail` dan `Delete`
22. Klik `Delete`
23. Verifikasi header dialog berjudul "Delete Client" dengan bullet `• PT Pengajuan Ditolak`
24. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
25. Verifikasi dialog memuat input "Type the client name to confirm" dan checkbox "I understand this action cannot be undone"
26. Verifikasi footer memuat `[Cancel]` dan `[Delete]` yang disabled sampai nama cocok dan checkbox dicentang
27. Verifikasi dialog blok "Cannot Delete Client" tidak tampil
28. Klik `[Cancel]`
29. Verifikasi dialog tertutup
30. Verifikasi Client `PT Pengajuan Ditolak` tetap ada

#### TC-AC-ACC-1027: Client Active dengan baris Trial Canceled sebagai satu-satunya term: Delete tampil di row action

31. Ganti isi Search dengan `PT Trial Dibatalkan Saja`, tekan Enter
32. Verifikasi sel SAMS baris `PT Trial Dibatalkan Saja` berisi teks "No Subscription" (teks sel, bukan badge)
33. Klik `[⋯]` pada baris `PT Trial Dibatalkan Saja`
34. Verifikasi daftar aksi baris memuat `Delete`

#### TC-AC-ACC-466: Client Active dengan term hanya Rejected: Delete tampil dan dapat dijalankan

35. Ganti isi Search dengan `PT Hanya Ditolak`, tekan Enter
36. Klik `[⋯]` pada baris `PT Hanya Ditolak`
37. Verifikasi menu `[⋯]` `PT Hanya Ditolak` memuat `Detail` dan `Delete`
38. Klik `Delete`
39. Verifikasi header dialog berjudul "Delete Client" dengan bullet `• PT Hanya Ditolak`
40. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
41. Verifikasi dialog memuat input "Type the client name to confirm", checkbox "I understand this action cannot be undone", `[Cancel]`, dan `[Delete]`
42. Ketik nama persis `PT Hanya Ditolak`, centang checkbox, klik `[Delete]`
43. Verifikasi toast sukses "Success, client has been deleted."
44. Verifikasi baris `PT Hanya Ditolak` tidak tampil di sub-tab Active

#### TC-AC-ACC-652: Delete dari sub-tab Suspended untuk Client tanpa riwayat subscription

45. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Suspend Tanpa Riwayat` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Delete` (N0), lalu tutup modal
46. Klik sub-tab Suspended, ketik Search `PT Suspend Tanpa Riwayat`, tekan Enter
47. Klik `[⋯]` pada baris `PT Suspend Tanpa Riwayat`
48. Verifikasi menu `[⋯]` `PT Suspend Tanpa Riwayat` memuat `Detail` dan `Delete`
49. Klik `Delete`
50. Verifikasi header dialog berjudul "Delete Client" dengan bullet `• PT Suspend Tanpa Riwayat`
51. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
52. Verifikasi dialog memuat input, checkbox, `[Cancel]`, dan `[Delete]` dengan lebar 480px
53. Ketik nama persis `PT Suspend Tanpa Riwayat`, centang checkbox, klik `[Delete]`
54. Verifikasi toast sukses "Success, client has been deleted."
55. Verifikasi baris `PT Suspend Tanpa Riwayat` tidak tampil di sub-tab Suspended
56. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Suspend Tanpa Riwayat` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu hitung baris Action `Delete` (N1)
57. Verifikasi jumlah baris Action `Delete` untuk Client tersebut bertambah tepat satu dibanding N0 (N1 = N0 + 1)
58. Verifikasi baris baru: Action `Delete`, Field `Company Name`, Old Value `PT Suspend Tanpa Riwayat`, New Value `—`
59. Tutup modal Changelog

#### TC-AC-ACC-223: Delete dari sub-tab Active untuk Client tanpa riwayat subscription: dialog D-05, toast, dan efek Soft Delete

60. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Baru Daftar` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, hitung baris Action `Delete` (N0), lalu tutup modal
61. Klik sub-tab Active
62. Ketik Search `PT Baru Daftar`, tekan Enter
63. Klik `[⋯]` pada baris `PT Baru Daftar` → klik `Delete`
64. Verifikasi header dialog berjudul "Delete Client" dengan bullet `• PT Baru Daftar`
65. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
66. Verifikasi dialog memuat input "Type the client name to confirm" dan checkbox "I understand this action cannot be undone"
67. Verifikasi footer memuat `[Cancel]` dan `[Delete]` (disabled sampai nama cocok dan checkbox dicentang) dengan lebar 480px
68. Ketik nama persis `PT Baru Daftar`, centang checkbox, klik `[Delete]`
69. Verifikasi toast sukses "Success, client has been deleted."
70. Verifikasi baris `PT Baru Daftar` tidak tampil di sub-tab Active
71. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Baru Daftar` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu hitung baris Action `Delete` (N1)
72. Verifikasi jumlah baris Action `Delete` untuk Client tersebut bertambah tepat satu dibanding N0 (N1 = N0 + 1)
73. Verifikasi baris baru: Action `Delete`, Field `Company Name`, Old Value `PT Baru Daftar`, New Value `—`
74. Tutup modal Changelog

### Blok 3: Group Manager

75. Ganti akun: logout lalu login sebagai Group Manager A-03

#### TC-AC-ACC-606: Delete Client oleh Group Manager di node descendant untuk Client tanpa riwayat subscription

76. Ketik Search `PT Menteng Hapus`, tekan Enter
77. Klik `[⋯]` pada baris `PT Menteng Hapus` → klik `Delete`
78. Ketik nama Client `PT Menteng Hapus` pada input konfirmasi
79. Centang checkbox "I understand this action cannot be undone"
80. Verifikasi header dialog berjudul "Delete Client" dengan bullet `• PT Menteng Hapus`
81. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
82. Verifikasi dialog memuat input "Type the client name to confirm", checkbox "I understand this action cannot be undone", `[Cancel]`, dan `[Delete]`
83. Klik `[Delete]`
84. Verifikasi toast sukses "Success, client has been deleted."
85. Verifikasi baris `PT Menteng Hapus` tidak ada lagi di sub-tab Active

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari urutan nomor: TC-AC-ACC-224, 656, 657, dan 1027 (tanpa mengubah data) mendahului Delete sukses (TC-AC-ACC-466, 652, 223, 606) karena aksi yang menghabisi data ditaruh paling akhir per blok (prinsip 5; S-05).
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas delapan TC satu topik (Delete Client Active/Suspended tanpa riwayat subscription); ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras; tiap Delete memakai Client sendiri dan semua blok satu kelas harness.
- Langkah penghubung (tanpa awalan Verifikasi): ganti akun (langkah 7 dan 75), Search yang menemukan baris target (R-16; langkah 11, 15, 19, 31, 35 mengganti isi kotak Search), penutupan modal Changelog, dan langkah baseline Changelog (langkah 45 dan 60, N0; langkah 56 dan 71, N1; S-12). Asersi absence baris sesudah Delete (langkah 44, 55, 70, 85) berlandaskan toast sukses Delete yang sudah diasersi sebagai anchor positif (bagian 8b butir 2).
- Baseline (S-12): TC-AC-ACC-652 dan 223 menyatakan baseline N0 (langkah 1 TC) dan Expected N1 = N0 + 1 (langkah terakhir TC) dengan Search nama Client di modal Changelog dan ukuran halaman 100; fixture di-seed ulang tiap run sehingga baris `Delete` lama bernama sama bisa ada. Spec menghitung jumlah baris Action `Delete` sebelum Delete (N0, langkah 45 dan 60) dan sesudahnya (N1, langkah 56 dan 71), lalu mengasersi N1 = N0 + 1 (langkah 57 dan 72) beserta Old/New Value (langkah 58 dan 73).
- Post Condition TC-AC-ACC-466, 652, 223, 606 ("Seed ulang ... tanpa syarat") dan efek Delete (soft-delete, Default User dihapus, relasi dilepas) tanpa langkah observasi di TC tidak diasersi; seed ulang dilakukan di hook. Langkah 56 sampai 58 dan 71 sampai 73 adalah Expected Changelog TC-AC-ACC-652 dan 223.
- Temuan untuk QA:
  - TC-AC-ACC-223 menghapus C-09 `PT Baru Daftar` yang dipakai sebagai target baca pada TC lain (TC-AC-ACC-168, 225, 244, 464); seed ulang diperlukan sebelum spec itu berjalan (suite serial).
  - TC-AC-ACC-224 tidak menyebut menu `[⋯]` selain Delete; spec hanya mengasersi Delete Hidden. TC-AC-ACC-606 tidak menyebut sub-tab; spec memakai sub-tab Active (Expected c).
  - TC-AC-ACC-656 judul menyebut "Hidden pada Client Active dengan term Waiting for Approval atau Pending", sedangkan Expected a menambahkan pembanding `PT Direct Jakarta` dengan `Detail | Delete`.
