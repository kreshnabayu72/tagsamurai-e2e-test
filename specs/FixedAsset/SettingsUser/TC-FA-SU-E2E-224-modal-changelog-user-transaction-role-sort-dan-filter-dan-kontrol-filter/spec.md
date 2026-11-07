---
id: TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter
title: "Modal Changelog User > Transaction Role: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-679
  - TC-FA-SU-680
  - TC-FA-SU-681
  - TC-FA-SU-682
coverage:
  web: automated
---

# Modal Changelog User > Transaction Role: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Changelog Budi Santoso > Transaction Role (Pre-setup #27, 5 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By):
  - TR-1: `Damaged — Branch Surabaya — Monitoring & Report`; Modified By `Ahmad D`
  - TR-2: `Missing — Branch Surabaya — Approver`; Modified By `Ahmad D`
  - TR-3: `Disposal — Logistics Warehouse — Asset Admin`; Modified By `Lina M`
  - TR-4: `Disposal — Logistics Warehouse — Staff`; Modified By `Lina M`
  - TR-5: `Transfer — Finance & Accounting — Asset Admin`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-679: Sort kelas teks (Action, Field)

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Transaction Role, lalu klik icon Changelog
2. Klik header Action satu kali
3. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: TR-1, TR-3, TR-5, TR-2, TR-4
4. Klik header Action kedua kali
5. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: TR-2, TR-4, TR-1, TR-3, TR-5
6. Klik header Action ketiga kali
7. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: TR-1, TR-2, TR-3, TR-4, TR-5
8. Klik header Field satu kali
9. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: TR-1, TR-3, TR-4, TR-2, TR-5
10. Klik header Field kedua kali
11. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: TR-5, TR-2, TR-4, TR-3, TR-1
12. Klik header Field ketiga kali
13. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: TR-1, TR-2, TR-3, TR-4, TR-5

### TC-FA-SU-680: Sort kelas mixed (Old Value, New Value)

14. Klik header Old Value satu kali
15. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: TR-2, TR-4, TR-1, TR-3, TR-5
16. Klik header Old Value kedua kali
17. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: TR-1, TR-3, TR-5, TR-2, TR-4
18. Klik header Old Value ketiga kali
19. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: TR-1, TR-2, TR-3, TR-4, TR-5
20. Klik header New Value satu kali
21. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: TR-1, TR-3, TR-5, TR-2, TR-4
22. Klik header New Value kedua kali
23. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: TR-2, TR-4, TR-1, TR-3, TR-5
24. Klik header New Value ketiga kali
25. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: TR-1, TR-2, TR-3, TR-4, TR-5

### TC-FA-SU-681: Sort kelas user (Modified By)

26. Klik header Modified By satu kali
27. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: TR-1, TR-2, TR-5, TR-3, TR-4
28. Klik header Modified By kedua kali
29. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: TR-3, TR-4, TR-1, TR-2, TR-5
30. Klik header Modified By ketiga kali
31. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: TR-1, TR-2, TR-3, TR-4, TR-5

### TC-FA-SU-682: Screening Filter Panel

32. Klik icon Filter
33. Verifikasi panel terbuka di bawah Table Tools
34. Verifikasi ikon Filter menjadi gelap
35. Hover icon Filter
36. Verifikasi tooltip `Filter`
37. Verifikasi field ke-1 adalah Date (date range picker) dengan placeholder `Select date`
38. Verifikasi field ke-2 adalah Action (multi-select searchable) dengan placeholder `All actions`
39. Verifikasi field ke-3 adalah Field (multi-select searchable) dengan placeholder `All fields`
40. Verifikasi field ke-4 adalah Modified By (multi-select searchable) dengan placeholder `All users`
41. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
42. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, R-16): Search `Budi Santoso` pada User List menyaring baris target sebelum membuka Detail (langkah 1) karena User List dapat memuat lebih dari satu halaman (bagian 8b butir 13); langkah ini tidak mengubah data dan tidak ada TC berikutnya yang membutuhkan tabel penuh (S-09).
- Asersi baris seed pada Modal Changelog (audit trail permanen) ditulis relatif terhadap baris seed: urutan relatif dan jumlah baris seed, dengan baris non-seed yang memenuhi kriteria boleh menyisip atau ikut tampil (S-14), mengikuti kualifier Expected TC sumber.
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Urutan beberapa sort tidak simetris: Date ascending (TR-5, TR-3, TR-4, TR-2, TR-1) bukan kebalikan urutan default descending (TR-1, TR-2, TR-3, TR-4, TR-5), dan Old Value serta Modified By descending bukan kebalikan ascending. TC tidak menyebut aturan tie-break untuk nilai seri (Date berketelitian menit); spec mengikuti urutan TC dan urutan itu bergantung pada seed yang disediakan tim FE/BE.
