---
id: TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature
title: "Screening Form Edit Default Plan: Free, Paid, Feature Suites, dan Fokus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-218
  - TC-AC-PF-219
  - TC-AC-PF-228
  - TC-AC-PF-232
  - TC-AC-PF-734
coverage:
  web: automated
---

# Screening Form Edit Default Plan: Free, Paid, Feature Suites, dan Fokus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Starter` v2 (default plan FAMS Free; Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None); `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month).
- Pengecualian S-06/S-12 butir A-14: `Starter` v2 dan `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]` yang berhasil) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`

### TC-AC-PF-218: Screening form Edit Default Plan Free: Pricing Type badge read-only, Asset cap terisi, Feature Suites terkunci

2. Buka Overlay Row Action `Starter`, lalu klik `Edit`
3. Verifikasi Header: breadcrumb `Plans & Licensing > Plans & Features > Edit Plan`
4. Susuri halaman dari atas ke bawah
5. Verifikasi Body SectionCard Plan: Product `FAMS` terkunci
6. Verifikasi Body SectionCard Plan: Plan Name `Starter` dapat diedit
7. Verifikasi Body SectionCard Plan: Pricing Type tampil sebagai badge read-only `Free` (bukan field yang dapat diubah)
8. Verifikasi Body SectionCard Plan: tidak ada field Template
9. Verifikasi Body Capacity Toggles terisi termasuk `Asset cap` `25`
10. Verifikasi Body Feature Suites tampil (visible) namun Disabled dengan semua nilai `None`
11. Verifikasi Footer: Estimated Total, `[Clear Field]`, dan `[Save]` tampil

### TC-AC-PF-228: Feature Suites plan Free pada Edit tetap terkunci None dan tidak dapat diubah

12. Coba buka dropdown Borrowing
13. Verifikasi dropdown Borrowing Disabled (tetap tampil) bernilai `None`
14. Verifikasi kelima field Feature Suites tidak dapat diubah
15. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`

### TC-AC-PF-219: Screening form Edit Default Plan Paid: badge Pricing Type Paid, tanpa Asset cap, Feature Suites aktif

16. Buka Overlay Row Action `Growth`, lalu klik `Edit`
17. Amati SectionCard Plan, Capacity Toggles, dan Feature Suites
18. Verifikasi Pricing Type tampil sebagai badge read-only `Paid`
19. Verifikasi Product `FAMS` terkunci
20. Verifikasi field `Asset cap` tidak ada
21. Verifikasi Feature Suites aktif dan dapat dipilih

### TC-AC-PF-232: Pricing Type tidak dapat diubah pada Edit Default Plan: tidak ada kontrol pengubah tier

22. Cari kontrol untuk mengubah Pricing Type atau posisi tier pada form
23. Verifikasi Pricing Type hanya badge read-only `Paid`
24. Verifikasi tidak ada radio, dropdown, atau input angka tier
25. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`

### TC-AC-PF-734: Edit Default Plan: input pertama langsung ter-focus saat form muncul dan Enter tidak men-submit

26. Buka Overlay Row Action `Growth`, lalu klik `Edit`
27. Verifikasi fokus langsung berada di field Plan Name
28. Ubah Plan Name menjadi `Ubah Enter`
29. Tekan Enter saat fokus berada di field Plan Name
30. Verifikasi tidak ada toast
31. Verifikasi form tetap terbuka dengan input dipertahankan (Plan Name `Ubah Enter`)
32. Klik segmen `Plans & Features` pada breadcrumb
33. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
34. Klik `[Leave]`
35. Verifikasi baris `Growth` pada list tetap bernama `Growth` dengan Version `v5` (tidak ada perubahan data)

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; kembali ke list lewat breadcrumb dari form bersih; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08). Baris terakhir adalah pengamatan perubahan data untuk Expected TC-AC-PF-734. Blok TC-AC-PF-228 memakai form Edit `Starter` yang dibuka blok TC-AC-PF-218, dan blok TC-AC-PF-232 memakai form Edit `Growth` yang dibuka blok TC-AC-PF-219 (halaman yang sama dipakai berulang).
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
