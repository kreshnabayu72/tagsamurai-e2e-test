---
id: TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim
title: "Plan Name Edit Default Plan: Validasi, Keunikan, Batas Karakter, dan Trim"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-220
  - TC-AC-PF-221
  - TC-AC-PF-615
  - TC-AC-PF-616
  - TC-AC-PF-617
coverage:
  web: automated
---

# Plan Name Edit Default Plan: Validasi, Keunikan, Batas Karakter, dan Trim

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month); default plan `professional` (FAMS) dan `SIEM` (Product SIEM).
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok TC-AC-PF-221, 615, dan 616 menyimpan rename sehingga Last Updated `Growth` berubah; efek itu dipulihkan Fixture BE, sedangkan entri Changelog Default bersifat permanen dan tidak dapat dihapus lewat UI. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Data uji: nama 121 karakter = `Paket` + 116 huruf `a`; nama 120 karakter = `Paket` + 115 huruf `a`; nilai injeksi `Growth 😊`.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`

### TC-AC-PF-220: Plan Name Edit Default Plan: dikosongkan ditolak dan 121 karakter memunculkan error

2. Buka Overlay Row Action `Growth`, lalu klik `Edit`
3. Kosongkan field Plan Name
4. Klik `[Save]`
5. Verifikasi pesan `Plan name must not be empty` muncul setelah Save
6. Ganti isi Plan Name dengan 121 karakter: `Paket` diikuti 116 karakter huruf `a`
7. Verifikasi pesan `Max. 120 characters` muncul langsung
8. Klik `[Save]`
9. Verifikasi Save diblok dan form tetap terbuka

### TC-AC-PF-617: Karakter Plan Name Edit Default Plan: emoji diblok di input dan ditolak server bila lolos filter

10. Kosongkan field Plan Name, lalu ketik `😊`
11. Verifikasi emoji tidak masuk saat diketik (field Plan Name tetap kosong)
12. Injeksi nilai `Growth 😊` langsung ke DOM field Plan Name
13. Klik `[Save]`
14. Verifikasi pesan inline `Plan name contains invalid characters` muncul
15. Verifikasi Save ditolak
16. Klik segmen `Plans & Features` pada breadcrumb
17. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
18. Klik `[Leave]`
19. Verifikasi baris `Growth` pada list tetap Version `v5` (versi tidak naik pada penolakan di atas)

### TC-AC-PF-221: Keunikan Plan Name Edit Default Plan di antara sesama default plan Product yang sama

20. Buka Overlay Row Action `Growth`, lalu klik `Edit`
21. Ganti isi Plan Name dengan `professional`, lalu tunggu 1 detik
22. Verifikasi `professional` ditandai `Plan name already exists` (Product FAMS sama)
23. Ganti isi Plan Name dengan `SIEM`
24. Verifikasi `SIEM` (nama default plan Product lain) diterima tanpa pesan duplikat
25. Klik `[Save]`
26. Verifikasi toast sukses: "Success, plan has been updated."
27. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Default` sub-tab `Active`

### TC-AC-PF-615: Batas karakter Plan Name Edit Default Plan: tepat 120 karakter diterima tanpa menaikkan versi

28. Buka Overlay Row Action `Growth`, lalu klik `Edit`
29. Ganti isi Plan Name dengan 120 karakter: `Paket` diikuti 115 karakter huruf `a`
30. Verifikasi tidak ada pesan `Max. 120 characters` di bawah field Plan Name
31. Klik `[Save]`
32. Verifikasi toast sukses: "Success, plan has been updated."
33. Verifikasi judul Plan Detail memuat nama 120 karakter dan versi tetap `v5` (rename saja)
34. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Default` sub-tab `Active`

### TC-AC-PF-616: Plan Name Edit Default Plan di-trim otomatis dan tersimpan ter-trim

35. Buka Overlay Row Action `Growth`, lalu klik `Edit`
36. Ganti isi Plan Name dengan 3 spasi + `Growth Trim` + 3 spasi
37. Klik `[Save]`
38. Verifikasi toast sukses: "Success, plan has been updated."
39. Verifikasi judul Plan Detail `Growth Trim – v5` tanpa spasi di ujung

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08); pemulihan Dataset lewat Fixture BE antar blok (A-6). Blok TC-AC-PF-220 dan TC-AC-PF-617 (penolakan) berurutan pada satu pembukaan form; blok yang menyimpan (TC-AC-PF-221, 615, 616) sesudahnya, sehingga urutan TC di spec berbeda dari nomor TC. Verifikasi Version `v5` sesudah penutupan form adalah pengamatan 'versi tetap v5' untuk TC-AC-PF-617 dan harus terjadi sebelum blok TC-AC-PF-221 menyimpan.
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Pre-setup TC-AC-PF-221 hanya menulis 'Dataset Plan A tersedia' tanpa menyebut nama default plan `professional` dan `SIEM`; spec mengasumsikan keduanya ada pada Dataset Plan A.
  - TC-AC-PF-221: Post Condition 'Growth berganti nama SIEM pada Product FAMS' tidak punya langkah observasi sehingga tidak diasersi.
