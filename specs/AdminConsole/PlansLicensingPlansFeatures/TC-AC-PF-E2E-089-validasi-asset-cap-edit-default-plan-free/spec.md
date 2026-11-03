---
id: TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free
title: "Validasi Asset cap Edit Default Plan Free"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-224
  - TC-AC-PF-225
  - TC-AC-PF-226
  - TC-AC-PF-227
coverage:
  web: automated
---

# Validasi Asset cap Edit Default Plan Free

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Starter` v2 (default plan FAMS Free; Asset cap 25, Group count 1, Group hierarchy depth 1, Category count 5, Category hierarchy depth 1, Asset Name cap 10, seluruh Binary OFF, Feature Suites None).
- Pengecualian S-06/S-12 butir A-14: `Starter` v2 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok TC-AC-PF-227 menyimpan Asset cap `0` (versi naik ke v3, Last Updated berubah, entri Changelog Default bertambah); blok TC-AC-PF-224 sampai 226 tidak menyimpan. Efek dipulihkan Fixture BE kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`

### TC-AC-PF-224: Validasi Asset cap Edit Default Plan Free: nilai kosong ditolak setelah Save

2. Buka Overlay Row Action `Starter`, lalu klik `Edit`
3. Kosongkan field Asset cap
4. Klik `[Save]`
5. Verifikasi pesan inline `Value must be a whole number of 0 or more` muncul setelah Save

### TC-AC-PF-225: Validasi Asset cap Edit Default Plan Free: nilai negatif -1 ditolak setelah Save

6. Isi Asset cap dengan `-1`
7. Klik `[Save]`
8. Verifikasi pesan inline `Value must be a whole number of 0 or more` muncul setelah Save

### TC-AC-PF-226: Validasi Asset cap Edit Default Plan Free: nilai desimal 2.5 ditolak setelah Save

9. Isi Asset cap dengan `2.5`
10. Klik `[Save]`
11. Verifikasi pesan inline `Value must be a whole number of 0 or more` muncul setelah Save
12. Klik segmen `Plans & Features` pada breadcrumb
13. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
14. Klik `[Leave]`
15. Verifikasi baris `Starter` pada list tetap Version `v2` (versi tidak naik pada ketiga penolakan di atas)

### TC-AC-PF-227: Asset cap Edit Default Plan Free bernilai 0 sah

16. Buka Overlay Row Action `Starter`, lalu klik `Edit`
17. Isi Asset cap dengan `0`
18. Klik `[Save]`
19. Verifikasi toast sukses: "Success, plan has been updated."
20. Verifikasi Tab Overview: Asset cap `0`

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active` di awal; menutup form dirty lewat breadcrumb, dialog Unsaved Changes, dan `[Leave]` (S-08). Blok penolakan (TC-AC-PF-224, 225, 226) berurutan pada satu pembukaan form dengan nilai Asset cap diganti di antara kasus; Verifikasi Version `v2` sesudah penutupan form adalah pengamatan 'versi tetap v2' untuk ketiganya dan terjadi sebelum blok TC-AC-PF-227 menyimpan.
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
