---
id: TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade
title: "Plan Tier: Registrasi Starter, Downgrade, dan Upgrade"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-267
  - TC-FA-CAID-268
  - TC-FA-CAID-269
  - TC-FA-CAID-270
coverage:
  web: automated
---

# Plan Tier: Registrasi Starter, Downgrade, dan Upgrade

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control Company Starter) di hook `before` spec ini. Spec ini tidak berawal di tab Custom Asset ID: layar awal tiap blok dinyatakan di langkahnya (langkah 1, 10, 21); hook `beforeEach` suite tetap membuka halaman untuk akun yang login di hook `before`, lalu langkah 1 membuka Registration.
- Role yang diuji (Total Control; email `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture). Email akun tiap Company khusus disediakan tim FE/BE; nama env password di tabel ini mengikuti kolom Akun dan Env Var Pre-setup No 13 dan 14 TC. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha).

| Blok | TC | Company (Pre-setup) | Env password |
|---|---|---|---|
| 1 | TC-FA-CAID-267 | Company Starter (No 13) | `Spectra.env.FA_STARTER_TC_PASSWORD` |
| 2 | TC-FA-CAID-268 | Company Downgrade (No 14) | `Spectra.env.FA_DOWNGRADE_TC_PASSWORD` |
| 3 | TC-FA-CAID-269, 270 | Company Upgrade (No 14) | `Spectra.env.FA_UPGRADE_TC_PASSWORD` |

- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk semua akun UI suite. Baseline Company Alpha yang dipulihkan `beforeEach` suite tidak dipakai spec ini.
- Data Pre-setup: No 13 Company Starter (plan Starter, konfigurasi tersimpan B1, aset S1 Active `JKT/LAP/T490/0926/1` ber-Increment 1); No 14 Company Downgrade (plan Growth dengan konfigurasi B1 dan aset G1 `JKT/LAP/T490/0926/1`, G2 `JKT/LAP/T490/0926/2`; plan diturunkan ke Starter oleh langkah 9) dan Company Upgrade (konfigurasi B1, plan Growth, aset polos U1 `1` dan U2 `2` tanpa Purchase Date); No 10 baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Quick Register (dipakai langkah 3, 15, 23; TC menyebut nilainya hanya pada TC-FA-CAID-267 dan 269): Asset Name `ThinkPad T490` (Code `T490`), Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office` (Code `JKT`), Condition `Normal`; master data Group, Category `Laptop` (Code `LAP`), Asset Name, dan Brand pada tiap Company disediakan tim FE (TC tidak menyebut master data tiap Company selain Pre-setup No 24).
- Data Dinamis: aset hasil Quick Register pada langkah 4, 16, 24 memakai nama master tetap (tidak bersuffix, karena nilai berasal dari master data Pre-setup) dan diidentifikasi lewat Asset ID turunan baseline (`2`, `3`, `JKT/LAP/T490/0000/3`).
- Kemampuan teknis: seed API untuk menurunkan plan Company Downgrade (langkah 9) dan mereset Company Starter, Company Downgrade, dan Company Upgrade ke Pre-setup (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD). Aset hasil registrasi dan Retroactive Mass Update dibersihkan oleh seed reset Company di hook `after` spec ini (dan sebelum tiap run). Pada TC-FA-CAID-270, aset Company Upgrade dikembalikan ke U1 dan U2 polos lewat seed reset sebelum langkah 29.
- State global: plan Company Downgrade (Growth diturunkan ke Starter) dan konfigurasi serta aset Company Upgrade dan Company Starter; dipulihkan di hook `after` spec ini walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-267: Plan Starter: registrasi memakai Increment polos (blok 1)

1. Buka Fixed Asset > Assets > Registration
2. Klik `[+ Quick Register]`
3. Isi form Quick Register: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`
4. Klik `[Save as Draft]`
5. Tunggu aksi selesai: tombol `[Save as Draft]` selesai diproses
6. Buka Fixed Asset > Assets > All Assets
7. Verifikasi aset baru terbit dengan Asset ID `2` (Increment polos karena entitlement plan tidak terpenuhi)
8. Verifikasi aset S1 tetap ber-Asset ID `JKT/LAP/T490/0926/1`

### TC-FA-CAID-268: Downgrade ke Starter: konfigurasi dipertahankan, registrasi baru polos (blok 2)

9. Turunkan plan Company Downgrade dari Growth ke Starter lewat seed hingga plan tersimpan; dipakai sebagai precondition TC, tidak diasersi
10. Ganti akun: logout akun Total Control Company Starter, login sebagai Total Control Company Downgrade, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID
11. Verifikasi form terkunci dengan banner Starter
12. Verifikasi form menampilkan konfigurasi tersimpan Separator `/ (Slash)` tanpa di-reset
13. Buka Fixed Asset > Assets > Registration
14. Klik `[+ Quick Register]`
15. Isi form Quick Register dengan data Quick Register di Prerequisites
16. Klik `[Save as Draft]`
17. Tunggu aksi selesai: tombol `[Save as Draft]` selesai diproses
18. Buka Fixed Asset > Assets > All Assets
19. Verifikasi aset G1 `JKT/LAP/T490/0926/1` dan G2 `JKT/LAP/T490/0926/2` tidak berubah
20. Verifikasi aset baru terbit dengan Asset ID `3` sebagai Increment polos

### TC-FA-CAID-269: Upgrade dari Starter: registrasi baru berformat kustom (blok 3)

21. Ganti akun: logout akun Total Control Company Downgrade, login sebagai Total Control Company Upgrade, lalu buka Fixed Asset > Assets > Registration
22. Klik `[+ Quick Register]`
23. Isi form Quick Register: Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`
24. Klik `[Save as Draft]`
25. Tunggu aksi selesai: tombol `[Save as Draft]` selesai diproses
26. Buka Fixed Asset > Assets > All Assets
27. Verifikasi aset baru terbit dengan Asset ID `JKT/LAP/T490/0000/3`
28. Verifikasi aset U1 dan U2 tetap `1` dan `2` karena upgrade plan tidak memicu Retroactive Mass Update

### TC-FA-CAID-270: Setelah upgrade Save zero-delta tidak me-reformat, Save perubahan riil me-reformat (blok 3)

29. Reset Company Upgrade lewat seed ke aset polos U1 `1` dan U2 `2`, plan Growth, konfigurasi B1 hingga seed tersimpan
30. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
31. Pilih Separator `- (Dash)`
32. Pilih kembali Separator `/ (Slash)`
33. Klik `[Save]`
34. Verifikasi toast `No changes to save.` tampil
35. Buka Fixed Asset > Assets > All Assets
36. Verifikasi aset U1 dan U2 tetap `1` dan `2`
37. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
38. Pilih Separator `- (Dash)`
39. Klik `[Save]`
40. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
41. Buka Fixed Asset > Assets > All Assets
42. Verifikasi aset U1 dan U2 menjadi `JKT-LAP-T490-0000-1` dan `JKT-LAP-T490-0000-2`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok Company karena ganti akun menuntut langkah eksplisit (langkah 10 dan 21).
- Spec ini 42 langkah tanpa langkah berulang, melewati sekitar 35 langkah. Alasan: semua blok satu kelas (state tenant plan tier), tiap blok berdiri sendiri pada Company dan data sendiri (Starter, Downgrade, Upgrade) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 6, 13, 18, 26, 35, 37, 41 (membuka halaman), langkah 9 dan 29 (seed state), langkah 10 dan 21 (ganti akun), langkah 31 dan 32 (mengubah lalu mengembalikan nilai agar zero-delta), dan aksi TC pada langkah 2 sampai 4, 14 sampai 16, 22 sampai 24, 33, 38, 39. Langkah 33 dan 39 diikuti `Verifikasi` toast sehingga tidak butuh langkah "Tunggu aksi selesai"; langkah 4, 16, 24 (`[Save as Draft]`) tidak punya asersi toast di TC dan langkah berikutnya membuka All Assets (pindah surface), sehingga langkah 5, 17, 25 adalah "Tunggu aksi selesai" (bagian 8b butir 8) dan hasil registrasi diamati di All Assets.
- Baris aset di All Assets dicari lewat Asset ID turunan baseline (`2`, `3`, `JKT/LAP/T490/0000/3`, `1`, `2`); tidak ada Search yang dipakai sebagai langkah (R-16).
- Temuan untuk QA:
  - TC-FA-CAID-268 menyebut "Registrasi aset baru di Fixed Asset > Assets > Registration" tanpa data form; spec memakai data Quick Register yang sama dengan TC-FA-CAID-267 dan 269.
  - Hasil Retroactive Mass Update pada TC-FA-CAID-270 dibaca langsung sesudah membuka All Assets; TC tidak menyebut waktu penyelesaian pembaruan massal bila berjalan asinkron.
  - Aset hasil registrasi tidak bisa bernama unik (Asset Name diambil dari master data Pre-setup); identifikasi hanya lewat Asset ID baseline.
  - Post Condition TC-FA-CAID-267 sampai 270 kosong; tidak ada yang diasersi.
