---
id: TC-FA-GRP-E2E-042-plan-gating-dialog-ok-esc-backdrop-dan-penurunan-cap-depth-tidak-memangkas-node
title: "Plan Gating: Dialog Hanya [OK] Tanpa [Upgrade], Esc dan Backdrop Tidak Menutup, dan Penurunan Cap Depth Tidak Memangkas Node"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-122
  - TC-FA-GRP-972
  - TC-FA-GRP-973
coverage:
  web: automated
---

# Plan Gating: Dialog Hanya [OK] Tanpa [Upgrade], Esc dan Backdrop Tidak Menutup, dan Penurunan Cap Depth Tidak Memangkas Node

## Prerequisites

- Mode: FE+BE (backend nyata; kelas h state tenant: dialog plan gating Starter, Growth, dan Enterprise/Unlimited serta client hasil penurunan plan).
- Akun aktor (empat client, urutan sesuai langkah): Total Control client Starter (cap 1), `Spectra.env.FA_STARTER_TC_PASSWORD`; Total Control client Growth (depth cap 2), `Spectra.env.FA_GROWTH_TC_PASSWORD`; Total Control client Enterprise/Unlimited, `Spectra.env.FA_ENTERPRISE_TC_PASSWORD`; Total Control client yang plan-nya turun dari Professional ke Growth (depth 2) dan masih punya node di level 4, `Spectra.env.FA_DOWNGRADE_TC_PASSWORD`. Semua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email keempat akun tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login akun client Starter di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; akun client lain lewat langkah ganti akun eksplisit (10, 16, 28); hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data client (disediakan tim FE): client Starter berisi tepat 1 group; client Growth punya node di level 2; client Enterprise/Unlimited; client hasil penurunan punya node `Deep Level 4 {runId}-042` di level 4 (Description awal `Deep Desc`, Description baru `Deep Desc Edited {runId}-042`).
- State global yang diubah: Master Data Count Limit client Enterprise/Unlimited diturunkan sama dengan jumlah group saat ini (langkah 17) dan dipulihkan di langkah 27 serta di hook `after`; pelaku dan mekanismenya disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD). Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: pembacaan jumlah group lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); penanganan Esc dan klik backdrop pada dialog.
- Pemulihan (hook `after`): pulihkan Master Data Count Limit; kembalikan Description node `Deep Level 4 {runId}-042` ke `Deep Desc`; kembalikan sesi ke akun default suite.

## Test Steps

### Client Starter (TC-FA-GRP-972 dan TC-FA-GRP-973, dialog D-06)

1. Klik [+] Group di sidebar
2. Verifikasi dialog D-06 hanya memuat tombol [OK]; tidak ada tombol [Upgrade] (TC-FA-GRP-972)
3. Tekan Esc
4. Verifikasi dialog D-06 tetap tampil (Esc tidak menutup, TC-FA-GRP-973)
5. Klik backdrop
6. Verifikasi dialog D-06 tetap tampil (klik backdrop tidak menutup, TC-FA-GRP-973)
7. Klik [OK]
8. Verifikasi dialog D-06 tertutup tanpa membuka alur upgrade plan (TC-FA-GRP-972)
9. Verifikasi popup form tidak terbuka dan tidak ada group dibuat: jumlah group lewat fixture BE sama dengan baseline (TC-FA-GRP-972)

### Client Growth (TC-FA-GRP-972, dialog D-07)

10. Ganti akun: logout, lalu login sebagai Total Control client Growth
11. Klik Add Subgroup pada node level 2
12. Verifikasi dialog D-07 hanya memuat tombol [OK]; tidak ada tombol [Upgrade]
13. Klik [OK]
14. Verifikasi dialog D-07 tertutup tanpa membuka alur upgrade plan
15. Verifikasi popup form tidak terbuka dan tidak ada group dibuat: jumlah group lewat fixture BE sama dengan baseline

### Client Enterprise/Unlimited (TC-FA-GRP-973, dialog D-08)

16. Ganti akun: logout, lalu login sebagai Total Control client Enterprise/Unlimited
17. Turunkan Master Data Count Limit di Lifecycle Settings > System Limits sama dengan jumlah group client saat ini
18. Klik [+] Group di sidebar
19. Tekan Esc
20. Verifikasi dialog D-08 tetap tampil (Esc tidak menutup)
21. Klik backdrop
22. Verifikasi dialog D-08 tetap tampil (klik backdrop tidak menutup)
23. Verifikasi dialog D-08 hanya memuat tombol [OK] (tanpa [Upgrade])
24. Klik [OK]
25. Verifikasi dialog D-08 tertutup
26. Verifikasi popup form tidak terbuka dan tidak ada group dibuat: jumlah group lewat fixture BE sama dengan sebelum langkah 17
27. Pulihkan Master Data Count Limit ke nilai awal

### Client hasil penurunan plan (TC-FA-GRP-122)

28. Ganti akun: logout, lalu login sebagai Total Control client hasil penurunan plan Professional ke Growth
29. Buka node `Deep Level 4 {runId}-042` (level 4), ubah Description menjadi `Deep Desc Edited {runId}-042`, lalu klik [Save]
30. Verifikasi node level 4 tetap tampil dan bukan Excess
31. Verifikasi Edit sukses dengan toast `Success, group has been updated.`
32. Klik Add Subgroup pada node level 4
33. Verifikasi dialog `This exceeds the group depth limit for your plan. Upgrade to nest deeper.` tampil
34. Klik [OK] dan kembalikan Description node ke `Deep Desc` (pemulihan)

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular; TC-FA-GRP-972 dan TC-FA-GRP-973 dipetakan per client (langkah Starter, Growth, dan Unlimited) supaya akun tidak berganti berulang kali, sehingga langkahnya tidak berurutan per TC.
- Urutan blok: tiap client satu blok, dengan Step ganti akun eksplisit (langkah 10, 16, 28); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 10 (Ganti akun: logout, lalu login sebagai Total Control client Growth); langkah 16 (Ganti akun: logout, lalu login sebagai Total Control client Enterprise...); langkah 17 (Turunkan Master Data Count Limit di Lifecycle Settings > System Limits...); langkah 27 (Pulihkan Master Data Count Limit ke nilai awal); langkah 28 (Ganti akun: logout, lalu login sebagai Total Control client hasil penu...); langkah 34 (Klik [OK] dan kembalikan Description node ke `Deep Desc` (pemulihan)).
- Temuan untuk QA:
  - Email dan password akun Total Control keempat client tidak tertulis di Pre-setup TC; spec memakai env baru dan akun yang disediakan tim FE.
  - TC-FA-GRP-972 menulis dialog D-06 dan D-07, TC-FA-GRP-973 menulis D-06 dan D-08; teks body tiap dialog tidak diulang di Expected kedua TC itu, sehingga spec hanya mengasersi komposisi tombol dan perilaku tutup.
  - TC-FA-GRP-122 tidak menyebut cara membuat client hasil penurunan plan dan node level 4; data disediakan tim FE.

