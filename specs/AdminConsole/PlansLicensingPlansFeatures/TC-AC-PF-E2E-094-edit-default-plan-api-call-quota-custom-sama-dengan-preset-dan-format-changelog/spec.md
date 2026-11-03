---
id: TC-AC-PF-E2E-094-edit-default-plan-api-call-quota-custom-sama-dengan-preset-dan-format-changelog
title: "Edit Default Plan Growth: API call quota Custom Sama dengan Preset dan Format Nilai Changelog"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-649
coverage:
  web: automated
---

# Edit Default Plan Growth: API call quota Custom Sama dengan Preset dan Format Nilai Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok Custom `150000` dan Custom `1000000` menyimpan perubahan (versi naik ke v7, Last Updated dan Changelog Default bertambah); Fixture BE memulihkan Dataset kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`
2. Catat baseline jumlah entri Changelog tab Default (N)

### TC-AC-PF-649: Edit Default Plan Growth: Custom bernilai sama dengan preset adalah no-op, sedangkan Custom 150000 lalu Custom 1000000 menaikkan versi dan Changelog menulis nilai dengan format tampil

3. Buka Overlay Row Action `Growth`, lalu klik `Edit`
4. Pilih API call quota `Custom`
5. Isi nilai Custom `100000`
6. Klik `[Save]`
7. Verifikasi toast netral: "No changes to save."
8. Verifikasi form ditutup dan Plan Detail `Growth` tampil
9. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
10. Verifikasi kolom Version `Growth` pada list tetap `v5`
11. Klik ikon Changelog pada toolbar tab Default
12. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri Edit `API call quota` untuk `Growth`)
13. Tutup modal Changelog
14. Buka Overlay Row Action `Growth`, lalu klik `Edit`
15. Pilih API call quota `Custom`
16. Isi nilai Custom `150000`
17. Klik `[Save]`
18. Verifikasi toast sukses: "Success, plan has been updated."
19. Verifikasi judul Plan Detail `Growth – v6`
20. Verifikasi Tab Overview baris API call quota `150,000/month`
21. Klik button `Edit` di header Plan Detail
22. Pilih API call quota `Custom`
23. Isi nilai Custom `1000000`
24. Klik `[Save]`
25. Verifikasi judul Plan Detail `Growth – v7`
26. Verifikasi Tab Overview baris API call quota `1M/month` (bukan `1,000,000/month`)
27. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
28. Klik ikon Changelog pada toolbar tab Default
29. Verifikasi jumlah entri Changelog naik 2 dari baseline N: dua entri Edit `Growth` Field `API call quota` dengan `100K/month` → `150,000/month` dan `150,000/month` → `1M/month`

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; mencatat baseline Changelog sebelum aksi pemicu (S-12); kembali ke list lewat breadcrumb; menutup modal Changelog; membuka Edit dari header Plan Detail (jalur setara row action).
- P-1 (state berat): Verifikasi 'tidak ada entri Changelog baru' untuk Custom `100000` ditulis sebagai Verifikasi berbaseline karena konteksnya bergantung pada state yang dibangun langkah sebelumnya dalam spec ini (Save No-Op); anchor positifnya toast netral "No changes to save.". Tidak ada spec absence terpisah untuk TC ini (S-05).
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
