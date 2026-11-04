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
- Data Pre-setup: #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Setiawan), #18 (pohon group), #21 (seed pemegang Update `Manage asset & TAG`: Ahmad Fauzi Create, Read, Update di `Head Office`), #24 (`Company Changelog`), #39 (Detail Role Group Role `Manage files` terisi 6 baris non-pola dan 35 baris pola Group Role pada tujuh group Pre-setup #18 untuk lima user pola Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, Maya Anggraeni; Ahmad Fauzi dan Budi Setiawan memegang baris pola menurut tingkat aksesnya). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog, System Log, dan Activity Log lewat UI; waktu aksi dicatat sesudah aksi pemicu. Baseline jumlah entri System Log dan Activity Log dicatat lewat kemampuan baca (disediakan tim FE/BE) sebelum aksi pemicu TC-FA-RP-1134 (S-12). Seeding status Total Control atau Read Only Ahmad Fauzi dan Budi Setiawan lewat seeding API (kemampuan disediakan tim FE/BE).
- State yang diubah dan pemulihannya: Tingkat akses Ahmad Fauzi dan Budi Setiawan (beserta baris pola Group Role-nya) diubah spec ini; dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1134: Changelog Remove Total Control: satu entri Remove (via Total Control) per baris pola Group Role (Role × Group) di Detail Role dan Changelog: User > Group Role, tanpa entri di System Log dan Activity Log

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` dan jumlah entri Object `Group Role`, Name `Ahmad Fauzi` pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS (baseline System Log dan baseline Activity Log)
2. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
3. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
4. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
5. Klik ikon Changelog di toolbar Detail Role
6. Verifikasi Modal memuat satu entri Action `Remove (via Total Control)` per baris pola `Manage files` (per group pada tujuh group Pre-setup #18: `Data Center`, `Dock 1`, `Head Office`, `Helpdesk`, `IT Infrastructure`, `Logistics Warehouse`, `Rack A1`): Role Name — User — Group Name `Manage files — Ahmad Fauzi — [Group Name]`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog, klik segmen `System` pada Breadcrumb, buka Detail Role Group Role `Manage asset & TAG`, lalu klik `All Groups`
8. Klik ikon Changelog di toolbar Detail Role
9. Verifikasi Modal memuat entri analog per baris pola `Manage asset & TAG — Ahmad Fauzi — [Group Name]` pada ketujuh group yang sama: Action `Remove (via Total Control)`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
10. Tutup modal Changelog lalu buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
11. Klik ikon Changelog
12. Verifikasi modal Changelog: User > Group Role memuat satu entri Action `Remove (via Total Control)` per Role × Group dengan Field `[Role Name] — [Group Name]`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`
13. Verifikasi modal Changelog: User > Group Role tidak memuat entri `Assign (via Total Control)` maupun entri `Edit` untuk baris pola itu
14. Verifikasi modal Changelog: User > Group Role tidak memuat entri `Remove (via Total Control)` untuk role `Manage user & role` (dikecualikan dari pola)
15. Tutup modal Changelog lalu buka Settings > User > Detail Siti Rahmawati > Tab System Log
16. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru di atas baseline: Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` (jumlah entri kombinasi ini bertambah tepat satu; anchor: entri milik aksi pemicu yang sama)
17. Verifikasi System Log tidak memuat entri baru Object `Group Role` untuk penugasan itu (jumlah entri Object `Group Role`, Name `Ahmad Fauzi` sama dengan baseline)
18. Buka Activity Log FAMS (menu Activity Log)
19. Verifikasi Activity Log memuat satu entri baru di atas baseline: Action `Remove`, Object `Total Control`, Name `Ahmad Fauzi` (jumlah entri kombinasi ini bertambah tepat satu; anchor: entri milik aksi pemicu yang sama)
20. Verifikasi Activity Log tidak memuat entri baru Object `Group Role` untuk penugasan itu (jumlah entri Object `Group Role`, Name `Ahmad Fauzi` sama dengan baseline)

### TC-FA-RP-1135: Changelog Remove Read Only: satu entri Remove (via Read Only) per baris pola Group Role (Role × Group) di Detail Role dan Changelog: User > Group Role

21. Tetapkan Ahmad Fauzi Read Only (baris pola Group Role Read saja pada setiap role × group, `FARP-LOGIC-04b`) lewat seeding API, hingga tersimpan
22. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Read Only`
23. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
24. Klik `[Remove]`, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
25. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
26. Klik ikon Changelog di toolbar Detail Role
27. Verifikasi Modal memuat satu entri Action `Remove (via Read Only)` per baris pola `Manage files` (per group pada tujuh group Pre-setup #18: `Data Center`, `Dock 1`, `Head Office`, `Helpdesk`, `IT Infrastructure`, `Logistics Warehouse`, `Rack A1`): Role Name — User — Group Name `Manage files — Ahmad Fauzi — [Group Name]`; Field `Access`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
28. Tutup modal Changelog lalu buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Group Role
29. Klik ikon Changelog
30. Verifikasi modal Changelog: User > Group Role memuat satu entri Action `Remove (via Read Only)` per Role × Group dengan Field `[Role Name] — [Group Name]`; Old Value `Assigned`; New Value `—`; Modified By `Siti R`
31. Verifikasi modal Changelog: User > Group Role tidak memuat entri `Remove (via Read Only)` untuk role `Manage user & role` (dikecualikan dari pola)

### TC-FA-RP-1136: Changelog Remove Total Control pada user yang hanya memegang baris pola Group Role: entri Remove (via Total Control) hanya untuk baris pola user itu

32. Tetapkan Budi Setiawan Total Control tanpa penugasan Group Role eksplisit (hanya baris pola Group Role, `FARP-LOGIC-04b`) lewat seeding API, hingga tersimpan
33. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Total Control`
34. Klik `[⋯]` baris Budi Setiawan lalu `Remove`
35. Klik `[Remove]`, catat waktu sesudah `[Remove]`
36. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
37. Klik Tab `System`, buka Detail Role Group Role `Manage files`, lalu klik `All Groups`
38. Klik ikon Changelog di toolbar Detail Role
39. Verifikasi Modal memuat entri Action `Remove (via Total Control)` dengan User `Budi Setiawan` untuk setiap baris pola `Manage files` pada waktu aksi (per group pada tujuh group Pre-setup #18: `Data Center`, `Dock 1`, `Head Office`, `Helpdesk`, `IT Infrastructure`, `Logistics Warehouse`, `Rack A1`); Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
40. Verifikasi Modal tidak memuat entri `Remove (via Total Control)` milik user selain `Budi Setiawan` pada waktu aksi langkah 35
41. Tutup modal Changelog lalu buka Settings > User > Detail Budi Setiawan > Tab Role sub-tab Group Role
42. Klik ikon Changelog
43. Verifikasi modal Changelog: User > Group Role memuat entri `Remove (via Total Control)` per baris pola
44. Verifikasi modal Changelog: User > Group Role tidak memuat entri Action `Edit` atau `Assign`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 44 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 7, 10, 15, 22, 25, 28, 33, 37, 41. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 21, 32; tidak ada `Verifikasi`.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri tidak diasersi. Pada System Log dan Activity Log, entri dikenali lewat kombinasi Action, Object, dan Name serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu, bukan baris teratas (S-12). Asersi absence pada System Log dan Activity Log TC-FA-RP-1134 memakai entri `Remove` Object `Total Control` dari aksi yang sama sebagai anchor positif (butir 8b.2); anchor itu adalah asersi tambahan di luar Expected TC (S-03).
- Anchor absence (butir 8b.2): langkah 13 dan 14 memakai entri Remove yang diasersi di langkah 12 pada modal yang sama; langkah 31 memakai langkah 30; langkah 40 memakai entri Budi Setiawan di langkah 39; langkah 44 memakai langkah 43. Tidak ada entri pembanding yang di-seed.
- Spec ini memuat lebih dari 35 langkah (di atas smell): ketiga blok satu kelas (Changelog pelepasan tingkat akses yang berdampak pada Group Role), tiap blok berdiri sendiri dengan seeding tingkat akses sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan berasal dari asersi absence berpola anchor pada dua surface log dan surface Changelog serta satu langkah pencatatan baseline (S-12).
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-1134 langkah 5 menyebut Settings > User > Detail Siti Rahmawati > Tab System Log dan Activity Log FAMS tanpa menyebut entri yang dicari; spec memakai entri `Remove` Object `Total Control` aksi yang sama sebagai anchor.
  - TC-FA-RP-1134 dan TC-FA-RP-1135 tidak menyebut daftar Role yang membentuk entri "per Role × Group" di Changelog: User > Group Role; spec tidak mengasersi jumlah entri absolut, hanya satu entri per Role × Group.
  - TC-FA-RP-1134 Expected e dan TC-FA-RP-1135 Expected c ("langkah 2 sampai 4" tidak ada entri untuk `Manage user & role`) mengacu ke modal Detail Role yang khusus satu role; spec mengasersinya pada modal Changelog: User > Group Role (langkah 14 dan 31), tempat entri semua role tampil.
  - TC-FA-RP-1136 precondition menyebut Budi Setiawan Total Control tanpa penugasan Group Role eksplisit; Pre-setup #15 mencatat Budi Setiawan tanpa tingkat akses; spec menetapkannya Total Control lewat seeding API.
  - TC-FA-RP-1136 Expected b "tidak ada entri `Remove (via Total Control)` milik user lain" tidak membatasi waktu, padahal Changelog adalah audit trail permanen yang memuat entri Ahmad Fauzi dari blok TC-FA-RP-1134; spec membatasi asersi pada waktu aksi langkah 35.
