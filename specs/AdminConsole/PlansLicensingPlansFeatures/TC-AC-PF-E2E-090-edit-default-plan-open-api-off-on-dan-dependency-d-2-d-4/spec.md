---
id: TC-AC-PF-E2E-090-edit-default-plan-open-api-off-on-dan-dependency-d-2-d-4
title: "Edit Default Plan: Open API OFF dan ON serta Dependency D-2 dan D-4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-756
  - TC-AC-PF-757
  - TC-AC-PF-758
coverage:
  web: automated
---

# Edit Default Plan: Open API OFF dan ON serta Dependency D-2 dan D-4

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month); `Starter` v2 (default plan FAMS Free; Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None) (API call quota —).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 dan `Starter` v2 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]` yang berhasil) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`

### TC-AC-PF-756: Edit Default Plan: Open API OFF mengunci API call quota ke — dengan tooltip penjelas

2. Buka Overlay Row Action `Growth`, lalu klik `Edit`
3. Matikan toggle Open API
4. Verifikasi API call quota berubah dari `100K/month` ke `—`
5. Verifikasi API call quota terkunci (Disabled, tetap tampil)
6. Hover field API call quota
7. Verifikasi tooltip `Turn on Open API to set an API call quota.` tampil
8. Klik segmen `Plans & Features` pada breadcrumb
9. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Klik `[Leave]`

### TC-AC-PF-758: Edit Default Plan: dependency D-2 dan D-4 kedua arah menyesuaikan Group count, Group hierarchy depth, dan License allocation per group dengan inline warning

11. Buka Overlay Row Action `Growth`, lalu klik `Edit`
12. Ubah Group count menjadi `1`
13. Verifikasi Group hierarchy depth otomatis `1`
14. Verifikasi License allocation per group otomatis OFF
15. Verifikasi inline warning "Group hierarchy depth was changed automatically because group count requires it." tampil
16. Verifikasi inline warning "License allocation per group was changed automatically because group count requires it." tampil
17. Ubah Group hierarchy depth menjadi `2`
18. Verifikasi Group count otomatis `3`
19. Verifikasi Group hierarchy depth tetap `2`
20. Verifikasi inline warning "Group count was changed automatically because group hierarchy depth requires it." tampil
21. Ubah Group count menjadi `1`
22. Nyalakan License allocation per group
23. Verifikasi Group count otomatis `3`
24. Verifikasi toggle License allocation per group tetap ON
25. Verifikasi inline warning "Group count was changed automatically because license allocation per group requires it." tampil
26. Klik segmen `Plans & Features` pada breadcrumb
27. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Leave]`

### TC-AC-PF-757: Edit Default Plan: Open API ON dengan API call quota kosong ditolak dengan pesan inline

29. Catat baseline jumlah entri Changelog tab Default (N)
30. Buka Overlay Row Action `Starter`, lalu klik `Edit`
31. Nyalakan toggle Open API tanpa memilih API call quota
32. Klik `[Save]`
33. Verifikasi pesan inline `API call quota must not be empty` muncul setelah Save
34. Klik segmen `Plans & Features` pada breadcrumb
35. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
36. Klik `[Leave]`
37. Verifikasi baris `Starter` pada list: Version tetap `v2`
38. Klik ikon Changelog pada toolbar tab Default
39. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
40. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; mencatat baseline Changelog sebelum aksi pemicu (S-12); menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08) setelah tiap blok karena tiap blok membiarkan form dirty (S-09); menutup modal Changelog.
- P-1 (state berat): Verifikasi 'tidak ada entri Changelog baru' pada TC-AC-PF-757 ditulis di spec ini sebagai Verifikasi berbaseline karena konteksnya bergantung pada state yang dibangun langkah sebelumnya dalam spec ini (Save ditolak validasi); anchor positifnya pesan inline `API call quota must not be empty`. Tidak ada spec absence terpisah untuk TC ini (S-05).
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
