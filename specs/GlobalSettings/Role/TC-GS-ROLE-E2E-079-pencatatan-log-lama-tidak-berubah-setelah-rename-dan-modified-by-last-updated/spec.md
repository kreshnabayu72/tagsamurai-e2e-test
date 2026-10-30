---
id: TC-GS-ROLE-E2E-079-pencatatan-log-lama-tidak-berubah-setelah-rename-dan-modified-by-last-updated
title: "Pencatatan Log Lama Tidak Berubah setelah Rename User serta Modified By dan Last Updated oleh Assign"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-220
  - TC-GS-ROLE-225
coverage:
  web: automated
---

# Pencatatan Log Lama Tidak Berubah setelah Rename User serta Modified By dan Last Updated oleh Assign

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Akun pendukung hook `before` (hanya Given, tanpa login UI): Budi Santoso (Default User, Total Control), `defaultUserGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2), lewat sesi API dengan `Spectra.env.GS_DEFAULT_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_DEFAULT_PASSWORD` (keduanya terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) | TC |
|---|---|---|---|
| Sari Wulandari | #11 kandidat (Active) | Tanpa access level dan tanpa baris role, lalu di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-58) sehingga entry Assign lama ada | TC-GS-ROLE-220 |
| Siti Nurhaliza | #4 (Read Only, Active, punya baris Manage TAG) | Read Only yang di-assign oleh Budi Santoso lewat sesi API (Precondition b TC-GS-ROLE-225; dipakai sebagai precondition TC, tidak diasersi) | TC-GS-ROLE-225 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada modal Changelog Tab Total Control, dicatat pada langkah 1 sampai 3 (sebelum aksi pemicu pertama yang diasersi) sebagai `B-PUTRI`, `B-SW`, dan `B-SITI`; asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): ubah nama user di modul User (First Name dan Last Name), Remove Total Control, dan Assign Total Control ke user Read Only (upgrade). Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58, TC-GS-ROLE-86, TC-GS-ROLE-60) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: nama Sari Wulandari Putri dikembalikan menjadi `Sari Wulandari` dan access level dikosongkan; Siti Nurhaliza dikembalikan ke Read Only (Remove Total Control lalu Assign Read Only). Efek pada Pre-setup: Modified By Siti Nurhaliza berubah dari `Budi S` menjadi `Ahmad F`, dan Last Updated Siti Nurhaliza serta Sari Wulandari berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam; Last Updated dibandingkan dengan Date entri Changelog aksi upgrade yang sama (S-12).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah nama dan access level user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-220 dan TC-GS-ROLE-225)

1. Klik [Changelog] pada Table Tools Tab Total Control, ketik Search `Sari Wulandari Putri`, tekan Enter, catat total hasil sebagai `B-PUTRI`
2. Ganti isi kotak search dengan `Sari Wulandari`, tekan Enter, catat total hasil sebagai `B-SW`
3. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter, catat total hasil sebagai `B-SITI`
4. Tutup modal Changelog dengan `✕`

### TC-GS-ROLE-220: Entry log lama tidak berubah setelah user di-rename

5. Aksi pemicu (sesi API Ahmad Fauzi): ubah nama Sari Wulandari menjadi `Sari Wulandari Putri` di modul User
6. Aksi pemicu (sesi API Ahmad Fauzi): Remove Total Control dari `Sari Wulandari Putri` (setara TC-GS-ROLE-86 langkah 1 sampai 2; menghasilkan entry baru sesudah rename)
7. Buka Global Settings > Role & Permission > Tab Total Control, klik [Changelog], ketik Search `Sari Wulandari`, tekan Enter
8. Verifikasi total hasil Search sama dengan `B-SW` + 1 (hanya entry Remove baru dari langkah 6 yang bertambah)
9. Verifikasi entry lama tepat di bawah entry baru (entry Assign dari hook `before`): Action `Assign`, User Name `Sari Wulandari` (bukan `Sari Wulandari Putri`)
10. Ganti isi kotak search dengan `Sari Wulandari Putri`, tekan Enter
11. Verifikasi total hasil Search sama dengan `B-PUTRI` + 1 (entry lama tidak ikut berganti nama; tepat 1 entry baru)
12. Verifikasi entry baru (teratas): Action `Remove`, User Name `Sari Wulandari Putri`

### TC-GS-ROLE-225: Modified By dan Last Updated hanya diperbarui oleh Assign

13. Tutup modal Changelog, aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Siti Nurhaliza (upgrade dari Read Only, setara TC-GS-ROLE-60 langkah 1 sampai 3)
14. Klik [Changelog], ketik Search `Siti Nurhaliza`, tekan Enter
15. Verifikasi total hasil Search sama dengan `B-SITI` + 1 (tepat 1 entry upgrade baru)
16. Verifikasi entry baru (teratas): Action `Assign`, Old Value `Read Only`, New Value `Total Control`; catat Date entry sebagai `D-225`
17. Tutup modal Changelog, ketik Search `Siti Nurhaliza` pada Table Tools Tab Total Control, tekan Enter
18. Verifikasi Modified By baris Siti Nurhaliza adalah `Ahmad F`
19. Verifikasi Last Updated baris Siti Nurhaliza sama dengan `D-225` (waktu upgrade)

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 19 langkah. Urutan TC sumber (220, 225) dipertahankan. Dependensi TC-GS-ROLE-58 (Given Sari Wulandari ber-Total Control), TC-GS-ROLE-86, dan TC-GS-ROLE-60 dijalankan lewat seeding API di hook `before` atau aksi pemicu (langkah 6 dan 13); Given Sari Wulandari dan Siti Nurhaliza terjadi sebelum baseline dicatat.
- Langkah 6 (Remove Total Control dari `Sari Wulandari Putri`) bukan langkah TC-GS-ROLE-220: aksi itu menghasilkan "entry baru setelah rename" yang diminta Expected b. Langkah ini dicatat di sini dan di "Temuan untuk QA".
- "Entry baru (teratas)" berarti entri teratas pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. Langkah 9 membaca entry Assign lama sebagai baris di bawah entry Remove baru pada hasil Search `Sari Wulandari`, sedangkan langkah 11 membuktikan entry lama tidak berganti nama lewat total hasil Search `Sari Wulandari Putri` yang bertambah tepat 1.
- Langkah 19 membandingkan Last Updated dengan Date entry Changelog aksi upgrade yang sama (kolom Date berketelitian menit, sehingga dibandingkan pada ketelitian yang sama).
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup modal Changelog, mengganti isi kotak search, dan mencari baris Siti Nurhaliza pada tabel (langkah 1 sampai 4, 7, 10, 13, 14, 17); aksi pemicu API (langkah 5, 6, 13).
- Temuan untuk QA:
  - TC-GS-ROLE-220 Langkah Uji hanya memuat rename dan membuka Changelog, tetapi Expected b ("Entry baru setelah rename memakai nama baru") membutuhkan aksi yang menghasilkan entry baru; spec menambahkan Remove Total Control dari user yang sudah di-rename (langkah 6) tanpa dasar langkah TC.
  - TC-GS-ROLE-220 tidak menyatakan cara rename (modul User); spec memakai sesi API Ahmad Fauzi untuk rename karena rename adalah pemicu state dan bukan objek asersi.
  - TC-GS-ROLE-225 Expected b ("Last Updated = waktu upgrade") tidak menyebut format atau ketelitian waktu; spec membandingkan dengan Date entry Changelog aksi yang sama pada ketelitian yang sama.
  - TC-GS-ROLE-225 Judul ("hanya diperbarui oleh Assign") menyiratkan aksi non-Assign tidak mengubah Modified By dan Last Updated, tetapi Expected hanya memuat dampak upgrade; spec tidak menambah asersi untuk aksi non-Assign.
  - TC-GS-ROLE-220 dan TC-GS-ROLE-225 tidak mendefinisikan cara menghitung entri pada modal Changelog dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
