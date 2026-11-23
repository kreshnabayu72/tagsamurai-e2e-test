---
id: TC-FA-SU-E2E-456-tab-transaction-admin-log-assignment-search-activity-group-dan-siklus-interaksi
title: "Tab Transaction Admin Log Sub-tab Assignment: Search Activity, Group, dan Siklus Interaksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1143
  - TC-FA-SU-1144
  - TC-FA-SU-1145
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Search Activity, Group, dan Siklus Interaksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

### TC-FA-SU-1143: Search kelas teks, kolom Activity (nama peristiwa node)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik icon Search
3. Ketik Search `Rejected`, tekan Enter
4. Verifikasi tabel menyisakan `ASG-20260715-0068` (1 baris, Activity `Rejected`)
5. Kosongkan isi kotak search, tekan Enter
6. Ketik Search `Handed over`, tekan Enter
7. Verifikasi tabel menyisakan `ASG-20260720-0071` (1 baris, Activity `Handed over`)
8. Kosongkan isi kotak search, tekan Enter
9. Ketik Search `Approved`, tekan Enter
10. Verifikasi tabel menyisakan `ASG-20260719-0070` (1 baris, Activity `Approved`)
11. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1144: Search kelas badge, kolom Group

12. Ketik Search `Surabaya`, tekan Enter
13. Verifikasi tabel menyisakan `ASG-20260720-0071` (1 baris, Group `Branch Surabaya`)
14. Kosongkan isi kotak search, tekan Enter
15. Klik `←` pada kotak Search

### TC-FA-SU-1145: Siklus interaksi Search: reveal, Enter, clear, collapse

16. Hover icon Search
17. Verifikasi tooltip `Search` tampil
18. Klik icon Search
19. Verifikasi input Search melebar
20. Verifikasi kursor fokus di input Search
21. Verifikasi placeholder Search `Search activity, transaction ID, asset, or assignee...` tampil
22. Ketik 1 karakter dari `0071` (`0`)
23. Verifikasi icon `✕` tampil di kanan input
24. Verifikasi tabel belum tersaring dan menampilkan keempat baris
25. Ketik sisa `071`, tekan Enter
26. Verifikasi tabel tersaring menjadi `ASG-20260720-0071`
27. Klik `✕`
28. Verifikasi input Search kosong
29. Verifikasi search bar tetap terbuka
30. Verifikasi kursor fokus di input Search
31. Verifikasi tabel tetap menampilkan hasil search terakhir (`ASG-20260720-0071`)
32. Tekan Enter pada input kosong
33. Verifikasi tabel kembali ke semua baris (empat baris)
34. Ketik Search `0071`, tekan Enter
35. Klik `←` pada kotak Search
36. Verifikasi search bar menutup
37. Verifikasi tabel langsung kembali ke semua baris (empat baris)
38. Klik icon Search
39. Verifikasi keyword dikosongkan (input kosong)
40. Ketik Search `  0071  ` (spasi awal dan akhir), tekan Enter
41. Verifikasi hasil sama dengan `0071` tanpa spasi (`ASG-20260720-0071`)
42. Verifikasi isi input tidak berubah (`  0071  ` dengan spasi awal dan akhir)
43. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan, penutupan, dan pengosongan input Search; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pembagian TC lintas spec: Search kolom Transaction ID, Name, dan Assignee (TC-FA-SU-1140) dicakup spec lain pada suite ini (id TC-nya ada di `sourceTc` spec itu); guard Search dan Sort ada di spec 457.
- Urutan baris pada langkah dengan keempat baris mengikuti default sort Date descending (Pre-setup #29).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1143 langkah 3 sampai 5 menyebut tiga keyword berurutan dengan satu langkah "kosongkan input" di akhir; spec mengosongkan input sesudah tiap keyword. (2) TC-FA-SU-1145 butir a menyebut "tooltip hover icon `Search`" tanpa menyebut kapan; spec menaruhnya sebelum klik karena tooltip dibaca saat hover. (3) TC-FA-SU-1145 langkah 3 menyebut "1 karakter dari `0071`"; spec memakai `0`. (4) Post Condition tidak ada.
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
