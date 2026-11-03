---
id: TC-AC-LCS-E2E-135-log-reset-recycle-approval-limits
title: "Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Recycle Bin, Approval Settings, dan System Limits"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-489
  - TC-AC-LCS-490
  - TC-AC-LCS-491
coverage:
  web: automated
---

# Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser tidak digeser.
- Data: user `Andi Wijaya` (Total Control) memiliki Detail user dengan tab System Log. Changelog tab yang diuji diseed lewat Fixture BE dengan tepat 1 entri Edit sebagai precondition TC (dipakai sebagai precondition TC, tidak diasersi selain lewat footer); entri System Log dan Activity Log bersifat permanen sehingga spec memakai baseline jumlah entri sebelum aksi (S-12).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menyimpan nilai non-default per tab, menyeed satu entri Changelog tab, dan memulihkan ketujuh tab ke nilai default; kemampuan membaca jumlah entri System Log aktor dan Activity Log Admin Console sebelum aksi.
- Pemulihan: ketujuh tab dipulihkan ke nilai default oleh langkah penghubung antar TC dan hook `after` suite; entri log yang ditulis spec ini permanen dan tidak dihapus.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-489: Reset to Default tab Recycle Bin menulis entri Edit per field yang berubah ke default pada tiga surface log

1. Atur lewat Fixture BE: tab `Recycle Bin` tersimpan dengan nilai non-default (Permanently Delete Recycle Bin 45) dan Changelog tab `Recycle Bin` berisi tepat 1 entri (Edit Permanently Delete Recycle Bin 30 menjadi 45), lalu muat ulang halaman Lifecycle Settings
2. Klik tab `Recycle Bin`
3. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
4. Klik `[Reset to Default]`
5. Verifikasi toast sukses "Success, recycle bin settings have been reset to default." tampil
6. Klik icon Changelog di pojok kanan atas panel tab `Recycle Bin`
7. Verifikasi footer modal Changelog menampilkan `1–2 of 2` (1 entri seed ditambah 1 baris baru)
8. Verifikasi 1 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Permanently Delete Recycle Bin`, Old Value `45`, New Value `30`
9. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
10. Verifikasi 1 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 1 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
11. Buka Activity Log (Admin Console)
12. Verifikasi 1 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`
13. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-490: Reset to Default tab Approval Settings menulis entri Edit per field yang berubah ke default pada tiga surface log

14. Atur lewat Fixture BE: tab `Approval Settings` tersimpan dengan nilai non-default (Approval Timeout 7) dan Changelog tab `Approval Settings` berisi tepat 1 entri (Edit Approval Timeout 3 menjadi 7), lalu muat ulang halaman Lifecycle Settings
15. Klik tab `Approval Settings`
16. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
17. Klik `[Reset to Default]`
18. Verifikasi toast sukses "Success, approval settings have been reset to default." tampil
19. Klik icon Changelog di pojok kanan atas panel tab `Approval Settings`
20. Verifikasi footer modal Changelog menampilkan `1–2 of 2` (1 entri seed ditambah 1 baris baru)
21. Verifikasi 1 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Approval Timeout`, Old Value `7`, New Value `3`
22. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
23. Verifikasi 1 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 1 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
24. Buka Activity Log (Admin Console)
25. Verifikasi 1 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`
26. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-491: Reset to Default tab System Limits menulis entri Edit per field yang berubah ke default pada tiga surface log

27. Atur lewat Fixture BE: tab `System Limits` tersimpan dengan nilai non-default (Bulk Transaction Row Limit 2000, Selection Limit 1500, Register Asset Bulk Limit 2500, Hierarchy Depth Limit 60, Master Data Count Limit 20000, Max Visible Columns 25) dan Changelog tab `System Limits` berisi tepat 1 entri (Edit Bulk Transaction Row Limit 1000 menjadi 2000), lalu muat ulang halaman Lifecycle Settings
28. Klik tab `System Limits`
29. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
30. Klik `[Reset to Default]`
31. Verifikasi toast sukses "Success, system limits settings have been reset to default." tampil
32. Klik icon Changelog di pojok kanan atas panel tab `System Limits`
33. Verifikasi footer modal Changelog menampilkan `1–7 of 7` (1 entri seed ditambah 6 baris baru)
34. Verifikasi 6 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Bulk Transaction Row Limit`, Old Value `2000`, New Value `1000`; Field `Selection Limit`, Old Value `1500`, New Value `1000`; Field `Register Asset Bulk Limit`, Old Value `2500`, New Value `1000`; Field `Hierarchy Depth Limit`, Old Value `60`, New Value `50`; Field `Master Data Count Limit`, Old Value `20000`, New Value `10000`; Field `Max Visible Columns`, Old Value `25`, New Value `20`
35. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
36. Verifikasi 6 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 6 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
37. Buka Activity Log (Admin Console)
38. Verifikasi 6 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ... lalu muat ulang" (precondition TC: nilai non-default dan satu entri Changelog), "Klik tab", "Catat jumlah entri ... sebagai baseline" (S-12), dan "Pulihkan ketujuh tab ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (S-03, S-09).
- Satu `Verifikasi` per surface memuat seluruh baris atau entri hasil satu aksi Reset yang disebut utuh pada butir Expected TC (satu baris per field); urutan antar baris dengan waktu sama tidak diasumsikan (S-01).
- Footer Changelog dihitung dari 1 entri seed ditambah baris baru, sesuai precondition TC "Changelog berisi tepat 1 entri" yang diseed spec; bukan total absolut audit trail (S-12).
- Temuan untuk QA: TC tidak menyebut cara membaca jumlah entri System Log dan Activity Log sebelum aksi; spec memakai kemampuan baca yang disediakan tim FE/BE (S-13).
- Temuan untuk QA: Post Condition TC (entri log Edit baru pada ketiga surface) sama dengan Expected butir b sampai d dan tidak diasersi terpisah (S-01).
- Alasan lebih dari sekitar 35 langkah: tiga blok memakai pola yang sama (Reset satu tab lalu membaca tiga surface log), semuanya satu kelas pencatatan log, dan tiap blok dimulai dari state yang diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
