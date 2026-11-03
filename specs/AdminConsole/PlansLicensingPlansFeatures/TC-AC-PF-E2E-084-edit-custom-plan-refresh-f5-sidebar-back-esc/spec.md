---
id: TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc
title: "Edit Custom Plan: Refresh F5, Sidebar, Back Browser, dan Esc"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-665
  - TC-AC-PF-669
  - TC-AC-PF-672
  - TC-AC-PF-738
  - TC-AC-PF-743
coverage:
  web: automated
---

# Edit Custom Plan: Refresh F5, Sidebar, Back Browser, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]`) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Dialog `beforeunload` browser ditangani harness (dibatalkan agar tetap di halaman); kemampuan itu disediakan tim FE.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`
2. Catat jumlah total plan tab Custom sub-tab Active (N)

### TC-AC-PF-665: Form Edit Custom Plan dirty lalu refresh F5: konfirmasi bawaan browser muncul

3. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
4. Ubah Plan Name menjadi `Ubah Dirty`
5. Tekan F5
6. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul karena form dirty
7. Batalkan dialog `beforeunload` agar tetap di halaman

### TC-AC-PF-669: Form Edit Custom Plan dirty lalu klik menu sidebar: dialog Unsaved Changes dengan Cancel dan Leave

8. Klik menu Plans & Licensing > Plans & Features di sidebar
9. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Verifikasi halaman belum berpindah
11. Klik `[Cancel]`
12. Verifikasi dialog tertutup dan user tetap di form dengan input dipertahankan
13. Klik menu Plans & Licensing > Plans & Features di sidebar lagi
14. Klik `[Leave]`
15. Verifikasi navigasi dilanjutkan ke halaman Plans & Licensing > Plans & Features
16. Klik tab `Custom`, lalu sub-tab `Active`
17. Verifikasi jumlah total plan tab Custom sub-tab Active sama dengan N (tidak ada plan baru)
18. Verifikasi baris `Growth Tier` pada list tetap bernama `Growth Tier` dengan Version `v20` (nilai plan tidak berubah)

### TC-AC-PF-672: Form Edit Custom Plan dirty lalu tombol Back browser: dialog Unsaved Changes muncul

19. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
20. Ubah Plan Name menjadi `Ubah Dirty`
21. Klik tombol Back browser
22. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Cancel]` pada dialog
24. Verifikasi user tetap di form dengan input dipertahankan

### TC-AC-PF-738: Edit Custom Plan dirty lalu tekan Esc: dialog Unsaved Changes muncul

25. Ubah Plan Name menjadi `Ubah Enter`
26. Tekan Esc
27. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
28. Klik `[Cancel]` pada dialog
29. Verifikasi user tetap di form dengan input dipertahankan
30. Klik segmen `Plans & Features` pada breadcrumb
31. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`
33. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-743: Edit Custom Plan bersih lalu tekan Esc: kembali ke daftar tanpa dialog

34. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
35. Tekan Esc tanpa mengubah apa pun
36. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung tanpa dialog Unsaved Changes

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal, sesudah navigasi sidebar (langkah 16), dan sesudah `[Leave]` lewat breadcrumb (langkah 33; landing breadcrumb adalah Default > Active); mencatat jumlah total plan (N) sebelum aksi; membatalkan dialog `beforeunload` sesudah F5; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08). Form dirty dari blok TC-AC-PF-665 dipakai ulang pada blok TC-AC-PF-669 (nilai yang sama), dan form dari blok TC-AC-PF-672 dipakai ulang pada blok TC-AC-PF-738 dengan Plan Name diganti `Ubah Enter` sesuai TC.
- Alasan spec melewati sekitar 35 langkah (36 langkah): kelima blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan klik tab `Custom` sub-tab `Active` sesudah `[Leave]` wajib ada karena landing breadcrumb adalah Default > Active (S-14).
- Temuan untuk QA:
  - TC-AC-PF-743 menyebut Expected halaman Plans & Licensing > Plans & Features > Default > Active, padahal form yang ditutup adalah Edit Custom Plan dan precondition-nya Custom > Active; spec mengasersi Default > Active sesuai Expected TC (sama dengan landing breadcrumb pada langkah 33) dan membuka form pada langkah 34 dari Custom > Active. Mohon QA memastikan apakah tab tujuan seharusnya Custom > Active.
  - TC-AC-PF-665: Expected menyebut teks konfirmasi 'ditentukan browser'; spec hanya mengasersi kemunculan dialog `beforeunload`.
