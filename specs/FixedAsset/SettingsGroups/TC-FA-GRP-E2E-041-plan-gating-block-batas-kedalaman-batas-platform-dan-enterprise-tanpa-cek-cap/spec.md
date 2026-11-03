---
id: TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap
title: "Plan Gating Preemptif: Block Depth Cap Growth, Batas Platform Count/Depth (Enterprise/Unlimited), dan Enterprise Hanya System Limits"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-114
  - TC-FA-GRP-115
  - TC-FA-GRP-116
  - TC-FA-GRP-121
coverage:
  web: automated
---

# Plan Gating Preemptif: Block Depth Cap Growth, Batas Platform Count/Depth (Enterprise/Unlimited), dan Enterprise Hanya System Limits

## Prerequisites

- Mode: FE+BE (backend nyata; kelas h state tenant: batas depth plan Growth dan System Limits platform Enterprise/Unlimited).
- Akun aktor: Total Control client Growth (depth cap 2), kredensial `Spectra.env.FA_GROWTH_TC_PASSWORD`; Total Control client Enterprise/Unlimited, kredensial `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`. Kedua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email kedua akun tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login akun client Growth di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; login akun client Enterprise lewat langkah ganti akun eksplisit (8) yang disusul langkah membuka halaman Groups (9); hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini. Untuk akun Total Control client Enterprise hasil ganti akun (langkah 8), flag Guided Tooltip `fa-settings-groups` disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE).
- Data client (disediakan tim FE): client Growth dengan sedikitnya satu node di level 2 (precondition TC-FA-GRP-114); client Enterprise dengan lebih dari 25 group dan kedalaman lebih dari 5 level, masih di bawah System Limits (precondition TC-FA-GRP-121, termasuk sebuah node di level 6), sebuah node parent untuk TC-FA-GRP-116 yang kedalamannya diketahui.
- Data Dinamis bersuffix `{runId}-041`: `Ent Group {runId}-041` dan `Ent Sub {runId}-041` (TC-FA-GRP-121); nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas fixture belum ada, dibuat di tahap script).
- State global yang diubah: Master Data Count Limit dan Hierarchy Depth Limit client Enterprise di Lifecycle Settings > System Limits (Admin Console). Pelaku dan mekanisme perubahan disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD; S-13). Langkah 15 menurunkan Master Data Count Limit sama dengan jumlah group client yang dicatat pada langkah 14 dan langkah 25 menurunkan Hierarchy Depth Limit sama dengan kedalaman parent saat ini; keduanya dipulihkan di langkah 23 dan 33 serta di hook `after` bila spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: pencatatan dan pembacaan jumlah group serta nilai System Limits lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD).
- Pemulihan (hook `after`): pulihkan Master Data Count Limit dan Hierarchy Depth Limit ke nilai awal; hapus lewat API `Ent Group {runId}-041` dan `Ent Sub {runId}-041`; kembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-GRP-114: Block depth cap plan Growth (depth cap 2), parent di level 2

1. Catat jumlah group client Growth via fixture BE sebagai baseline
2. Klik Add Subgroup pada node level 2 (elipsis (⋯) baris node level 2)
3. Verifikasi popup form tidak terbuka
4. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `This exceeds the group depth limit for your plan. Upgrade to nest deeper.`
5. Verifikasi tombol dialog hanya [OK] (tanpa [Upgrade])
6. Klik [OK]
7. Verifikasi dialog tertutup tanpa membuat group: jumlah group client Growth lewat fixture BE sama dengan jumlah yang dicatat pada langkah 1

### Ganti akun ke client Enterprise

8. Ganti akun: logout, lalu login sebagai Total Control client Enterprise
9. Buka Fixed Asset > Settings > Groups

### TC-FA-GRP-121: Enterprise tanpa cek cap plan, hanya System Limits

10. Klik [+] Group, isi Group Name `Ent Group {runId}-041`, lalu klik [Submit]
11. Verifikasi create sukses dengan toast `Success, group has been created.` (count lebih dari 25, tanpa cek cap plan)
12. Klik Add Subgroup pada node level 6, isi Group Name `Ent Sub {runId}-041`, lalu klik [Submit]
13. Verifikasi create sukses dengan toast `Success, group has been created.` (depth lebih dari 5, tanpa cek cap plan)

