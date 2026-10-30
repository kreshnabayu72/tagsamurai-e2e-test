---
id: TC-GS-ROLE-E2E-078-pencatatan-changelog-remove-baris-target-tc-dan-bulk-remove-per-tier
title: "Pencatatan Changelog: Remove Baris Target Total Control dan Bulk Remove per Tier"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-217
  - TC-GS-ROLE-218
coverage:
  web: automated
---

# Pencatatan Changelog: Remove Baris Target Total Control dan Bulk Remove per Tier

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) | TC |
|---|---|---|---|
| Rudi Hartono | #11 kandidat (Pending Activation) | Di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-59, hanya Rudi Hartono; dipakai sebagai precondition TC, tidak diasersi); baris Manage files dan Manage TAG ada sebagai akibat Total Control | TC-GS-ROLE-217 |
| Wawan Setiawan | #11 kandidat (Active) | Tanpa access level; ditambahkan baris Manage master reference lewat Assign Role (sesi API) | TC-GS-ROLE-218 |
| Siti Nurhaliza | #4 (Read Only, Active, punya baris Manage TAG) | Di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-60 langkah 1 sampai 3; dependensi TC-GS-ROLE-131) | TC-GS-ROLE-218 |
| Rina Putri | #4 (Read Only, Inactive, punya baris Manage TAG) | Read Only (state Pre-setup) | TC-GS-ROLE-218 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada modal Changelog, dicatat pada langkah 1 sampai 9 (sebelum aksi pemicu pertama yang diasersi) dengan nama `B-...` per surface; asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Remove baris role yang memicu konfirmasi auto-revert (target Total Control) dan Bulk Remove tiga baris sekaligus pada satu Detail. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-114 dan TC-GS-ROLE-131) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Rudi Hartono dikembalikan ke tanpa access level dan tanpa baris role (state kandidat Pending Activation); Wawan Setiawan dikembalikan ke tanpa access level dan tanpa baris role; Siti Nurhaliza dan Rina Putri dikembalikan ke Read Only dengan baris Manage TAG masing-masing tetap ada. Efek pada Pre-setup: Modified By dan Last Updated keempat user berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level dan baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-217 dan TC-GS-ROLE-218)

1. Klik Tab System, klik Role Name `Manage files`, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter, catat total hasil sebagai `B-RH-DET`
2. Tutup modal Changelog dengan `✕`, klik breadcrumb `System`, klik Role Name `Manage master reference`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `B-WS-MR`
3. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter, catat total hasil sebagai `B-SN-MR`
4. Ganti isi kotak search dengan `Rina Putri`, tekan Enter, catat total hasil sebagai `B-RP-MR`
5. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter, catat total hasil sebagai `B-RH-SYS`
6. Tutup modal Changelog, klik Tab Total Control, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter, catat total hasil sebagai `B-RH-TC`
7. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter, catat total hasil sebagai `B-SN-TC`
8. Tutup modal Changelog, klik Tab Read Only, klik [Changelog], ketik Search `Rina Putri`, tekan Enter, catat total hasil sebagai `B-RP-RO`
9. Tutup modal Changelog

### TC-GS-ROLE-217: Remove baris target Total Control mencatat Remove dan Auto-Revert terpisah

10. Aksi pemicu (sesi API Ahmad Fauzi): Remove baris Rudi Hartono dari Detail "Manage files" dan konfirmasi `[Remove]` pada dialog auto-revert (setara TC-GS-ROLE-114 langkah 1 sampai 3)
11. Klik Tab System, klik Role Name `Manage files`, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter
12. Verifikasi total hasil Search sama dengan `B-RH-DET` + 1 (tepat 1 entry baru)
13. Verifikasi entry baru (teratas): Action `Remove`, Role — User `Manage files — Rudi Hartono`, Field `Access`
14. Tutup modal Changelog, klik Tab Total Control, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter
15. Verifikasi total hasil Search sama dengan `B-RH-TC` + 1 (tepat 1 entry baru)
16. Verifikasi entry baru (teratas): Action `Auto-Revert`, User Name `Rudi Hartono`
17. Tutup modal Changelog, klik Tab System, klik [Changelog], ketik Search `Rudi Hartono`, tekan Enter
18. Verifikasi total hasil Search sama dengan `B-RH-SYS` + 1 (hanya entry Remove dari langkah 13; tidak ada entry per-role untuk role lain Rudi Hartono)

