---
id: TC-GS-ROLE-E2E-081-pencatatan-system-log-aktor-dan-activity-log-baris-role
title: "Pencatatan System Log Aktor dan Activity Log untuk Edit, Assign, dan Remove Baris Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-222
coverage:
  web: automated
---

# Pencatatan System Log Aktor dan Activity Log untuk Edit, Assign, dan Remove Baris Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal | Aksi pemicu di spec ini |
|---|---|---|---|
| Doni Pratama | #10 (Staff, IT) | Manage TAG: Read checked, Update unchecked | Update Manage TAG dicentang (Edit), lalu baris Manage TAG di-Remove |
| Wawan Setiawan | #11 kandidat (Active) | Tanpa access level dan tanpa baris role | Assign baris Manage TAG |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada System Log Ahmad Fauzi (`S-DP`, `S-WS`) dan pada Activity Log (`A-DP`, `A-WS`), dicatat pada langkah 1 sampai 4 (sebelum aksi pemicu pertama yang diasersi); asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada System Log dan Activity Log disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Edit CRUD satu kolom (tersimpan langsung tanpa dialog), Assign Role, dan Remove baris role. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-101, TC-GS-ROLE-94, TC-GS-ROLE-112) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: baris Manage TAG milik Wawan Setiawan dihapus (kembali ke state kandidat); baris Manage TAG milik Doni Pratama ditambahkan kembali dengan Read checked dan Update unchecked. Efek pada Pre-setup: Modified By dan Last Updated baris Doni Pratama berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-222)

1. Buka Global Settings > User > Ahmad Fauzi > Tab System Log, ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `S-DP`
2. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `S-WS`
3. Buka Global Settings > Activity Log, ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `A-DP`
4. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `A-WS`

### TC-GS-ROLE-222: System Log aktor dan Activity Log untuk Edit, Assign, dan Remove baris role

5. Aksi pemicu (sesi API Ahmad Fauzi): centang Update baris Doni Pratama di Detail "Manage TAG" (setara TC-GS-ROLE-101 langkah 1)
6. Aksi pemicu (sesi API Ahmad Fauzi): Assign baris Manage TAG ke Wawan Setiawan (setara TC-GS-ROLE-94 langkah 1 sampai 3, hanya Wawan Setiawan)
7. Aksi pemicu (sesi API Ahmad Fauzi): Remove baris Doni Pratama dari Detail "Manage TAG" (setara TC-GS-ROLE-112 langkah 1 sampai 2)
8. Buka Global Settings > User > Ahmad Fauzi > Tab System Log, ketik Search `Doni Pratama`, tekan Enter
9. Verifikasi total hasil Search sama dengan `S-DP` + 2 (entry Edit dan entry Remove baru)
10. Verifikasi entry Remove (teratas) pada System Log: Action `Remove`, Object `System Role`, Name `Doni Pratama`, Field `Manage TAG`, Old Value `Assigned`, New Value `—`; catat Date entry sebagai `D-DP-REMOVE`
11. Verifikasi entry Edit (kedua) pada System Log: Action `Edit`, Object `System Role`, Name `Doni Pratama`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`; catat Date entry sebagai `D-DP-EDIT`
12. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
13. Verifikasi total hasil Search sama dengan `S-WS` + 1 (tepat 1 entry baru)
14. Verifikasi entry baru (teratas) pada System Log: Action `Assign`, Object `System Role`, Name `Wawan Setiawan`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`; catat Date entry sebagai `D-WS-ASSIGN`
15. Buka Global Settings > Activity Log, ketik Search `Doni Pratama`, tekan Enter
16. Verifikasi total hasil Search sama dengan `A-DP` + 2 (baris Edit dan baris Remove baru)
17. Verifikasi baris Remove (teratas) pada Activity Log: Action `Remove`, Object `System Role`, Name `Doni Pratama`, Field `Manage TAG`, Old Value `Assigned`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-DP-REMOVE`
18. Verifikasi baris Edit (kedua) pada Activity Log: Action `Edit`, Object `System Role`, Name `Doni Pratama`, Field `Manage TAG — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Ahmad F`, Date sama dengan `D-DP-EDIT`
19. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
20. Verifikasi total hasil Search sama dengan `A-WS` + 1 (tepat 1 baris baru)
21. Verifikasi baris baru (teratas) pada Activity Log: Action `Assign`, Object `System Role`, Name `Wawan Setiawan`, Field `Manage TAG`, Old Value `—`, New Value `Assigned`, Modified By `Ahmad F`, Date sama dengan `D-WS-ASSIGN`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Satu TC sumber; subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Dependensi TC-GS-ROLE-101, 94, dan 112 dijalankan lewat aksi pemicu sesi API (langkah 5 sampai 7). Urutan aksi Edit (Doni Pratama), Assign (Wawan Setiawan), lalu Remove (Doni Pratama) mengikuti urutan Expected a, b, c; semua aksi pemicu dijalankan sebelum surface log dibuka, supaya satu pembukaan System Log dan satu pembukaan Activity Log membaca seluruh entri. Nina Kartika tidak di-assign karena tidak diasersi di spec ini (seeding minimal, S-11).
- "Entry baru (teratas)" dan "(kedua)" berarti urutan pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12) karena Expected d "baris yang sama".
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah ke System Log atau Activity Log dan mengganti isi kotak search (langkah 1 sampai 4, 8, 12, 15, 19); aksi pemicu API (langkah 5 sampai 7).
- Temuan untuk QA:
  - TC-GS-ROLE-222 Expected d ("baris yang sama + Modified By") tidak menyebut Date; spec membandingkan Date dengan baris System Log aksi yang sama, dengan dasar frasa "baris yang sama".
  - TC-GS-ROLE-222 tidak mendefinisikan cara menghitung entri pada System Log dan Activity Log dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
