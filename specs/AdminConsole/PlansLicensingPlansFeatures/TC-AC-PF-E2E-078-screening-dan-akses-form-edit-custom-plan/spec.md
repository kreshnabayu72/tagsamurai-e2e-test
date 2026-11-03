---
id: TC-AC-PF-E2E-078-screening-dan-akses-form-edit-custom-plan
title: "Screening dan Akses Form Edit Custom Plan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-195
  - TC-AC-PF-196
  - TC-AC-PF-733
coverage:
  web: automated
---

# Screening dan Akses Form Edit Custom Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Spec ini tidak menyimpan perubahan (tidak ada `[Save]` yang berhasil) sehingga Last Updated dan Changelog tidak berubah. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-195: Screening form Edit Custom Plan: Product terkunci, tanpa field Template, nilai terisi dari versi terakhir

2. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
3. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Edit Plan`
4. Susuri halaman dari atas ke bawah tanpa mengubah apa pun
5. Verifikasi Body SectionCard Plan: Product `FAMS` terkunci (Disabled, tidak dapat diubah)
6. Verifikasi Body SectionCard Plan: Plan Name `Growth Tier` terisi dan dapat diedit
7. Verifikasi Body SectionCard Plan: tidak ada field Template dan tidak ada field Pricing Type
8. Verifikasi Body Capacity Toggles terisi: Group count `25`
9. Verifikasi Body Capacity Toggles terisi: Group hierarchy depth `5`
10. Verifikasi Body Capacity Toggles terisi: Asset Name cap `500`
11. Verifikasi Body Capacity Toggles terisi: API call quota `1M/month`
12. Verifikasi Body Binary Toggles: Open API ON
13. Verifikasi Body Feature Suites aktif dengan Borrowing `Full`
14. Verifikasi Footer: Estimated Total, `[Clear Field]`, dan `[Save]` tampil
15. Verifikasi Footer: tidak ada `[Submit]` dan tidak ada `[Cancel]`
16. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`

### TC-AC-PF-196: Edit Custom Plan dapat dibuka dari row action dan dari tombol Edit di header Plan Detail ke form yang sama

17. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
18. Verifikasi halaman Plans & Licensing > Plans & Features > Edit Plan terbuka dengan Plan Name `Growth Tier`
19. Verifikasi nilai Capacity Toggles, Binary Toggles, dan Borrowing sama seperti langkah 8 sampai 13
20. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
21. Buka Plan Detail `Growth Tier`, lalu klik button `Edit` di header
22. Verifikasi halaman Edit Plan terbuka dengan field dan nilai yang sama seperti jalur row action
23. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`

### TC-AC-PF-733: Edit Custom Plan: input pertama langsung ter-focus saat form muncul dan Enter tidak men-submit

24. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
25. Verifikasi fokus langsung berada di field Plan Name
26. Ubah Plan Name menjadi `Ubah Enter`
27. Tekan Enter saat fokus berada di field Plan Name
28. Verifikasi tidak ada toast
29. Verifikasi form tetap terbuka dengan input dipertahankan (Plan Name `Ubah Enter`)
30. Klik segmen `Plans & Features` pada breadcrumb
31. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`
33. Klik tab `Custom`, lalu sub-tab `Active`
34. Verifikasi baris `Growth Tier` pada list tetap bernama `Growth Tier` dengan Version `v20` (tidak ada perubahan data)

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active` di awal, setelah kembali ke list, dan pada langkah 33 sesudah `[Leave]` (landing breadcrumb adalah Default > Active) (hook `beforeEach` suite membuka halaman, bukan tab tertentu); kembali ke list lewat breadcrumb dari form bersih; pembukaan ulang form untuk TC-AC-PF-196 adalah langkah sumber TC. Form Edit adalah halaman penuh, sehingga penutupan form dirty memakai breadcrumb sebagai pengganti `✕` (S-08). Baris terakhir adalah pengamatan perubahan data untuk Expected TC-AC-PF-733.
- Temuan untuk QA:
  - Tidak ada temuan TC sumber untuk spec ini.
