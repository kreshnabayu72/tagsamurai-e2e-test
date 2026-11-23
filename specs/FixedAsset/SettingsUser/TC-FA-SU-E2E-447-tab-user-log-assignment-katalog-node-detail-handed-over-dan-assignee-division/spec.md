---
id: TC-FA-SU-E2E-447-tab-user-log-assignment-katalog-node-detail-handed-over-dan-assignee-division
title: "Tab User Log Sub-tab Assignment: Katalog Node, Detail Handed over, dan Assignee Division"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1129
  - TC-FA-SU-1130
  - TC-FA-SU-1131
coverage:
  web: automated
---

# Tab User Log Sub-tab Assignment: Katalog Node, Detail Handed over, dan Assignee Division

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca, tidak ada yang ditulis atau diubah, S-06): Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Assignment memuat 10 baris (3 baris Assignee Division General Affairs dengan Budi Santoso sebagai PIC, 7 baris Assignee Employee). Transaksi yang dibaca: `ASG-20260625-0102` (baris `Requested`, `Approved`, `Handed over`), `ASG-20260512-0067` (baris `Requested`, `Handed over`, `Damage reported`), dan `ASG-20260618-0089` (Assignee Division General Affairs; baris `Requested`, `Handed over`, `Unassigned`). Baris `Rejected` dibaca dari baris Pre-setup #30 yang memuat Activity itu. Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis: hover pada sel tabel untuk membaca tooltip nama lengkap (langkah 37 dan 38); tidak ada intercept, jam server, atau klien HTTP.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah, tidak ada pemulihan; state Search dan Filter dikosongkan oleh langkah penghubung. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1129: Tab User Log sub-tab Assignment: satu baris per peristiwa katalog node tanpa batas dua baris per transaksi

1. Ketik Search `Budi Santoso`, tekan Enter, klik nama Budi Santoso, buka Tab User Log, lalu klik Sub-tab Assignment
2. Ketik Search `ASG-20260625-0102`, tekan Enter
3. Verifikasi `ASG-20260625-0102` menghasilkan tiga baris: `Requested|ASG-20260625-0102`, `Approved|ASG-20260625-0102`, dan `Handed over|ASG-20260625-0102`
4. Verifikasi jumlah baris `ASG-20260625-0102` tiga, tidak dibatasi dua baris per transaksi
5. Ganti isi kotak search dengan `ASG-20260512-0067`, tekan Enter
6. Verifikasi `ASG-20260512-0067` menghasilkan tiga baris: `Requested|ASG-20260512-0067`, `Handed over|ASG-20260512-0067`, dan `Damage reported|ASG-20260512-0067`
7. Verifikasi Activity tampil sebagai teks biasa, bukan badge berwarna
8. Klik `(←)` pada kotak Search
9. Klik icon Filter
10. Buka dropdown Activity
11. Verifikasi opsi dropdown Activity = DISTINCT data tabel: `Approved`, `Damage reported`, `Handed over`, `Rejected`, `Requested`, `Unassigned`, seluruhnya nama node katalog `assignment.md` §8.1
12. Verifikasi tidak ada opsi `Assigned`
13. Tutup dropdown Activity lalu klik icon Filter untuk menutup Filter Panel

### TC-FA-SU-1130: Tab User Log sub-tab Assignment: Description baris Handed over memuat detail akseptasi (cara, penerima, waktu, Statement)

14. Ketik Search `ASG-20260625-0102`, tekan Enter
15. Verifikasi Description `Handed over|ASG-20260625-0102` memuat `Handed over by Ahmad D`
16. Verifikasi Description `Handed over|ASG-20260625-0102` memuat `Acceptance: Signed on admin device by Budi S, 27/06/26 10:05`
17. Verifikasi Description `Handed over|ASG-20260625-0102` memuat Statement `I acknowledge receipt of these assets and accept responsibility for them.`
18. Verifikasi Description baris `Approved|ASG-20260625-0102` memuat approver
19. Verifikasi Description baris `Approved|ASG-20260625-0102` memuat `Mode: Any one`
20. Ganti isi kotak search dengan `ASG-20260618-0089`, tekan Enter
21. Verifikasi Description `Handed over|ASG-20260618-0089` memuat `Acceptance: Accepted on phone by Budi S, 19/06/26 09:30`
22. Verifikasi Description `Handed over|ASG-20260618-0089` memuat Statement varian Division `I acknowledge receipt of these assets on behalf of General Affairs and accept responsibility for them.`
23. Ganti isi kotak search dengan `ASG-20260512-0067`, tekan Enter
24. Verifikasi Description `Handed over|ASG-20260512-0067` memuat `Acceptance: Not required`
25. Verifikasi Description `Handed over|ASG-20260512-0067` tanpa Statement
26. Verifikasi Description baris `Damage reported|ASG-20260512-0067` memuat pelapor
27. Verifikasi Description baris `Damage reported|ASG-20260512-0067` memuat deskripsi kerusakan
28. Ganti isi kotak search dengan `Rejected`, tekan Enter
29. Verifikasi Description baris `Rejected` memuat approver
30. Verifikasi Description baris `Rejected` memuat `Reason: Budget not approved`
31. Klik `(←)` pada kotak Search

