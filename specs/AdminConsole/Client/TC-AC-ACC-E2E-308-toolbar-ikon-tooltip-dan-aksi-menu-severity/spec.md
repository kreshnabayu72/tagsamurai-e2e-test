---
id: TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity
title: "Client List: Tooltip Ikon Toolbar, Tombol New Client, Ikon dan Severity Aksi Menu Row dan Bulk Action"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-677
  - TC-AC-ACC-680
  - TC-AC-ACC-681
  - TC-AC-ACC-682
  - TC-AC-ACC-683
  - TC-AC-ACC-684
  - TC-AC-ACC-685
coverage:
  web: automated
---

# Client List: Tooltip Ikon Toolbar, Tombol New Client, Ikon dan Severity Aksi Menu Row dan Bulk Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen Pre-setup hanya dibaca: C-01 `PT Sejahtera Abadi` (ada riwayat subscription), C-09 `PT Baru Daftar` (belum pernah punya subscription), C-03 `PT Wahana Nusantara` (Suspended, ada riwayat), C-04 `PT Karya Abadi` (Archived).
- Tidak ada data yang dibuat atau diubah; bulk action hanya dibuka menunya, tidak dijalankan. Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Toolbar (TC-AC-ACC-677 dan TC-AC-ACC-680)

1. Arahkan kursor ke ikon Download di toolbar List
2. Verifikasi tooltip ikon Download `Download`
3. Arahkan kursor ke ikon Changelog di toolbar List
4. Verifikasi tooltip ikon Changelog `Changelog`
5. Lihat toolbar List
6. Verifikasi tombol `[+ New Client]` tampil di ujung kanan toolbar, setelah ikon Changelog
7. Verifikasi tombol `[+ New Client]` berupa varian primary

### Aksi menu row sub-tab Active (TC-AC-ACC-681)

8. Ketik Search `PT Sejahtera Abadi`, tekan Enter
9. Buka menu `⋯` pada baris `PT Sejahtera Abadi` dan lihat ikon serta severity tiap aksi
10. Verifikasi `Detail` berikon FileInfoLine severity dark
11. Verifikasi `Edit` berikon Edit2Line severity dark
12. Verifikasi `Change Partner` berikon MoveTo severity dark
13. Verifikasi `Suspend` berikon InformationLine severity danger
14. Verifikasi `Delete` tidak tampil (Client memiliki riwayat subscription)
15. Tutup menu, ganti isi kotak search dengan `PT Baru Daftar`, tekan Enter
16. Buka menu `⋯` pada baris `PT Baru Daftar` dan lihat aksi Delete
17. Verifikasi `Delete` berikon DeleteBin6Line severity danger

### Aksi menu row sub-tab Suspended dan Archived (TC-AC-ACC-682 dan TC-AC-ACC-683)

18. Tutup menu, lalu klik `(←)` pada kotak Search dan klik sub-tab Suspended
19. Ketik Search `PT Wahana Nusantara`, tekan Enter
20. Buka menu `⋯` pada baris `PT Wahana Nusantara` dan lihat ikon serta severity tiap aksi
21. Verifikasi `Detail` berikon FileInfoLine severity dark
22. Verifikasi `Unsuspend` berikon CloseLine severity dark
23. Verifikasi `Edit`, `Change Partner`, dan `Suspend` tidak tampil
24. Verifikasi `Delete` tidak tampil (Client memiliki riwayat subscription)
25. Tutup menu, klik `(←)` pada kotak Search, lalu klik sub-tab Archived
26. Buka menu `⋯` pada baris `PT Karya Abadi` dan lihat ikon serta severity tiap aksi
27. Verifikasi `Detail` berikon FileInfoLine severity dark
28. Verifikasi `Edit` berikon Edit2Line severity dark
29. Verifikasi `Delete` berikon DeleteBin6Line severity danger
30. Verifikasi `Change Partner`, `Suspend`, dan `Unsuspend` tidak tampil

### Bulk Action (TC-AC-ACC-684 dan TC-AC-ACC-685)

31. Tutup menu, lalu klik sub-tab Active, ketik Search `PT Sejahtera Abadi`, tekan Enter, dan centang baris `PT Sejahtera Abadi`
32. Klik Bulk Action dan lihat menu
33. Verifikasi `Suspend` berikon InformationLine severity danger
34. Verifikasi `Unsuspend` tidak tampil (seluruh baris terpilih berstatus Active)
35. Tutup menu, klik ikon `×` pada Bulk Action Bar, klik sub-tab Suspended, ganti isi kotak search dengan `PT Wahana Nusantara`, tekan Enter, dan centang baris `PT Wahana Nusantara`
36. Klik Bulk Action dan lihat menu
37. Verifikasi `Unsuspend` berikon CloseLine severity dark
38. Verifikasi `Suspend` tidak tampil (seluruh baris terpilih berstatus Suspended)
39. Tutup menu, klik ikon `×` pada Bulk Action Bar, klik `(←)` pada kotak Search, lalu klik sub-tab Active

## Notes

- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (verifikasi tampilan Toolbar dan menu List) dan dataset Pre-setup yang hanya dibaca, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): menutup menu, `(←)`, perpindahan sub-tab, dan pembersihan seleksi memulihkan state (S-09).
- Expected `Delete tidak tampil (Client memiliki riwayat subscription)` memakai baris `Detail`/`Edit` pada menu sama sebagai anchor positif absence (bagian 8b butir 2).
- Temuan untuk QA
  - TC-AC-ACC-684 dan TC-AC-ACC-685: Langkah memilih satu baris saja; Expected hanya menyebut dua entri menu Bulk Action. Item Bulk Action lain (mis. Delete) tidak diasersi.
