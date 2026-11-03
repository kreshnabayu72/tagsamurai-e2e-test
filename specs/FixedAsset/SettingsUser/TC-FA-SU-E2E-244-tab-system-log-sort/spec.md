---
id: TC-FA-SU-E2E-244-tab-system-log-sort
title: "Tab System Log: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-742
  - TC-FA-SU-743
coverage:
  web: automated
---

# Tab System Log: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-742: Sort kelas teks (Action, Object, Name, Field)

1. Buka Detail pengguna Budi Santoso lalu klik tab System Log
2. Klik header Action satu kali
3. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-7, S-4, S-5, S-6, S-2
4. Klik header Action kedua kali
5. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-1, S-3, S-2, S-4, S-5
6. Klik header Action ketiga kali
7. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5
8. Klik header Object satu kali
9. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-6, S-2, S-3, S-5, S-4
10. Klik header Object kedua kali
11. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-1, S-7, S-4, S-3, S-5
12. Klik header Object ketiga kali
13. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5
14. Klik header Name satu kali
15. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-5, S-6, S-7, S-1, S-4
16. Klik header Name kedua kali
17. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-2, S-3, S-4, S-1, S-5
18. Klik header Name ketiga kali
19. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5
20. Klik header Field satu kali
21. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-4, S-1, S-2, S-6, S-5
22. Klik header Field kedua kali
23. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-7, S-3, S-5, S-6, S-2
24. Klik header Field ketiga kali
25. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5

### TC-FA-SU-743: Sort kelas mixed (Old Value, New Value)

26. Klik header Old Value satu kali
27. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-3, S-2, S-7, S-1, S-4
28. Klik header Old Value kedua kali
29. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-1, S-4, S-5, S-6, S-7
30. Klik header Old Value ketiga kali
31. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5
32. Klik header New Value satu kali
33. Verifikasi urutan lima baris pertama klik 1 ascending (↑): S-7, S-5, S-6, S-1, S-3
34. Klik header New Value kedua kali
35. Verifikasi urutan lima baris pertama klik 2 descending (↓): S-2, S-4, S-3, S-1, S-5
36. Klik header New Value ketiga kali
37. Verifikasi urutan lima baris pertama klik 3 netral kembali ke default: S-1, S-2, S-3, S-4, S-5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 37 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris.
