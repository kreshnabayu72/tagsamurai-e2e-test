---
id: TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert
title: "Pencatatan Changelog Tab Total Control: Assign, Upgrade dari Read Only, Remove, dan Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-207
  - TC-GS-ROLE-208
  - TC-GS-ROLE-209
  - TC-GS-ROLE-210
coverage:
  web: automated
---

# Pencatatan Changelog Tab Total Control: Assign, Upgrade dari Read Only, Remove, dan Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) | Dipakai di TC |
|---|---|---|---|
| Sari Wulandari | #11 kandidat (Active) | Tanpa access level dan tanpa baris role | TC-GS-ROLE-207, TC-GS-ROLE-209 |
| Siti Nurhaliza | #4 (Read Only, Active, punya baris Manage TAG) | Read Only | TC-GS-ROLE-208 |
| Maya Anggraini | #11 kandidat (Inactive) | Di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-59, hanya Maya Anggraini; Rudi Hartono tidak diasersi di spec ini sehingga tidak di-assign); baris Manage TAG punya Update checked | TC-GS-ROLE-210 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada modal Changelog, dicatat pada langkah 1 sampai 7 (sebelum aksi pemicu pertama yang diasersi); asersi "entry baru" memakai selisih terhadap baseline itu (`B-207`, `B-208`, `B-210`, `B-208-RO`, `B-207-SYS`, `B-209-DET`, `B-210-DET`). Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign Total Control, Assign Total Control ke user Read Only (upgrade), Remove Total Control, serta Edit CRUD pada baris Manage TAG beserta konfirmasi `[Remove]` auto-revert. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58, TC-GS-ROLE-60, TC-GS-ROLE-86, TC-GS-ROLE-106) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Sari Wulandari dikembalikan ke tanpa access level dan tanpa baris role; Siti Nurhaliza dikembalikan ke Read Only (Remove Total Control lalu Assign Read Only; baris Manage TAG milik Siti Nurhaliza dikembalikan bila berubah); Maya Anggraini dikembalikan ke tanpa access level dan tanpa baris role. Efek pada Pre-setup: Modified By dan Last Updated Siti Nurhaliza dan Maya Anggraini berubah menjadi `Ahmad F` dan waktu pemulihan; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-207, 208, 209, 210)

1. Klik [Changelog] pada Table Tools Tab Total Control, ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `B-207`
2. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter, catat total hasil sebagai `B-208`
3. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter, catat total hasil sebagai `B-210`
4. Tutup modal Changelog dengan `✕`, klik Tab Read Only, klik [Changelog], ketik Search `Siti Nurhaliza`, tekan Enter, catat total hasil sebagai `B-208-RO`
5. Tutup modal Changelog, klik Tab System, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `B-207-SYS`
6. Tutup modal Changelog, klik Role Name `Manage TAG` untuk membuka Detail, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `B-209-DET`
7. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter, catat total hasil sebagai `B-210-DET`
8. Tutup modal Changelog

### TC-GS-ROLE-207: Changelog Total Control, entry Assign user baru

9. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Sari Wulandari (setara TC-GS-ROLE-58 langkah 1 sampai 3)
10. Buka Global Settings > Role & Permission > Tab Total Control, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
11. Verifikasi total hasil Search sama dengan `B-207` + 1 (tepat 1 entry baru)
12. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 11): Action `Assign`, User Name `Sari Wulandari`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Ahmad F`
13. Tutup modal Changelog, klik Tab System, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
14. Verifikasi total hasil Search sama dengan `B-207-SYS` (tidak ada entry Sari Wulandari baru di Changelog Tab System)

### TC-GS-ROLE-208: Changelog Total Control, entry Assign upgrade dari Read Only

15. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Siti Nurhaliza (upgrade dari Read Only, setara TC-GS-ROLE-60 langkah 1 sampai 3)
16. Tutup modal Changelog, buka Global Settings > Role & Permission > Tab Total Control, klik [Changelog], ketik Search `Siti Nurhaliza`, tekan Enter
17. Verifikasi total hasil Search sama dengan `B-208` + 1 (tepat 1 entry baru)
18. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 17): Action `Assign`, User Name `Siti Nurhaliza`, Field `Access Level`, Old Value `Read Only`, New Value `Total Control`, Modified By `Ahmad F`
19. Tutup modal Changelog, klik Tab Read Only, klik [Changelog], ketik Search `Siti Nurhaliza`, tekan Enter
20. Verifikasi total hasil Search sama dengan `B-208-RO` (tidak ada entry baru untuk Siti Nurhaliza akibat upgrade; tidak ada entry Remove atau Auto-Revert)

### TC-GS-ROLE-209: Changelog Total Control, entry Remove

21. Aksi pemicu (sesi API Ahmad Fauzi): Remove Total Control dari Sari Wulandari (setara TC-GS-ROLE-86 langkah 1 sampai 2)
22. Tutup modal Changelog, buka Global Settings > Role & Permission > Tab Total Control, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
23. Verifikasi total hasil Search sama dengan `B-207` + 2 (entry Assign dari langkah 9 dan tepat 1 entry Remove baru)
24. Verifikasi entry Remove baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 23): Action `Remove`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`
25. Tutup modal Changelog, klik Tab System, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
26. Verifikasi total hasil Search sama dengan `B-207-SYS` (Changelog Tab System tidak memuat entry Remove per-role untuk Sari Wulandari)
27. Tutup modal Changelog, klik Role Name `Manage TAG` untuk membuka Detail, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
28. Verifikasi total hasil Search sama dengan `B-209-DET` (Changelog Detail "Manage TAG" tidak memuat entry Remove per-role untuk Sari Wulandari)

