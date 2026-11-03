---
id: TC-FA-SU-E2E-275-tab-transaction-admin-log-pin-dan-unpin-setup-column
title: "Tab Transaction Admin Log: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-787
coverage:
  web: automated
---

# Tab Transaction Admin Log: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan viewport (disediakan tim FE): ukuran viewport browser diatur cukup sempit di hook `before` spec ini supaya tabel memiliki scroll horizontal; langkah `Scroll tabel secara horizontal` bergantung pada kemampuan ini.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment

### TC-FA-SU-787: Pin dan unpin Setup Column kelas Hideable (default tampil)

2. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Klik icon Pin pada kolom `Transaction ID`, `Group`, `Role`
4. Hover icon Pin pada kolom `Action Taken`
5. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` setelah tiga kolom di-pin
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi kolom `Transaction ID` membeku di kiri saat tabel di-scroll horizontal
9. Verifikasi kolom `Group` membeku di kiri saat tabel di-scroll horizontal
10. Verifikasi kolom `Role` membeku di kiri saat tabel di-scroll horizontal
11. Klik F5
12. Scroll tabel secara horizontal
13. Verifikasi kolom `Transaction ID` tetap membeku di kiri setelah refresh (F5)
14. Verifikasi kolom `Group` tetap membeku di kiri setelah refresh (F5)
15. Verifikasi kolom `Role` tetap membeku di kiri setelah refresh (F5)
16. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
17. Unpin kolom `Transaction ID`, `Group`, `Role`
18. Klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi kolom `Transaction ID` terlepas (tidak membeku) saat tabel di-scroll horizontal
21. Verifikasi kolom `Group` terlepas (tidak membeku) saat tabel di-scroll horizontal
22. Verifikasi kolom `Role` terlepas (tidak membeku) saat tabel di-scroll horizontal
23. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
24. Klik icon Pin pada kolom `Action Taken`, `Date`, `Transaction Status`
25. Klik `[Save]`
26. Scroll tabel secara horizontal
27. Verifikasi kolom `Action Taken` membeku di kiri saat tabel di-scroll horizontal
28. Verifikasi kolom `Date` membeku di kiri saat tabel di-scroll horizontal
29. Verifikasi kolom `Transaction Status` membeku di kiri saat tabel di-scroll horizontal
30. Klik F5
31. Scroll tabel secara horizontal
32. Verifikasi kolom `Action Taken` tetap membeku di kiri setelah refresh (F5)
33. Verifikasi kolom `Date` tetap membeku di kiri setelah refresh (F5)
34. Verifikasi kolom `Transaction Status` tetap membeku di kiri setelah refresh (F5)
35. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
36. Unpin kolom `Action Taken`, `Date`, `Transaction Status`
37. Klik `[Save]`
38. Scroll tabel secara horizontal
39. Verifikasi kolom `Action Taken` terlepas (tidak membeku) saat tabel di-scroll horizontal
40. Verifikasi kolom `Date` terlepas (tidak membeku) saat tabel di-scroll horizontal
41. Verifikasi kolom `Transaction Status` terlepas (tidak membeku) saat tabel di-scroll horizontal
42. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16) dan penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Pin dikerjakan dalam dua kelompok tiga kolom (`Transaction ID`, `Group`, `Role` lalu `Action Taken`, `Date`, `Transaction Status`) karena batas tiga kolom Pin (butir g TC-FA-SU-787); TC memerintahkan Pin pada semua enam kolom sekaligus yang bertentangan dengan butir g.
- Pembagian TC lintas spec: TC-FA-SU-785, 786, dan 788 ada di spec 259 dan 260.
- Temuan untuk QA (S-15): (1) TC-FA-SU-787 Langkah Uji nomor 3 memerintahkan Pin pada keenam kolom, sedangkan butir g menyatakan hanya tiga kolom dapat di-pin; spec memakai dua kelompok. (2) Tooltip icon Pin yang disabled diasersi pada kelompok pertama sesudah tiga kolom di-pin. (3) TC tidak menyebut cara men-scroll horizontal; skrip uji menentukan. (4) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
