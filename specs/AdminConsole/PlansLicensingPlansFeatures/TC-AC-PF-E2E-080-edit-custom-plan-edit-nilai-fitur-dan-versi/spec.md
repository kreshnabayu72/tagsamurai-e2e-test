---
id: TC-AC-PF-E2E-080-edit-custom-plan-edit-nilai-fitur-dan-versi
title: "Edit Custom Plan: Edit Nilai Fitur, Rename, dan Versi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-203
  - TC-AC-PF-204
  - TC-AC-PF-205
coverage:
  web: automated
---

# Edit Custom Plan: Edit Nilai Fitur, Rename, dan Versi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features).
- Data Pre-setup: `Growth Tier` v20 (Pre-setup; Group count 25, Group hierarchy depth 5, Asset Name cap 500, API call quota 1M/month, Open API ON, Borrowing Full; nilai lain sama dengan `Growth` v5; satu client `PT Wahana Nusantara` memegang v20).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Asersi Last Modified: waktu dicatat sesudah `[Save]`, Last Modified dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron.
- Kemampuan baca jumlah entri Changelog (tab Default atau Custom) dan jumlah total plan sebelum dan sesudah aksi disediakan tim FE/BE; Changelog adalah audit trail permanen sehingga N tidak diturunkan dari seeding dan asersi memakai selisih terhadap baseline N yang dicatat sebelum aksi pemicu.
- Pengecualian S-06/S-12 butir A-14: `Growth Tier` v20 adalah data Pre-setup bersama yang dipakai dengan nama literal tanpa suffix. Ketiga blok menyimpan perubahan: Last Modified `Growth Tier` berubah, versi naik ke v21, client `PT Wahana Nusantara` menjadi Outdated, dan Changelog Custom bertambah; semua dipulihkan Fixture BE kecuali entri Changelog yang permanen. Pemulihan seluruh Dataset ke keadaan awal dijamin Fixture BE idempoten, dijalankan di hook `before` dan `after` spec ini dan sebagai langkah penghubung antar blok TC; suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk memulihkan Dataset Pre-setup (idempoten) disediakan tim FE/BE (lihat `suite.md`). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data pada langkah dirujuk lewat `Fixture.plansFeatures.<kunci>` setelah tim FE menyediakannya.
- State global: suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `Custom`, lalu sub-tab `Active`

### TC-AC-PF-203: Edit satu nilai fitur: versi naik satu, Changelog Edit satu baris, client existing menjadi Outdated

2. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
3. Ubah Group count `25` menjadi `3`
4. Klik `[Save]`, lalu catat waktu Save
5. Verifikasi toast sukses: "Success, plan has been updated."
6. Verifikasi Plan Detail terbuka dengan judul `Growth Tier – v21`
7. Buka Tab Assigned Clients, lalu amati kolom Plan Version `PT Wahana Nusantara`
8. Verifikasi baris `PT Wahana Nusantara` memegang `v20`
9. Verifikasi baris `PT Wahana Nusantara` berbadge `Outdated` (client existing tetap di versi lama)
10. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
11. Verifikasi baris `Growth Tier` pada list: Version `v21`
12. Verifikasi baris `Growth Tier` pada list: Last Modified diperbarui ke waktu Save
13. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Custom` sub-tab `Active`

### TC-AC-PF-204: Edit beberapa field sekaligus: satu kenaikan versi dan Changelog satu baris per field yang berubah

14. Catat baseline jumlah entri Changelog tab Custom (N)
15. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
16. Ubah Group count `25` menjadi `3`
17. Matikan Open API
18. Ubah Borrowing `Full` menjadi `Basic`
19. Klik `[Save]`
20. Verifikasi Plan Detail terbuka dengan judul `Growth Tier – v21` (versi naik sekali)
21. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
22. Buka Changelog dari toolbar tab Custom
23. Verifikasi jumlah entri Changelog naik 4 dari baseline N, semuanya Action `Edit` untuk Plan `Growth Tier`: Field `Group count` (25 → 3), Field `Open API` (Yes → No), Field `API call quota` (1M/month → —), Field `Borrowing` (Full → Basic)
24. Tutup modal Changelog
25. Pulihkan Dataset Pre-setup lewat Fixture BE, muat halaman Plans & Licensing > Plans & Features dari menu sidebar, lalu klik tab `Custom` sub-tab `Active`

### TC-AC-PF-205: Edit hanya mengganti Plan Name: versi tidak naik, Changelog tercatat, client tidak menjadi Outdated

26. Catat baseline jumlah entri Changelog tab Custom (N)
27. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
28. Ganti Plan Name menjadi `Growth Tier Rename`
29. Klik `[Save]`, lalu catat waktu Save
30. Verifikasi toast sukses: "Success, plan has been updated."
31. Verifikasi judul Plan Detail `Growth Tier Rename – v20` (versi tidak naik)
32. Buka Tab Assigned Clients
33. Verifikasi `PT Wahana Nusantara` memegang `v20`
34. Verifikasi `PT Wahana Nusantara` tanpa badge `Outdated`
35. Kembali ke list: klik segmen `Plans & Features` pada breadcrumb, lalu tab `Custom` sub-tab `Active`
36. Verifikasi baris `Growth Tier Rename` pada list: Last Modified diperbarui ke waktu Save
37. Klik ikon Changelog pada toolbar tab Custom
38. Verifikasi jumlah entri Changelog naik 1 dari baseline N dengan satu baris Action `Edit`, Field `Plan Name`, Old `Growth Tier`, New `Growth Tier Rename`

## Notes

- Langkah penghubung (S-03): klik tab `Custom` sub-tab `Active`; kembali ke list lewat breadcrumb; buka Tab Assigned Clients dari Plan Detail; pemulihan Dataset lewat Fixture BE antar blok (A-6); baseline N dicatat sebelum aksi pemicu (S-12).
- Entri `API call quota` (1M/month → —) pada Changelog adalah akibat otomatis dari Open API OFF (TC-AC-PF-210), bukan perubahan yang dilakukan langkah; aksi di TC hanya tiga: Group count, Open API, Borrowing.
- Alasan spec melewati sekitar 35 langkah: semua blok berkelas fungsional pada halaman Edit Plan yang sama dan berdiri sendiri; tiap blok memuat pembukaan form dan penutupan form dirty yang wajib eksplisit (S-08, S-09), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Judul TC-AC-PF-203 menyebut 'Changelog Edit satu baris' tetapi Expected a sampai c tidak memuat asersi Changelog; spec mengikuti Expected dan tidak menambah asersi Changelog.
  - TC-AC-PF-204 menetapkan empat baris Changelog tetapi tidak menyebut urutan baris; spec mengasersi isi keempat baris tanpa urutan.
