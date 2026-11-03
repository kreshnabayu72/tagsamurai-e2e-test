---
id: TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade
title: "Asset Name Excess: Badge Over Plan Limit, Aksi Edit Hidden, Bulk Delete, dan Urutan Excess"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-27
  - TC-FA-FAAM-58
  - TC-FA-FAAM-296
  - TC-FA-FAAM-311
  - TC-FA-FAAM-646
  - TC-FA-FAAM-705
  - TC-FA-FAAM-730
coverage:
  web: automated
---

# Asset Name Excess: Badge Over Plan Limit, Aksi Edit Hidden, Bulk Delete, dan Urutan Excess

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) pada client downgrade (Pre-setup #20) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD` ke client downgrade; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Akun kedua Update-Only (Pre-setup #5, `updateOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_UO_PASSWORD`) pada client downgrade yang sama login lewat langkah Ganti akun eksplisit (langkah 32). Hook `after` mengembalikan sesi ke akun default suite dan client utama. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.downgradeClient`): client downgrade efektif (#20) dengan cap 3 dan empat Asset Name urut pembuatan `Excess Alpha` (terlama, Total Asset 0), `Excess Beta` (Total Asset 2), `Excess Delta` (Total Asset 0), `Excess Gamma` (terbaru, Total Asset 0); tiga tertua usable dan hanya `Excess Gamma` excess; tanpa Asset Name Category Locked. Akses aktor Total Control dan Update-Only ke client downgrade disediakan tim FE/BE (TC tidak merinci akunnya).
- State global: tidak ada yang diubah; spec tidak menghapus atau mengubah Asset Name (dialog Bulk Delete di langkah 29 dibatalkan). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-646: Pada downgrade, Asset Name terlama tetap usable dan yang terbaru menjadi excess

1. Amati tab Asset Name pada client downgrade (cap 3) yang dibuka hook `beforeEach`
2. Verifikasi baris `Excess Gamma` menampilkan badge `Over Plan Limit`
3. Verifikasi baris `Excess Alpha`, `Excess Beta`, dan `Excess Delta` tanpa badge `Over Plan Limit`

### TC-FA-FAAM-730: Tidak ada pilihan manual Asset Name mana yang tetap usable pada client downgrade

4. Verifikasi hanya `Excess Gamma` (terbaru) berbadge `Over Plan Limit`
5. Verifikasi Table Tools hanya `Search | Filter | Download | Changelog | [+ Asset Name]`
6. Verifikasi tidak ada notice, dialog, tombol, atau menu untuk memilih Asset Name mana yang tetap usable
7. Klik `⋯` baris `Excess Gamma`
8. Verifikasi menu `⋯` baris `Excess Gamma` tanpa aksi `Edit` (TC-FA-FAAM-646 b)
9. Verifikasi menu `⋯` baris `Excess Gamma` memuat `Detail` dan `Delete` tanpa `Edit` (TC-FA-FAAM-730 d)
10. Tekan Esc untuk menutup menu `⋯`
11. Klik `⋯` baris `Excess Alpha`
12. Verifikasi `Excess Alpha` tanpa badge `Over Plan Limit`
13. Verifikasi menu `⋯` baris `Excess Alpha` memuat `Detail`, `Edit`, `Delete`
14. Tekan Esc untuk menutup menu `⋯`

### TC-FA-FAAM-705: Asset Name excess hanya berbadge Over Plan Limit tanpa notice dan tanpa quick filter

15. Verifikasi baris Asset Name excess hanya menampilkan badge `Over Plan Limit`
16. Verifikasi tidak ada notice di atas tabel dan tidak ada tautan `Show only`
17. Verifikasi tidak ada chip quick filter

### TC-FA-FAAM-27: Asset Name excess menampilkan badge Over Plan Limit dengan tooltip

18. Hover badge `Over Plan Limit` pada sel Asset Name baris `Excess Gamma`
19. Verifikasi badge `Over Plan Limit` (severity warning) tampil di samping nama `Excess Gamma`
20. Verifikasi tooltip `This asset name exceeds your current plan limit and is read-only. Upgrade your plan to edit it.`

### TC-FA-FAAM-311: Popup Detail Asset Name excess menampilkan badge Over Plan Limit di samping nama

21. Klik nama `Excess Gamma`
22. Verifikasi Identitas Utama Popup Detail menampilkan badge `Over Plan Limit`
23. Hover badge `Over Plan Limit` pada Identitas Utama
24. Verifikasi tooltip badge sama dengan tooltip pada kolom nama di List
25. Verifikasi Popup Detail tidak memiliki aksi tulis
26. Klik `✕` pada Popup Detail

### TC-FA-FAAM-296: Asset Name excess dapat dipilih untuk Bulk Delete

27. Centang baris `Excess Gamma`
28. Klik `Bulk Action` lalu `Delete`
29. Verifikasi dialog single `Delete Asset Name` untuk `Excess Gamma` tampil
30. Klik `[Cancel]` pada dialog konfirmasi
31. Hapus centang baris `Excess Gamma` (Unselect)

### TC-FA-FAAM-58: Pemegang Update-Only tidak melihat aksi Edit pada Asset Name excess

32. Ganti akun: Logout, login sebagai Update-Only pada client downgrade, lalu buka Fixed Asset > Settings > Asset Master > Asset Name
33. Klik `⋯` baris `Excess Gamma`
34. Verifikasi menu `⋯` baris `Excess Gamma` memuat `Detail` saja
35. Verifikasi aksi `Edit` Hidden

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 646, 730, 705, 27, 311, 296, 58. Pembacaan dan screening dahulu; ganti akun Update-Only di akhir (S-07, S-10).
- Langkah 8 dan 9 mengasersi menu `⋯` `Excess Gamma` dari satu pembukaan menu, masing-masing untuk Expected TC-646 b dan TC-730 d.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (mengamati halaman yang dibuka hook), langkah 10 dan 14 (menutup menu), langkah 26 (menutup popup), langkah 30 dan 31 (membatalkan dialog dan menghapus centang, S-09), langkah 32 (Ganti akun eksplisit).
- Langkah 2 adalah anchor positif untuk asersi absence badge pada langkah 3, 12; langkah 5 (Table Tools) adalah anchor permukaan untuk absence notice pada langkah 6 dan 16; langkah 34 memuat `Detail` sebagai anchor positif bagi absence `Edit` pada langkah 35.
- Langkah 15 dan langkah 4 mengasersi klaim yang berdekatan pada TC berbeda (TC-705 a dan TC-730 c) dan ditulis terpisah supaya tiap TC punya `Verifikasi` sendiri.
- Spec tidak menghapus atau mengubah Asset Name pada client downgrade (#20); TC-296 hanya membuka dialog Bulk Delete lalu membatalkannya.
- Temuan untuk QA:
  - TC-27, TC-58, TC-296, TC-311, TC-646, TC-705, dan TC-730 memakai "Client downgrade (Pre-setup #20)" tanpa menyebut akun, email, atau cara mengarahkan sesi ke client itu; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-296 Expected hanya "Dialog single `Delete Asset Name` untuk `Excess Gamma` tampil"; Langkah uji tidak menyebut membatalkan dialog; spec menambahkan `[Cancel]` sebagai langkah penghubung supaya katalog client downgrade tidak berubah.
  - TC-296 Precondition menyebut `Excess Alpha` tetapi tidak dipakai di Langkah uji dan Expected; spec tidak memakainya.
  - TC-646 dan TC-730 saling tumpang tindih (badge hanya pada `Excess Gamma`, menu `Excess Gamma` tanpa `Edit`); keduanya diasersi sesuai Expected masing-masing.
