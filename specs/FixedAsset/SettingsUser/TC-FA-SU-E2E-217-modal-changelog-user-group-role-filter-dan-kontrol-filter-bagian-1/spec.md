---
id: TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1
title: "Modal Changelog User > Group Role: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-651
  - TC-FA-SU-652
  - TC-FA-SU-653
  - TC-FA-SU-654
coverage:
  web: automated
---

# Modal Changelog User > Group Role: Filter dan Kontrol Filter (Bagian 1)

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
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed Changelog #27 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface Changelog dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-651: Filter kelas date (Date)

1. Buka Detail pengguna Budi Santoso, klik tab Role, klik sub-tab Group Role, lalu klik icon Changelog
2. Klik icon Filter
3. Pilih rentang 12/08/26 sampai 14/08/26 pada Date
4. Klik `[Apply]`
5. Verifikasi rentang inklusif 12/08/26 sampai 14/08/26 menyisakan GR-2, GR-3, GR-4 (3 baris)
6. Klik `[Clear Field]` pada field Date, lalu klik `[Apply]`

### TC-FA-SU-652: Filter kelas enum (Action, Field)

7. Buka dropdown Action
8. Verifikasi opsi dropdown = DISTINCT data tabel (`Assign`, `Edit`, `Remove`)
9. Centang `Assign`
10. Klik `[Apply]`
11. Verifikasi memilih `Assign` menyisakan GR-2 (1 baris)
12. Verifikasi chip `Assign` tampil di dalam field Action
13. Klik `[Clear Field]` pada field Action, lalu klik `[Apply]`
14. Buka dropdown Field
15. Verifikasi opsi dropdown = DISTINCT data tabel (`Group Manager — IT Infrastructure`, `Manage files — Branch Surabaya`, `Manage files — IT Infrastructure`, `Manage group — IT Infrastructure — Update`)
16. Centang `Group Manager — IT Infrastructure`
17. Klik `[Apply]`
18. Verifikasi memilih `Group Manager — IT Infrastructure` menyisakan GR-3 (1 baris)
19. Verifikasi chip `Group Manager — IT Infrastructure` tampil di dalam field Field

### TC-FA-SU-653: Filter kelas fk (Modified By)

20. Klik `[Clear Field]` pada field Field, lalu klik `[Apply]`
21. Buka dropdown Modified By
22. Verifikasi opsi dropdown = DISTINCT data tabel (`Ahmad D`, `Lina M`)
23. Centang `Ahmad D`
24. Klik `[Apply]`
25. Verifikasi memilih `Ahmad D` menyisakan GR-2, GR-3, GR-4 (3 baris)
26. Verifikasi chip `Ahmad D` tampil di dalam field Modified By

### TC-FA-SU-654: Kombinasi Search dan Filter dua arah

27. Klik `[Clear Field]` pada field Modified By, lalu klik `[Apply]`, lalu tutup Filter Panel dengan klik icon Filter
28. Ketik Search `Assign`, tekan Enter
29. Klik icon Filter
30. Buka dropdown Action, centang `Assign`
31. Klik `[Apply]`
32. Verifikasi Search `Assign` lalu Filter Action `Assign`: hasil irisan GR-2 (1 baris)
33. Verifikasi keyword Search `Assign` tidak dikosongkan oleh Filter
34. Klik `[Clear Field]` lalu `[Apply]`, lalu klik `(←)` pada kotak Search
35. Buka dropdown Action, centang `Assign`
36. Klik `[Apply]`
37. Ketik Search `Assign`, tekan Enter
38. Verifikasi Filter Action `Assign` lalu Search `Assign`: hasil identik, hasil irisan GR-2 (1 baris)
39. Verifikasi Filter Action `Assign` tidak direset oleh Search
40. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Spec ini berjumlah 40 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #27 yang disediakan ulang di hook `before` dan `after` (S-14). (2) Tanggal baris seed Changelog (Pre-setup #27) tidak tertulis di Tabel Pre-setup; asersi yang memakai nilai atau rentang Date (12/08/26 sampai 14/08/26) mengikuti angka di TC dan bergantung pada seed yang disediakan tim FE/BE. (3) Filter Action `Assign` hanya menyisakan 1 baris (TC-FA-SU-652) sedangkan Search `Assign` menyisakan 3 baris (TC-FA-SU-640); selisih ini konsisten hanya bila Search juga mencocokkan kolom lain (mis. New Value `Assigned`, TC-FA-SU-641). Label "kolom Action" pada TC-FA-SU-640 menyiratkan pencocokan kolom Action saja. Spec mengikuti angka TC. (4) TC tidak menyebut status Filter Panel (terbuka atau tertutup) sesudah `[Apply]`; spec menutup panel dengan klik icon Filter sebelum mengetik Search pada kombinasi Search lalu Filter, dan membukanya kembali pada langkah berikutnya.
