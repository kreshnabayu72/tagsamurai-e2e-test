---
id: TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter
title: "Tab Changelog: Sort dan Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-583
  - TC-FA-SU-584
  - TC-FA-SU-585
  - TC-FA-SU-586
coverage:
  web: automated
---

# Tab Changelog: Sort dan Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab Changelog Budi Santoso (Pre-setup #27, 7 baris; urutan default Date descending). Alias baris yang dipakai langkah (nilai kolom Field; Modified By dalam format `[First Name] [Last Initial]`):
  - T-1: Field `Manage files — IT Infrastructure`, Modified By `Ahmad D`
  - T-2: Field `Manage group — IT Infrastructure — Delete`, Modified By `Ahmad D`
  - T-3: Field `Manage group — IT Infrastructure — Update`, Modified By `Ahmad D`
  - T-4: Field `Home Group`, Modified By `Lina M`
  - T-5: Field `Manage asset master data — Delete`, Modified By `Ahmad D`
  - T-6: Field `Manage accounting`, Modified By `Ahmad D`
  - T-7: Field `Status`, Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-583: Sort kelas teks (Action, Field)

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab Changelog
3. Klik header Action satu kali
4. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-7, T-1, T-6, T-2, T-3
5. Klik header Action kedua kali
6. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-4, T-2, T-3, T-5, T-1
7. Klik header Action ketiga kali
8. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5
9. Klik header Field satu kali
10. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-4, T-6, T-5, T-1, T-2
11. Klik header Field kedua kali
12. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-7, T-3, T-2, T-1, T-5
13. Klik header Field ketiga kali
14. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5

### TC-FA-SU-584: Sort kelas mixed (Old Value, New Value)

15. Klik header Old Value satu kali
16. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-2, T-3, T-5, T-7, T-4
17. Klik header Old Value kedua kali
18. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-1, T-6, T-4, T-5, T-7
19. Klik header Old Value ketiga kali
20. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5
21. Klik header New Value satu kali
22. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-5, T-7, T-1, T-6, T-4
23. Klik header New Value kedua kali
24. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-2, T-3, T-4, T-1, T-6
25. Klik header New Value ketiga kali
26. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5

### TC-FA-SU-585: Sort kelas user (Modified By)

27. Klik header Modified By satu kali
28. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: T-1, T-2, T-3, T-5, T-6
29. Klik header Modified By kedua kali
30. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: T-4, T-1, T-2, T-3, T-5
31. Klik header Modified By ketiga kali
32. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: T-1, T-2, T-3, T-4, T-5

### TC-FA-SU-586: Screening Filter Panel

33. Klik icon Filter
34. Verifikasi panel terbuka di bawah Table Tools
35. Verifikasi ikon Filter menjadi gelap
36. Hover icon Filter
37. Verifikasi tooltip `Filter`
38. Verifikasi field ke-1 adalah Date (date range picker) dengan placeholder `Select date`
39. Verifikasi field ke-2 adalah Action (multi-select searchable) dengan placeholder `All actions`
40. Verifikasi field ke-3 adalah Field (multi-select searchable) dengan placeholder `All fields`
41. Verifikasi field ke-4 adalah Modified By (multi-select searchable) dengan placeholder `All users`
42. Verifikasi footer panel: `[Clear Field]` di kiri dan `[Apply]` di kanan
43. Verifikasi tidak ada badge titik pada ikon Filter selama belum ada filter ter-Apply

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung tambahan (S-03): langkah 1 (Ketik Search `Budi Santoso`, tekan Enter sebelum membuka Detail, supaya spec tidak mengandalkan posisi baris pada User List 25 pengguna 3 halaman, R-16, bagian 8b butir 13).
- Spec ini berjumlah 43 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14).
