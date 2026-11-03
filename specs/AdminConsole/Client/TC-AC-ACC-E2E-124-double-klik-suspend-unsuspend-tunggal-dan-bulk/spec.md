---
id: TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk
title: "Double-klik Konfirmasi Suspend dan Unsuspend (Tunggal dan Bulk) Hanya Memproses Satu Kali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-647
  - TC-AC-ACC-648
  - TC-AC-ACC-649
  - TC-AC-ACC-650
coverage:
  web: automated
---

# Double-klik Konfirmasi Suspend dan Unsuspend (Tunggal dan Bulk) Hanya Memproses Satu Kali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan (S-06): C-11 `PT Sinar Distributor` (Active) dan C-13 `PT Ganti Mitra` (Active) disuspend lalu di-Unsuspend; C-03 `PT Wahana Nusantara` (Suspended) dan C-LIF-6 `PT Ditahan Dua` (Suspended, FAMS Active; Tabel A3) di-Unsuspend lalu di-Suspend kembali. Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated keempat Client bertambah; badge subscription tidak berubah.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-647: Double-klik [Suspend] pada dialog Suspend hanya memproses satu kali

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sinar Distributor` lalu tekan Enter
2. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` untuk "PT Sinar Distributor" (N0), lalu tutup modal
3. Ketik Search `PT Sinar Distributor`, tekan Enter
4. Klik `[⋯]` pada baris `PT Sinar Distributor` → pilih `Suspend`
5. Klik `[Suspend]` dua kali cepat
6. Verifikasi `[Suspend]` ter-disable segera setelah klik pertama
7. Verifikasi toast "Success, client has been suspended." tampil satu kali
8. Klik sub-tab Suspended
9. Verifikasi `PT Sinar Distributor` tampil di sub-tab Suspended
10. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sinar Distributor` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
11. Verifikasi jumlah baris Action `Suspend` untuk "PT Sinar Distributor" adalah N0 + 1
12. Verifikasi baris baru: Client Name "PT Sinar Distributor", Field `Status`, Old Value `Active`, New Value `Suspended`
13. Tutup modal Changelog
14. Klik `[⋯]` pada baris `PT Sinar Distributor` → pilih `Unsuspend`, lalu klik `[Unsuspend]`

### TC-AC-ACC-648: Double-klik [Unsuspend] pada dialog Unsuspend hanya memproses satu kali

15. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Ditahan Dua` lalu tekan Enter
16. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Unsuspend` untuk "PT Ditahan Dua" (N0), lalu tutup modal
17. Klik sub-tab Suspended, ketik Search `PT Ditahan Dua`, tekan Enter
18. Klik `[⋯]` pada baris `PT Ditahan Dua` → pilih `Unsuspend`
19. Tunggu toast lama hilang
20. Klik `[Unsuspend]` dua kali cepat
21. Verifikasi `[Unsuspend]` ter-disable segera setelah klik pertama
22. Verifikasi toast "Success, client has been unsuspended." tampil satu kali
23. Klik sub-tab Active
24. Verifikasi `PT Ditahan Dua` tampil di sub-tab Active
25. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Ditahan Dua` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
26. Verifikasi jumlah baris Action `Unsuspend` untuk "PT Ditahan Dua" adalah N0 + 1
27. Verifikasi baris baru: Client Name "PT Ditahan Dua", Field `Status`, Old Value `Suspended`, New Value `Active`
28. Tutup modal Changelog
29. Klik `[⋯]` pada baris `PT Ditahan Dua` → pilih `Suspend`, lalu klik `[Suspend]`

### TC-AC-ACC-649: Double-klik [Suspend] pada dialog Bulk Suspend hanya memproses satu kali

30. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sinar Distributor` lalu tekan Enter
31. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` untuk "PT Sinar Distributor" (N1)
32. Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter, catat jumlah baris Action `Suspend` untuk "PT Ganti Mitra" (N2), lalu tutup modal
33. Klik sub-tab Active
34. Ketik Search `PT Sinar Distributor`, tekan Enter, lalu centang barisnya
35. Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter, lalu centang barisnya
36. Klik Bulk Action → pilih `Suspend`
37. Tunggu toast lama hilang
38. Klik `[Suspend]` dua kali cepat
39. Verifikasi `[Suspend]` ter-disable segera setelah klik pertama
40. Verifikasi toast "Success, client has been suspended." tampil satu kali
41. Klik sub-tab Suspended
42. Ketik Search `PT Sinar Distributor`, tekan Enter
43. Verifikasi `PT Sinar Distributor` tampil di sub-tab Suspended
44. Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter
45. Verifikasi `PT Ganti Mitra` tampil di sub-tab Suspended
46. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sinar Distributor` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` (N3)
47. Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter, catat jumlah baris Action `Suspend` (N4)
48. Verifikasi N3 adalah N1 + 1 dan N4 adalah N2 + 1
49. Verifikasi baris baru kedua Client: Field `Status`, Old Value `Active`, New Value `Suspended`
50. Tutup modal Changelog
51. Ketik Search `PT Sinar Distributor`, tekan Enter, centang barisnya
52. Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter, centang barisnya
53. Klik Bulk Action → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

### TC-AC-ACC-650: Double-klik [Unsuspend] pada dialog Bulk Unsuspend hanya memproses satu kali

54. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter
55. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Unsuspend` untuk "PT Wahana Nusantara" (N1)
56. Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter, catat jumlah baris Action `Unsuspend` (N2), lalu tutup modal
57. Klik sub-tab Suspended
58. Ketik Search `PT Wahana Nusantara`, tekan Enter, lalu centang barisnya
59. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, lalu centang barisnya
60. Klik Bulk Action → pilih `Unsuspend`
61. Tunggu toast lama hilang
62. Klik `[Unsuspend]` dua kali cepat
63. Verifikasi `[Unsuspend]` ter-disable segera setelah klik pertama
64. Verifikasi toast "Success, client has been unsuspended." tampil satu kali
65. Klik sub-tab Active
66. Ketik Search `PT Wahana Nusantara`, tekan Enter
67. Verifikasi `PT Wahana Nusantara` tampil di sub-tab Active
68. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter
69. Verifikasi `PT Ditahan Dua` tampil di sub-tab Active
70. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Unsuspend` (N3)
71. Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter, catat jumlah baris Action `Unsuspend` (N4)
72. Verifikasi N3 adalah N1 + 1 dan N4 adalah N2 + 1
73. Verifikasi baris baru kedua Client: Field `Status`, Old Value `Suspended`, New Value `Active`
74. Tutup modal Changelog
75. Ketik Search `PT Wahana Nusantara`, tekan Enter, centang barisnya
76. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, centang barisnya
77. Klik Bulk Action → pilih `Suspend`, lalu klik `[Suspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah (di atas smell): empat TC satu topik (guard double-klik pada dialog konfirmasi Suspend/Unsuspend), satu akun, satu kelas harness; tiap blok memakai Client sendiri atau memulihkan statusnya dan menulis baseline Changelog sendiri sehingga tetap bermakna walau blok sebelumnya gagal. Baseline N0/N1/N2 dicatat sebelum aksi pemicu (S-12); TC menulis "bertambah tepat satu baris" dan spec mengasersi selisih terhadap baseline.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan status di akhir tiap blok (langkah 14, 29, 53, 77; Post Condition TC), penutupan modal Changelog, dan "Tunggu toast lama hilang" sebelum asersi hitungan toast (R-12). Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-647 sampai 650 adalah aksi pemulihan dan sudah menjadi langkah.
- Temuan untuk QA:
  - TC-AC-ACC-647 dan 648 Expected a ("ter-disable segera setelah klik pertama") dan b (toast satu kali) menuntut asersi state sementara tepat waktu; spec mengasersinya segera setelah double-klik (butir 5 bagian 8b).
