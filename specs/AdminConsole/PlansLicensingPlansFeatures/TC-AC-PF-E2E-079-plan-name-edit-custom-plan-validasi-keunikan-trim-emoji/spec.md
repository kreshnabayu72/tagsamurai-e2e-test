---
id: TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji
title: "Plan Name Edit Custom Plan: Validasi, Keunikan, Trim, dan Emoji"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-197
  - TC-AC-PF-198
  - TC-AC-PF-199
  - TC-AC-PF-200
  - TC-AC-PF-201
  - TC-AC-PF-202
coverage:
  web: automated
---

# Plan Name Edit Custom Plan: Validasi, Keunikan, Trim, dan Emoji

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20); Dataset C (`alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok TC-AC-PF-199 dan TC-AC-PF-200 menyimpan rename sehingga Last Updated `Growth Tier` berubah; efek itu dipulihkan Fixture BE, sedangkan entri Changelog Custom bersifat permanen dan tidak dapat dihapus lewat UI. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Data uji: nama 121 karakter = `Paket` + 116 huruf `a`; nama 120 karakter = `Paket` + 115 huruf `a`; nilai injeksi `Growth 😊`.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-197: Validasi Plan Name Edit Custom Plan: dikosongkan lalu Save ditolak setelah Submit

2. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
3. Kosongkan field Plan Name
4. Klik `[Save]`
5. Verifikasi pesan inline `Plan name must not be empty` muncul setelah Save
6. Verifikasi form tetap terbuka

### TC-AC-PF-198: Batas karakter Plan Name Edit Custom Plan: 121 karakter memunculkan error langsung dan Save diblok

7. Ganti isi Plan Name dengan 121 karakter: `Paket` diikuti 116 karakter huruf `a`
8. Verifikasi pesan `Max. 120 characters` muncul langsung
9. Klik `[Save]`
10. Verifikasi Save diblok dan form tetap terbuka

### TC-AC-PF-201: Keunikan Plan Name Edit Custom Plan: nama custom plan lain entitas sama ditandai saat mengetik

11. Ganti isi Plan Name dengan `beta pro  ` (dua spasi di ujung), lalu tunggu 1 detik tanpa blur
12. Verifikasi pesan inline `Plan name already exists` muncul (tidak peka huruf besar-kecil, abai spasi ujung)
13. Klik `[Save]`
14. Verifikasi Save ditolak dan form tetap terbuka

### TC-AC-PF-202: Karakter Plan Name Edit Custom Plan: emoji diblok di input dan ditolak server bila lolos filter

15. Kosongkan field Plan Name, lalu ketik `😊`
16. Verifikasi emoji tidak masuk saat diketik (field Plan Name tetap kosong)
17. Injeksi nilai `Growth 😊` langsung ke DOM field Plan Name
18. Klik `[Save]`
19. Verifikasi pesan inline `Plan name contains invalid characters` muncul
20. Verifikasi Save ditolak dan form tetap terbuka
21. Klik segmen `Plans & Features` pada breadcrumb
22. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`
24. Klik tab `Custom`, lalu sub-tab `Active`
25. Verifikasi baris `Growth Tier` pada list tetap Version `v20` (versi tidak naik pada keempat penolakan di atas)

### TC-AC-PF-199: Batas karakter Plan Name Edit Custom Plan: tepat 120 karakter diterima

26. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
27. Ganti isi Plan Name dengan 120 karakter: `Paket` diikuti 115 karakter huruf `a`
28. Verifikasi tidak ada pesan error di bawah field Plan Name
29. Klik `[Save]`
30. Verifikasi toast sukses: "Success, plan has been updated."
31. Verifikasi judul Plan Detail memuat nama 120 karakter dan versi tetap `v20` (rename saja)
32. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Custom` sub-tab `Active`

### TC-AC-PF-200: Plan Name Edit Custom Plan dihitung setelah trim dan tersimpan ter-trim

33. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
34. Ganti isi Plan Name dengan 3 spasi + `Growth Tier Baru` + 3 spasi
35. Klik `[Save]`
36. Verifikasi toast sukses: "Success, plan has been updated."
37. Verifikasi judul Plan Detail `Growth Tier Baru – v20` tanpa spasi di ujung

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal dan pada langkah 24 sesudah `[Leave]` (landing breadcrumb adalah Default > Active); menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08); pemulihan Dataset lewat Fixture BE antar blok (A-6). Urutan blok TC-AC-PF-197, 198, 201, 202 (semuanya ditolak) berurutan pada satu pembukaan form dengan field diganti di antara kasus (bagian 3 prinsip: halaman yang sama dipakai berulang); blok yang menyimpan (TC-AC-PF-199, 200) ditaruh sesudahnya, jadi urutan TC di spec berbeda dari nomor TC.
- Verifikasi Version `v20` sesudah penutupan form menjadi pengamatan untuk Expected 'versi tetap v20' / 'versi tidak naik' pada TC-AC-PF-197, 198, 201, dan 202.
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Dataset C (TC-AC-PF-201) memuat `Growth Tier`, yaitu plan yang sedang diedit; Expected hanya menyebut `beta pro` sebagai duplikat. Spec mengikuti TC.
