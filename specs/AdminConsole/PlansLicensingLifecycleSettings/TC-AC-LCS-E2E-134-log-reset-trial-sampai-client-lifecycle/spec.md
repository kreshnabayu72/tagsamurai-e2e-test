---
id: TC-AC-LCS-E2E-134-log-reset-trial-sampai-client-lifecycle
title: "Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-485
  - TC-AC-LCS-486
  - TC-AC-LCS-487
  - TC-AC-LCS-488
coverage:
  web: automated
---

# Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle

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

### TC-AC-LCS-485: Reset to Default tab Trial Settings menulis entri Edit per field yang berubah ke default pada tiga surface log

1. Atur lewat Fixture BE: tab `Trial Settings` tersimpan dengan nilai non-default (Max Trial Duration 45, Max Trial Asset Quota 100, Max Trial Concurrent User Quota 20, Require Approval for Trial Activation ON, First Notification 14, Second Notification 3) dan Changelog tab `Trial Settings` berisi tepat 1 entri (Edit Max Trial Duration 30 menjadi 45), lalu muat ulang halaman Lifecycle Settings
2. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
3. Klik `[Reset to Default]`
4. Verifikasi toast sukses "Success, trial settings have been reset to default." tampil
5. Klik icon Changelog di pojok kanan atas panel tab `Trial Settings`
6. Verifikasi footer modal Changelog menampilkan `1–7 of 7` (1 entri seed ditambah 6 baris baru)
7. Verifikasi 6 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Max Trial Duration`, Old Value `45`, New Value `30`; Field `Max Trial Asset Quota`, Old Value `100`, New Value `50`; Field `Max Trial Concurrent User Quota`, Old Value `20`, New Value `10`; Field `Require Approval for Trial Activation`, Old Value `On`, New Value `Off`; Field `First Notification`, Old Value `14`, New Value `7`; Field `Second Notification`, Old Value `3`, New Value `1`
8. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
9. Verifikasi 6 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 6 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
10. Buka Activity Log (Admin Console)
11. Verifikasi 6 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`
12. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-486: Reset to Default tab Free Plan Settings menulis entri Edit per field yang berubah ke default pada tiga surface log

13. Atur lewat Fixture BE: tab `Free Plan Settings` tersimpan dengan nilai non-default (Free Plan Duration 400) dan Changelog tab `Free Plan Settings` berisi tepat 1 entri (Edit Free Plan Duration 365 menjadi 400), lalu muat ulang halaman Lifecycle Settings
14. Klik tab `Free Plan Settings`
15. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
16. Klik `[Reset to Default]`
17. Verifikasi toast sukses "Success, free plan settings have been reset to default." tampil
18. Klik icon Changelog di pojok kanan atas panel tab `Free Plan Settings`
19. Verifikasi footer modal Changelog menampilkan `1–2 of 2` (1 entri seed ditambah 1 baris baru)
20. Verifikasi 1 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Free Plan Duration`, Old Value `400`, New Value `365`
21. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
22. Verifikasi 1 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 1 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
23. Buka Activity Log (Admin Console)
24. Verifikasi 1 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`
25. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-487: Reset to Default tab License Timing menulis entri Edit per field yang berubah ke default pada tiga surface log

26. Atur lewat Fixture BE: tab `License Timing` tersimpan dengan nilai non-default (Managed Transition Time 48, Managed Action Retry Delay 5, Addon Reactivation Delay 7) dan Changelog tab `License Timing` berisi tepat 1 entri (Edit Managed Transition Time 24 menjadi 48), lalu muat ulang halaman Lifecycle Settings
27. Klik tab `License Timing`
28. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
29. Klik `[Reset to Default]`
30. Verifikasi toast sukses "Success, license timing settings have been reset to default." tampil
31. Klik icon Changelog di pojok kanan atas panel tab `License Timing`
32. Verifikasi footer modal Changelog menampilkan `1–4 of 4` (1 entri seed ditambah 3 baris baru)
33. Verifikasi 3 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Managed Transition Time`, Old Value `48`, New Value `24`; Field `Managed Action Retry Delay`, Old Value `5`, New Value `2`; Field `Addon Reactivation Delay`, Old Value `7`, New Value `2`
34. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
35. Verifikasi 3 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 3 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
36. Buka Activity Log (Admin Console)
37. Verifikasi 3 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`
38. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-488: Reset to Default tab Client Lifecycle menulis entri Edit per field yang berubah ke default pada tiga surface log

