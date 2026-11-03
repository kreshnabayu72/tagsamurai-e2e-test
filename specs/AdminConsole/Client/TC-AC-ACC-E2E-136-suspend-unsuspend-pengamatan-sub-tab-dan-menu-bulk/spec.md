---
id: TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk
title: "Pengamatan Total Control: Grace dan Expired Tetap di Sub-tab Active, Tanpa Aksi Archive, Archived Tanpa Bulk, dan Dialog Bulk Suspend 25 Client"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-640
  - TC-AC-ACC-641
  - TC-AC-ACC-215
  - TC-AC-ACC-642
coverage:
  web: automated
---

# Pengamatan Total Control: Grace dan Expired Tetap di Sub-tab Active, Tanpa Aksi Archive, Archived Tanpa Bulk, dan Dialog Bulk Suspend 25 Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca; spec ini tidak mengonfirmasi aksi apa pun): C-02 `PT Teknologi Maju` (Active, FAMS Grace); C-LIF-5 `PT Berakhir Belum Aktivasi` (Active, FAMS Expired; Tabel A3); C-01 `PT Sejahtera Abadi` (Active), C-03 `PT Wahana Nusantara` (Suspended), C-04 `PT Karya Abadi` (Archived). Sub-tab Active memuat sedikitnya 25 Client (populasi Tabel A2/A3 memuat lebih dari 100 baris Active).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-640: Client dengan term Grace atau Expired tetap berada di sub-tab Active dan tidak otomatis Suspended

1. Klik sub-tab Active
2. Ketik Search `PT Teknologi Maju`, tekan Enter
3. Verifikasi baris `PT Teknologi Maju` tampil dengan sel FAMS `Grace` (severity warning)
4. Ganti isi Search dengan `PT Berakhir Belum Aktivasi`, tekan Enter
5. Verifikasi baris `PT Berakhir Belum Aktivasi` tampil dengan sel FAMS `Expired` (severity danger)
6. Klik sub-tab Suspended
7. Ketik Search `PT Teknologi Maju`, tekan Enter
8. Verifikasi empty state Title "No results found" dengan Description "Try adjusting your search or filter."
9. Ganti isi Search dengan `PT Berakhir Belum Aktivasi`, tekan Enter
10. Verifikasi empty state Title "No results found" dengan Description "Try adjusting your search or filter."

### TC-AC-ACC-641: Tidak ada aksi Archive manual di menu baris semua sub-tab dan di Bulk Action sub-tab Active dan Suspended

11. Klik sub-tab Active
12. Ketik Search `PT Sejahtera Abadi`, tekan Enter
13. Klik `[⋯]` pada baris `PT Sejahtera Abadi`
14. Verifikasi menu `[⋯]` `PT Sejahtera Abadi` memuat `Detail`, `Edit`, `Change Partner`, dan `Suspend`
15. Verifikasi menu `[⋯]` `PT Sejahtera Abadi` tidak memuat item Archive
16. Centang baris `PT Sejahtera Abadi` lalu klik Bulk Action
17. Verifikasi menu Bulk Action sub-tab Active hanya memuat `Suspend`
18. Verifikasi menu Bulk Action sub-tab Active tidak memuat item Archive
19. Tutup menu Bulk Action, hilangkan centang baris `PT Sejahtera Abadi`, lalu klik sub-tab Suspended
20. Ketik Search `PT Wahana Nusantara`, tekan Enter
21. Klik `[⋯]` pada baris `PT Wahana Nusantara`
22. Verifikasi menu `[⋯]` `PT Wahana Nusantara` memuat `Detail` dan `Unsuspend`
23. Verifikasi menu `[⋯]` `PT Wahana Nusantara` tidak memuat item Archive
24. Centang baris `PT Wahana Nusantara` lalu klik Bulk Action
25. Verifikasi menu Bulk Action sub-tab Suspended hanya memuat `Unsuspend`
26. Verifikasi menu Bulk Action sub-tab Suspended tidak memuat item Archive
27. Tutup menu Bulk Action, hilangkan centang baris `PT Wahana Nusantara`, lalu klik sub-tab Archived
28. Ketik Search `PT Karya Abadi`, tekan Enter
29. Klik `[⋯]` pada baris `PT Karya Abadi`
30. Verifikasi menu `[⋯]` `PT Karya Abadi` memuat `Detail`, `Edit`, dan `Delete`
31. Verifikasi menu `[⋯]` `PT Karya Abadi` tidak memuat item Archive

### TC-AC-ACC-215: Sub-tab Archived tidak memiliki bulk action

32. Klik sub-tab Archived
33. Verifikasi tabel sub-tab Archived memuat sedikitnya satu baris
34. Verifikasi tidak ada kolom Checkbox
35. Verifikasi tidak ada Bulk Action Bar

### TC-AC-ACC-642: Dialog Bulk Suspend dengan 25 Client terpilih menampilkan daftar nama dalam container scrollable

36. Klik sub-tab Active
37. Atur Rows per page menjadi 25
38. Klik checkbox header kolom
39. Klik Bulk Action → pilih `Suspend`
40. Verifikasi dialog Title "Suspend Clients" dengan lebar 480px
41. Verifikasi daftar Company Name satu bullet per baris memuat 25 bullet dalam container yang dapat di-scroll vertikal
42. Scroll daftar nama di dalam dialog sampai bullet terakhir
43. Verifikasi bullet ke-25 terjangkau setelah scroll sampai akhir daftar
44. Klik `[Cancel]`
45. Verifikasi dialog tertutup
46. Verifikasi status ke-25 Client tidak berubah (ke-25 baris tetap tampil di sub-tab Active)

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (pengamatan menu dan sub-tab Suspend/Unsuspend), satu akun, tanpa mengubah data; tiap blok membaca data berbeda sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): menutup menu Bulk Action dan menghilangkan centang (langkah 19 dan 27), Search yang menemukan baris target (R-16). Asersi absence item Archive memakai item menu lain pada menu yang sama sebagai anchor positif (butir 2 bagian 8b); absence kolom Checkbox dan Bulk Action Bar (TC-AC-ACC-215) memakai baris tabel Archived sebagai anchor (langkah 33).
- Asersi tambahan yang dicatat (S-03): langkah 46 mengamati Post Condition status ke-25 Client (Expected d TC-AC-ACC-642) lewat baris yang tetap tampil.
- Post Condition TC-AC-ACC-640, 641, 215, 642: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-642 tidak menyebut cara membuktikan "status ke-25 Client tidak berubah" selain dialog tertutup; spec membacanya dari baris yang tetap berada di sub-tab Active.
  - TC-AC-ACC-641 Expected tidak menyebut Delete pada menu `[⋯]` sub-tab Active; spec mengikuti persis daftar item yang disebut TC.
