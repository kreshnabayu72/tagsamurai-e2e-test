---
id: TC-GS-ROLE-E2E-033-konflik-assign-concurrent-user-sama-dua-admin
title: "Konflik Assign: Dua Admin Meng-Assign User yang Sama Secara Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-279
  - TC-GS-ROLE-280
coverage:
  web: automated
---

# Konflik Assign: Dua Admin Meng-Assign User yang Sama Secara Bersamaan

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (c), dua admin dengan dua sesi UI paralel; sesi B (admin kedua) menjadi objek asersi sehingga bukan pemicu `P-2`.
- Akun sesi A (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Akun sesi B: Eko Prasetyo (Total Control, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`; login di konteks browser kedua pada langkah 1 (bukan di hook).
- Layar awal sesi A (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control. Layar sesi B dibuka oleh langkah spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`), termasuk akun Eko Prasetyo.
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-033`; dipulihkan sesuai catatan "Reset Pre-setup per TC" di `tc-role.md`):
  - Zahra Nabila (Pre-setup #18, Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) untuk TC-GS-ROLE-279; memiliki 1 baris Manage hardware sesudahnya (Tabel Dinamis #13).
  - Nina Kartika (Pre-setup #11, Active, state kandidat: tanpa access level dan tanpa baris role) untuk TC-GS-ROLE-280.
  - Wawan Setiawan (Pre-setup #11, kandidat) hanya sebagai baris pembanding di picker Detail "Manage hardware"; tidak diubah.
- Pemulihan: langkah penghubung 19 dan 38 mengembalikan Zahra Nabila (hapus baris Manage hardware) dan Nina Kartika (cabut Total Control); hook `after` menjadi cadangan dan menutup konteks browser kedua.
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): dua konteks browser paralel dengan sesi login terpisah (sesi A dan sesi B) yang dapat diatur urutan aksinya langkah demi langkah; mengatur baris role dan access level user Pre-setup lewat API untuk pemulihan; membaca jumlah entry Modal Changelog dari UI.
- Sesi B ditutup dan sesi login browser terkait dihapus di langkah terakhir (S-09).

## Test Steps

### TC-GS-ROLE-279: Assign Role concurrent ke user yang sama oleh dua admin

1. Buka konteks browser kedua (sesi B) dan login sebagai Eko Prasetyo
2. Sesi A: Buka Tab System
3. Sesi A: Buka Detail "Manage hardware"
4. Sesi B: Buka Global Settings > Role & Permission > Tab System
5. Sesi B: Buka Detail "Manage hardware"
6. Sesi A: Klik `[+ Assign]`
7. Sesi B: Klik `[+ Assign]`
8. Sesi A: Centang Zahra Nabila
9. Sesi B: Centang Zahra Nabila
10. Sesi A: Klik `[Assign]`
11. Verifikasi sesi A: toast sukses `Success, role has been assigned.` tampil
12. Sesi B: Klik `[Assign]`
13. Verifikasi sesi B: alert inline `Zahra Nabila is no longer eligible. Please select another.` tampil
14. Verifikasi sesi B: baris Wawan Setiawan tampil di picker
15. Verifikasi sesi B: tidak ada user tercentang di picker (centangan Zahra Nabila hilang)
16. Sesi A: Ketik Search `Zahra Nabila`, tekan Enter
17. Verifikasi sesi A: Detail "Manage hardware" memuat tepat 1 baris Zahra Nabila
18. Sesi B: Klik `[Cancel]`
19. Pulihkan lewat API: hapus baris Manage hardware milik Zahra Nabila

### TC-GS-ROLE-280: Assign Total Control concurrent ke user yang sama oleh dua admin

20. Sesi A: Buka Tab Total Control
21. Sesi A: Buka Modal Changelog Tab Total Control
22. Sesi A: Catat jumlah entry Assign untuk Nina Kartika sebagai baseline
23. Sesi A: Tutup Modal Changelog
24. Sesi B: Buka Tab Total Control
25. Sesi A: Klik `[+ Assign]`
26. Sesi B: Klik `[+ Assign]`
27. Sesi A: Centang Nina Kartika
28. Sesi B: Centang Nina Kartika
29. Sesi A: Klik `[Assign]`
30. Verifikasi sesi A: toast sukses `Success, Total Control has been assigned.` tampil
31. Sesi B: Klik `[Assign]`
32. Verifikasi sesi B: alert inline `Nina Kartika is no longer eligible. Please select another.` tampil
33. Verifikasi sesi B: popup Assign Total Control tetap terbuka
34. Sesi A: Buka Modal Changelog Tab Total Control
35. Verifikasi sesi A: jumlah entry Assign untuk Nina Kartika bertambah tepat 1 dari baseline pada langkah 22
36. Sesi A: Tutup Modal Changelog
37. Sesi B: Klik `[Cancel]`
38. Pulihkan lewat API: cabut access level Total Control dari Nina Kartika
39. Tutup konteks browser kedua (sesi B) dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (c), dua admin; sesi B adalah objek asersi (Expected b TC-GS-ROLE-279 dan TC-GS-ROLE-280), sehingga sesi UI kedua dipakai dan butir `P-2` tidak berlaku.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 39 langkah nominal. Alasan di atas sekitar 35 langkah: seluruh spec satu kelas harness (multi-konteks, dua admin) dan kedua blok TC berdiri sendiri; TC-GS-ROLE-280 dimulai dari state yang dipulihkan lewat API pada langkah 19, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah terbanyak berasal dari koreografi dua sesi yang harus eksplisit (tiap aksi diberi awalan sesi) dan dari pencatatan baseline.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka Tab System, Detail, dan Tab Total Control (langkah 2 sampai 5, 20, 24), mencatat baseline dan membuka atau menutup Modal Changelog (langkah 21 sampai 23, 34, 36), Search untuk menghitung baris (langkah 16; Search tereset saat sesi A pindah tab pada langkah 20), klik `[Cancel]` menutup popup sesi B (langkah 18 dan 37), pemulihan lewat API (langkah 19 dan 38), dan menutup sesi B (langkah 39).
- Urutan aksi mengikuti TC: kedua sesi mencentang user yang sama sebelum sesi A mengklik `[Assign]`, baru sesi B (S-04); precondition "dua admin membuka popup" dipenuhi langkah 2 sampai 7 dan 20 sampai 26.
- Asersi tambahan di luar kalimat Expected TC (S-03): langkah 14 (baris Wawan Setiawan tampil di picker sesi B) menjadi anchor positif bagi asersi absence centangan pada langkah 15 (bagian 8b butir 2); langkah 16 dan 17 menjadi cara mengamati "Detail hanya memuat 1 baris Zahra Nabila".
- Asersi "jumlah entry Assign Nina Kartika" (langkah 35) memakai baseline jumlah (S-12), bukan posisi entry teratas.
- Temuan untuk QA:
  - TC-GS-ROLE-279 dan TC-GS-ROLE-280 tidak menyebut identitas sesi A dan sesi B; spec memakai Ahmad Fauzi (sesi A, Pre-setup #1) dan Eko Prasetyo (sesi B, Pre-setup #13).
  - TC-GS-ROLE-279 tidak menyebut kondisi picker sesi B yang dapat dijadikan data pembanding; spec memakai Wawan Setiawan (Pre-setup #11, eligible untuk Manage hardware).
  - TC-GS-ROLE-279 dan TC-GS-ROLE-280 menyebut "mencentang" tanpa cara menemukan baris bila picker lebih dari satu halaman; mekanisme menemukan baris diputuskan di tahap script.
  - TC-GS-ROLE-279 Expected b tidak menyebut apakah popup sesi B tetap terbuka (TC-GS-ROLE-280 Expected b menyebutnya); spec hanya mengasersi popup tetap terbuka pada TC-GS-ROLE-280.
