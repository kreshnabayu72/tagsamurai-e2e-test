---
id: TC-FA-SU-E2E-234-modal-combined-changelog-user-sort
title: "Modal Combined Changelog: User: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-711
  - TC-FA-SU-712
  - TC-FA-SU-713
coverage:
  web: automated
---

# Modal Combined Changelog: User: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Changelog (#27). Modal Combined Changelog dibuka dari icon Changelog di Table Tools halaman User List dan memuat riwayat seluruh pengguna Client `FaUserMain`. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Modal Combined Changelog (Pre-setup #27, 6 baris; urutan default Date descending). Alias baris yang dipakai langkah (Action | User Name | Field; Modified By dalam format `[First Name] [Last Initial]`):
  - C-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`; Modified By `Ahmad D`
  - C-2: `Deactivate` | `Doni Prasetyo` | `Status`; Modified By `Budi S`
  - C-3: `Edit Home Group` | `Budi Santoso` | `Home Group`; Modified By `Lina M`
  - C-4: `Edit` | `Gita Permata` | `Manage group — Finance & Accounting — Update`; Modified By `Ahmad D`
  - C-5: `Assign` | `Budi Santoso` | `Manage accounting`; Modified By `Ahmad D`
  - C-6: `Activate` | `Eka Wulandari` | `Status`; Modified By `Ahmad D`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Combined Changelog dan tidak menambah entri.

## Test Steps

### TC-FA-SU-711: Sort kelas teks (Action, User Name, Field)

1. Klik icon Changelog di Table Tools halaman User List
2. Klik header Action satu kali
3. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-6, C-5, C-2, C-4, C-3
4. Klik header Action kedua kali
5. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-1, C-3, C-4, C-2, C-5
6. Klik header Action ketiga kali
7. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5
8. Klik header User Name satu kali
9. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-3, C-5, C-2, C-6, C-4
10. Klik header User Name kedua kali
11. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-1, C-4, C-6, C-2, C-3
12. Klik header User Name ketiga kali
13. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5
14. Klik header Field satu kali
15. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-1, C-3, C-5, C-4, C-2
16. Klik header Field kedua kali
17. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-2, C-6, C-4, C-5, C-3
18. Klik header Field ketiga kali
19. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5

### TC-FA-SU-712: Sort kelas mixed (Old Value, New Value)

20. Klik header Old Value satu kali
21. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-2, C-4, C-6, C-3, C-1
22. Klik header Old Value kedua kali
23. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-1, C-5, C-3, C-4, C-6
24. Klik header Old Value ketiga kali
25. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5
26. Klik header New Value satu kali
27. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-4, C-6, C-5, C-3, C-1
28. Klik header New Value kedua kali
29. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-2, C-1, C-3, C-5, C-4
30. Klik header New Value ketiga kali
31. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5

### TC-FA-SU-713: Sort kelas user (Modified By)

32. Klik header Modified By satu kali
33. Verifikasi urutan relatif baris seed klik 1 ascending (↑), baris non-seed boleh menyisip: C-1, C-4, C-5, C-6, C-2
34. Klik header Modified By kedua kali
35. Verifikasi urutan relatif baris seed klik 2 descending (↓), baris non-seed boleh menyisip: C-3, C-2, C-1, C-4, C-5
36. Klik header Modified By ketiga kali
37. Verifikasi urutan relatif baris seed klik 3 netral kembali ke default, baris non-seed boleh menyisip: C-1, C-2, C-3, C-4, C-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). Modal Combined Changelog memuat riwayat seluruh pengguna Client, sehingga entri dari spec lain (Activate, Deactivate, Resend, Edit Home Group) menambah baris di surface ini; TC tidak menyatakan cara menjaga isi keenam baris seed selain penyediaan ulang seed.
