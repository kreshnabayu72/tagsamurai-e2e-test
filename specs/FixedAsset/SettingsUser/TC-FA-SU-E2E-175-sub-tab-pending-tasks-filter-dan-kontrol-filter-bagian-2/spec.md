---
id: TC-FA-SU-E2E-175-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-2
title: "Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-520
  - TC-FA-SU-521
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.

## Test Steps

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-520: Kombinasi Search dan Filter dua arah

2. Ketik Search `ASG-2026`, tekan Enter
3. Klik icon Filter
4. Buka dropdown Transaction lalu centang `Assignment`
5. Klik `[Apply]`
6. Verifikasi irisan Search `ASG-2026` dan Filter Transaction `Assignment` menyisakan `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris)
7. Verifikasi keyword Search `ASG-2026` tidak dikosongkan oleh Apply Filter
8. Klik `[Clear Field]` pada field Transaction
9. Klik `[Apply]`
10. Klik `←` pada kotak Search
11. Buka dropdown Transaction lalu centang `Assignment`
12. Klik `[Apply]`
13. Ketik Search `ASG-2026`, tekan Enter
14. Verifikasi Filter Transaction `Assignment` lalu Search `ASG-2026` menghasilkan `ASG-20260715-0045`, `ASG-20260718-0067`, identik dengan urutan sebaliknya
15. Verifikasi chip Filter Transaction `Assignment` tidak di-reset oleh Search
16. Verifikasi tabel berada di halaman 1

### TC-FA-SU-521: Pelepasan kontrol Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

17. Klik `[Clear Field]` pada field Transaction
18. Klik `[Apply]`
19. Klik `←` pada kotak Search
20. Ketik Search `ASG-2026`, tekan Enter
21. Buka dropdown Transaction lalu centang `Assignment`
22. Klik `[Apply]`
23. Klik header Transaction ID satu kali
24. Klik `[Clear Field]` pada field Transaction
25. Klik `[Apply]`
26. Verifikasi Search `ASG-2026` tetap berlaku setelah Clear Field (hasil `ASG-20260715-0045`, `ASG-20260718-0067`)
27. Verifikasi Sort Transaction ID ascending (↑) tetap berlaku setelah Clear Field
28. Buka dropdown Transaction lalu centang `Assignment`
29. Klik `[Apply]`
30. Klik `←` pada kotak Search
31. Verifikasi Filter Transaction `Assignment` tetap berlaku setelah Search dikosongkan
32. Verifikasi Sort Transaction ID ascending (↑) tetap berlaku setelah Search dikosongkan
33. Ketik Search `ASG-2026`, tekan Enter
34. Klik header Request Date satu kali
35. Verifikasi sort berpindah ke kolom Request Date (indikator pada Request Date, bukan Transaction ID)
36. Verifikasi Search `ASG-2026` dan Filter Transaction `Assignment` tidak di-reset oleh pergantian kolom sort
37. Ganti isi kotak search dengan `zzz`, tekan Enter
38. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
39. Klik `←` pada kotak Search
40. Verifikasi baris yang cocok langsung pulih: `ASG-20260715-0045`, `ASG-20260718-0067`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; `[Clear Field]`, `[Apply]`, dan `←` pada Search di awal TC-FA-SU-521 mengosongkan kontrol sisa TC-FA-SU-520 (S-09); `Ketik Search` ulang sebelum mengganti kolom sort mengembalikan Search yang dikosongkan sebelumnya.
- TC-FA-SU-522 ada di spec 192.
- Jumlah langkah: 40 tertulis, 40 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (40 langkah). Seluruh blok berada pada satu surface (satu sub-tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-520 Expected d menyebut tabel kembali ke halaman 1 saat kriteria berubah; fixture memuat satu halaman data sehingga perpindahan dari halaman lain tidak dapat dicapai (lihat TC-FA-SU-530 Expected e); spec mengasersi tabel berada di halaman 1.
  - TC-FA-SU-521 Expected c menyebut sort berpindah "tanpa mereset Search dan Filter" tanpa langkah mengembalikan Search yang sudah dikosongkan pada langkah sebelumnya; spec mengaktifkan kembali Search `ASG-2026` sebelum mengganti sort.
