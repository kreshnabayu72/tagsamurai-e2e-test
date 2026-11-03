---
id: TC-AC-PF-E2E-093-edit-api-call-quota-custom-bernilai-sama-dengan-preset
title: "Edit Custom Plan: API call quota Custom Bernilai Sama dengan Preset"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-648
coverage:
  web: automated
---

# Edit Custom Plan: API call quota Custom Bernilai Sama dengan Preset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan CP (`Paket Kuota Seratus` v1 dengan API call quota 100000 dan `Paket Kuota Sejuta` v1 dengan API call quota 1000000, Open API ON).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Paket Kuota Seratus` dan `Paket Kuota Sejuta` adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Kedua Save adalah No-Op sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`
2. Catat Version dan Last Modified `Paket Kuota Seratus` dan `Paket Kuota Sejuta` pada list, lalu catat baseline jumlah entri Changelog tab Custom (N)

### TC-AC-PF-648: Edit Custom Plan: memilih Custom lalu mengetik nilai yang sama dengan preset bukan perubahan field, sehingga Edit no-op tanpa versi baru dan tanpa entri Changelog

3. Buka Overlay Row Action `Paket Kuota Seratus`, lalu klik `Edit`
4. Pilih API call quota `Custom`
5. Isi nilai Custom `100000`
6. Klik `[Save]`
7. Verifikasi toast netral: "No changes to save." (bukan toast sukses dan bukan toast error)
8. Verifikasi form ditutup dan Plan Detail `Paket Kuota Seratus` tampil
9. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
10. Buka Overlay Row Action `Paket Kuota Sejuta`, lalu klik `Edit`
11. Pilih API call quota `Custom`
12. Isi nilai Custom `1000000`
13. Klik `[Save]`
14. Verifikasi toast netral: "No changes to save." (bukan toast sukses dan bukan toast error)
15. Verifikasi form ditutup dan Plan Detail `Paket Kuota Sejuta` tampil
16. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
17. Verifikasi Version `Paket Kuota Seratus` dan `Paket Kuota Sejuta` tetap `v1`
18. Verifikasi Last Modified kedua plan sama dengan nilai yang dicatat
19. Buka Plan Detail `Paket Kuota Seratus`
20. Verifikasi Tab Overview baris API call quota `100K/month`
21. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
22. Buka Plan Detail `Paket Kuota Sejuta`
23. Verifikasi Tab Overview baris API call quota `1M/month`
24. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
25. Klik ikon Changelog pada toolbar tab Custom
26. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru untuk `Paket Kuota Seratus` maupun `Paket Kuota Sejuta`)

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal; mencatat Version, Last Modified, dan baseline Changelog sebelum aksi pemicu (S-12); kembali ke list lewat breadcrumb; membuka Plan Detail dari list untuk Tab Overview.
- P-1 (state berat): Verifikasi 'tidak ada entri Changelog baru' ditulis di spec ini sebagai Verifikasi berbaseline karena konteksnya bergantung pada state yang dibangun langkah sebelumnya dalam spec ini (dua Save No-Op); anchor positifnya toast netral "No changes to save.". Tidak ada spec absence terpisah untuk TC ini (S-05).
- Temuan untuk QA:
  - Pre-setup TC-AC-PF-648 tidak menyebut Last Modified awal kedua plan; spec mencatat nilainya dari list sebelum aksi.
