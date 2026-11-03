---
id: TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses
title: "Suspend dan Unsuspend Client: Screening Dialog, Cancel, Aksi Sukses, Subscription Tidak Berubah, dan Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-189
  - TC-AC-ACC-190
  - TC-AC-ACC-194
  - TC-AC-ACC-191
  - TC-AC-ACC-193
coverage:
  web: automated
---

# Suspend dan Unsuspend Client: Screening Dialog, Cancel, Aksi Sukses, Subscription Tidak Berubah, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-01 `PT Sejahtera Abadi` (Active; FAMS, SAMS, SIEM Active; disuspend lalu di-Unsuspend) dan C-03 `PT Wahana Nusantara` (Suspended; FAMS Expired, SAMS Archive, SIEM No Subscription; di-Unsuspend lalu di-Suspend kembali). Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated kedua Client bertambah; badge subscription tidak berubah.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-189: Screening Dialog Suspend

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter
2. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Suspend` untuk "PT Sejahtera Abadi" (N0), lalu tutup modal
3. Ketik Search `PT Sejahtera Abadi`, tekan Enter, lalu klik `[⋯]` pada baris `PT Sejahtera Abadi`
4. Klik `Suspend`
5. Verifikasi header dialog berjudul "Suspend Client"
6. Verifikasi body dialog memuat bullet `• PT Sejahtera Abadi`
7. Verifikasi body dialog memuat "Suspending this client will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend it?"
8. Verifikasi footer memuat `[Cancel]` (Text, Contrast) dan `[Suspend]` (danger)
9. Verifikasi lebar dialog 480px

### TC-AC-ACC-190: Cancel pada dialog Suspend tidak mengubah status

10. Klik `[Cancel]` pada dialog
11. Verifikasi dialog tertutup
12. Verifikasi toast tidak tampil
13. Verifikasi baris `PT Sejahtera Abadi` tetap berstatus Active di sub-tab Active
14. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
15. Verifikasi jumlah baris Action `Suspend` untuk "PT Sejahtera Abadi" tetap N0 (tanpa log)
16. Tutup modal Changelog

### TC-AC-ACC-194: Cancel pada dialog Unsuspend

17. Klik sub-tab Suspended
18. Ketik Search `PT Wahana Nusantara`, tekan Enter
19. Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Unsuspend`
20. Klik `[Cancel]` pada dialog
21. Verifikasi dialog tertutup
22. Verifikasi baris `PT Wahana Nusantara` tetap berstatus Suspended di sub-tab Suspended

### TC-AC-ACC-191: Suspend Client: status Suspended, subscription tidak berubah

23. Klik sub-tab Active, ketik Search `PT Sejahtera Abadi`, tekan Enter
24. Klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Suspend`
25. Klik `[Suspend]` pada dialog
26. Verifikasi toast sukses "Success, client has been suspended."
27. Klik sub-tab Suspended, ketik Search `PT Sejahtera Abadi`, tekan Enter
28. Verifikasi `PT Sejahtera Abadi` pindah ke sub-tab Suspended
29. Verifikasi baris `PT Sejahtera Abadi` berteks muted
30. Lihat sel FAMS, SAMS, SIEM baris `PT Sejahtera Abadi`
31. Verifikasi badge FAMS, SAMS, dan SIEM tetap `Active`
32. Buka `[⋯]` baris `PT Sejahtera Abadi`
33. Verifikasi menu `[⋯]` memuat `Detail` dan `Unsuspend`
34. Verifikasi menu `[⋯]` tidak memuat Edit, Change Partner, Suspend, dan Delete
35. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
36. Verifikasi jumlah baris Action `Suspend` untuk "PT Sejahtera Abadi" adalah N0 + 1
37. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Suspend`, Client Name `PT Sejahtera Abadi`, Field `Status`, Old `Active`, New `Suspended`
38. Tutup modal Changelog
39. Klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

### TC-AC-ACC-193: Unsuspend Client: kembali Active, status subscription tidak berubah, dan Changelog Unsuspend tercatat

40. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter
41. Ubah ukuran halaman modal menjadi 100, catat jumlah baris Action `Unsuspend` untuk "PT Wahana Nusantara" (U0), lalu tutup modal
42. Klik sub-tab Suspended
43. Ketik Search `PT Wahana Nusantara`, tekan Enter
44. Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Unsuspend`
45. Verifikasi header dialog berjudul "Unsuspend Client"
46. Verifikasi body dialog memuat bullet `• PT Wahana Nusantara`
47. Verifikasi body dialog memuat "Unsuspending this client will restore access to all subscribed products. Are you sure you want to unsuspend it?"
48. Verifikasi footer memuat `[Cancel]` dan `[Unsuspend]`
49. Verifikasi lebar dialog 480px
50. Klik `[Unsuspend]`
51. Verifikasi toast sukses "Success, client has been unsuspended."
52. Klik sub-tab Active, ketik Search `PT Wahana Nusantara`, tekan Enter
53. Verifikasi baris `PT Wahana Nusantara` tampil di sub-tab Active
54. Verifikasi sel FAMS `Expired`, SAMS `Archive`, dan SIEM "No Subscription" (tidak direset)
55. Klik `[Changelog]` di toolbar List
56. Klik ikon Search di modal Changelog, ketik `PT Wahana Nusantara` lalu tekan Enter, ubah ukuran halaman modal menjadi 100
57. Verifikasi jumlah baris Action `Unsuspend` untuk "PT Wahana Nusantara" adalah U0 + 1
58. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Unsuspend`, Client Name `PT Wahana Nusantara`, Field `Status`, Old Value `Suspended`, New Value `Active` (bukan baris seed L-05 bertanggal 05 Jul 2026)
59. Tutup modal Changelog
60. Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas lima TC satu topik (dialog dan aksi Suspend/Unsuspend tunggal) dengan satu akun; screening dan Cancel berada di awal dan aksi yang mengubah status di akhir. Tiap aksi memulihkan status Client-nya sendiri sehingga blok berikutnya tetap bermakna.
- Langkah penghubung (tanpa awalan Verifikasi): baseline Changelog N0 dan U0 (langkah 1 sampai 2 dan 40 sampai 41; S-12), pemulihan status (langkah 39 dan 60; Post Condition TC-AC-ACC-191 dan 193), penutupan modal Changelog, dan Search yang menemukan baris target (R-16). Langkah 1 sampai 2 mendahului dialog TC-AC-ACC-189 karena dialog yang sedang terbuka tidak dapat dipakai membuka Changelog; dialog dipakai bersama oleh TC-AC-ACC-189 dan 190 (Cancel pada dialog yang sama).
- Asersi tambahan yang dicatat (S-03): langkah 14 sampai 15 mengamati "tanpa log" (Expected a TC-AC-ACC-190) lewat selisih jumlah baris terhadap baseline N0 (asersi jumlah, bukan kelas g).
- Post Condition TC-AC-ACC-189, 190, 194: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-190 dan 194 tidak menyebut Client; spec memakai C-01 untuk Suspend (TC-AC-ACC-190) dan C-03 untuk Unsuspend (TC-AC-ACC-194). TC-AC-ACC-190 Expected "tanpa log" tidak punya langkah observasi di TC; spec memakai Modal Changelog dengan baseline.
  - TC-AC-ACC-191 Expected c menyebut menu ⋯ tanpa "Delete" (Delete Hidden karena Client sudah memiliki subscription) dalam kurung; spec mengasersi tidak adanya Delete.
