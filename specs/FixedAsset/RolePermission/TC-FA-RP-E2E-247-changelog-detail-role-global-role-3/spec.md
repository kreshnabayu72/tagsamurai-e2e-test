---
id: TC-FA-RP-E2E-247-changelog-detail-role-global-role-3
title: "Changelog Detail Role Global Role (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1134
  - TC-FA-RP-1135
  - TC-FA-RP-1136
coverage:
  web: automated
---

# Changelog Detail Role Global Role (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Setiawan), #18 (pohon group), #21 (seed pemegang Update `Manage asset & TAG`: Ahmad Fauzi Create, Read, Update di `Head Office`), #24 (`Company Changelog`), #39 (Detail Role Group Role `Manage files` terisi: Ahmad Fauzi di `Data Center`). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Entri pembanding (8b.2): blok TC-FA-RP-1136 membuat entri Assign dan Remove biasa untuk Budi Setiawan (Group Role `Manage files` di `Helpdesk`) lewat sesi API aktor sebelum Budi Setiawan dijadikan Total Control; entri itu menjadi pembanding di modal Changelog Detail Role `Manage files` dan modal Changelog: User > Group Role Budi Setiawan. Penugasan itu tidak tersisa sesudah dilepas.
- Kemampuan teknis: Membaca modal Changelog, System Log, dan Activity Log lewat UI; waktu aksi dicatat sesudah aksi pemicu. Baseline jumlah entri System Log dan Activity Log dicatat lewat kemampuan baca (disediakan tim FE/BE) sebelum aksi pemicu TC-FA-RP-1134 (S-12). Seeding Group Role Ahmad Fauzi di `Helpdesk` serta status Total Control atau Read Only Ahmad Fauzi dan Budi Setiawan lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Tingkat akses dan Group Role Ahmad Fauzi dan Budi Setiawan diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1134: Changelog Remove Total Control: satu entri Remove (via Total Control) per penugasan Group Role (Role × Group) di Detail Role dan Changelog: User > Group Role, tanpa entri di System Log dan Activity Log

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` dan jumlah entri Object `Group Role`, Name `Ahmad Fauzi` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
3. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
4. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
5. Klik ikon Changelog di toolbar Detail Role
6. Verifikasi Modal memuat entri terbaru Action `Remove (via Total Control)`: Role Name — User — Group Name `Manage files — Ahmad Fauzi — Data Center`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Verifikasi Modal memuat entri terbaru Action `Remove (via Total Control)`: Role Name — User — Group Name `Manage files — Ahmad Fauzi — Helpdesk`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
8. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, buka Detail Role Group Role `Manage asset & TAG`, lalu klik `All Groups`
9. Klik ikon Changelog di toolbar Detail Role
10. Verifikasi Modal memuat satu entri Action `Remove (via Total Control)`: Role Name — User — Group Name `Manage asset & TAG — Ahmad Fauzi — Head Office`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
11. Tutup modal Changelog lalu buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
12. Klik ikon Changelog
13. Verifikasi modal Changelog: User > Group Role memuat tiga entri Action `Remove (via Total Control)` dengan Field `Manage files — Data Center`, `Manage files — Helpdesk`, dan `Manage asset & TAG — Head Office`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`
14. Verifikasi modal Changelog: User > Group Role tidak memuat entri `Assign (via Total Control)` maupun entri `Edit` untuk penugasan itu
15. Tutup modal Changelog lalu buka Settings > User > Detail Siti Rahmawati > Tab System Log
16. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline: Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` (jumlah entri kombinasi ini bertambah tepat satu; anchor: entri milik aksi pemicu yang sama)
17. Verifikasi System Log tidak memuat entri baru Object `Group Role` untuk ketiga penugasan itu (jumlah entri Object `Group Role`, Name `Ahmad Fauzi` sama dengan baseline)
18. Buka Activity Log FAMS (menu Activity Log)
19. Verifikasi Activity Log memuat satu entri baru di atas baseline: Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` (jumlah entri kombinasi ini bertambah tepat satu; anchor: entri milik aksi pemicu yang sama)
20. Verifikasi Activity Log tidak memuat entri baru Object `Group Role` untuk ketiga penugasan itu (jumlah entri Object `Group Role`, Name `Ahmad Fauzi` sama dengan baseline)

### TC-FA-RP-1135: Changelog Remove Read Only: satu entri Remove (via Read Only) per penugasan Group Role (Role × Group) di Detail Role dan Changelog: User > Group Role

