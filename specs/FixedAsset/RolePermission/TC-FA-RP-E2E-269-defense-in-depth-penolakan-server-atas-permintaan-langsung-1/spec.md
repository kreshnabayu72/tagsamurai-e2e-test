---
id: TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1
title: "Defense-in-depth: penolakan server atas permintaan langsung (1/9)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-913
  - TC-FA-RP-914
  - TC-FA-RP-915
  - TC-FA-RP-916
  - TC-FA-RP-948
  - TC-FA-RP-968
coverage:
  web: automated
---

# Defense-in-depth: penolakan server atas permintaan langsung (1/9)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only (Pre-setup #4), email `readOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.readOnly.email`), password `Spectra.env.FA_RO_PASSWORD`.
- Akun ganti (urut): Manage global user & role tanpa Update (Pre-setup #8, Bayu Prakoso), email `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobalReadOnly.email`), password `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD`; lalu Manage global user & role dengan Update (Pre-setup #6, Hendra Wijaya), email `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`), password `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso; Ahmad Fauzi memegang `Manage accounting` dengan Create nonaktif; baris Budi Santoso pada `Manage accounting` sudah dihapus untuk TC-FA-RP-948), #3 (Rina Wulandari, Total Control kedua; TC-FA-RP-916), #18 (pohon group Company Alpha; dipakai Tab Group Manager dan Tab Transaction Role pada TC-FA-RP-968), dan #6 serta #8 sebagai aktor.
- Request langsung ke server (bukan lewat UI) dikirim lewat klien HTTP yang disediakan tim FE/BE memakai sesi API aktor (`suite.md`); endpoint tidak disebut karena tidak ada di TC. State data diperiksa lewat fixture BE (kemampuan disediakan tim FE/BE). Asersi hanya status respons dan state data (bagian 8b butir 1).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung; data Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`). Nilai awal baris yang diasersi "tidak berubah" di-seed deterministik (dicatat di Data Pre-setup spec ini).
- Env var yang dipakai: `FA_RO_PASSWORD`, `FA_MUR_GLOBAL_RO_PASSWORD`, `FA_MUR_GLOBAL_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-913: Read Only mengedit CRUD ditolak server

1. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Ahmad Fauzi pada `Manage accounting`
2. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
3. Verifikasi lewat fixture BE nilai Create baris Ahmad Fauzi pada `Manage accounting` tidak berubah (tetap nonaktif)

### TC-FA-RP-948: Aktor tanpa wewenang mendapat 403 walau target sudah dihapus

4. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Budi Santoso yang sudah dihapus pada `Manage accounting`
5. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
6. Verifikasi lewat fixture BE tidak ada perubahan tersimpan (baris Budi Santoso tidak ada dan respons target tidak tersedia hanya untuk aktor berwenang)

### TC-FA-RP-968: Read Only dapat membaca seluruh tab dan Detail Role

7. Kirim request langsung ke server (bukan lewat UI) untuk membaca daftar Tab Total Control, Tab Group Manager, Tab Transaction Role, dan Detail Role (empat request baca)
8. Verifikasi seluruh request baca berhasil dengan status `200`
9. Ganti akun: sesi API aktor beralih ke Manage global user & role tanpa Update (Pre-setup #8, Bayu Prakoso)

### TC-FA-RP-914: Manage global user & role tanpa Update mengedit CRUD ditolak server

10. Kirim request langsung ke server (bukan lewat UI) untuk mengubah Create baris Ahmad Fauzi pada `Manage accounting`
11. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
12. Verifikasi lewat fixture BE nilai Create baris Ahmad Fauzi pada `Manage accounting` tidak berubah (tetap nonaktif)
13. Ganti akun: sesi API aktor beralih ke Manage global user & role dengan Update (Pre-setup #6, Hendra Wijaya)

### TC-FA-RP-915: Manage user & role meng-Assign Total Control ditolak server

14. Kirim request langsung ke server (bukan lewat UI) untuk meng-Assign Total Control ke Ahmad Fauzi
15. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
16. Verifikasi lewat fixture BE Ahmad Fauzi tidak berstatus Total Control

### TC-FA-RP-916: Manage user & role meng-Remove Total Control ditolak server

17. Kirim request langsung ke server (bukan lewat UI) untuk meng-Remove Total Control milik Rina Wulandari
18. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
19. Verifikasi lewat fixture BE Rina Wulandari tetap Total Control

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- `K-1` (TC defense-in-depth dengan Expected respons API): TC kelas a ini tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; Expected berupa status respons dan state data lewat fixture BE (BE mencatatnya pada tingkat endpoint).
- Langkah penghubung (S-03): ganti akun (bila ada) dan pencatatan state awal. Seluruh langkah "Kirim request langsung" tidak melewati browser; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Urutan TC dikelompokkan per akun supaya ganti akun hanya dua kali (Read Only: TC-FA-RP-913, 948, 968; Bayu Prakoso: TC-FA-RP-914; Hendra Wijaya: TC-FA-RP-915, 916); `sourceTc` diurutkan menurut nomor TC.
- TC-FA-RP-913 Expected b menyebut juga "tidak ada entri log"; asersi itu ada di spec 292 (Absence log: permintaan langsung yang ditolak; aksi nyata dengan baseline sendiri, S-05); spec ini hanya mengasersi status respons dan nilai Create.
- Temuan untuk QA:
  - TC-FA-RP-948 Expected b menulis klausa parentetik "(respons target tidak tersedia hanya untuk aktor berwenang)"; spec mengasersi tidak ada perubahan tersimpan saja. TC-FA-RP-968 bertipe Positive pada section defense-in-depth dan hanya menyebut status `200` untuk empat request baca.
  - Precondition TC-FA-RP-913 sampai 916 dan 948 hanya merujuk Pre-setup #15 (dan #3); baris Ahmad Fauzi pada `Manage accounting` dan akun aktor #6, #8 tidak dijelaskan di #15, sehingga di-seed dan diambil dari Pre-setup #4, #6, #8. Post Condition kosong pada seluruh TC.
