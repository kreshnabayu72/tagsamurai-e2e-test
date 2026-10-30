---
id: TC-GS-ROLE-E2E-077-pencatatan-changelog-system-dan-detail-assign-remove-baris-dan-superset
title: "Pencatatan Changelog Tab System dan Detail: Assign dan Remove Baris Role serta Tab System sebagai Superset Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-215
  - TC-GS-ROLE-216
  - TC-GS-ROLE-219
coverage:
  web: automated
---

# Pencatatan Changelog Tab System dan Detail: Assign dan Remove Baris Role serta Tab System sebagai Superset Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal | Aksi di spec ini | TC |
|---|---|---|---|---|
| Wawan Setiawan | #11 kandidat (Active) | Tanpa access level, tanpa baris role | Assign baris Manage TAG (Read checked), lalu Update Manage TAG dicentang | TC-GS-ROLE-215, TC-GS-ROLE-219 |
| Nina Kartika | #11 kandidat (Active) | Tanpa access level, tanpa baris role | Assign baris Manage TAG (Read checked) | TC-GS-ROLE-215 |
| Doni Pratama | #10 (Staff, IT) | Manage TAG: Read checked, Update unchecked; Manage files: Read dan Delete checked | Remove baris Manage TAG, lalu Delete Manage files dihapus centang | TC-GS-ROLE-216, TC-GS-ROLE-219 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada modal Changelog: Detail "Manage TAG" (`B-WS-DET`, `B-NK-DET`, `B-DP-DET`) dan Tab System (`B-WS-SYS`, `B-NK-SYS`, `B-DP-SYS`), dicatat pada langkah 1 sampai 6 (sebelum aksi pemicu pertama yang diasersi); asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign Role (Manage TAG) ke dua user, Remove baris role, dan Edit CRUD satu kolom (tersimpan langsung tanpa dialog). Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-94, TC-GS-ROLE-112, TC-GS-ROLE-101) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: baris Manage TAG milik Wawan Setiawan dan Nina Kartika dihapus (kembali ke state kandidat, tanpa baris role); baris Manage TAG milik Doni Pratama ditambahkan kembali (Read checked, Update unchecked); Delete Manage files milik Doni Pratama dikembalikan `Active`. Efek pada Pre-setup: Modified By dan Last Updated baris yang dipulihkan berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-215, 216, 219)

1. Klik Tab System, klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `B-WS-DET`
2. Ganti isi kotak search dengan `Nina Kartika`, tekan Enter, catat total hasil sebagai `B-NK-DET`
3. Ganti isi kotak search dengan `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-DP-DET`
4. Tutup modal Changelog dengan `✕`, klik breadcrumb `System`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `B-WS-SYS`
5. Ganti isi kotak search dengan `Nina Kartika`, tekan Enter, catat total hasil sebagai `B-NK-SYS`
6. Ganti isi kotak search dengan `Doni Pratama`, tekan Enter, catat total hasil sebagai `B-DP-SYS`
7. Tutup modal Changelog

### TC-GS-ROLE-215: Entry Assign baris role

8. Aksi pemicu (sesi API Ahmad Fauzi): Assign baris Manage TAG ke Wawan Setiawan dan Nina Kartika (setara TC-GS-ROLE-94 langkah 1 sampai 3)
9. Klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
10. Verifikasi total hasil Search sama dengan `B-WS-DET` + 1 (tepat 1 entry baru)
11. Verifikasi entry baru (teratas): Action `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`
12. Verifikasi tidak ada entry Edit tambahan untuk Read; satu-satunya entry baru adalah Assign pada langkah 11
13. Ganti isi kotak search dengan `Nina Kartika`, tekan Enter
14. Verifikasi total hasil Search sama dengan `B-NK-DET` + 1 (tepat 1 entry baru)
15. Verifikasi entry baru (teratas): Action `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`
16. Verifikasi tidak ada entry Edit tambahan untuk Read; satu-satunya entry baru adalah Assign pada langkah 15
17. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
18. Verifikasi total hasil Search sama dengan `B-WS-SYS` + 1 (tepat 1 entry baru)
19. Verifikasi entry baru (teratas): Action `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`
20. Ganti isi kotak search dengan `Nina Kartika`, tekan Enter
21. Verifikasi total hasil Search sama dengan `B-NK-SYS` + 1 (tepat 1 entry baru)
22. Verifikasi entry baru (teratas): Action `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`

### TC-GS-ROLE-216: Entry Remove baris role

23. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): Remove baris Doni Pratama dari Detail "Manage TAG" (setara TC-GS-ROLE-112 langkah 1 sampai 2)
24. Klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
25. Verifikasi total hasil Search sama dengan `B-DP-DET` + 1 (tepat 1 entry baru)
26. Verifikasi entry baru (teratas): Action `Remove`, Role — User `Manage TAG — Doni Pratama`, Field `Access`, Old Value `Assigned`, New Value `—`
27. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Doni Pratama`, tekan Enter
28. Verifikasi total hasil Search sama dengan `B-DP-SYS` + 1 (tepat 1 entry baru)
29. Verifikasi entry baru (teratas): Action `Remove`, Role — User `Manage TAG — Doni Pratama`, Field `Access`, Old Value `Assigned`, New Value `—`

### TC-GS-ROLE-219: Changelog Detail memuat entry role itu saja, Changelog System superset

30. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): centang Update baris Wawan Setiawan di Detail "Manage TAG" (Edit CRUD, setara TC-GS-ROLE-101 langkah 1)
31. Aksi pemicu (sesi API Ahmad Fauzi): hapus centang Delete baris Doni Pratama di Detail "Manage files" (Edit CRUD)
32. Klik Role Name `Manage TAG`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
33. Verifikasi entry Edit tampil di Changelog Detail "Manage TAG" (teratas): Action `Edit`, Role — User `Manage TAG — Wawan Setiawan`, Field `Update`
34. Ganti isi kotak search dengan `Doni Pratama`, tekan Enter
35. Verifikasi total hasil Search sama dengan `B-DP-DET` + 1 (hanya entry Remove dari langkah 23; Changelog Detail "Manage TAG" tidak memuat entry `Manage files — Doni Pratama`)
36. Tutup modal Changelog, klik breadcrumb `System`, klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
37. Verifikasi Changelog Tab System memuat entry Manage TAG (teratas): Action `Edit`, Role — User `Manage TAG — Wawan Setiawan`, Field `Update`
38. Ganti isi kotak search dengan `Doni Pratama`, tekan Enter
39. Verifikasi total hasil Search sama dengan `B-DP-SYS` + 2 (entry Remove Manage TAG dari langkah 23 dan entry Edit Manage files baru)
40. Verifikasi Changelog Tab System memuat entry Manage files (teratas): Action `Edit`, Role — User `Manage files — Doni Pratama`, Field `Delete`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 40 langkah nominal. Alasan di atas sekitar 35 langkah: seluruh spec satu kelas (pencatatan Changelog Detail dan Tab System), dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) serta baseline, yang tidak dihitung ke ambang (bagian 3 konvensi). TC-GS-ROLE-215 membaca dua user pada dua surface, sehingga jumlah blok baca-log berlipat; tiap blok berdiri sendiri dengan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber (215, 216, 219) dipertahankan. TC-GS-ROLE-219 berjalan terakhir karena memakai Wawan Setiawan (baris Manage TAG hasil TC-GS-ROLE-215) dan Doni Pratama (sesudah Remove baris Manage TAG pada TC-GS-ROLE-216); entry Edit Manage TAG dan Manage files yang diminta Precondition TC-GS-ROLE-219 dibuat oleh aksi pemicu langkah 30 dan 31 dan diasersi, sehingga baseline `B-DP-DET` dan `B-DP-SYS` dicatat sebelumnya.
- Dependensi TC-GS-ROLE-94, 112, dan 101 dijalankan lewat aksi pemicu sesi API (langkah 8, 23, 30). Edit Delete pada Manage files milik Doni Pratama (langkah 31) tidak punya dependensi TC dan memakai pola yang sama.
- "Entry baru (teratas)" berarti entri teratas pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. Langkah 35 adalah asersi jumlah terhadap baseline (bukan absence): entry Edit Manage files milik Doni Pratama yang baru tercatat tidak menambah hasil Search di Detail "Manage TAG", sedangkan di Tab System hasil Search bertambah 2 (langkah 39). Entry Manage TAG pada Detail tampil sebagai anchor positif di langkah 33.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog, berpindah tab atau Detail lewat breadcrumb `System`, dan mengganti isi kotak search (langkah 1 sampai 7, 9, 13, 17, 20, 24, 27, 32, 34, 36, 38); aksi pemicu API (langkah 8, 23, 30, 31).
- Temuan untuk QA:
  - TC-GS-ROLE-219 Expected a menyebut "hanya memuat entry ber-Role — User 'Manage TAG — …'" (asersi universal); spec memverifikasinya lewat total hasil Search nama user yang memuat entry Manage TAG dan yang diubah di role lain (langkah 35), bukan lewat pemeriksaan seluruh baris modal karena modal dapat memuat banyak halaman dari run sebelumnya.
  - TC-GS-ROLE-219 Precondition tidak menyebut user dan kolom CRUD yang di-Edit; spec memakai Update Manage TAG milik Wawan Setiawan dan Delete Manage files milik Doni Pratama (Pre-setup #10).
  - TC-GS-ROLE-215 dan TC-GS-ROLE-216 tidak mendefinisikan cara menghitung entri pada modal Changelog dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
