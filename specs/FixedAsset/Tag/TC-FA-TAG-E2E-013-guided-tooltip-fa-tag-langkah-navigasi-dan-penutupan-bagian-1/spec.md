---
id: TC-FA-TAG-E2E-013-guided-tooltip-fa-tag-langkah-navigasi-dan-penutupan-bagian-1
title: "Guided Tooltip fa-tag: Kunjungan Pertama, Langkah 1 sampai 4, serta Penutupan lewat Done, Skip, dan Overlay"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-62
  - TC-FA-TAG-63
  - TC-FA-TAG-64
  - TC-FA-TAG-65
  - TC-FA-TAG-66
  - TC-FA-TAG-67
  - TC-FA-TAG-68
coverage:
  web: automated
---

# Guided Tooltip fa-tag: Kunjungan Pertama, Langkah 1 sampai 4, serta Penutupan lewat Done, Skip, dan Overlay

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-tag` sendiri sehingga mengecualikan pernyataan hook suite. Hook `before` spec ini menyetel flag itu belum ada untuk akun Total Control sesudah hook suite, dan hook `after` memulihkannya ke true (nilai awal akun dicatat di hook `before`). Langkah 19, 23, 27, 31, dan 35 menghapus atau memeriksa flag lewat kemampuan teknis di bawah.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak didefinisikan di TC maupun PRD yang dibaca, S-13): menghapus dan menyetel flag `guided_tooltip_seen_fa-tag` untuk akun Total Control, serta membaca nilainya untuk asersi bahwa flag bernilai true.
- Data Pre-setup tab Paired (dipakai sebagai latar; hanya dibaca, tidak diubah): grup Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena data Pre-setup yang sama dipakai spec lain (suite.md).
- State global yang diubah: flag Guided Tooltip akun Total Control (dipulihkan di hook `after`); suite berjalan serial.

## Test Steps

### TC-FA-TAG-62: Guided Tooltip fa-tag muncul otomatis pada kunjungan pertama dengan langkah 1

1. Buka menu Fixed Asset > TAG lewat sidebar
2. Verifikasi overlay gelap dengan spotlight pada Tabs
3. Verifikasi Tooltip box menampilkan `Step 1 of 4`, judul `Tabs`, dan deskripsi `Switch views here. Each tab keeps its own table, search, and filters.`
4. Verifikasi navigasi memuat `[Skip]` dan `[Next]`
5. Verifikasi tombol `[Back]` Hidden pada Step 1

### TC-FA-TAG-63: Guided Tooltip langkah 2 menyorot kartu filter

6. Klik `[Next]`
7. Verifikasi Step 2 of 4 dengan judul `Needs attention` dan deskripsi `Click a card to filter the table to the rows that need follow-up.`
8. Verifikasi spotlight pada kartu filter
9. Verifikasi `[Back]` tampil

### TC-FA-TAG-64: Guided Tooltip langkah 3 pada tab Paired menyorot tabel grup

10. Klik `[Next]`
11. Verifikasi Step 3 of 4 dengan judul `Groups` dan deskripsi `Click a group to review its TAGs.`
12. Verifikasi spotlight pada tabel grup tab Paired

### TC-FA-TAG-65: Guided Tooltip langkah 4 pada tab Paired menyorot tombol Changelog

13. Klik `[Next]`
14. Verifikasi Step 4 of 4 dengan judul `Changelog` dan deskripsi `Review the history of TAG replacements you have access to.`
15. Verifikasi spotlight pada tombol `Changelog`
16. Verifikasi tombol `[Next]` berganti menjadi `[Done]`

### TC-FA-TAG-66: Klik Done pada langkah terakhir menutup walkthrough dan menandai seen

17. Klik `[Done]`
18. Verifikasi walkthrough tertutup
19. Verifikasi flag `guided_tooltip_seen_fa-tag` bernilai true pada akun
20. Muat ulang halaman
21. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tampil
22. Verifikasi walkthrough tidak muncul lagi

### TC-FA-TAG-67: Klik Skip menutup walkthrough dan menandai seen

23. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
24. Buka menu Fixed Asset > TAG lewat sidebar
25. Klik `[Skip]`
26. Verifikasi walkthrough tertutup
27. Verifikasi flag `guided_tooltip_seen_fa-tag` bernilai true
28. Muat ulang halaman
29. Verifikasi Breadcrumb `Fixed Asset > TAG > Paired` tampil
30. Verifikasi walkthrough tidak muncul lagi

### TC-FA-TAG-68: Klik overlay gelap menutup walkthrough sebagai Skip

31. Hapus flag `guided_tooltip_seen_fa-tag` akun Total Control
32. Buka menu Fixed Asset > TAG lewat sidebar
33. Klik area overlay gelap di luar Tooltip box
34. Verifikasi walkthrough tertutup
35. Verifikasi flag seen ditetapkan (bernilai true)

## Notes

- Langkah 23 dan 31 adalah langkah penghubung (menghapus flag agar kunjungan berikutnya dianggap pertama), tanpa asersi (S-03). Flag awal untuk TC-FA-TAG-62 dibentuk hook `before` spec ini.
- Langkah 6, 10, dan 13 melanjutkan walkthrough yang dibuka pada langkah 1: langkah 1 TC-FA-TAG-63 sampai 65 ("Buka menu Fixed Asset > TAG") identik dengan langkah 1 TC-FA-TAG-62 sehingga walkthrough dibuka satu kali dan di-`[Next]` bertahap (langkah 2 TC-FA-TAG-64 "klik `[Next]` dua kali" dan langkah 2 TC-FA-TAG-65 "tiga kali" dipenuhi oleh langkah 6, 10, dan 13 secara berurutan). Urutan TC tidak diubah.
- Langkah 22 dan 30 adalah asersi absence atas walkthrough sesudah muat ulang; anchor positif adalah Verifikasi Breadcrumb tampil pada halaman yang sama (langkah 21 dan 29) (bagian 8b butir 2, R-21).
- TC-FA-TAG-69, 70, 73 sampai 75 ada di spec 014 dan 019; TC-FA-TAG-71 dan 72 ada di spec 015.
- Temuan untuk QA:
  - TC-FA-TAG-66, 67, 68, dan 70 memuat Post Condition "Flag seen tersimpan pada akun" yang juga muncul sebagai klausa Expected; spec mengasersi flag lewat kemampuan baca flag di atas, yang mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
  - TC-FA-TAG-62 Precondition c ("flag belum ada untuk akun ini") dan "pertama kali" mengharuskan flag dihapus sebelum tiap TC kunjungan pertama; mekanisme penghapusan tidak disebut TC dan disediakan tim FE/BE.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut data tab Paired yang sama dengan spec lain, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
