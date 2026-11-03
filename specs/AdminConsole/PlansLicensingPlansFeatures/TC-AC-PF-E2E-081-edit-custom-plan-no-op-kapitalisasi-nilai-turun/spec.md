---
id: TC-AC-PF-E2E-081-edit-custom-plan-no-op-kapitalisasi-nilai-turun
title: "Edit Custom Plan: No-Op, Kapitalisasi Nama, dan Nilai Turun"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-206
  - TC-AC-PF-207
  - TC-AC-PF-208
coverage:
  web: automated
---

# Edit Custom Plan: No-Op, Kapitalisasi Nama, dan Nilai Turun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Hanya blok TC-AC-PF-208 menyimpan perubahan (versi naik ke v21, `PT Wahana Nusantara` Outdated, Last Updated dan Changelog Custom bertambah); blok TC-AC-PF-206 dan 207 adalah No-Op sehingga tidak mengubah apa pun. Efek blok TC-AC-PF-208 dipulihkan Fixture BE kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`
2. Catat Version dan Last Modified baris `Growth Tier` pada list, lalu catat baseline jumlah entri Changelog tab Custom (N)

### TC-AC-PF-206: Edit tanpa perubahan apa pun adalah No-Op: toast netral, nol entri log, versi dan Last Modified tidak berubah

3. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
4. Klik `[Save]` tanpa mengubah apa pun
5. Verifikasi toast netral: "No changes to save." (bukan toast sukses dan bukan toast error)
6. Verifikasi tidak ada pesan duplikat nama terhadap diri sendiri
7. Verifikasi form ditutup dan Plan Detail `Growth Tier` tampil
8. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
9. Buka Changelog toolbar tab Custom
10. Verifikasi baris `Growth Tier` pada list: Version tetap `v20`
11. Verifikasi baris `Growth Tier` pada list: Last Modified sama dengan nilai yang dicatat
12. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
13. Tutup modal Changelog

### TC-AC-PF-207: Edit yang hanya mengubah kapitalisasi nama diperlakukan No-Op menurut basis pembanding default

14. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
15. Ganti Plan Name menjadi `growth tier`
16. Klik `[Save]`
17. Verifikasi toast netral: "No changes to save."
18. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
19. Verifikasi baris pada list tetap bernama `Growth Tier` dengan Version `v20`
20. Klik ikon Changelog pada toolbar tab Custom
21. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
22. Tutup modal Changelog

### TC-AC-PF-208: Edit yang menurunkan nilai fitur tetap disimpan tanpa dialog konfirmasi tambahan dan memblokir Push Update client

23. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
24. Turunkan Group count `25` menjadi `3`
25. Klik `[Save]`
26. Verifikasi toast sukses: "Success, plan has been updated."
27. Verifikasi tidak ada dialog konfirmasi tambahan
28. Buka Tab Assigned Clients, lalu buka Overlay Row Action `PT Wahana Nusantara`
29. Verifikasi `PT Wahana Nusantara` berbadge `Outdated` dengan icon peringatan
30. Verifikasi Overlay Row Action `PT Wahana Nusantara` hanya `Detail` (tidak ada `Push Update`)

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active`; mencatat Version, Last Modified, dan baseline Changelog sebelum aksi pemicu pertama (S-12); kembali ke list lewat breadcrumb; menutup modal Changelog. Blok No-Op (TC-AC-PF-206, 207) ditaruh sebelum blok yang menyimpan (TC-AC-PF-208) sehingga baseline tidak bergeser.
- P-1 (state berat): Verifikasi 'tidak ada entri Changelog baru' pada TC-AC-PF-206 dan TC-AC-PF-207 ditulis di spec ini sebagai Verifikasi berbaseline karena konteksnya bergantung pada state yang dibangun langkah sebelumnya dalam spec ini (Save No-Op); anchor positifnya toast netral "No changes to save.". Tidak ada spec absence terpisah untuk kedua TC ini (S-05).
- Temuan untuk QA:
  - Pre-setup TC-AC-PF-206 tidak menyebut nilai Last Modified awal `Growth Tier`; spec mencatatnya dari list sebelum aksi sebagai pembanding.
  - TC-AC-PF-207 menyebut 'basis pembanding default' di judul tanpa definisi; Expected hanya toast netral dan nama tetap `Growth Tier`.
