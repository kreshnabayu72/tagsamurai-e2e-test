---
id: TC-GS-ROLE-E2E-048-bulk-remove-satu-baris-dialog-single-dan-klik-ganda
title: "Bulk Remove Satu Baris: Dialog Single dan Klik Ganda pada [Remove]"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-135
  - TC-GS-ROLE-294
  - TC-GS-ROLE-295
coverage:
  web: automated
---

# Bulk Remove Satu Baris: Dialog Single dan Klik Ganda pada [Remove]

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login di hook `before`): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Tidak ada env baru.
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > System > Detail `Manage hardware`. Blok TC-GS-ROLE-295 berpindah ke Detail `Manage master reference` lewat langkah 27.
- Data Dinamis milik spec (hook `before`, lewat seeding API): dua user Access Global Settings tanpa access level dengan baris Manage hardware untuk TC-GS-ROLE-135: `Ganda Satu {runId}-048` (`gandasatu+{runId}-048@qwertysystem.net`) dan `Ganda Dua {runId}-048` (`gandadua+{runId}-048@qwertysystem.net`). Entri Changelog atas dua nama bersuffix ini belum ada sebelum aksi (baseline nol, S-12).
- Data Pre-setup yang dipakai (Tabel Data Uji Pre-setup): Nina Kartika (baris 11, kandidat) dengan baris Manage hardware dari seeding (TC-GS-ROLE-294); Rina Putri (baris 4, Read Only, Inactive) dengan baris Manage master reference dari seeding dan Read Only di-assign ulang bila sudah hilang (Tabel Data Uji Dinamis baris 14; TC-GS-ROLE-295). Siti Nurhaliza (Read Only, baris 4) dipakai sebagai baris pembanding di Tab Read Only.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user `Ganda Satu {runId}-048` dan `Ganda Dua {runId}-048`; hapus baris Manage hardware milik Nina Kartika yang masih ada (aksi spec menghapusnya, sehingga Nina Kartika kembali tanpa baris role); hapus baris Manage master reference milik Rina Putri yang masih ada, lalu kembalikan Read Only Rina Putri (aksi TC-GS-ROLE-295 mencabut Read Only lewat auto-revert; baris Manage TAG milik Rina Putri tidak disentuh). Last Updated Rina Putri berubah dan tidak dipulihkan. Entri Changelog tidak dapat dihapus.
- Kemampuan teknis: klik dua kali cepat pada `[Remove]` (dua klik dalam satu aksi); hover pada komponen user di body dialog; membaca entri Changelog Detail dengan Search per nama bersuffix.
- Kemampuan teknis (seeding): seeding API untuk akses level, baris role, dan data user disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-135: Klik ganda [Remove] dialog Bulk Remove

1. Centang baris `Ganda Satu {runId}-048`
2. Centang baris `Ganda Dua {runId}-048`
3. Klik `Bulk Action`
4. Klik `Remove`
5. Klik `[Remove]` dua kali cepat
6. Verifikasi tepat satu toast sukses `Success, user has been removed.` tampil
7. Klik Changelog di toolbar Detail `Manage hardware`
8. Ketik Search `Ganda Satu {runId}-048`, tekan Enter
9. Verifikasi Changelog memuat tepat 1 entry Action `Remove` untuk `Ganda Satu {runId}-048`
10. Ganti isi kotak search dengan `Ganda Dua {runId}-048`, tekan Enter
11. Verifikasi Changelog memuat tepat 1 entry Action `Remove` untuk `Ganda Dua {runId}-048`
12. Tutup modal Changelog

### TC-GS-ROLE-294: Bulk Remove tepat 1 baris memakai dialog single (target bukan Total Control/Read Only)

13. Centang baris `Nina Kartika`
14. Verifikasi counter `1 User selected`
15. Klik `Bulk Action`
16. Klik `Remove`
17. Verifikasi Title dialog `Remove Access`
18. Verifikasi body dialog memuat bullet `• Nina K` berupa komponen user (ikon user generik + first name + inisial last name)
19. Arahkan kursor ke `Nina K`
20. Verifikasi hover pada `Nina K` menampilkan nama lengkap `Nina Kartika`
21. Verifikasi body dialog memuat kalimat `This will remove Manage hardware access from this user. Are you sure you want to remove it?` (bukan varian bulk `remove them?`)
22. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
23. Klik `[Remove]`
24. Verifikasi toast sukses `Success, user has been removed.`
25. Verifikasi baris `Nina Kartika` hilang dari Detail `Manage hardware`
26. Verifikasi Bulk Action Bar tertutup
27. Buka Tab System, lalu klik role `Manage master reference` untuk membuka Detail-nya

### TC-GS-ROLE-295: Bulk Remove tepat 1 baris target Read Only memakai dialog single auto-revert

28. Centang baris `Rina Putri`
29. Klik `Bulk Action`
30. Klik `Remove`
31. Verifikasi Title dialog `Remove Read Only`
32. Verifikasi body dialog memuat bullet `• Rina P` berupa komponen user (ikon user generik + first name + inisial last name)
33. Arahkan kursor ke `Rina P`
34. Verifikasi hover pada `Rina P` menampilkan nama lengkap `Rina Putri`
35. Verifikasi body dialog memuat kalimat `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`
36. Verifikasi tombol `[Cancel]` dan `[Remove]` (danger) tampil
37. Klik `[Remove]`
38. Verifikasi toast sukses `Success, user has been removed.`
39. Verifikasi Bulk Action Bar tertutup
40. Verifikasi baris `Rina Putri` hilang dari Detail `Manage master reference`
41. Buka Tab Read Only
42. Verifikasi baris `Siti Nurhaliza` tampil di Tab Read Only
43. Verifikasi baris `Rina Putri` tidak ada di Tab Read Only

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog (langkah 12) dan berpindah ke Detail `Manage master reference` (langkah 27).
- Spec melewati sekitar 35 langkah (43 langkah) karena tiga TC menguji dialog Bulk Remove yang sama (klik ganda, dialog single target regular, dialog single target Read Only) dan tiap klausa Expected (judul, bullet, hover nama lengkap, kalimat, tombol, toast, hilangnya baris, Bulk Action Bar) menjadi satu `Verifikasi` (S-01). Satu kelas harness (fungsional), satu aktor; tiap blok memakai baris target sendiri (dua user milik spec, Nina Kartika, Rina Putri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Detail `Manage hardware` dipakai oleh dua TC pertama; Detail `Manage master reference` oleh TC-GS-ROLE-295.
- Anchor absence: toast sukses sebelum asersi baris hilang adalah anchor respons server selesai; baris `Siti Nurhaliza` tampil di Tab Read Only menjadi anchor positif sebelum asersi ketiadaan `Rina Putri`.
- Temuan untuk QA:
  - TC-GS-ROLE-294 menulis counter `1 User selected`, sedangkan PRD (Selection Counter) menetapkan `1 user selected` (huruf kecil); spec mengikuti TC.
  - TC-GS-ROLE-135 menyebut `Centang 2 baris` tanpa menyebut barisnya; spec memakai dua user milik spec.
  - TC-GS-ROLE-135 Expected b (`tepat 1 entry Remove per baris`) tidak menyebut cara membaca entry di Changelog; spec memakai Search per nama bersuffix di Changelog Detail dan menghitung entry Action `Remove`.
  - TC-GS-ROLE-135 tidak menyebut apakah klik kedua mengirim request kedua; hanya jumlah toast dan entry Changelog yang diasersi.
