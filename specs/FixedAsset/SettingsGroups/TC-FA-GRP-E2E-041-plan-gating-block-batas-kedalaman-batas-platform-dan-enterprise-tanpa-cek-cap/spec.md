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
- Akun aktor: Total Control client Growth (depth cap 2), kredensial `Spectra.env.FA_GROWTH_TC_PASSWORD`; Total Control client Enterprise/Unlimited, kredensial `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`. Kedua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email kedua akun tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login akun client Growth di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; login akun client Enterprise lewat langkah ganti akun eksplisit (7); hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data client (disediakan tim FE): client Growth dengan sedikitnya satu node di level 2 (precondition TC-FA-GRP-114); client Enterprise dengan lebih dari 25 group dan kedalaman lebih dari 5 level, masih di bawah System Limits (precondition TC-FA-GRP-121, termasuk sebuah node di level 6), sebuah node parent untuk TC-FA-GRP-116 yang kedalamannya diketahui.
- Data Dinamis bersuffix `{runId}-041`: `Ent Group {runId}-041` dan `Ent Sub {runId}-041` (TC-FA-GRP-121); nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas fixture belum ada, dibuat di tahap script).
- State global yang diubah: Master Data Count Limit dan Hierarchy Depth Limit client Enterprise di Lifecycle Settings > System Limits (Admin Console). Pelaku dan mekanisme perubahan disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD; S-13). Langkah 12 menurunkan Master Data Count Limit sama dengan jumlah group client saat ini dan langkah 20 menurunkan Hierarchy Depth Limit sama dengan kedalaman parent saat ini; keduanya dipulihkan di langkah 19 dan 27 serta di hook `after` bila spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: pembacaan jumlah group dan nilai System Limits lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD).
- Pemulihan (hook `after`): pulihkan Master Data Count Limit dan Hierarchy Depth Limit ke nilai awal; hapus lewat API `Ent Group {runId}-041` dan `Ent Sub {runId}-041`; kembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-GRP-114: Block depth cap plan Growth (depth cap 2), parent di level 2

1. Klik Add Subgroup pada node level 2 (elipsis (⋯) baris node level 2)
2. Verifikasi popup form tidak terbuka
3. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `This exceeds the group depth limit for your plan. Upgrade to nest deeper.`
4. Verifikasi tombol dialog hanya [OK] (tanpa [Upgrade])
5. Klik [OK]
6. Verifikasi dialog tertutup tanpa membuat group: jumlah group client Growth lewat fixture BE sama dengan baseline

### Ganti akun ke client Enterprise

7. Ganti akun: logout, lalu login sebagai Total Control client Enterprise

### TC-FA-GRP-121: Enterprise tanpa cek cap plan, hanya System Limits

8. Klik [+] Group, isi Group Name `Ent Group {runId}-041`, lalu klik [Submit]
9. Verifikasi create sukses dengan toast `Success, group has been created.` (count lebih dari 25, tanpa cek cap plan)
10. Klik Add Subgroup pada node level 6, isi Group Name `Ent Sub {runId}-041`, lalu klik [Submit]
11. Verifikasi create sukses dengan toast `Success, group has been created.` (depth lebih dari 5, tanpa cek cap plan)

### TC-FA-GRP-115: Block platform count (Master Data Count Limit)

12. Turunkan Master Data Count Limit di Lifecycle Settings > System Limits sama dengan jumlah group client saat ini
13. Klik [+] Group di sidebar
14. Verifikasi popup form tidak terbuka
15. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the platform limit of [Group Limit] groups. Contact support if you need a higher limit.` ([Group Limit] = nilai Master Data Count Limit pada langkah 12)
16. Verifikasi tombol dialog hanya [OK]
17. Klik [OK]
18. Verifikasi dialog tertutup tanpa membuat group: jumlah group lewat fixture BE sama dengan sebelum langkah 12
19. Pulihkan Master Data Count Limit ke nilai awal

### TC-FA-GRP-116: Block platform depth (Hierarchy Depth Limit)

20. Turunkan Hierarchy Depth Limit di Lifecycle Settings > System Limits sama dengan kedalaman parent saat ini
21. Klik Add Subgroup pada node parent tersebut
22. Verifikasi popup form tidak terbuka
23. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the platform limit of [Level Limit] levels. Contact support if you need a higher limit.` ([Level Limit] = nilai Hierarchy Depth Limit pada langkah 20)
24. Verifikasi tombol dialog hanya [OK]
25. Klik [OK]
26. Verifikasi dialog tertutup tanpa membuat group: jumlah group lewat fixture BE sama dengan sebelum langkah 20
27. Pulihkan Hierarchy Depth Limit ke nilai awal

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-114 (client Growth) lebih dulu, lalu ganti akun (langkah 7) ke client Enterprise: TC-FA-GRP-121 sebelum TC-FA-GRP-115 dan 116 karena TC-FA-GRP-121 membutuhkan System Limits belum diturunkan; berbeda dari urutan nomor TC sumber. Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 7 (Ganti akun: logout, lalu login sebagai Total Control client Enterprise); langkah 12 (Turunkan Master Data Count Limit di Lifecycle Settings > System Limits...); langkah 19 (Pulihkan Master Data Count Limit ke nilai awal); langkah 20 (Turunkan Hierarchy Depth Limit di Lifecycle Settings > System Limits s...); langkah 27 (Pulihkan Hierarchy Depth Limit ke nilai awal).
- Temuan untuk QA:
  - Email dan password akun Total Control client Growth dan Enterprise tidak tertulis di Pre-setup TC; spec memakai env baru `FA_GROWTH_TC_PASSWORD` dan `FA_ENTERPRISE_TC_PASSWORD` dan akun yang disediakan tim FE.
  - TC-FA-GRP-115 dan TC-FA-GRP-116 Expected b menulis placeholder `[Group Limit]` dan `[Level Limit]` (TC sendiri keliru menyebut `[Selection Limit]` pada catatan kurung); spec memakai nilai System Limits yang diturunkan di langkah 12 dan 20.
  - TC-FA-GRP-115 dan TC-FA-GRP-116 tidak menyebut pelaku dan mekanisme penurunan System Limits (Admin Console); dicatat sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-GRP-121 mensyaratkan client Enterprise dengan lebih dari 25 group dan lebih dari 5 level; data ini disediakan tim FE dan tidak ada di Pre-setup TC.

