---
id: TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form
title: "Plan Gating Preemptif: Block Cap Jumlah Group (Starter 1, Growth 3), Stay on Form Sampai Cap, Urutan Cek Count Sebelum Depth, Tombol Tidak Disable, dan Cap Dihitung terhadap Semua Node Terlepas Function"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-84
  - TC-FA-GRP-112
  - TC-FA-GRP-113
  - TC-FA-GRP-117
  - TC-FA-GRP-118
  - TC-FA-GRP-120
coverage:
  web: automated
---

# Plan Gating Preemptif: Block Cap Jumlah Group (Starter 1, Growth 3), Stay on Form Sampai Cap, Urutan Cek Count Sebelum Depth, Tombol Tidak Disable, dan Cap Dihitung terhadap Semua Node Terlepas Function

## Prerequisites

- Mode: FE+BE (backend nyata; kelas h state tenant: cap jumlah group ditentukan plan tier client; spec ini tidak mengubah plan, hanya memakai client yang disiapkan di cap).
- Akun aktor: Total Control client Starter (cap 1), kredensial `Spectra.env.FA_STARTER_TC_PASSWORD`; Total Control client Growth (cap 3, depth cap 2), kredensial `Spectra.env.FA_GROWTH_TC_PASSWORD`. Kedua nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; email kedua akun tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Login akun client Starter di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite; login akun client Growth lewat langkah ganti akun eksplisit (11); hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup No 1).
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data client (disediakan tim FE; Pre-setup No 8 hanya menyebut client tambahan Starter, Growth, Enterprise): client Starter berisi tepat 1 group (precondition TC-FA-GRP-112 dan TC-FA-GRP-118); client Growth berisi tepat 2 group (Head Office > Floor 2) pada awal spec (precondition TC-FA-GRP-84). Setelah langkah 21 client Growth berisi 3 group: Head Office, Floor 2, dan `Cap Fill {runId}-040` ber-Function Assignable (menjadi precondition TC-FA-GRP-113, TC-FA-GRP-117, dan TC-FA-GRP-120 "jumlah group sama dengan cap, termasuk 1 node Assignable dan 1 node None").
- Data Dinamis bersuffix `{runId}-040`: `Cap Fill {runId}-040` dan `Over Cap {runId}-040` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script).
- Kemampuan teknis: pembacaan jumlah group client lewat fixture BE (baseline dicatat di hook `before`; disediakan tim FE/BE, nama endpoint tidak disebut di TC dan PRD); pembacaan status respons simpan (409 Conflict) pada langkah 18 lewat intercept pasif atau fixture BE (disediakan tim FE).
- Pemulihan (hook `after`): hapus lewat API `Cap Fill {runId}-040` pada client Growth sehingga client kembali berisi 2 group; sesi dikembalikan ke akun default suite. State global (plan, cap) tidak diubah.

## Test Steps

### TC-FA-GRP-112: Block count cap plan Starter (cap 1) dengan 1 group

1. Klik [+] Group di sidebar
2. Verifikasi popup form tidak terbuka
3. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the group limit for your plan. Upgrade to add more.`
4. Verifikasi tombol dialog hanya [OK] (tanpa [Upgrade])
5. Klik [OK]
6. Verifikasi dialog tertutup tanpa membuat group: jumlah group client Starter lewat fixture BE sama dengan baseline

### TC-FA-GRP-118: Tombol [+] Group dan Add Subgroup tidak pernah di-disable karena cap

7. Verifikasi [+] Group tetap tampil dan enabled pada client Starter yang count = cap
8. Buka elipsis (⋯) pada sebuah node group di sidebar
9. Verifikasi Add Subgroup di elipsis tetap tampil dan enabled
10. Tutup elipsis (Esc)

### Ganti akun ke client Growth

11. Ganti akun: logout, lalu login sebagai Total Control client Growth
12. Buka Fixed Asset > Settings > Groups

### TC-FA-GRP-84: Stay on this form sampai cap tercapai, submit berikutnya ditolak

13. Klik [+] Group, lalu centang `Stay on this form after submitting`
14. Isi Group Name `Cap Fill {runId}-040`, pilih Function Assignable, lalu klik [Submit]
15. Verifikasi Cap Fill tersimpan
16. Verifikasi form direset dan tetap terbuka
17. Isi Group Name `Over Cap {runId}-040`, lalu klik [Submit]
18. Verifikasi Over Cap ditolak server sebagai konflik (`409 Conflict`)
19. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the group limit for your plan. Upgrade to add more.` dan tombol hanya [OK] tampil di atas popup form
20. Klik [OK]
21. Verifikasi dialog dan popup form tertutup
22. Verifikasi state di-refresh: sidebar menampilkan Cap Fill (3 group)
23. Verifikasi Over Cap tidak tersimpan

### TC-FA-GRP-113: Block count cap plan Growth (cap 3) dengan 3 group, via Add Subgroup

24. Klik Add Subgroup pada Head Office (elipsis (⋯) baris Head Office)
25. Verifikasi popup form tidak terbuka
26. Verifikasi dialog 🔒 `Cannot Add Group` dengan Body `You've reached the group limit for your plan. Upgrade to add more.`
27. Verifikasi tombol dialog hanya [OK] (tanpa [Upgrade])
28. Klik [OK]
29. Verifikasi dialog tertutup tanpa membuat group: jumlah group client Growth lewat fixture BE = 3

### TC-FA-GRP-117: Urutan cek count sebelum depth pada Add Subgroup

30. Klik Add Subgroup pada node level 2 (Floor 2)
31. Verifikasi dialog yang tampil varian count: `You've reached the group limit for your plan. Upgrade to add more.` (cek pertama yang gagal menghentikan proses)
32. Klik [OK]

### TC-FA-GRP-120: Cap dihitung terhadap semua node terlepas Function

33. Klik [+] Group di sidebar
34. Verifikasi dialog `Cannot Add Group` varian count cap tampil (node Assignable dan None sama-sama dihitung)
35. Klik [OK]

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: blok client Starter lebih dulu (TC-FA-GRP-112, 118), lalu ganti akun ke client Growth (TC-FA-GRP-84, lalu 113, 117, 120) karena TC-FA-GRP-84 membangun state 3 group yang menjadi precondition ketiga TC berikutnya; berbeda dari urutan nomor TC sumber. Ganti akun punya langkah eksplisit (langkah 11) dan bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah (b)).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 10 (Tutup elipsis (Esc)); langkah 11 (Ganti akun: logout, lalu login sebagai Total Control client Growth); langkah 12 (Buka Fixed Asset > Settings > Groups, karena hook `beforeEach` tidak jalan lagi sesudah login ulang, S-14); langkah 32 (Klik [OK]); langkah 35 (Klik [OK]).
- Temuan untuk QA:
  - Email dan password akun Total Control client Starter dan Growth tidak tertulis di Pre-setup TC; spec memakai env baru `FA_STARTER_TC_PASSWORD` dan `FA_GROWTH_TC_PASSWORD` dan akun yang disediakan tim FE.
  - TC-FA-GRP-84 Expected c "state di-refresh" tidak menyebut apa yang teramati; spec mengasersi sidebar menampilkan Cap Fill.
  - TC-FA-GRP-118 Expected "hanya klik yang memunculkan dialog blok" dianggap sudah teramati di TC-FA-GRP-112 (dialog hanya muncul setelah klik); tidak diasersi terpisah.
  - TC-FA-GRP-112 dan TC-FA-GRP-113 menyebut cap Starter 1 dan Growth 3 sebagai "seed default" `plans.md`; spec memakai client yang berada tepat di cap dan tidak mengasersi angka cap.

