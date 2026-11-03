---
id: TC-AC-PF-E2E-082-edit-custom-plan-dependency-d-2-open-api-off-open-api-on
title: "Edit Custom Plan: Dependency D-2, Open API OFF, dan Open API ON Tanpa Quota"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-209
  - TC-AC-PF-210
  - TC-AC-PF-211
coverage:
  web: automated
---

# Edit Custom Plan: Dependency D-2, Open API OFF, dan Open API ON Tanpa Quota

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20); custom plan `Paket Open API Off` (Open API OFF, API call quota —).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 dan `Paket Open API Off` adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]` yang berhasil) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-209: Dependency D-2 pada form Edit Custom Plan: Group count 1 mengubah depth ke 1 dengan inline warning

2. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
3. Ubah Group count menjadi `1`
4. Verifikasi Group hierarchy depth otomatis `1`
5. Verifikasi License allocation per group otomatis OFF
6. Verifikasi inline warning "Group hierarchy depth was changed automatically because group count requires it." tampil
7. Verifikasi inline warning "License allocation per group was changed automatically because group count requires it." tampil
8. Klik segmen `Plans & Features` pada breadcrumb
9. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
10. Klik `[Leave]`
11. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-210: Open API OFF pada form Edit Custom Plan mereset API call quota ke — dan mengunci field

12. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
13. Matikan Open API
14. Verifikasi API call quota berubah dari `1M/month` ke `—`
15. Verifikasi API call quota terkunci (Disabled)
16. Hover field API call quota
17. Verifikasi tooltip `Turn on Open API to set an API call quota.` tampil
18. Klik segmen `Plans & Features` pada breadcrumb
19. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
20. Klik `[Leave]`
21. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-211: Open API ON dengan API call quota kosong pada Edit ditolak dengan pesan inline

22. Catat Version baris `Paket Open API Off` pada list tab Custom
23. Buka Overlay Row Action `Paket Open API Off`, lalu klik `Edit`
24. Nyalakan Open API tanpa memilih API call quota
25. Klik `[Save]`
26. Verifikasi pesan inline `API call quota must not be empty` muncul setelah Save
27. Klik segmen `Plans & Features` pada breadcrumb
28. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
29. Klik `[Leave]`
30. Klik tab `Custom`, lalu sub-tab `Active`
31. Verifikasi baris `Paket Open API Off` pada list: Version sama dengan nilai yang dicatat (versi tidak naik)

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal dan pada langkah 11, 21, dan 30 sesudah `[Leave]` (landing breadcrumb adalah Default > Active); mencatat Version `Paket Open API Off` sebelum aksi; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08) setelah tiap blok karena tiap blok membiarkan form dirty (S-09).
- Temuan untuk QA:
  - Pre-setup TC-AC-PF-211 tidak menyebut Version awal `Paket Open API Off`; Expected 'versi tidak naik' diasersi lewat Version yang dicatat sebelum aksi.
