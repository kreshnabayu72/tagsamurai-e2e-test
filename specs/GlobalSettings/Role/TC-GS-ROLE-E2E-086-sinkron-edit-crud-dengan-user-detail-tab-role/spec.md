---
id: TC-GS-ROLE-E2E-086-sinkron-edit-crud-dengan-user-detail-tab-role
title: "Sinkronisasi Edit CRUD antara Detail Role dan Tab Role User Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-231
  - TC-GS-ROLE-232
coverage:
  web: automated
---

# Sinkronisasi Edit CRUD antara Detail Role dan Tab Role User Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah: Wawan Setiawan (Pre-setup #11, Active, Access Global Settings, tanpa baris role). Hook `before` meng-assign baris Manage TAG ke Wawan Setiawan lewat API (Read checked, Update unchecked), setara Dynamic #5 TC-GS-ROLE-94, dipakai sebagai precondition TC (baris tidak diasersi keberadaannya). TC-GS-ROLE-231 mencentang Update dan TC-GS-ROLE-232 meng-uncheck Update. Hook `after` menghapus baris Manage TAG Wawan Setiawan lewat API sehingga kembali ke state kandidat Pre-setup #11. Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log (log bersifat immutable).
- Kemampuan teknis: seeding dan pemulihan baris role lewat API (sesi API aktor Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-231: Edit CRUD dari Detail tercermin di User Detail Tab Role

1. Buka Tab System, lalu Detail "Manage TAG"
2. Ketik Search `Wawan Setiawan`, tekan Enter
3. Centang Update pada baris Wawan Setiawan
4. Tunggu aksi selesai
5. Buka Global Settings > User, ketik Search `Wawan Setiawan`, tekan Enter
6. Buka Detail Wawan Setiawan, klik Tab Role
7. Verifikasi baris Manage TAG di Tab Role: Update checked

### TC-GS-ROLE-232: Edit dari User Detail Tab Role tercermin di Detail role

8. Uncheck Update pada baris Manage TAG di Tab Role Wawan Setiawan
9. Tunggu aksi selesai
10. Buka Role & Permission > Tab System, lalu Detail "Manage TAG"
11. Ketik Search `Wawan Setiawan`, tekan Enter
12. Verifikasi baris Wawan Setiawan: Update unchecked

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-ROLE-231 dijalankan lebih dulu karena Update checked hasilnya menjadi keadaan awal TC-GS-ROLE-232.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search baris target (langkah 2, 5, 11); "Tunggu aksi selesai" sebelum berpindah surface (langkah 4, 9); membuka Detail role dan User Detail (langkah 1, 5, 6, 10).
- Temuan untuk QA:
  - TC-GS-ROLE-231 dan TC-GS-ROLE-232 tidak menyebut baris Manage TAG Wawan Setiawan sebagai precondition; spec men-seed baris itu lewat API (mekanisme seeding disediakan tim FE/BE, tidak didefinisikan TC).
  - TC-GS-ROLE-232 langkah 1 tidak menyebut apakah perubahan di Tab Role User Detail tersimpan langsung atau lewat tombol; spec mengikuti TC tanpa tombol simpan.
  - TC-GS-ROLE-231 dan TC-GS-ROLE-232 tidak menyebut toast hasil edit; spec tidak mengasersinya.
