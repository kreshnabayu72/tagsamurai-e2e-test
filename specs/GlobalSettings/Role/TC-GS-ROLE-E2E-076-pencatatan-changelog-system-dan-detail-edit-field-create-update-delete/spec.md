---
id: TC-GS-ROLE-E2E-076-pencatatan-changelog-system-dan-detail-edit-field-create-update-delete
title: "Pencatatan Changelog Tab System dan Detail: Edit Field Create, Update, dan Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-212
  - TC-GS-ROLE-213
  - TC-GS-ROLE-214
coverage:
  web: automated
---

# Pencatatan Changelog Tab System dan Detail: Edit Field Create, Update, dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`): Doni Pratama (#10, Staff, IT) sebagai user target tiga Edit CRUD.

| Baris role Doni Pratama | State awal | Edit CRUD di spec ini | TC |
|---|---|---|---|
| Manage hardware | Baris ditambahkan di hook `before` lewat sesi API (setara Assign Role; Read checked, Create unchecked) sebagai Given precondition TC, tidak diasersi | Create: `Inactive` menjadi `Active` | TC-GS-ROLE-212 |
| Manage TAG | Pre-setup #10: Read checked, Update unchecked | Update: `Inactive` menjadi `Active` | TC-GS-ROLE-213 |
| Manage files | Pre-setup #10: Read dan Delete checked | Delete: `Active` menjadi `Inactive` | TC-GS-ROLE-214 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search `Doni Pratama` pada modal Changelog, dicatat pada langkah 1 sampai 4 (sebelum aksi pemicu pertama yang diasersi) sebagai `B-212-DET`, `B-213-DET`, `B-214-DET`, dan `B-SYS`; asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Edit CRUD satu kolom pada satu baris role (tersimpan langsung tanpa dialog, setara TC-GS-ROLE-101 langkah 1) dan Assign Role untuk Given. Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: baris Manage hardware milik Doni Pratama dihapus; Update Manage TAG dikembalikan `Inactive`; Delete Manage files dikembalikan `Active`. Efek pada Pre-setup: Modified By dan Last Updated baris Doni Pratama berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam; Date entri Tab System dibandingkan dengan Date entri Detail yang sama (S-12).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-212, 213, 214)

1. Klik Tab System, klik Role Name `Manage hardware` untuk membuka Detail, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-212-DET`
2. Tutup modal Changelog dengan `✕`, klik breadcrumb `System`, klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-213-DET`
3. Tutup modal Changelog, klik breadcrumb `System`, klik Role Name `Manage files`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-214-DET`
4. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-SYS`
5. Tutup modal Changelog

### TC-GS-ROLE-212: Edit Field Create

6. Aksi pemicu (sesi API Ahmad Fauzi): centang Create baris Doni Pratama di Detail "Manage hardware"
7. Klik Role Name `Manage hardware`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
8. Verifikasi total hasil Search sama dengan `B-212-DET` + 1 (tepat 1 entry baru)
9. Verifikasi entry baru (teratas): Action `Edit`, Role — User `Manage hardware — Doni Pratama`, Field `Create`, Old Value `Inactive`, New Value `Active`, Modified By `Ahmad F`; catat Date entry sebagai `D-212`
10. Verifikasi tidak ada entry baru untuk kolom CRUD lain (Field `Read`, `Update`, atau `Delete`); satu-satunya entry baru adalah Field `Create` pada langkah 9
11. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
12. Verifikasi total hasil Search sama dengan `B-SYS` + 1
13. Verifikasi entry yang sama tampil (teratas): Action `Edit`, Role — User `Manage hardware — Doni Pratama`, Field `Create`, Old Value `Inactive`, New Value `Active`, Modified By `Ahmad F`, Date sama dengan `D-212`

### TC-GS-ROLE-213: Edit Field Update

14. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): centang Update baris Doni Pratama di Detail "Manage TAG" (setara TC-GS-ROLE-101 langkah 1)
15. Klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
16. Verifikasi total hasil Search sama dengan `B-213-DET` + 1 (tepat 1 entry baru)
17. Verifikasi entry baru (teratas): Action `Edit`, Role — User `Manage TAG — Doni Pratama`, Field `Update`, Old Value `Inactive`, New Value `Active`, Modified By `Ahmad F`; catat Date entry sebagai `D-213`
18. Verifikasi tidak ada entry baru untuk kolom CRUD lain (Field `Read`, `Create`, atau `Delete`); satu-satunya entry baru adalah Field `Update` pada langkah 17
19. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
20. Verifikasi total hasil Search sama dengan `B-SYS` + 2
21. Verifikasi entry yang sama tampil (teratas): Action `Edit`, Role — User `Manage TAG — Doni Pratama`, Field `Update`, Old Value `Inactive`, New Value `Active`, Modified By `Ahmad F`, Date sama dengan `D-213`

### TC-GS-ROLE-214: Edit Field Delete

22. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): hapus centang Delete baris Doni Pratama di Detail "Manage files"
23. Klik Role Name `Manage files`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
24. Verifikasi total hasil Search sama dengan `B-214-DET` + 1 (tepat 1 entry baru)
25. Verifikasi entry baru (teratas): Action `Edit`, Role — User `Manage files — Doni Pratama`, Field `Delete`, Old Value `Active`, New Value `Inactive`, Modified By `Ahmad F`; catat Date entry sebagai `D-214`
26. Verifikasi tidak ada entry baru untuk kolom CRUD lain (Field `Read`, `Create`, atau `Update`); satu-satunya entry baru adalah Field `Delete` pada langkah 25
27. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
28. Verifikasi total hasil Search sama dengan `B-SYS` + 3
29. Verifikasi entry yang sama tampil (teratas): Action `Edit`, Role — User `Manage files — Doni Pratama`, Field `Delete`, Old Value `Active`, New Value `Inactive`, Modified By `Ahmad F`, Date sama dengan `D-214`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 29 langkah. Dependensi TC-GS-ROLE-101 (Edit CRUD Update) dijalankan lewat aksi pemicu sesi API pada langkah 14; Edit Create dan Delete (TC-GS-ROLE-212 dan TC-GS-ROLE-214) tidak punya dependensi TC dan juga dijalankan lewat sesi API (langkah 6 dan 22), karena TC sumber hanya menyatakannya sebagai precondition.
- Satu user target (Doni Pratama) dipakai tiga Edit pada tiga baris role berbeda; tiap TC punya baseline Detail sendiri, dan baseline `B-SYS` Tab System dipakai berurutan (selisih +1, +2, +3). Urutan TC sumber (212, 213, 214) dipertahankan.
- "Entry baru (teratas)" berarti entri teratas pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. Pada Tab System, "entry yang sama" dikenali lewat Role — User, Field, Old Value, dan New Value yang sama dengan entri Detail, ditambah Date yang sama dengan Date entri Detail.
- Langkah 10, 18, dan 26 (TC Expected c, "tidak ada entry untuk kolom CRUD lain") didahului anchor positif: entry Field yang berubah pada langkah sebelumnya pada hasil Search yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog, berpindah tab atau Detail lewat breadcrumb `System`, dan mengganti isi kotak search (langkah 1 sampai 5, 7, 11, 15, 19, 23, 27); aksi pemicu API (langkah 6, 14, 22).
- Temuan untuk QA:
  - TC-GS-ROLE-212 sampai TC-GS-ROLE-214 menulis user target sebagai `[User]` tanpa nama dan tanpa data Pre-setup yang menyebut baris Manage hardware; spec memakai Doni Pratama (Pre-setup #10) dan menambahkan baris Manage hardware sebagai Given.
  - TC-GS-ROLE-212 sampai TC-GS-ROLE-214 menulis "Modified By aktor" tanpa nilai; spec memakai `Ahmad F` (aktor Ahmad Fauzi).
  - TC-GS-ROLE-212 sampai TC-GS-ROLE-214 tidak mendefinisikan cara menghitung entri pada modal Changelog dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
