---
id: TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified
title: "Edit Default Plan: Nilai Fitur, Rename, No-Op, dan Last Modified"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-222
  - TC-AC-PF-230
  - TC-AC-PF-231
  - TC-AC-PF-236
coverage:
  web: automated
---

# Edit Default Plan: Nilai Fitur, Rename, No-Op, dan Last Modified

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth` v5 (default plan FAMS Paid, Dataset Plan A; Group count 3, Group hierarchy depth 2, License allocation per group ON, Open API ON, API call quota 100K/month); satu client `PT Sejahtera Abadi` memegang v5; Last Modified `Growth` `15 Jun 26, 10:00`.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Asersi Last Modified: waktu dicatat sesudah `[Save]`, Last Modified dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron.
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Growth` v5 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Blok rename dan blok TC-AC-PF-222 menyimpan perubahan (Last Modified dan Last Updated berubah, versi v6 pada blok TC-AC-PF-222, `PT Sejahtera Abadi` menjadi Outdated); Fixture BE memulihkan semuanya termasuk Last Modified awal `15 Jun 26, 10:00`, sedangkan entri Changelog Default bersifat permanen dan tidak dapat dihapus lewat UI. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Default`, lalu sub-tab `Active`
2. Catat baseline jumlah entri Changelog tab Default (N)

### TC-AC-PF-231: Edit default plan tanpa perubahan adalah No-Op dengan toast netral dan nol entri log (juga TC-AC-PF-236 bagian No-Op)

3. Buka Overlay Row Action `Growth`, lalu klik `Edit`
4. Klik `[Save]` tanpa mengubah apa pun
5. Verifikasi toast netral: "No changes to save."
6. Verifikasi form ditutup dan Plan Detail `Growth` tampil
7. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
8. Verifikasi baris `Growth` pada list: Version tetap `v5`
9. Verifikasi baris `Growth` pada list: Last Modified tetap `15 Jun 26, 10:00`
10. Klik ikon Changelog pada toolbar tab Default
11. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri baru)
12. Tutup modal Changelog

### TC-AC-PF-230: Edit default plan hanya mengganti Plan Name: versi tidak naik dan client tidak Outdated (juga TC-AC-PF-236 bagian rename)

13. Buka Overlay Row Action `Growth`, lalu klik `Edit`
14. Ganti Plan Name menjadi `Growth Utama`
15. Klik `[Save]`, lalu catat waktu Save
16. Verifikasi toast sukses: "Success, plan has been updated."
17. Verifikasi judul Plan Detail `Growth Utama – v5`
18. Buka Tab Assigned Clients
19. Verifikasi `PT Sejahtera Abadi` tanpa badge `Outdated`
20. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Default` sub-tab `Active`
21. Verifikasi baris `Growth Utama` pada list: Last Modified berubah ke waktu Save
22. Klik ikon Changelog pada toolbar tab Default
23. Verifikasi jumlah entri Changelog naik 1 dari baseline N dengan satu baris Field `Plan Name` (Old `Growth`, New `Growth Utama`)
24. Tutup modal Changelog
25. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Default` sub-tab `Active`

### TC-AC-PF-222: Edit nilai fitur default plan Paid: versi naik, Changelog Edit, client existing Outdated

26. Buka Overlay Row Action `Growth`, lalu klik `Edit`
27. Ubah Group count `3` menjadi `25`
28. Klik `[Save]`
29. Verifikasi toast sukses: "Success, plan has been updated."
30. Verifikasi judul Plan Detail `Growth – v6`
31. Buka Tab Assigned Clients
32. Verifikasi `PT Sejahtera Abadi` memegang `v5`
33. Verifikasi `PT Sejahtera Abadi` berbadge `Outdated`

## Notes

- Langkah penghubung (S-03): klik tab `Default` sub-tab `Active`; mencatat baseline Changelog sebelum aksi pemicu pertama (S-12); kembali ke list lewat breadcrumb; menutup modal Changelog; pemulihan Dataset lewat Fixture BE antar blok (A-6).
- Aksi No-Op (TC-AC-PF-231 dan bagian pertama TC-AC-PF-236) dan aksi rename `Growth` menjadi `Growth Utama` (TC-AC-PF-230 dan bagian kedua TC-AC-PF-236) identik antar TC sehingga dijalankan sekali dan diasersi untuk kedua TC; Expected tiap TC tetap punya Verifikasi sendiri. Blok No-Op ditaruh paling awal agar Last Modified awal `15 Jun 26, 10:00` masih berlaku.
- P-1 (state berat): Verifikasi 'tidak ada entri Changelog baru' pada TC-AC-PF-231 ditulis di spec ini sebagai Verifikasi berbaseline karena konteksnya bergantung pada state yang dibangun langkah sebelumnya dalam spec ini (Save No-Op); anchor positifnya toast netral "No changes to save.". Tidak ada spec absence terpisah untuk TC ini (S-05).
- Temuan untuk QA:
  - Judul TC-AC-PF-236 menyebut 'dan Archive' tetapi langkah dan Expected hanya memuat No-Op dan rename; tidak ada aksi Archive yang diasersi.
  - TC-AC-PF-236 menetapkan Last Modified awal `15 Jun 26, 10:00` sebagai Pre-setup; spec mengasumsikan Fixture BE memulihkan nilai itu pada hook `before` (nilai itu tidak tercantum di Tabel Data Uji Pre-setup yang dibaca).