### TC-GS-ROLE-218: Bulk Remove mencatat satu entry per baris dan Auto-Revert per user tier

19. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): Bulk Remove baris Wawan Setiawan, Siti Nurhaliza (Total Control), dan Rina Putri (Read Only) dari Detail "Manage master reference" (setara TC-GS-ROLE-131 langkah 1 sampai 2)
20. Klik Role Name `Manage master reference`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
21. Verifikasi total hasil Search sama dengan `B-WS-MR` + 1 (tepat 1 entry Remove baru, tanpa duplikat)
22. Verifikasi entry baru (teratas): Action `Remove`
23. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter
24. Verifikasi total hasil Search sama dengan `B-SN-MR` + 1 (tepat 1 entry Remove baru, tanpa duplikat)
25. Verifikasi entry baru (teratas): Action `Remove`
26. Ganti isi kotak search dengan `Rina Putri`, tekan Enter
27. Verifikasi total hasil Search sama dengan `B-RP-MR` + 1 (tepat 1 entry Remove baru, tanpa duplikat)
28. Verifikasi entry baru (teratas): Action `Remove`
29. Tutup modal Changelog, klik breadcrumb `System`, klik Tab Total Control, klik [Changelog], ketik Search `Siti Nurhaliza`, tekan Enter
30. Verifikasi total hasil Search sama dengan `B-SN-TC` + 1 (tepat 1 entry Auto-Revert baru)
31. Verifikasi entry baru (teratas): Action `Auto-Revert`, User Name `Siti Nurhaliza`
32. Tutup modal Changelog, klik Tab Read Only, klik [Changelog], ketik Search `Rina Putri`, tekan Enter
33. Verifikasi total hasil Search sama dengan `B-RP-RO` + 1 (tepat 1 entry Auto-Revert baru)
34. Verifikasi entry baru (teratas): Action `Auto-Revert`, User Name `Rina Putri`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 34 langkah. Urutan TC sumber (217, 218) dipertahankan. Dependensi TC-GS-ROLE-114 dan TC-GS-ROLE-131 dijalankan lewat aksi pemicu sesi API (langkah 10 dan 19); Given Rudi Hartono ber-Total Control (setara TC-GS-ROLE-59) dan Siti Nurhaliza ber-Total Control (setara TC-GS-ROLE-60) dijalankan di hook `before` sebelum baseline dicatat, sehingga entry Assign keduanya tidak termasuk entri baru yang diasersi.
- "Entry baru (teratas)" berarti entri teratas pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. "Tanpa duplikat" (TC-GS-ROLE-218 Expected a) dipenuhi oleh selisih tepat +1 per user pada langkah 21, 24, dan 27; "tepat 3 entry Remove" dipenuhi oleh ketiga langkah itu bersama.
- Langkah 18 menyatakan "tidak ada entry per-role untuk role lain Rudi Hartono" sebagai asersi jumlah terhadap baseline Tab System (superset semua role), dengan anchor positif entry Remove baris Manage files pada langkah 13.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog, berpindah tab atau Detail lewat breadcrumb `System`, dan mengganti isi kotak search (langkah 1 sampai 9, 11, 14, 17, 20, 23, 26, 29, 32); aksi pemicu API (langkah 10 dan 19).
- Temuan untuk QA:
  - TC-GS-ROLE-217 Expected b dan TC-GS-ROLE-218 Expected b tidak menyebut kolom Field, Old Value, New Value, dan Modified By entry Auto-Revert; spec hanya mengasersi Action dan User Name (User Name dari Search nama).
  - TC-GS-ROLE-217 Expected c ("tidak ada entry per-role untuk role lain") tidak menyebut surface; spec memakai Tab System sebagai superset semua role.
  - TC-GS-ROLE-217 sampai TC-GS-ROLE-218 tidak mendefinisikan cara menghitung entri pada modal Changelog dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
