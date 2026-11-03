---
id: TC-AC-PF-E2E-095-edit-default-plan-asset-cap-free-dan-product-siem
title: "Edit Default Plan: Asset cap Free dan Product SIEM"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-223
  - TC-AC-PF-229
coverage:
  web: automated
---

# Edit Default Plan: Asset cap Free dan Product SIEM

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Starter` v2 (default plan FAMS Free; Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None); Dataset Plan A: default plan `SIEM` (Product SIEM).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Starter` v2 dan `SIEM` adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Kedua blok menyimpan perubahan (Last Updated berubah, versi naik, Changelog Default bertambah); Fixture BE memulihkan Dataset kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`
2. Catat baseline jumlah entri Changelog tab Default (N)

### TC-AC-PF-223: Edit Asset cap default plan Free menaikkan versi dan tercatat di Changelog

3. Buka Overlay Row Action `Starter`, lalu klik `Edit`
4. Ubah Asset cap `25` menjadi `50`
5. Klik `[Save]`
6. Verifikasi toast sukses: "Success, plan has been updated."
7. Verifikasi judul Plan Detail `Starter – v3`
8. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
9. Klik ikon Changelog pada toolbar tab Default
10. Verifikasi jumlah entri Changelog naik 1 dari baseline N: Action `Edit`, Plan `Starter`, Field `Asset cap`, Old `25`, New `50`
11. Tutup modal Changelog
12. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Default` sub-tab `Active`

### TC-AC-PF-229: Edit default plan SIEM berperilaku sama seperti Product lain: rename dan nilai fitur

13. Buka Overlay Row Action `SIEM` (Product SIEM), lalu klik `Edit`
14. Ubah Plan Name menjadi `SIEM Utama`
15. Klik `[Save]`
16. Verifikasi toast sukses: "Success, plan has been updated."
17. Verifikasi judul Plan Detail `SIEM Utama – v1` (tanpa kenaikan versi)
18. Klik button `Edit` di header Plan Detail
19. Ubah Group count ke nilai yang berbeda dari nilai tersimpan
20. Klik `[Save]`
21. Verifikasi judul Plan Detail `SIEM Utama – v2` (versi naik menjadi v2)

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; mencatat baseline Changelog sebelum aksi pemicu (S-12); kembali ke list lewat breadcrumb; menutup modal Changelog; pemulihan Dataset lewat Fixture BE antar blok (A-6); membuka Edit dari header Plan Detail (jalur setara row action).
- Temuan untuk QA:
  - TC-AC-PF-229 menulis langkah 'ubah Group count' tanpa nilai dan tidak menyebut Pricing Type (Free atau Paid) default plan `SIEM`; bila `SIEM` plan Free, Group count dapat terkunci. Spec memakai nilai yang berbeda dari nilai tersimpan dan mengikuti TC.
  - TC-AC-PF-229: Pre-setup hanya 'Dataset Plan A tersedia' tanpa nilai fitur `SIEM`; Post Condition 'SIEM Utama v2' dibaca dari judul Plan Detail.
