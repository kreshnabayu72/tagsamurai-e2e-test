---
id: TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda
title: "Edit Custom dan Default Plan: State Submitting dan Klik Ganda pada Save"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-216
  - TC-AC-PF-608
  - TC-AC-PF-701
  - TC-AC-PF-702
coverage:
  web: automated
---

# Edit Custom dan Default Plan: State Submitting dan Klik Ganda pada Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20); Dataset Plan A: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month).
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Intercept: `Spectra.intercept` parsial di atas backend nyata menunda respons request simpan Edit Plan pada blok TC-AC-PF-701 dan TC-AC-PF-702; pencocokan request disediakan tim FE (endpoint tidak tertulis di TC). Intercept dilepas segera setelah pengamatan (S-09).
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 dan `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok TC-AC-PF-216 dan TC-AC-PF-608 menyimpan perubahan (versi naik, Last Updated dan Changelog bertambah); blok TC-AC-PF-701 dan 702 tidak menyimpan. Efek dipulihkan Fixture BE kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`
2. Catat baseline jumlah entri Changelog tab Custom (N)

### TC-AC-PF-216: Klik ganda cepat pada Save Edit Custom Plan hanya menaikkan versi satu kali

3. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
4. Ubah Group count menjadi `3`
5. Klik `[Save]` dua kali dengan cepat
6. Verifikasi satu toast sukses: "Success, plan has been updated."
7. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
8. Verifikasi kolom Version `Growth Tier` pada list `v21` (bukan v22)
9. Klik ikon Changelog pada toolbar tab Custom
10. Verifikasi jumlah entri Changelog naik 1 dari baseline N dengan satu baris Field `Group count`
11. Tutup modal Changelog
12. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Default` sub-tab `Active`
13. Catat baseline jumlah entri Changelog tab Default (N)

### TC-AC-PF-608: Klik ganda cepat pada Save Edit Default Plan hanya menaikkan versi satu kali

14. Buka Overlay Row Action `Growth`, lalu klik `Edit`
15. Ubah Group count `3` menjadi `25`
16. Klik `[Save]` dua kali dengan cepat
17. Verifikasi satu toast sukses: "Success, plan has been updated."
18. Verifikasi judul Plan Detail `Growth – v6` (bukan v7)
19. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
20. Klik ikon Changelog pada toolbar tab Default
21. Verifikasi jumlah entri Changelog naik 1 dari baseline N dengan satu baris Edit Field `Group count` (3 → 25) untuk `Growth`
22. Tutup modal Changelog
23. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Custom` sub-tab `Active`

### TC-AC-PF-701: Saat Save Edit Custom Plan berlangsung: tombol Save loading dan Disabled, kontrol lain dibekukan

24. Tahan respons request simpan Edit Plan lewat `Spectra.intercept` (respons ditunda)
25. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
26. Ubah Group count menjadi `3`
27. Klik `[Save]`
28. Verifikasi tombol `[Save]` menampilkan indikator loading
29. Verifikasi tombol `[Save]` berstatus Disabled
30. Verifikasi field input dan tombol `[Clear Field]` tidak dapat dipakai selama request berlangsung
31. Lepas intercept dengan membatalkan request yang tertunda
32. Kembalikan Group count ke `25` (nilai tersimpan)

### TC-AC-PF-702: Saat Save Edit Default Plan berlangsung: tombol Save loading dan Disabled, kontrol lain dibekukan

33. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
34. Tahan respons request simpan Edit Plan lewat `Spectra.intercept` (respons ditunda)
35. Buka Overlay Row Action `Growth`, lalu klik `Edit`
36. Ubah Group count `3` menjadi `25`
37. Klik `[Save]`
38. Verifikasi tombol `[Save]` menampilkan indikator loading
39. Verifikasi tombol `[Save]` berstatus Disabled
40. Verifikasi field input dan tombol `[Clear Field]` tidak dapat dipakai selama request berlangsung
41. Lepas intercept dengan membatalkan request yang tertunda
42. Kembalikan Group count ke `3` (nilai tersimpan)

## Notes

- Langkah penghubung (S-03): klik tab `Custom` atau `Default` sub-tab `Active` sebelum membuka row action; mencatat baseline Changelog sebelum aksi pemicu (S-12); kembali ke list lewat breadcrumb; pemulihan Dataset lewat Fixture BE antar blok (A-6); menahan dan melepas intercept; mengembalikan Group count ke nilai tersimpan pada akhir blok TC-AC-PF-701 dan TC-AC-PF-702 agar form tidak dirty saat berpindah (S-09). Blok TC-AC-PF-701 dan 702 ditaruh sesudah blok klik ganda karena dua blok pertama memulihkan Dataset sebelum blok berikutnya.
- Alasan spec melewati sekitar 35 langkah: keempat blok berkelas fungsional (state tombol Save Edit Plan), berdiri sendiri, dan memakai dua entitas (Custom dan Default) sehingga masing-masing butuh pembukaan form dan pemulihan Dataset sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-PF-701 dan TC-AC-PF-702: Post Condition 'Tidak ada perubahan data' berbenturan dengan request simpan yang ditunda, karena request itu menyimpan data bila respons dilepaskan. Spec membatalkan request tertunda (kemampuan Spectra.intercept disediakan tim FE) agar tidak ada perubahan data; TC tidak menyebut cara melepas tahanan.
  - TC-AC-PF-702: langkah 'Ubah Group count' tanpa nilai; spec memakai `3` menjadi `25` seperti TC-AC-PF-608.
