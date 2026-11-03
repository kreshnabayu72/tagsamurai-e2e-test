---
id: TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc
title: "Edit Default Plan: Refresh F5, Sidebar, Back Browser, dan Esc"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-666
  - TC-AC-PF-670
  - TC-AC-PF-673
  - TC-AC-PF-739
  - TC-AC-PF-744
coverage:
  web: automated
---

# Edit Default Plan: Refresh F5, Sidebar, Back Browser, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month).
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]`) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Dialog `beforeunload` browser ditangani harness (dibatalkan agar tetap di halaman); kemampuan itu disediakan tim FE.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`
2. Catat jumlah total plan tab Default sub-tab Active (N)

### TC-AC-PF-666: Form Edit Default Plan dirty lalu refresh F5: konfirmasi bawaan browser muncul

3. Buka Overlay Row Action `Growth`, lalu klik `Edit`
4. Ubah Plan Name menjadi `Dirty`
5. Tekan F5
6. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul karena form dirty
7. Batalkan dialog `beforeunload` agar tetap di halaman

### TC-AC-PF-670: Form Edit Default Plan dirty lalu klik menu sidebar: dialog Unsaved Changes dengan Cancel dan Leave

8. Klik menu Plans & Licensing > Plans & Features di sidebar
9. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Verifikasi halaman belum berpindah
11. Klik `[Cancel]`
12. Verifikasi dialog tertutup dan user tetap di form dengan input dipertahankan
13. Klik menu Plans & Licensing > Plans & Features di sidebar lagi
14. Klik `[Leave]`
15. Verifikasi navigasi dilanjutkan ke halaman Plans & Licensing > Plans & Features
16. Klik tab `Default`, lalu sub-tab `Active`
17. Verifikasi jumlah total plan tab Default sub-tab Active sama dengan N (tidak ada plan baru)
18. Verifikasi baris `Growth` pada list tetap bernama `Growth` dengan Version `v5` (nilai plan tidak berubah)

### TC-AC-PF-673: Form Edit Default Plan dirty lalu tombol Back browser: dialog Unsaved Changes muncul

19. Buka Overlay Row Action `Growth`, lalu klik `Edit`
20. Ubah Plan Name menjadi `Dirty`
21. Klik tombol Back browser
22. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Cancel]` pada dialog
24. Verifikasi user tetap di form dengan input dipertahankan

### TC-AC-PF-739: Edit Default Plan dirty lalu tekan Esc: dialog Unsaved Changes muncul

25. Ubah Plan Name menjadi `Ubah Enter`
26. Tekan Esc
27. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Cancel]` pada dialog
29. Verifikasi user tetap di form dengan input dipertahankan
30. Klik segmen `Plans & Features` pada breadcrumb
31. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

### TC-AC-PF-744: Edit Default Plan bersih lalu tekan Esc: kembali ke daftar tanpa dialog

33. Buka Overlay Row Action `Growth`, lalu klik `Edit`
34. Tekan Esc tanpa mengubah apa pun
35. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung tanpa dialog Unsaved Changes

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal dan sesudah navigasi sidebar; mencatat jumlah total plan (N) sebelum aksi; membatalkan dialog `beforeunload` sesudah F5; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08). Form dirty dari blok TC-AC-PF-666 dipakai ulang pada blok TC-AC-PF-670 (nilai yang sama), dan form dari blok TC-AC-PF-673 dipakai ulang pada blok TC-AC-PF-739 dengan Plan Name diganti `Ubah Enter` sesuai TC.
- Temuan untuk QA:
  - TC-AC-PF-666: Expected menyebut teks konfirmasi 'ditentukan browser'; spec hanya mengasersi kemunculan dialog `beforeunload`.