### TC-GS-ROLE-210: Changelog Total Control, entry Auto-Revert

29. Aksi pemicu (sesi API Ahmad Fauzi): hapus centang Update baris Manage TAG milik Maya Anggraini dan konfirmasi `[Remove]` (setara TC-GS-ROLE-106 langkah 1 sampai 2)
30. Tutup modal Changelog, buka Global Settings > Role & Permission > Tab Total Control, klik [Changelog], ketik Search `Maya Anggraini`, tekan Enter
31. Verifikasi total hasil Search sama dengan `B-210` + 1 (tepat 1 entry baru)
32. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 31): Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, New Value `—`
33. Verifikasi Modified By entry Auto-Revert adalah `Ahmad F` (bukan `System`)
34. Tutup modal Changelog, klik Tab System, klik Role Name `Manage TAG` untuk membuka Detail, klik [Changelog], ketik Search `Maya Anggraini`, tekan Enter
35. Verifikasi total hasil Search sama dengan `B-210-DET` + 1 (entry Edit pemicu tercatat terpisah di Changelog "Manage TAG")
36. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 35): Action `Edit`, Role — User `Manage TAG — Maya Anggraini`, Field `Update`, Old Value `Active`, New Value `Inactive`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 36 langkah nominal. Alasan di atas sekitar 35 langkah: seluruh spec satu kelas (pencatatan Changelog Tab Total Control, dibaca di Role & Permission), dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) serta baseline, yang tidak dihitung ke ambang (bagian 3 konvensi). Tiap blok TC berdiri sendiri dengan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; satu-satunya keterkaitan data adalah Sari Wulandari pada TC-GS-ROLE-207 dan TC-GS-ROLE-209 (Assign lalu Remove), sesuai Dependensi TC sumber.
- Urutan TC sumber (207, 208, 209, 210) dipertahankan. TC-GS-ROLE-209 (Remove Sari Wulandari) berjalan sesudah TC-GS-ROLE-207 karena Remove membutuhkan Sari Wulandari ber-Total Control hasil Assign TC-GS-ROLE-207.
- Dependensi TC-GS-ROLE-58, 60, 86, dan 106 dijalankan lewat aksi pemicu sesi API (langkah 9, 15, 21, 29). Given Maya Anggraini ber-Total Control (setara TC-GS-ROLE-59) dijalankan di hook `before` dan tidak diasersi di spec ini (dipakai sebagai precondition TC, tidak diasersi); Assign Maya Anggraini oleh hook terjadi sebelum baseline `B-210` dan `B-210-DET` dicatat.
- "Entry baru" dikenali lewat kombinasi kolom yang diasersi pada langkah Verifikasinya dan selisih jumlah terhadap baseline, bukan lewat posisi baris (S-12, S-14); urutan antar-entri yang jatuh pada menit yang sama tidak diasersi karena kolom Date berketelitian menit.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog, berpindah tab, membuka Detail, dan mengganti isi kotak search (langkah 2 sampai 8, 10, 13, 16, 19, 22, 25, 27, 30, 34); aksi pemicu API (langkah 9, 15, 21, 29).
- TC-GS-ROLE-207 Expected b, TC-GS-ROLE-208 Expected b, dan TC-GS-ROLE-209 Expected b ditulis sebagai asersi jumlah terhadap baseline (langkah 14, 20, 26, 28), bukan asersi absence kelas g: tiap aksi pemicu punya aksi nyata di spec ini, dan jumlah entri sebelum aksi dicatat sebagai baseline.
- Temuan untuk QA:
  - TC-GS-ROLE-209 Expected b menyebut "Changelog Tab System dan Detail" tanpa menyebut role Detail-nya; spec memakai Detail "Manage TAG" (role yang sama dengan TC-GS-ROLE-210 dan TC-GS-ROLE-213).
  - TC-GS-ROLE-207 sampai TC-GS-ROLE-210 menyebut "tepat 1 entry" tanpa mendefinisikan cara menghitung entri pada modal Changelog (kontrol total tidak disebut TC maupun PRD) dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
  - TC-GS-ROLE-210 Expected b tidak menyebut Role — User entry Edit pemicu; spec memakai pola `Manage TAG — Maya Anggraini` dari TC-GS-ROLE-213 Expected a. Modified By entry Auto-Revert (Expected a, "bukan System") diasersi pada langkah 33.
