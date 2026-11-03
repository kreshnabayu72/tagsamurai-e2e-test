---
id: TC-AC-ACC-E2E-138-bulk-suspend-unsuspend-semua-terpilih
title: "Bulk Suspend dan Bulk Unsuspend: Dialog Gabungan Tanpa Jumlah, Toast Sukses, Badge Subscription Tidak Berubah, dan Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-208
  - TC-AC-ACC-209
coverage:
  web: automated
---

# Bulk Suspend dan Bulk Unsuspend: Dialog Gabungan Tanpa Jumlah, Toast Sukses, Badge Subscription Tidak Berubah, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-01 `PT Sejahtera Abadi` (Active; FAMS, SAMS, SIEM Active) dan C-02 `PT Teknologi Maju` (Active; FAMS Grace; SAMS dan SIEM No Subscription) disuspend lalu di-Unsuspend; C-03 `PT Wahana Nusantara` (Suspended; FAMS Expired, SAMS Archive, SIEM No Subscription) dan C-LIF-6 `PT Ditahan Dua` (Suspended, FAMS Active; Tabel A3) di-Unsuspend lalu di-Suspend kembali. Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated keempat Client bertambah; badge subscription tidak berubah.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-208: Bulk Suspend semua Active: dialog gabungan tanpa jumlah, toast sukses, badge subscription tidak berubah

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter
2. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` untuk "PT Sejahtera Abadi" (N1)
3. Ganti isi Search modal dengan `PT Teknologi Maju` lalu tekan Enter, catat jumlah baris Action `Suspend` untuk "PT Teknologi Maju" (N2), lalu tutup modal
4. Ketik Search `PT Sejahtera Abadi`, tekan Enter
5. Centang baris `PT Sejahtera Abadi`
6. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
7. Centang baris `PT Teknologi Maju`
8. Klik Bulk Action lalu pilih `Suspend`
9. Verifikasi header dialog berjudul "Suspend Clients"
10. Verifikasi body dialog memuat bullet `• PT Sejahtera Abadi` dan `• PT Teknologi Maju`
11. Verifikasi body dialog memuat "Suspending these clients will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend them?"
12. Verifikasi footer memuat `[Cancel]` dan `[Suspend]`
13. Verifikasi lebar dialog 480px
14. Verifikasi dialog tidak menampilkan jumlah Client
15. Klik `[Suspend]` pada dialog
16. Verifikasi toast sukses "Success, client has been suspended."
17. Klik sub-tab Suspended
18. Ketik Search `PT Sejahtera Abadi`, tekan Enter
19. Verifikasi `PT Sejahtera Abadi` tampil di sub-tab Suspended
20. Verifikasi sel FAMS `Active`, SAMS `Active`, dan SIEM `Active` baris `PT Sejahtera Abadi`
21. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
22. Verifikasi `PT Teknologi Maju` tampil di sub-tab Suspended
23. Verifikasi sel FAMS `Grace`, SAMS "No Subscription", dan SIEM "No Subscription" baris `PT Teknologi Maju` (sama seperti sebelum Suspend)
24. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
25. Verifikasi jumlah baris Action `Suspend` untuk "PT Sejahtera Abadi" adalah N1 + 1
26. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Suspend`, Client Name `PT Sejahtera Abadi`, Field `Status`, Old Value `Active`, New Value `Suspended`
27. Ganti isi Search modal dengan `PT Teknologi Maju` lalu tekan Enter
28. Verifikasi jumlah baris Action `Suspend` untuk "PT Teknologi Maju" adalah N2 + 1
29. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Suspend`, Client Name `PT Teknologi Maju`, Field `Status`, Old Value `Active`, New Value `Suspended`
30. Tutup modal Changelog
31. Ketik Search `PT Sejahtera Abadi`, tekan Enter, centang barisnya
32. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter, centang barisnya
33. Klik Bulk Action → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

### TC-AC-ACC-209: Bulk Unsuspend semua Suspended: menu hanya Unsuspend, dialog tanpa jumlah, badge subscription tidak berubah

34. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter
35. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Unsuspend` untuk "PT Wahana Nusantara" (U1)
36. Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter, catat jumlah baris Action `Unsuspend` untuk "PT Ditahan Dua" (U2), lalu tutup modal
37. Klik sub-tab Suspended
38. Ketik Search `PT Wahana Nusantara`, tekan Enter
39. Centang baris `PT Wahana Nusantara`
40. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter
41. Centang baris `PT Ditahan Dua`
42. Klik Bulk Action
43. Verifikasi menu Bulk Action hanya memuat `Unsuspend`
44. Verifikasi `Suspend` tidak ada di menu Bulk Action
45. Klik `Unsuspend`
46. Verifikasi header dialog berjudul "Unsuspend Clients"
47. Verifikasi body dialog memuat bullet `• PT Wahana Nusantara` dan `• PT Ditahan Dua`
48. Verifikasi body dialog memuat "Unsuspending these clients will restore access to all subscribed products. Are you sure you want to unsuspend them?"
49. Verifikasi footer memuat `[Cancel]` dan `[Unsuspend]`
50. Verifikasi lebar dialog 480px
51. Verifikasi dialog tidak menampilkan jumlah Client
52. Klik `[Unsuspend]`
53. Verifikasi toast sukses "Success, client has been unsuspended."
54. Klik sub-tab Active
55. Ketik Search `PT Wahana Nusantara`, tekan Enter
56. Verifikasi `PT Wahana Nusantara` tampil di sub-tab Active
57. Verifikasi sel FAMS `Expired`, SAMS `Archive`, dan SIEM "No Subscription" baris `PT Wahana Nusantara` (sama seperti sebelum Unsuspend)
58. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter
59. Verifikasi `PT Ditahan Dua` tampil di sub-tab Active
60. Verifikasi sel FAMS `Active` baris `PT Ditahan Dua` (sama seperti sebelum Unsuspend)
61. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
62. Verifikasi jumlah baris Action `Unsuspend` untuk "PT Wahana Nusantara" adalah U1 + 1
63. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Unsuspend`, Client Name `PT Wahana Nusantara`, Field `Status`, Old Value `Suspended`, New Value `Active`
64. Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter
65. Verifikasi jumlah baris Action `Unsuspend` untuk "PT Ditahan Dua" adalah U2 + 1
66. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Unsuspend`, Client Name `PT Ditahan Dua`, Field `Status`, Old Value `Suspended`, New Value `Active`
67. Tutup modal Changelog
68. Ketik Search `PT Wahana Nusantara`, tekan Enter, centang barisnya
69. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, centang barisnya
70. Klik Bulk Action → pilih `Suspend`, lalu klik `[Suspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah (di atas smell): satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas dua TC satu topik (Bulk Suspend dan Bulk Unsuspend semua terpilih), satu akun, dua Client per TC; tiap blok memulihkan status Client-nya sendiri dan menulis baseline sendiri sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan Bulk Unsuspend/Suspend (langkah 31 sampai 33 dan 68 sampai 70; Post Condition TC), baseline N1, N2, U1, U2 (langkah 1 sampai 3 dan 34 sampai 36; S-12, TC menyatakan "baris teratas" sedangkan baseline melindungi dari baris seed), penutupan modal Changelog, dan Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-208 dan 209 adalah aksi pemulihan dan sudah menjadi langkah.
- Temuan untuk QA:
  - TC-AC-ACC-208 dan 209 Expected c dan d ("Setelah langkah 8 dan 9") memakai nomor langkah TC, bukan nomor langkah spec; spec memakai Verifikasi per Client sesudah Search masing-masing.