21. Tetapkan Ahmad Fauzi Read Only dengan Group Role `Manage files` Read di `Data Center` dan `Helpdesk` lewat seeding API, hingga tersimpan
22. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Read Only`
23. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
24. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
25. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
26. Klik ikon Changelog di toolbar Detail Role
27. Verifikasi Modal memuat entri terbaru Action `Remove (via Read Only)`: Role Name — User — Group Name `Manage files — Ahmad Fauzi — Data Center`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
28. Verifikasi Modal memuat entri terbaru Action `Remove (via Read Only)`: Role Name — User — Group Name `Manage files — Ahmad Fauzi — Helpdesk`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
29. Tutup modal Changelog lalu buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
30. Klik ikon Changelog
31. Verifikasi modal Changelog: User > Group Role memuat dua entri Action `Remove (via Read Only)` dengan Field `Manage files — Data Center` dan `Manage files — Helpdesk`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`

### TC-FA-RP-1136: Changelog Remove Total Control pada user tanpa penugasan Group Role: tidak ada entri Group Role

32. Buat entri pembanding Changelog: User > Group Role untuk Budi Setiawan: tetapkan Group Role `Manage files` di `Helpdesk` lalu lepaskan lewat sesi API aktor (Remove biasa, bukan via Total Control), hingga tersimpan
33. Tetapkan Budi Setiawan Total Control tanpa penugasan Group Role lewat seeding API, hingga tersimpan
34. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Total Control`
35. Klik `[⋯]` baris Budi Setiawan lalu `Remove`
36. Klik `[Remove]`, catat waktu sesudah `[Remove]`
37. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
38. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
39. Klik ikon Changelog di toolbar Detail Role
40. Verifikasi Modal Changelog `Manage files` terbuka
41. Verifikasi Modal memuat entri pembanding milik spec: entri Action `Remove` (bukan via Total Control) untuk `Manage files — Budi Setiawan — Helpdesk`
42. Verifikasi Modal tidak memuat entri Action `Remove (via Total Control)` dengan User `Budi Setiawan`
43. Tutup modal Changelog lalu buka Settings > User > Detail Budi Setiawan > Tab Role sub-tab Group Role
44. Klik ikon Changelog
45. Verifikasi modal Changelog: User > Group Role terbuka
46. Verifikasi modal Changelog: User > Group Role memuat entri pembanding milik spec: entri Action `Remove` (bukan via Total Control) dengan Field `Manage files — Helpdesk`
47. Verifikasi modal Changelog: User > Group Role tidak memuat entri `Remove (via Total Control)`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 47 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 8, 11, 15, 22, 25, 29, 34, 38, 43. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 21, 32, 33; tidak ada `Verifikasi`.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri tidak diasersi. Pada System Log dan Activity Log, entri dikenali lewat kombinasi Action, Object, dan Name serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu, bukan baris teratas (S-12). Asersi absence pada System Log dan Activity Log TC-FA-RP-1134 memakai entri `Remove` Object `Total Control` dari aksi yang sama sebagai anchor positif (butir 8b.2); anchor itu adalah asersi tambahan di luar Expected TC (S-03).
- Anchor tambahan (S-03, bukan dari TC sumber): langkah 41 dan 46 membuktikan sedikitnya satu entri pembanding tampil di modal Changelog yang sama sebelum asersi absence pada langkah 42 dan 47 (butir 8b.2); entri pembandingnya dibuat langkah seeding 32.
- Spec ini memuat lebih dari 35 langkah (di atas smell): ketiga blok satu kelas (Changelog pelepasan tingkat akses yang berdampak pada Group Role), tiap blok berdiri sendiri dengan seeding tingkat akses sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan berasal dari asersi absence berpola anchor pada dua surface log dan dua surface Changelog, satu langkah pencatatan baseline (S-12), satu langkah seeding entri pembanding, dan dua Verifikasi entri pembanding (butir 8b.2).
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-1134 langkah 5 menyebut Settings > User > Detail Siti Rahmawati > Tab System Log dan Activity Log FAMS tanpa menyebut entri yang dicari; spec memakai entri `Remove` Object `Total Control` aksi yang sama sebagai anchor.
  - TC-FA-RP-1134 dan TC-FA-RP-1135 menyebut Group Role `Helpdesk` dari "seed API" dan Pre-setup #39 tidak memuat penugasan Ahmad Fauzi di `Helpdesk`; spec menyiapkannya lewat seeding API.
  - TC-FA-RP-1136 precondition menyebut Budi Setiawan Total Control tanpa penugasan Group Role; Pre-setup #15 mencatat Budi Setiawan tanpa tingkat akses; spec menetapkannya Total Control lewat seeding API.
  - TC-FA-RP-1136 Expected b dan c memakai kata "tidak memuat entri" tanpa baris pembanding; spec memakai modal yang terbuka sebagai anchor.
