---
id: TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon
title: "Aksesibilitas: aria-describedby Pesan Error Form Create dan Global Settings serta Nama Aksesibel Ikon Tanpa Teks"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-791
  - TC-AC-PF-792
  - TC-AC-PF-793
  - TC-AC-PF-798
coverage:
  web: automated
---

# Aksesibilitas: aria-describedby Pesan Error Form Create dan Global Settings serta Nama Aksesibel Ikon Tanpa Teks

## Prerequisites

- Mode: FE+BE (hanya membuka form, memicu validasi yang diblokir, dan membaca atribut; TC bertanda UI Only, tanpa intercept dan tanpa data yang tersimpan).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: default `Growth` aktif, custom `Growth Tier` aktif) dan Global FAMS Settings dengan nilai awal Max custom fields per asset name `5` dan Max depreciation methods (Multi Depreciation tier) `2`. Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal `Growth` dan `Growth Tier` dipakai hanya sebagai target pembacaan nama aksesibel row action; spec tidak mengubahnya. Plan Name `Paket Tanpa Product {runId}-021`, `Paket Tanpa Tipe {runId}-021`, dan nilai kosong pada Global Settings diblokir validasi sehingga tidak ada data tersimpan. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pembacaan atribut ARIA (aria-describedby dan nama aksesibel) elemen form dan ikon (accessibility tree atau atribut DOM), fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-791: Accessibility form Create Custom Plan: Template, Plan Name, dan Product yang error menunjuk pesan error lewat aria-describedby

1. Klik tab Custom, lalu klik `+ Custom Plan`
2. Pilih Product `FAMS`, biarkan Template dan Plan Name kosong
3. Klik `[Submit]`
4. Verifikasi pesan inline `Template must not be empty` tampil di bawah field Template
5. Verifikasi aria-describedby field Template menunjuk ke elemen pesan error milik field tersebut
6. Verifikasi pesan inline `Plan name must not be empty` tampil di bawah field Plan Name
7. Verifikasi aria-describedby field Plan Name menunjuk ke elemen pesan error milik field tersebut
8. Klik `[Clear Field]`
9. Isi Plan Name `Paket Tanpa Product {runId}-021`, biarkan Product belum dipilih
10. Klik `[Submit]`
11. Verifikasi pesan inline `Product must not be empty` tampil di bawah field Product
12. Verifikasi aria-describedby field Product menunjuk ke elemen pesan error milik field tersebut
13. Klik segmen Breadcrumb `Plans & Features`
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-AC-PF-792: Accessibility form Create Default Plan: Plan Name, Pricing Type, dan Product yang error menunjuk pesan error lewat aria-describedby

16. Klik tab Default, lalu klik `+ Default Plan`
17. Pilih Product `SAMS` dan Pricing Type `Paid`, biarkan Plan Name kosong
18. Klik `[Submit]`
19. Verifikasi pesan inline `Plan name must not be empty` tampil di bawah field Plan Name
20. Verifikasi aria-describedby field Plan Name menunjuk ke elemen pesan error milik field tersebut
21. Klik `[Clear Field]`
22. Isi Plan Name `Paket Tanpa Tipe {runId}-021`, pilih Product `SAMS`, biarkan Pricing Type belum dipilih
23. Klik `[Submit]`
24. Verifikasi pesan inline `Pricing type must not be empty` tampil pada field Pricing Type
25. Verifikasi aria-describedby field Pricing Type menunjuk ke elemen pesan error milik field tersebut
26. Klik `[Clear Field]`
27. Isi Plan Name `Paket Tanpa Product {runId}-021`, biarkan Product belum dipilih
28. Klik `[Submit]`
29. Verifikasi pesan inline `Product must not be empty` tampil di bawah field Product
30. Verifikasi aria-describedby field Product menunjuk ke elemen pesan error milik field tersebut
31. Klik segmen Breadcrumb `Plans & Features`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`

### TC-AC-PF-793: Accessibility tab Global Settings: field kosong yang error menunjuk pesan error lewat aria-describedby

34. Klik tab Global Settings
35. Hapus seluruh isi input Max custom fields per asset name dan input Max depreciation methods (Multi Depreciation tier)
36. Klik `[Save]`
37. Verifikasi pesan inline `Max custom fields per asset name must not be empty` tampil di bawah field Max custom fields per asset name
38. Verifikasi aria-describedby field Max custom fields per asset name menunjuk ke elemen pesan error milik field tersebut
39. Verifikasi pesan inline `Max depreciation methods (Multi Depreciation tier) must not be empty` tampil di bawah field Max depreciation methods (Multi Depreciation tier)
40. Verifikasi aria-describedby field Max depreciation methods (Multi Depreciation tier) menunjuk ke elemen pesan error milik field tersebut
41. Isi kembali kedua input ke nilai tersimpan `5` dan `2`

### TC-AC-PF-798: Accessibility kontrol ikon tanpa teks: ikon Changelog, ikon Download, dan row action ⋯ memiliki nama aksesibel

42. Klik tab Default
43. Verifikasi ikon Changelog dan ikon Download pada toolbar tab Default masing-masing memiliki nama aksesibel yang tidak kosong
44. Verifikasi row action `⋯` pada baris `Growth` memiliki nama aksesibel yang tidak kosong
45. Klik tab Custom sub-tab Active
46. Verifikasi ikon Changelog dan ikon Download pada toolbar tab Custom masing-masing memiliki nama aksesibel yang tidak kosong
47. Verifikasi row action `⋯` pada baris `Growth Tier` memiliki nama aksesibel yang tidak kosong

## Notes

- Langkah penghubung (S-03): klik tab pada langkah 1, 16, 34, 42, dan 45 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 13 sampai 15 dan 31 sampai 33 menutup form dirty (S-08, S-09); langkah 41 mengembalikan field Global Settings ke nilai tersimpan sebelum meninggalkan tab (S-09, pemulihan form dirty tanpa `Verifikasi`).
- Alasan di atas sekitar 35 langkah (47 langkah): keempat blok satu kelas harness (pembacaan atribut aksesibilitas pada UI, TC bertanda UI Only), tiap blok memakai form atau toolbar sendiri dan berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; tiap Expected dipecah menjadi `Verifikasi` pesan inline dan `Verifikasi` aria-describedby (S-01).
- Temuan untuk QA:
  - TC-AC-PF-792: Expected b menyebut pesan inline Pricing Type tanpa posisi ("tampil dan aria-describedby menunjuk ..."), sedangkan butir a dan c menyebut "di bawah field"; spec mengikuti kalimat TC.
