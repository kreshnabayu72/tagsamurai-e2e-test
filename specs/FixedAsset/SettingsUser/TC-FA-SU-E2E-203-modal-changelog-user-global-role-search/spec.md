---
id: TC-FA-SU-E2E-203-modal-changelog-user-global-role-search
title: "Modal Changelog User > Global Role: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-611
  - TC-FA-SU-612
  - TC-FA-SU-1059
coverage:
  web: automated
---

# Modal Changelog User > Global Role: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Global Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | Role Name | Field; Modified By):
  - G-1: `Remove` | `Manage global license` | `Manage global license`; Modified By `Lina M`
  - G-2: `Remove (via Total Control)` | `Manage global license` | `Access`; Modified By `Ahmad D`
  - G-3: `Assign (via Total Control)` | `Import Data` | `Access`; Modified By `Ahmad D`
  - G-4: `Edit` | `Manage asset master data` | `Manage asset master data — Delete`; Modified By `Ahmad D`
  - G-5: `Assign` | `Manage accounting` | `Manage accounting`; Modified By `Ahmad D`
- Nilai Date seed untuk Search kolom non-searchable (Pre-setup #27, TC-FA-SU-612): baris G-5 `15/07/26, 09:15` (Example Data PRD); nilai ini harus tampil pada sel Date tabel sebelum dipakai sebagai keyword.
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-611: Siklus interaksi Search

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Global Role, lalu klik icon Changelog
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
12. Verifikasi tabel tersaring memuat baris seed G-1, G-2, G-3, G-5 (4 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
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
26. Verifikasi hasil sama dengan `Assign` tanpa spasi: G-1, G-2, G-3, G-5 (4 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
27. Verifikasi isi input tidak berubah

### TC-FA-SU-612: Guard kolom non-searchable Date

28. Kosongkan isi kotak search, tekan Enter
29. Verifikasi sel Date baris G-5 menampilkan `15/07/26, 09:15`
30. Ketik Search `15/07/26, 09:15` (nilai kolom Date), tekan Enter
31. Verifikasi nilai Date tidak mencocokkan baris melalui Search; empty state `No results found` tampil
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1059: Search mencocokkan semua kolom searchable

33. Ketik Search `Edit` (kolom Action), tekan Enter
34. Verifikasi keyword `Edit` menyisakan G-4 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
35. Ganti isi kotak search dengan `Access` (kolom Field), tekan Enter
36. Verifikasi keyword `Access` menyisakan G-2, G-3 (2 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
37. Ganti isi kotak search dengan `Inactive` (kolom Old Value), tekan Enter
38. Verifikasi keyword `Inactive` menyisakan G-4 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
39. Ganti isi kotak search dengan `Marlina` (kolom Modified By), tekan Enter
40. Verifikasi keyword `Marlina` menyisakan G-1 (1 baris seed; baris non-seed yang memenuhi kriteria boleh ikut tampil)
41. Kosongkan isi kotak search, tekan Enter
42. Verifikasi setiap kata kunci hanya ada pada satu kolom searchable sehingga hasilnya membuktikan kolom yang dicari; Search mencocokkan kolom Action, Role Name, Field, Old Value, New Value, dan Modified By sekaligus

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber. TC-FA-SU-611 dan TC-FA-SU-1059 menulis hasil Search tanpa kualifier seed; spec memakai kualifier yang sama seperti TC sibling pada surface ini (Pre-setup butir d TC-FA-SU-614 dan seterusnya), dicatat di Temuan untuk QA.
- Asersi tambahan di luar Expected (S-03): langkah 29 (sel Date baris G-5 tampil) memverifikasi nilai Date seed sebelum dipakai sebagai keyword Search kolom non-searchable (bagian 8b butir 15 b); langkah 28 (mengosongkan Search) adalah langkah penghubung yang mengembalikan tabel penuh agar sel Date terlihat (S-03, S-09).
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) TC-FA-SU-1059 butir e adalah kesimpulan dari butir a sampai d; spec menulisnya sebagai satu `Verifikasi` tersendiri sesuai S-01. (4) TC-FA-SU-611 dan TC-FA-SU-1059 menulis hasil Search sebagai daftar baris tanpa kualifier seed; spec menulisnya sebagai baris seed dengan baris non-seed boleh ikut tampil, seperti TC sibling pada surface yang sama (TC-FA-SU-614 dan seterusnya, Pre-setup butir d), karena audit trail permanen dapat memuat baris non-seed. Mohon pemilik TC mengonfirmasi atau menyamakan kualifier.