### TC-FA-SU-1131: Tab User Log sub-tab Assignment: Assignee Division tercatat di User log PIC dengan penanda `on behalf of [Division]`, PIC kosong untuk Assignee Employee

32. Ketik Search `ASG-20260618-0089`, tekan Enter
33. Verifikasi `ASG-20260618-0089` menghasilkan tiga baris di User log Budi Santoso: `Requested|ASG-20260618-0089`, `Handed over|ASG-20260618-0089`, dan `Unassigned|ASG-20260618-0089`
34. Verifikasi Description ketiga baris `ASG-20260618-0089` memuat `on behalf of General Affairs`
35. Verifikasi jumlah baris `ASG-20260618-0089` tiga, tidak dibatasi dua baris per transaksi
36. Verifikasi kolom PIC pada baris `ASG-20260618-0089` tampil `Budi S`
37. Hover sel PIC pada baris `ASG-20260618-0089`
38. Verifikasi hover menampilkan nama lengkap `Budi Santoso`
39. Ganti isi kotak search dengan `ASG-20260625-0102`, tekan Enter
40. Verifikasi kolom PIC baris Assignee Employee `ASG-20260625-0102` menampilkan `—`
41. Verifikasi Description baris `ASG-20260625-0102` tanpa penanda `on behalf of`
42. Ganti isi kotak search dengan `ASG-20260512-0067`, tekan Enter
43. Verifikasi kolom PIC baris Assignee Employee `ASG-20260512-0067` menampilkan `—`
44. Verifikasi Description baris `ASG-20260512-0067` tanpa penanda `on behalf of`
45. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1, 8, 9, 10, 13, 31, 45 (membuka Detail, mengosongkan Search, membuka dan menutup Filter Panel dan dropdown). Search `ASG-...` pada langkah 2, 5, 14, 20, 23, 32, 39, 42 dan Search `Rejected` (langkah 28) adalah langkah penghubung untuk menemukan baris target (R-16, 8b butir 13); langkah 1 juga Search nama pengguna target.
- Opsi dropdown Activity (langkah 11 dan 12) adalah daftar per pengguna yang kecil dan diasersi sebagai "opsi = DISTINCT data tabel", sehingga dikecualikan dari keharusan mengetik di kotak cari dropdown (8b butir 15c). Absence `Assigned` (langkah 12) ditulis saat dropdown masih terbuka dan didahului `Verifikasi` daftar opsi yang tampil (langkah 11, 8b butir 2 dan 5).
- Absence Statement (langkah 25) dan penanda `on behalf of` (langkah 41 dan 44) didahului `Verifikasi` isi Description atau kolom PIC baris yang sama (langkah 24, 40, dan 43), sehingga hasil kosong bukan karena baris belum dimuat.
- Spec ini 45 langkah, di atas sekitar 35 langkah. Alasan: ketiga TC berkelas sama (fungsional baca), memakai surface yang sama (Tab User Log sub-tab Assignment Budi Santoso) dan seed Pre-setup #30 yang sama, tanpa mengubah data; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), terutama Description tiap baris `Handed over`, `Approved`, `Rejected`, dan `Damage reported`, bukan dari langkah tambahan.
- Temuan untuk QA (S-15):
  - Kolom ACC ketiga TC menyebut `#20`, yaitu Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, #1).
  - TC-FA-SU-1131 langkah 1 menyebut Budi Santoso sebagai PIC transaksi `ASG-20260618-0089` atas nama General Affairs dan bergantung pada Pre-setup #30 (Assignment 10 baris); bila seed #30 tidak memuat baris itu, langkah 32 sampai 38 tidak dapat dijalankan.
  - TC-FA-SU-1130 butir d tidak menyebut transaksi baris `Approved` dan `Rejected`, nama approver, dan nama pelapor; spec mengasersi baris `Approved` pada `ASG-20260625-0102`, baris `Rejected` lewat Search `Rejected`, dan hanya keberadaan approver atau pelapor, bukan nama tertentu.
  - TC-FA-SU-1129 butir a menyebut "tiga baris" per transaksi tetapi tidak mengunci jumlah total baris sub-tab; spec mengasersi jumlah baris per transaksi lewat Search.
  - TC-FA-SU-1129 dan TC-FA-SU-1131 menulis "amati baris transaksi" tanpa menyebut Search; Search ditambahkan sebagai langkah penghubung agar baris target tidak bergantung posisi halaman.
