---
id: TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort
title: "Modal Changelog User > Group Role: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-643
  - TC-FA-SU-644
  - TC-FA-SU-645
  - TC-FA-SU-646
coverage:
  web: automated
---

# Modal Changelog User > Group Role: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Group Role (Pre-setup #27, 4 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - GR-1: `Manage files — Branch Surabaya`; Modified By `Lina M`
  - GR-2: `Manage files — IT Infrastructure`; Modified By `Ahmad D`
  - GR-3: `Group Manager — IT Infrastructure`; Modified By `Ahmad D`
  - GR-4: `Manage group — IT Infrastructure — Update`; Modified By `Ahmad D`
- Nilai Date seed untuk Search kolom non-searchable (Pre-setup #27, TC-FA-SU-644): `12/08/26, 11:40`; nilai ini harus tampil pada sel Date tabel sebelum dipakai sebagai keyword.
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-643: Siklus interaksi Search

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Group Role, lalu klik icon Changelog
2. Klik icon Search
3. Verifikasi input melebar
4. Verifikasi kursor fokus di input
5. Verifikasi placeholder `Search action, role, field, or value...`
6. Hover icon Search
7. Verifikasi tooltip `Search`
8. Ketik 1 karakter dari `Assign` (`A`)
9. Verifikasi icon ✕ tampil di kanan input
10. Verifikasi tabel belum tersaring
11. Ketik sisa `Assign` (`ssign`) lalu tekan Enter
12. Verifikasi tabel tersaring menjadi GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
13. Klik ✕
14. Verifikasi input kosong
15. Verifikasi search bar tetap terbuka
16. Verifikasi kursor fokus di input
17. Verifikasi tabel tetap menampilkan hasil search terakhir
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali ke semua baris
20. Ketik `Assign`, tekan Enter, lalu klik icon ←
21. Verifikasi search bar menutup
22. Verifikasi keyword dikosongkan
23. Verifikasi tabel langsung kembali ke semua baris
24. Klik icon Search
25. Ketik `  Assign  ` (spasi awal dan akhir), tekan Enter
26. Verifikasi hasil sama dengan `Assign` tanpa spasi (GR-1, GR-2, GR-3; 3 baris seed, baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Verifikasi isi input tidak berubah

### TC-FA-SU-644: Guard kolom non-searchable Date

28. Klik `(←)` pada kotak Search
29. Verifikasi nilai Date `12/08/26, 11:40` tampil pada sel kolom Date tabel
30. Ketik Search `12/08/26, 11:40` (nilai kolom Date), tekan Enter
31. Verifikasi nilai Date tidak mencocokkan baris melalui Search; empty state `No results found` tampil
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-645: Search terikat visibilitas kolom Action

33. Ketik Search `Assign`, tekan Enter
34. Verifikasi sebelum hide: keyword `Assign` menyisakan GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
35. Klik header Column Visibility (⋯), hilangkan centang Action
36. Ganti isi kotak search dengan `Assign`, tekan Enter
37. Verifikasi setelah kolom Action di-hide: keyword yang sama menyisakan GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
38. Klik header Column Visibility (⋯), centang kembali Action
39. Ganti isi kotak search dengan `Assign`, tekan Enter
40. Verifikasi setelah kolom Action di-unhide: hasil kembali GR-1, GR-2, GR-3 (3 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
41. Klik `(←)` pada kotak Search

### TC-FA-SU-646: Sort kelas date (Date)

42. Klik header Date satu kali
43. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: GR-3, GR-4, GR-2, GR-1
44. Klik header Date kedua kali
45. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: GR-1, GR-2, GR-3, GR-4
46. Klik header Date ketiga kali
47. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: GR-1, GR-2, GR-3, GR-4

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber. Pada blok yang Expected TC-nya tidak memuat kualifier (TC-FA-SU-643, TC-FA-SU-645), spec menambahkan kualifier yang sama karena surface-nya sama.
- Asersi tambahan (S-03): langkah 29 (`Verifikasi` nilai Date `12/08/26, 11:40` tampil pada sel kolom Date) bukan dari Expected TC-FA-SU-644; langkah itu menjadi anchor positif sebelum Search nilai kolom non-searchable Date pada langkah 30 (bagian 8b butir 15 b).
- Spec ini berjumlah 47 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date (12/08/26, 11:40) mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) Filter Action `Assign` hanya menyisakan 1 baris (TC-FA-SU-652) sedangkan Search `Assign` menyisakan 3 baris (TC-FA-SU-640); selisih ini konsisten hanya bila Search juga mencocokkan kolom lain (mis. New Value `Assigned`, TC-FA-SU-641). Label "kolom Action" pada TC-FA-SU-640 menyiratkan pencocokan kolom Action saja. Spec mengikuti angka TC. (4) Urutan beberapa sort tidak simetris: Date ascending (GR-3, GR-4, GR-2, GR-1) bukan kebalikan urutan default descending (GR-1, GR-2, GR-3, GR-4), dan Old Value descending bukan kebalikan ascending. TC tidak menyebut aturan tie-break untuk nilai seri (Date berketelitian menit); spec mengikuti urutan TC dan urutan itu bergantung pada seed yang disediakan tim FE/BE.