39. Atur lewat Fixture BE: tab `Client Lifecycle` tersimpan dengan nilai non-default (Notify Plan Owner Before Event 60, First Reminder Before Event 45, Second Reminder Before Event 14, Final Reminder Before Event 3, Grace Period Duration 20, Archive Period Duration 25, Purge Warning Email 12, Purge Urgent Warning Email 4, Post-Purge Retention 1000) dan Changelog tab `Client Lifecycle` berisi tepat 1 entri (Edit Notify Plan Owner Before Event 45 menjadi 60), lalu muat ulang halaman Lifecycle Settings
40. Klik tab `Client Lifecycle`
41. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
42. Klik `[Reset to Default]`
43. Verifikasi toast sukses "Success, client lifecycle settings have been reset to default." tampil
44. Klik icon Changelog di pojok kanan atas panel tab `Client Lifecycle`
45. Verifikasi footer modal Changelog menampilkan `1–10 of 10` (1 entri seed ditambah 9 baris baru)
46. Verifikasi 9 baris baru , seluruhnya Action `Edit` dan Modified By `Andi W`, satu per field yang berubah: Field `Notify Plan Owner Before Event`, Old Value `60`, New Value `45`; Field `First Reminder Before Event`, Old Value `45`, New Value `30`; Field `Second Reminder Before Event`, Old Value `14`, New Value `7`; Field `Final Reminder Before Event`, Old Value `3`, New Value `1`; Field `Grace Period Duration`, Old Value `20`, New Value `30`; Field `Archive Period Duration`, Old Value `25`, New Value `30`; Field `Purge Warning Email`, Old Value `12`, New Value `10`; Field `Purge Urgent Warning Email`, Old Value `4`, New Value `2`; Field `Post-Purge Retention`, Old Value `1000`, New Value `730`
47. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
48. Verifikasi 9 entri baru System Log di atas entri sebelumnya (jumlah entri bertambah 9 dari baseline), masing-masing Action `Edit`, Object `Lifecycle Settings`, Name `—`, dengan Field, Old Value, dan New Value sama seperti baris Changelog, tanpa kolom Modified By
49. Buka Activity Log (Admin Console)
50. Verifikasi 9 entri baru Activity Log dengan isi yang sama seperti System Log dan Modified By `Andi W`

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ... lalu muat ulang" (precondition TC: nilai non-default dan satu entri Changelog), "Klik tab", "Catat jumlah entri ... sebagai baseline" (S-12), dan "Pulihkan ketujuh tab ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (S-03, S-09).
- Satu `Verifikasi` per surface memuat seluruh baris atau entri hasil satu aksi Reset yang disebut utuh pada butir Expected TC (satu baris per field); urutan antar baris dengan waktu sama tidak diasumsikan (S-01).
- Footer Changelog dihitung dari 1 entri seed ditambah baris baru, sesuai precondition TC "Changelog berisi tepat 1 entri" yang diseed spec; bukan total absolut audit trail (S-12).
- Temuan untuk QA: TC tidak menyebut cara membaca jumlah entri System Log dan Activity Log sebelum aksi; spec memakai kemampuan baca yang disediakan tim FE/BE (S-13).
- Temuan untuk QA: Post Condition TC (entri log Edit baru pada ketiga surface) sama dengan Expected butir b sampai d dan tidak diasersi terpisah (S-01).
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (Reset satu tab lalu membaca tiga surface log), semuanya satu kelas pencatatan log, dan tiap blok dimulai dari state yang diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