### TC-FA-GRP-115: Block platform count (Master Data Count Limit)

14. Catat jumlah group client Enterprise via fixture BE sebagai baseline
15. Turunkan Master Data Count Limit di Lifecycle Settings > System Limits sama dengan jumlah group client yang dicatat pada langkah 14
16. Buka Fixed Asset > Settings > Groups
17. Klik [+] Group di sidebar
18. Verifikasi popup form tidak terbuka
19. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the platform limit of [Group Limit] groups. Contact support if you need a higher limit.` ([Group Limit] = nilai Master Data Count Limit pada langkah 15)
20. Verifikasi tombol dialog hanya [OK]
21. Klik [OK]
22. Verifikasi dialog tertutup tanpa membuat group: jumlah group lewat fixture BE sama dengan jumlah yang dicatat pada langkah 14
23. Pulihkan Master Data Count Limit ke nilai awal

### TC-FA-GRP-116: Block platform depth (Hierarchy Depth Limit)

24. Catat jumlah group client Enterprise via fixture BE sebagai baseline
25. Turunkan Hierarchy Depth Limit di Lifecycle Settings > System Limits sama dengan kedalaman parent saat ini
26. Buka Fixed Asset > Settings > Groups
27. Klik Add Subgroup pada node parent tersebut
28. Verifikasi popup form tidak terbuka
29. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the platform limit of [Level Limit] levels. Contact support if you need a higher limit.` ([Level Limit] = nilai Hierarchy Depth Limit pada langkah 25)
30. Verifikasi tombol dialog hanya [OK]
31. Klik [OK]
32. Verifikasi dialog tertutup tanpa membuat group: jumlah group lewat fixture BE sama dengan jumlah yang dicatat pada langkah 24
33. Pulihkan Hierarchy Depth Limit ke nilai awal

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-114 (client Growth) lebih dulu, lalu ganti akun (langkah 8) ke client Enterprise: TC-FA-GRP-121 sebelum TC-FA-GRP-115 dan 116 karena TC-FA-GRP-121 membutuhkan System Limits belum diturunkan; berbeda dari urutan nomor TC sumber. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Catat jumlah group client Growth via fixture BE sebagai baseline); langkah 8 (Ganti akun: logout, lalu login sebagai Total Control client Enterprise); langkah 9 (Buka Fixed Asset > Settings > Groups; hook `beforeEach` suite tidak berlaku sesudah ganti akun); langkah 14 dan 24 (Catat jumlah group client Enterprise via fixture BE sebagai baseline); langkah 15 (Turunkan Master Data Count Limit di Lifecycle Settings > System Limits sama dengan jumlah group client yang dicatat pada langkah 14); langkah 23 (Pulihkan Master Data Count Limit ke nilai awal); langkah 25 (Turunkan Hierarchy Depth Limit di Lifecycle Settings > System Limits sama dengan kedalaman parent saat ini); langkah 33 (Pulihkan Hierarchy Depth Limit ke nilai awal); langkah 16 dan 26 (Buka Fixed Asset > Settings > Groups: System Limits diubah lewat UI Admin Console, sehingga halaman Groups dibuka lagi sebelum Klik [+] Group atau Add Subgroup, S-14).
- Temuan untuk QA:
  - Email dan password akun Total Control client Growth dan Enterprise tidak tertulis di Pre-setup TC; spec memakai env baru `FA_GROWTH_TC_PASSWORD` dan `FA_ENTERPRISE_TC_PASSWORD` dan akun yang disediakan tim FE.
  - TC-FA-GRP-115 dan TC-FA-GRP-116 Expected b menulis placeholder `[Group Limit]` dan `[Level Limit]` (TC sendiri keliru menyebut `[Selection Limit]` pada catatan kurung); spec memakai nilai System Limits yang diturunkan di langkah 15 dan 25.
  - TC-FA-GRP-115 dan TC-FA-GRP-116 tidak menyebut pelaku dan mekanisme penurunan System Limits (Admin Console); dicatat sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-GRP-121 mensyaratkan client Enterprise dengan lebih dari 25 group dan lebih dari 5 level; data ini disediakan tim FE dan tidak ada di Pre-setup TC.

