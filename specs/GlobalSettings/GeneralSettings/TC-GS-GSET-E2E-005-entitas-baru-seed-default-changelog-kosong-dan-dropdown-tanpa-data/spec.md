---
id: TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data
title: "Entitas baru belum Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-11
  - TC-GS-GSET-12
  - TC-GS-GSET-63
  - TC-GS-GSET-178
coverage:
  web: automated
---

# Entitas baru belum Save

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen untuk akun aktor spec ini (Total Control staf Client Baru dan staf Client Negara Lain) dan dipulihkan di `after`. Pemulihan record Client A tidak relevan karena spec memakai entitas lain.
- Akun aktor (Total Control; akun tidak ada di Tabel Pre-setup TC, disediakan tim FE):
  - Staf Total Control `Client Baru` (Pre-setup No 14, negara Indonesia, belum Save): email disediakan tim FE, kredensial `Spectra.env.GS_NEWCLIENT_TC_PASSWORD`. Login di hook `before`; halaman General Settings dibuka di hook `beforeEach`.
  - Staf Total Control `Client Negara Lain` (Pre-setup No 15, negara bukan Indonesia, belum Save): email disediakan tim FE, kredensial `Spectra.env.GS_OTHERCOUNTRY_TC_PASSWORD`. Login lewat langkah ganti akun eksplisit (langkah 19 sampai 21); hook `after` mengembalikan sesi ke akun default suite.
  - Nama env baru, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftaran dikerjakan di tahap script.
- Data: kedua entitas harus belum pernah Save General Settings (dan `Client Baru` punya Changelog kosong) sebelum run. Spec hanya membaca, tidak menekan `[Save]`; entitas direset tim FE/BE sebelum tiap run bila pernah di-Save (tidak ada endpoint reset di TC, PRD, atau LLD).
- Seed default yang diasersi: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes` (nilai dibaca dari `Fixture.generalSettings.<kunci>`; berkas `fixtures/generalSettings.json` belum ada, ditandai untuk tahap script).
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-GSET-11 dan TC-GS-GSET-63: Seed default dan Modal Changelog kosong (Client Baru)

1. Verifikasi Select "Currency Code" bernilai seed default `IDR`
2. Verifikasi Select "Date Format" bernilai seed default `dd/MM/yy`
3. Verifikasi Select "Time Format" bernilai seed default `HH:mm`
4. Verifikasi Select "Time Zone" bernilai seed default `Asia/Jakarta`
5. Verifikasi Select "Session Idle Timeout" bernilai seed default `30 minutes`
6. Verifikasi Button "Save" disabled
7. Klik icon Changelog
8. Verifikasi Modal Changelog menampilkan empty state dengan ilustrasi
9. Verifikasi empty state memiliki title "No changelog yet" dan description "Activities and changes will appear here."
10. Verifikasi tidak ada baris data di tabel Modal Changelog

### TC-GS-GSET-178: Dropdown filter tanpa data sumber

11. Klik Filter pada Modal Changelog
12. Buka dropdown Field
13. Verifikasi dropdown Field menampilkan teks "No options available"
14. Verifikasi dropdown Field bukan error dan bukan daftar kelima nilai Field
15. Tutup dropdown Field
16. Buka dropdown Modified By
17. Verifikasi dropdown Modified By menampilkan teks "No options available"
18. Tutup dropdown Modified By dan tutup Modal Changelog dengan `✕`

### TC-GS-GSET-12: Time Zone default entitas negara bukan Indonesia

19. Klik menu profil lalu Logout dari akun staf Client Baru
20. Tunggu aksi selesai (halaman Login tampil)
21. Login sebagai Total Control staf `Client Negara Lain` (`Spectra.env.GS_OTHERCOUNTRY_TC_PASSWORD`)
22. Buka Global Settings > General Settings
23. Verifikasi Select "Time Zone" terpilih `Asia/Jakarta`

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 23 langkah.
- Pembagian TC: TC-GS-GSET-11 langkah 3 (klik icon Changelog) dan TC-GS-GSET-63 langkah 1 (klik icon Changelog) adalah aksi yang sama pada entitas yang sama, sehingga memakai satu pembukaan modal (langkah 7); Expected TC-GS-GSET-63 menjadi langkah 8 dan 9, Expected c TC-GS-GSET-11 menjadi langkah 10. Urutan Expected c (langkah 10) mengikuti empty state agar absence baris memakai empty state sebagai anchor positif (butir 2 bagian 8b). TC-GS-GSET-178 langkah 1 (klik icon Changelog) dipenuhi pembukaan modal langkah 7 dan modal baru ditutup di langkah 18.
- TC-GS-GSET-12 dijalankan terakhir karena memakai akun dan entitas lain; langkah 19 sampai 23 adalah Step ganti akun eksplisit (S-07). Langkah penghubung tanpa `Verifikasi`: langkah 15, 18, 19, 20, 21, 22 (langkah 20 mengikuti butir 8 bagian 8b karena berpindah akun).
- Temuan untuk QA:
  - Akun staf `Client Baru` dan `Client Negara Lain` tidak tertulis di Pre-setup TC (email disediakan tim FE). Reset entitas ke keadaan "belum Save" setiap run tidak didefinisikan di TC, PRD, atau LLD (juga berlaku untuk TC-GS-GSET-117 di spec 006).
  - TC-GS-GSET-178 Expected a menyebut dropdown "bukan error, bukan daftar kelima nilai Field"; spec memecahnya menjadi satu `Verifikasi` (langkah 14) setelah teks "No options available".
  - Teks "No options available" tidak ada di PRD modul; ditelusuri ke `foundation/process/prd-process/prd-conventions.md` §9.8 sesuai kolom Sumber PRD TC.
