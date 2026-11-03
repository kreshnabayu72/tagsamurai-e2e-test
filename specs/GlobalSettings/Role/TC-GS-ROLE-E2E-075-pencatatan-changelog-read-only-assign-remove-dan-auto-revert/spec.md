---
id: TC-GS-ROLE-E2E-075-pencatatan-changelog-read-only-assign-remove-dan-auto-revert
title: "Pencatatan Changelog Tab Read Only: Assign, Remove, dan Auto-Revert"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-211
coverage:
  web: automated
---

# Pencatatan Changelog Tab Read Only: Assign, Remove, dan Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) |
|---|---|---|
| Rahmat Hidayat | #11 kandidat (Active) | Tanpa access level, punya baris Manage files (Read dan Delete checked) |
| Wawan Setiawan | #11 kandidat (Active) | Di-assign Read Only oleh Ahmad Fauzi lewat sesi API (Given TC-GS-ROLE-107 precondition c; dipakai sebagai precondition TC, tidak diasersi) |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada modal Changelog Tab Read Only, dicatat pada langkah 1 dan 2 (sebelum aksi pemicu pertama yang diasersi) sebagai `B-RH` dan `B-WS`; asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada modal Changelog disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign Read Only, Remove Read Only, serta Edit CRUD pada baris Manage hardware beserta konfirmasi `[Remove]` auto-revert. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-80, TC-GS-ROLE-88, TC-GS-ROLE-107) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Rahmat Hidayat dikembalikan ke tanpa access level dengan baris Manage files (Read dan Delete checked); Wawan Setiawan dikembalikan ke state kandidat (tanpa access level dan tanpa baris role). Efek pada Pre-setup: Modified By dan Last Updated kedua user berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-211)

1. Klik Tab Read Only, klik [Changelog], ketik Search `Rahmat Hidayat`, tekan Enter, catat total hasil sebagai `B-RH`
2. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `B-WS`
3. Tutup modal Changelog dengan `✕`

### TC-GS-ROLE-211: Changelog Read Only, entry Assign, Remove, dan Auto-Revert

4. Aksi pemicu (sesi API Ahmad Fauzi): Assign Read Only ke Rahmat Hidayat (setara TC-GS-ROLE-80 langkah 1 sampai 3)
5. Klik [Changelog], ketik Search `Rahmat Hidayat`, tekan Enter
6. Verifikasi total hasil Search sama dengan `B-RH` + 1 (tepat 1 entry baru)
7. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 6): Action `Assign`, Field `Access Level`, Old Value `—`, New Value `Read Only`
8. Tutup modal Changelog
9. Aksi pemicu (sesi API Ahmad Fauzi): Remove Read Only dari Rahmat Hidayat (setara TC-GS-ROLE-88 langkah 1 sampai 3)
10. Klik [Changelog], ketik Search `Rahmat Hidayat`, tekan Enter
11. Verifikasi total hasil Search sama dengan `B-RH` + 2 (entry Assign dari langkah 4 dan tepat 1 entry Remove baru)
12. Verifikasi entry Remove baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 11): Action `Remove`, Old Value `Read Only`, New Value `—`
13. Tutup modal Changelog
14. Aksi pemicu (sesi API Ahmad Fauzi): centang Create baris Wawan Setiawan di Detail "Manage hardware" dan konfirmasi `[Remove]` (setara TC-GS-ROLE-107 langkah 1 sampai 3)
15. Klik [Changelog], ketik Search `Wawan Setiawan`, tekan Enter
16. Verifikasi total hasil Search sama dengan `B-WS` + 1 (tepat 1 entry baru)
17. Verifikasi entry baru (dikenali lewat kombinasi kolom yang diasersi di bawah, bukan posisi baris; selisih pada langkah 16): Action `Auto-Revert`, Old Value `Read Only`, New Value `—`
18. Verifikasi Modified By entry Auto-Revert adalah `Ahmad F`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Satu TC sumber; subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Dependensi TC-GS-ROLE-80, 88, dan 107 dijalankan lewat aksi pemicu sesi API (langkah 4, 9, 14). Urutan TC sumber (Rahmat Hidayat Assign, Rahmat Hidayat Remove, Wawan Setiawan Auto-Revert) dipertahankan; Remove (Expected b) berjalan sesudah Assign (Expected a) karena membutuhkan Rahmat Hidayat ber-Read Only.
- Given Wawan Setiawan ber-Read Only dijalankan di hook `before` sebelum baseline `B-WS` dicatat, sehingga entry Assign Wawan Setiawan tidak termasuk entri baru yang diasersi.
- "Entry baru" dikenali lewat kombinasi kolom yang diasersi pada langkah Verifikasinya dan selisih jumlah terhadap baseline, bukan lewat posisi baris (S-12, S-14); urutan antar-entri yang jatuh pada menit yang sama tidak diasersi karena kolom Date berketelitian menit.
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah tab, menutup modal Changelog, mengganti isi kotak search (langkah 1 sampai 3, 5, 8, 10, 13, 15); aksi pemicu API (langkah 4, 9, 14).
- Temuan untuk QA:
  - TC-GS-ROLE-211 Expected c menyebut Modified By "Ahmad F" hanya untuk Auto-Revert Wawan Setiawan; Expected a dan b tidak menyebut Modified By, sehingga tidak diasersi untuk entry Assign dan Remove Rahmat Hidayat. Entri dikenali lewat Search nama user, sehingga User Name tidak diasersi terpisah.
  - TC-GS-ROLE-211 memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run, dan tidak mendefinisikan cara menghitung entri pada modal Changelog; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
