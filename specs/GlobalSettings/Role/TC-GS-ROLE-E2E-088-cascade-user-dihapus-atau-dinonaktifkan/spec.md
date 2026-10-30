---
id: TC-GS-ROLE-E2E-088-cascade-user-dihapus-atau-dinonaktifkan
title: "Cascade User Dihapus atau Dinonaktifkan pada Tab dan Detail Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-235
  - TC-GS-ROLE-236
coverage:
  web: automated
---

# Cascade User Dihapus atau Dinonaktifkan pada Tab dan Detail Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data milik spec (suffix per run dan nomor spec): `Wawan Setiawan {runId}-088` (email `wawansetiawan+{runId}-088@qwertysystem.net`, Active, Access Global Settings, punya baris Manage TAG). Di-seed lewat API di hook `before` sebagai pengganti Wawan Setiawan Pre-setup #11 supaya aksi Delete tidak menghapus user Pre-setup bersama (S-06). Dihapus oleh TC-GS-ROLE-235; hook `after` menghapus lewat API bila masih ada.
- Data Pre-setup yang diubah: Siti Nurhaliza (Pre-setup #4, Read Only, Active, punya baris Manage TAG). Hook `before` meng-assign Total Control lewat API (precondition b TC-GS-ROLE-236, Dynamic #3). TC-GS-ROLE-236 menonaktifkannya; langkah 12 sampai 15 mengaktifkannya kembali. Hook `after` memulihkan Siti Nurhaliza ke Pre-setup #4 (Active, Total Control dicabut, Read Only di-assign ulang; baris Manage TAG tidak berubah). Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log (log bersifat immutable).
- Kemampuan teknis: seeding dan penghapusan user, penetapan access level dan baris role lewat API (sesi API aktor Total Control); membaca nilai kolom Users dan jumlah total entri Modal Changelog.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-236: User dinonaktifkan tetap tampil di Tab dan Detail

1. Buka Global Settings > User, ketik Search `Siti Nurhaliza`, tekan Enter
2. Klik switch Active baris Siti Nurhaliza (ON)
3. Klik `[Deactivate]` pada dialog
4. Tunggu aksi selesai
5. Buka Role & Permission > Tab Total Control, ketik Search `Siti Nurhaliza`, tekan Enter
6. Verifikasi baris Siti Nurhaliza tampil di Tab Total Control dengan Status `Inactive`
7. Buka Tab System > Detail "Manage TAG", ketik Search `Siti Nurhaliza`, tekan Enter
8. Verifikasi baris Siti Nurhaliza tampil di Detail "Manage TAG"
9. Klik `⋯` pada baris Siti Nurhaliza
10. Verifikasi row action `Remove` enabled
11. Tutup row action menu dengan Esc
12. Buka Global Settings > User, ketik Search `Siti Nurhaliza`, tekan Enter
13. Klik switch Active baris Siti Nurhaliza (OFF)
14. Klik `[Activate]` pada dialog
15. Tunggu aksi selesai

### TC-GS-ROLE-235: User dihapus di modul User hilang dari Detail role

16. Buka Tab System, catat nilai kolom Users role `Manage TAG` sebagai baseline Users
17. Buka Modal Changelog Tab System, catat jumlah total entri sebagai baseline Changelog, tutup modal
18. Buka Global Settings > User, ketik Search `Wawan Setiawan {runId}-088`, tekan Enter
19. Klik `⋯` pada baris `Wawan Setiawan {runId}-088`, pilih `Delete`
20. Klik `[Delete]` pada dialog
21. Tunggu aksi selesai
22. Buka Role & Permission > Tab System > Detail "Manage TAG", ketik Search `Wawan Setiawan {runId}-088`, tekan Enter
23. Verifikasi empty state `No results found` tampil di Detail "Manage TAG"
24. Buka Tab System
25. Verifikasi kolom Users role `Manage TAG` sama dengan baseline langkah 16 dikurangi 1
26. Buka Modal Changelog Tab System
27. Verifikasi jumlah total entri sama dengan baseline langkah 17 (tidak ada entri baru)
28. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dibalik dari TC sumber: TC-GS-ROLE-236 (user tetap ada, dinonaktifkan lalu diaktifkan kembali) lebih dulu, TC-GS-ROLE-235 (Delete, aksi yang menghabiskan data) paling akhir (bagian 3 prinsip 5). Dua TC memakai user yang berbeda sehingga tidak ada ketergantungan data.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search user target (langkah 1, 12, 18); "Tunggu aksi selesai" (langkah 4, 15, 21); mencatat baseline (langkah 16, 17); membuka dan menutup Modal Changelog (langkah 17, 26, 28); menutup row action menu dengan Esc (langkah 11); pemulihan Siti Nurhaliza (langkah 12 sampai 15).
- Urutan Expected TC-GS-ROLE-235: a (langkah 23), b (langkah 25), c (langkah 27).
- Nama `Wawan Setiawan {runId}-088` menggantikan Wawan Setiawan Pre-setup #11 karena identitas user tidak memengaruhi perilaku yang diuji dan aksi Delete tidak boleh menghapus Pre-setup bersama (S-06).
- Temuan untuk QA:
  - TC-GS-ROLE-236 Langkah Uji 3 ("centang/edit tidak dilakukan; buka overlay (⋯) baris") ambigu tentang baris yang dibuka overlay-nya dan tidak menyebut Remove sebagai row action; spec memakai overlay `⋯` baris Siti Nurhaliza di Detail "Manage TAG" dan memverifikasi row action `Remove` enabled sesuai Expected b.
  - TC-GS-ROLE-236 memakai Siti Nurhaliza dari Pre-setup #4 (Read Only) sedangkan precondition b menyebut "Siti Nurhaliza (Total Control)"; spec meng-assign Total Control sebagai Given.
  - TC-GS-ROLE-235 Expected c ("Tidak ada entry baru di Changelog Role & Permission") dan Langkah Uji 2 menyebut Changelog Tab System; spec memeriksa Changelog Tab System.
  - Mekanisme seeding user dan penetapan access level lewat API disediakan tim FE/BE (tidak didefinisikan TC).
