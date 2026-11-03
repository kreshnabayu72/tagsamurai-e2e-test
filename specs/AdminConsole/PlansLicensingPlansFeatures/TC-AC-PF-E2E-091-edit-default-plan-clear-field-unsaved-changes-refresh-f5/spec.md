---
id: TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5
title: "Edit Default Plan: Clear Field dan Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-233
  - TC-AC-PF-234
  - TC-AC-PF-661
  - TC-AC-PF-663
coverage:
  web: automated
---

# Edit Default Plan: Clear Field dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Starter` v2 (default plan FAMS Free; Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None); Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month).
- Pengecualian S-06/S-12 butir A-14: `Starter` v2 dan `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]` yang berhasil) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`

### TC-AC-PF-233: Clear Field Edit Default Plan mengembalikan input ke nilai tersimpan tanpa mereset field terkunci

2. Buka Overlay Row Action `Starter`, lalu klik `Edit`
3. Ubah Plan Name menjadi `Sementara`
4. Ubah Asset cap menjadi `99`
5. Klik `[Clear Field]`
6. Verifikasi Plan Name kembali `Starter`
7. Verifikasi Asset cap kembali `25`
8. Verifikasi Product dan Pricing Type badge tetap
9. Verifikasi Feature Suites tetap Disabled `None`
10. Verifikasi tidak ada dialog
11. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`

### TC-AC-PF-661: Clear Field Edit Default Plan menghapus pesan error inline dan memindahkan fokus ke Plan Name

12. Buka Overlay Row Action `Growth`, lalu klik `Edit`
13. Kosongkan field Plan Name
14. Klik `[Save]`
15. Verifikasi pesan error `Plan name must not be empty` tampil
16. Klik `[Clear Field]`
17. Verifikasi pesan error `Plan name must not be empty` hilang
18. Verifikasi Plan Name kembali `Growth`
19. Verifikasi fokus pada Plan Name
20. Verifikasi tidak ada dialog konfirmasi
21. Verifikasi form tetap terbuka

### TC-AC-PF-234: Form Edit Default Plan dirty lalu klik breadcrumb: dialog Unsaved Changes dengan Cancel dan Leave

22. Ubah Plan Name menjadi `Dirty`
23. Klik segmen `Plans & Features` pada breadcrumb
24. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Cancel]`
26. Verifikasi user tetap di form Edit
27. Klik segmen `Plans & Features` pada breadcrumb lagi
28. Klik `[Leave]`
29. Verifikasi perubahan dibuang: nama plan pada list tetap `Growth`

### TC-AC-PF-663: Form Edit Default Plan tanpa perubahan atau dikembalikan identik tidak memunculkan dialog Unsaved Changes

30. Buka Overlay Row Action `Growth`, lalu klik `Edit`
31. Klik segmen `Plans & Features` pada breadcrumb tanpa mengubah apa pun
32. Verifikasi navigasi berlangsung langsung tanpa dialog Unsaved Changes
33. Pada list tab Default sub-tab Active, buka Overlay Row Action `Growth`, lalu klik `Edit`
34. Ubah Group count `3` menjadi `25`, lalu kembalikan ke `3`
35. Klik segmen `Plans & Features` pada breadcrumb
36. Verifikasi navigasi berlangsung langsung tanpa dialog Unsaved Changes

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; kembali ke list lewat breadcrumb dari form bersih; form bersih sesudah `[Clear Field]` pada blok TC-AC-PF-661 dipakai ulang oleh blok TC-AC-PF-234; menutup form dirty lewat dialog Unsaved Changes dan `[Leave]` (S-08).
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
