---
id: TC-FA-SU-E2E-463-tab-transaction-admin-log-assignment-pin-dan-unpin-setup-column
title: "Tab Transaction Admin Log Sub-tab Assignment: Pin dan Unpin Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1164
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Pin dan Unpin Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.
- Kemampuan viewport (disediakan tim FE): ukuran viewport browser diatur cukup sempit di hook `before` spec ini supaya tabel memiliki scroll horizontal; langkah `Scroll tabel secara horizontal` bergantung pada kemampuan ini.

## Test Steps

### TC-FA-SU-1164: Pin dan unpin Setup Column kelas Hideable (default tampil)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
3. Klik icon Pin pada kolom `Date`, `Activity`, `Transaction ID`
4. Hover icon Pin pada kolom `Name`
5. Verifikasi icon Pin kolom lain disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` setelah tiga kolom di-pin
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi kolom `Date` membeku di kiri saat tabel di-scroll horizontal
9. Verifikasi kolom `Activity` membeku di kiri saat tabel di-scroll horizontal
10. Verifikasi kolom `Transaction ID` membeku di kiri saat tabel di-scroll horizontal
11. Klik F5
12. Scroll tabel secara horizontal
13. Verifikasi kolom `Date` tetap membeku di kiri setelah refresh (F5)
14. Verifikasi kolom `Activity` tetap membeku di kiri setelah refresh (F5)
15. Verifikasi kolom `Transaction ID` tetap membeku di kiri setelah refresh (F5)
16. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
17. Unpin kolom `Date`, `Activity`, `Transaction ID`
18. Klik `[Save]`
19. Scroll tabel secara horizontal
20. Verifikasi kolom `Date` terlepas (tidak membeku) saat tabel di-scroll horizontal
21. Verifikasi kolom `Activity` terlepas (tidak membeku) saat tabel di-scroll horizontal
22. Verifikasi kolom `Transaction ID` terlepas (tidak membeku) saat tabel di-scroll horizontal
23. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
24. Klik icon Pin pada kolom `Name`, `Assignee`, `Group`
25. Klik `[Save]`
26. Scroll tabel secara horizontal
27. Verifikasi kolom `Name` membeku di kiri saat tabel di-scroll horizontal
28. Verifikasi kolom `Assignee` membeku di kiri saat tabel di-scroll horizontal
29. Verifikasi kolom `Group` membeku di kiri saat tabel di-scroll horizontal
30. Klik F5
31. Scroll tabel secara horizontal
32. Verifikasi kolom `Name` tetap membeku di kiri setelah refresh (F5)
33. Verifikasi kolom `Assignee` tetap membeku di kiri setelah refresh (F5)
34. Verifikasi kolom `Group` tetap membeku di kiri setelah refresh (F5)
35. Buka Setup Column: klik header kolom `⋯`, lalu klik item `Setup Column...`
36. Unpin kolom `Name`, `Assignee`, `Group`
37. Klik `[Save]`
38. Scroll tabel secara horizontal
39. Verifikasi kolom `Name` terlepas (tidak membeku) saat tabel di-scroll horizontal
40. Verifikasi kolom `Assignee` terlepas (tidak membeku) saat tabel di-scroll horizontal
41. Verifikasi kolom `Group` terlepas (tidak membeku) saat tabel di-scroll horizontal
42. Hapus preferensi kolom tabel di browser lalu muat ulang halaman (kemampuan disediakan tim FE)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan Setup Column, dan penghapusan preferensi kolom; semuanya hanya mengembalikan state (S-09).
- Pin dikerjakan dalam dua kelompok tiga kolom (`Date`, `Activity`, `Transaction ID` lalu `Name`, `Assignee`, `Group`) sesuai Langkah Uji nomor 3 TC-FA-SU-1164 dan batas tiga kolom Pin (butir g).
- Pembagian TC lintas spec: ceklis ada di spec 461; geser kolom dan Reset to Default ada di spec 462.
- Temuan untuk QA (S-15): (1) Tooltip icon Pin yang disabled diasersi pada kelompok pertama sesudah tiga kolom di-pin. (2) TC tidak menyebut cara men-scroll horizontal; skrip uji menentukan. (3) Post Condition preferensi kolom tersimpan per perangkat tidak punya langkah observasi dan tidak diasersi.
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
