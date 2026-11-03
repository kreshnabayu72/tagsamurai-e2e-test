---
id: TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes
title: "Edit Custom Plan: Clear Field dan Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-212
  - TC-AC-PF-213
  - TC-AC-PF-214
  - TC-AC-PF-660
coverage:
  web: automated
---

# Edit Custom Plan: Clear Field dan Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan nilai (Save pada TC-AC-PF-212 adalah No-Op) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-212: Clear Field Edit Custom Plan mengembalikan seluruh input ke nilai tersimpan dan tidak mereset field terkunci

2. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
3. Ubah Plan Name menjadi `Ubah Sementara`
4. Ubah Group count menjadi `3`
5. Klik `[Clear Field]`
6. Verifikasi Plan Name kembali `Growth Tier`
7. Verifikasi Group count kembali `25`
8. Verifikasi Product tetap `FAMS` terkunci
9. Verifikasi tidak ada dialog konfirmasi dan tidak ada dialog Unsaved Changes
10. Klik `[Save]`
11. Verifikasi toast netral: "No changes to save." (Save tidak ditolak validasi Required)

### TC-AC-PF-660: Clear Field Edit Custom Plan menghapus pesan error inline dan memindahkan fokus ke Plan Name

12. Klik button `Edit` di header Plan Detail `Growth Tier`
13. Kosongkan field Plan Name
14. Klik `[Save]`
15. Verifikasi pesan error `Plan name must not be empty` tampil
16. Klik `[Clear Field]`
17. Verifikasi pesan error `Plan name must not be empty` hilang
18. Verifikasi Plan Name kembali `Growth Tier`
19. Verifikasi fokus pada Plan Name (field input pertama yang dapat diedit karena Product terkunci)
20. Verifikasi tidak ada dialog konfirmasi
21. Verifikasi form tetap terbuka

### TC-AC-PF-213: Form Edit Custom Plan dirty lalu klik breadcrumb: dialog Unsaved Changes dengan Cancel dan Leave

22. Ubah Plan Name menjadi `Ubah Dirty`
23. Klik segmen `Plans & Features` pada breadcrumb
24. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Cancel]`
26. Verifikasi user tetap di form Edit
27. Klik segmen `Plans & Features` pada breadcrumb lagi
28. Klik `[Leave]`
29. Klik tab `Custom`, lalu sub-tab `Active`
30. Verifikasi perubahan dibuang: nama plan pada list tetap `Growth Tier`

### TC-AC-PF-214: Form Edit Custom Plan tanpa perubahan atau dikembalikan identik tidak memunculkan dialog Unsaved Changes

31. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
32. Klik segmen `Plans & Features` pada breadcrumb tanpa mengubah apa pun
33. Verifikasi navigasi berlangsung langsung tanpa dialog Unsaved Changes
34. Klik tab `Custom`, lalu sub-tab `Active`
35. Pada list tab Custom sub-tab Active, buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
36. Ubah Group count `25` menjadi `3`, lalu kembalikan ke `25`
37. Klik segmen `Plans & Features` pada breadcrumb
38. Verifikasi navigasi berlangsung langsung tanpa dialog Unsaved Changes

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal, pada langkah 29 sesudah `[Leave]`, dan pada langkah 34 sesudah breadcrumb bersih langkah 32 (landing breadcrumb adalah Default > Active); membuka Edit dari header Plan Detail setelah Save No-Op (jalur setara row action, TC-AC-PF-196); menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08). Form pada blok TC-AC-PF-660 yang bersih sesudah `[Clear Field]` dipakai ulang oleh blok TC-AC-PF-213.
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
