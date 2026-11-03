---
id: TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx
title: "Resilience Suspend dan Unsuspend (Tunggal dan Bulk): Global Settings Tidak Terjangkau dan Respons 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-199
  - TC-AC-ACC-200
  - TC-AC-ACC-214
  - TC-AC-ACC-460
  - TC-AC-ACC-463
coverage:
  web: automated
---

# Resilience Suspend dan Unsuspend (Tunggal dan Bulk): Global Settings Tidak Terjangkau dan Respons 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan kegagalan sisi server; asersi memakai state backend nyata sehingga bukan `Mode: mock`).
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (hanya dibaca; semua aksi gagal sehingga status tidak berubah): C-01 `PT Sejahtera Abadi` (Active), C-02 `PT Teknologi Maju` (Active), C-03 `PT Wahana Nusantara` (Suspended), C-LIF-6 `PT Ditahan Dua` (Suspended; Tabel A3). TC tidak menyebut Client untuk TC-AC-ACC-199, 200, 214, 463; spec memakai Client di atas (lihat Temuan).
- Kemampuan teknis: memaksa Global Settings tidak terjangkau (kegagalan sisi server, bukan respons HTTP browser; disediakan tim FE/BE; GS dipulihkan di akhir tiap blok dan di hook `after`); `Spectra.intercept()` untuk memaksa respons 500 pada request konfirmasi Suspend (TC-AC-ACC-200), dilepas segera setelah pemicu selesai (S-09).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-199: Global Settings tidak terjangkau saat Suspend: gagal seluruhnya tanpa perubahan parsial

1. Paksa Global Settings tidak terjangkau
2. Ketik Search `PT Sejahtera Abadi`, tekan Enter
3. Klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Suspend`
4. Klik `[Suspend]` pada dialog
5. Verifikasi toast error "Error, failed to suspend client."
6. Klik `[Cancel]` pada dialog
7. Pulihkan Global Settings terjangkau
8. Muat ulang List dan ketik Search `PT Sejahtera Abadi`, tekan Enter
9. Verifikasi baris `PT Sejahtera Abadi` tetap berstatus Active di sub-tab Active

### TC-AC-ACC-200: Suspend gagal 5xx: dialog tetap terbuka

10. Pasang intercept respons 500 pada request konfirmasi Suspend
11. Klik `[⋯]` pada baris `PT Sejahtera Abadi` → pilih `Suspend`
12. Klik `[Suspend]` pada dialog
13. Verifikasi toast error "Error, failed to suspend client."
14. Verifikasi dialog Suspend tetap terbuka
15. Lepas intercept respons 500
16. Klik `[Cancel]` pada dialog
17. Muat ulang List dan ketik Search `PT Sejahtera Abadi`, tekan Enter
18. Verifikasi baris `PT Sejahtera Abadi` tetap berstatus Active di sub-tab Active

### TC-AC-ACC-214: Bulk Suspend gagal seluruhnya karena Global Settings

19. Ketik Search `PT Sejahtera Abadi`, tekan Enter, lalu centang barisnya
20. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter, lalu centang barisnya
21. Paksa Global Settings tidak terjangkau
22. Klik Bulk Action → pilih `Suspend`, lalu klik `[Suspend]` pada dialog
23. Verifikasi toast error "Error, failed to suspend clients."
24. Verifikasi dialog konfirmasi Title "Suspend Clients" tetap terbuka
25. Verifikasi bullet Company Name terpilih (`PT Sejahtera Abadi`, `PT Teknologi Maju`) dipertahankan pada dialog
26. Verifikasi tombol `[Suspend]` kembali enabled (retry manual)
27. Pulihkan Global Settings terjangkau
28. Klik `[Cancel]` pada dialog "Suspend Clients"
29. Muat ulang List
30. Verifikasi `PT Sejahtera Abadi` tetap di sub-tab Active
31. Verifikasi `PT Teknologi Maju` tetap di sub-tab Active

### TC-AC-ACC-460: Global Settings tidak terjangkau saat Unsuspend: toast error, dialog tetap terbuka, status tidak berubah

32. Paksa Global Settings tidak terjangkau
33. Klik sub-tab Suspended
34. Ketik Search `PT Wahana Nusantara`, tekan Enter
35. Klik `[⋯]` pada baris `PT Wahana Nusantara` → pilih `Unsuspend`
36. Klik `[Unsuspend]` pada dialog
37. Verifikasi toast error "Error, failed to unsuspend client."
38. Verifikasi dialog "Unsuspend Client" tetap terbuka
39. Klik `[Cancel]` pada dialog
40. Pulihkan Global Settings terjangkau
41. Verifikasi `PT Wahana Nusantara` masih berada di sub-tab Suspended dengan status tetap Suspended

### TC-AC-ACC-463: Bulk Unsuspend gagal seluruhnya karena Global Settings

42. Ketik Search `PT Wahana Nusantara`, tekan Enter, lalu centang barisnya
43. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, lalu centang barisnya
44. Paksa Global Settings tidak terjangkau
45. Klik Bulk Action → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog
46. Verifikasi toast error "Error, failed to unsuspend clients."
47. Verifikasi dialog konfirmasi Title "Unsuspend Clients" tetap terbuka
48. Verifikasi bullet Company Name terpilih (`PT Wahana Nusantara`, `PT Ditahan Dua`) dipertahankan pada dialog
49. Verifikasi tombol `[Unsuspend]` kembali enabled (retry manual)
50. Pulihkan Global Settings terjangkau
51. Klik `[Cancel]` pada dialog "Unsuspend Clients"
52. Muat ulang List dan klik sub-tab Suspended
53. Ketik Search `PT Wahana Nusantara`, tekan Enter
54. Verifikasi `PT Wahana Nusantara` tetap berstatus Suspended
55. Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter
56. Verifikasi `PT Ditahan Dua` tetap berstatus Suspended

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas lima TC satu kelas harness (fault injection pada Suspend/Unsuspend), satu akun; tiap blok memakai Client dan pemicu kegagalan sendiri sehingga tetap bermakna walau blok sebelumnya gagal. `P-5` butir b tidak dipakai karena seluruh spec adalah kelas b.
- Langkah penghubung (tanpa awalan Verifikasi): memulihkan Global Settings dan melepas intercept segera setelah pemicu (langkah 7, 15, 27, 40, 50; S-09), `[Cancel]` menutup dialog yang tetap terbuka (langkah 28, 51; dialog diasersi tetap terbuka lebih dulu), muat ulang List dan Search ulang untuk membaca status. Asersi absence "status tetap Active" memakai baris yang tampil di sub-tab sebagai anchor positif (baris dibuktikan oleh pencarian nama).
- Post Condition TC-AC-ACC-199, 200, 214, 460, 463: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-199, 200, 214, 463 tidak menyebut Client target; spec memakai Pre-setup C-01, C-02, C-03, dan C-LIF-6. TC-AC-ACC-214 dan 463 tidak menyebut baris yang dipilih; spec memilih dua Client di atas.
  - TC-AC-ACC-199 Expected hanya "status tetap Active" tanpa langkah observasi; spec membaca status dari List setelah memulihkan GS.
  - TC-AC-ACC-463 judulnya "Bulk Suspend/Unsuspend" tetapi langkah dan Expected hanya Bulk Unsuspend; spec mengikuti Langkah dan Expected.
