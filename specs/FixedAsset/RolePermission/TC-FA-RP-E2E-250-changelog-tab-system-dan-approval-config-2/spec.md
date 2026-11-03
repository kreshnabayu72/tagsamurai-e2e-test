---
id: TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2
title: "Changelog Tab System dan Approval Config (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-825
  - TC-FA-RP-826
  - TC-FA-RP-827
  - TC-FA-RP-828
  - TC-FA-RP-829
coverage:
  web: automated
---

# Changelog Tab System dan Approval Config (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #18 (pohon group), #20 (seed approval Transfer pada `IT Infrastructure`: Require Approval ON, Approver Pandu Wijaya, aturan OR, Approval Scope `Both`), #21 (seed pemegang Update `Manage asset & TAG`: Budi Santoso Read dan Update di `IT Infrastructure`), #24 (`Company Changelog`). Precondition TC-FA-RP-829: toggle registrasi `IT Infrastructure` ON (dipenuhi oleh hasil TC-FA-RP-828). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu.
- State yang diubah dan pemulihannya: Approval Scope `Transfer` dan toggle Require Approval for Registration pada `IT Infrastructure` diubah spec ini; dipulihkan ke Pre-setup #20 dan #21 di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-825: Changelog Approval Config: Approval Scope Both ke Origin only

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
3. Pilih `Origin only`, catat waktu sesudahnya
4. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
5. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
6. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Both`; New Value `Origin only`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
7. Tutup modal Changelog

### TC-FA-RP-826: Changelog Approval Config: Approval Scope Origin only ke Both

8. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
9. Pilih `Both`, catat waktu sesudahnya
10. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
11. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
12. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Origin only`; New Value `Both`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
13. Tutup modal Changelog

### TC-FA-RP-827: Changelog Approval Config: Approval Scope Both ke Destination only

14. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
15. Pilih `Destination only`, catat waktu sesudahnya
16. Tunggu aksi selesai: pilihan tetap terpilih dan indikator memuat hilang
17. Klik ikon `[Changelog]` di baris sub-tab `Transfer`
18. Verifikasi Modal `Changelog: Role & Permission > Transaction Role > Transfer` memuat entri terbaru: Action `Edit`; Field `Approval Scope — IT Infrastructure`; Old Value `Both`; New Value `Destination only`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
19. Tutup modal Changelog

### TC-FA-RP-828: Changelog Approval Config registrasi: Off ke On pada Detail Role Manage asset & TAG

20. Klik Tab `System` lalu buka Detail Role `Manage asset & TAG`
21. Klik node `IT Infrastructure`
22. Aktifkan toggle `Require Approval for Registration`, catat waktu sesudahnya
23. Tunggu aksi selesai: toggle tetap pada kondisi baru dan indikator memuat hilang
24. Klik ikon Changelog di toolbar Detail Role
25. Verifikasi Modal `Changelog: Role & Permission > Manage asset & TAG` memuat entri terbaru: Action `Edit`; Object `Manage asset & TAG` (tanpa segmen User); Field `Require Approval for Registration — IT Infrastructure`; Old Value `Off`; New Value `On`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
26. Tutup modal Changelog

### TC-FA-RP-829: Changelog Approval Config registrasi: On ke Off

27. Klik node `IT Infrastructure`
28. Matikan toggle `Require Approval for Registration`, catat waktu sesudahnya
29. Tunggu aksi selesai: toggle tetap pada kondisi baru dan indikator memuat hilang
30. Klik ikon Changelog di toolbar Detail Role
31. Verifikasi Modal memuat entri terbaru: Action `Edit`; Object `Manage asset & TAG`; Field `Require Approval for Registration — IT Infrastructure`; Old Value `On`; New Value `Off`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
32. Verifikasi Modal tidak memuat baris `Approval Rule` untuk registrasi
33. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 33 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 4, 7, 10, 13, 16, 19, 20, 23, 26, 29, 33. Akun aktor pertama sudah login di hook `before` (S-07).
- Urutan TC mengikuti urutan nomor; hasil tiap TC menjadi precondition TC berikutnya (Approval Scope: Both, Origin only, Both, Destination only; toggle registrasi Off lalu On lalu Off), sehingga tidak ada seeding ulang antar blok.
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- TC-FA-RP-820 sampai TC-FA-RP-824 ada di spec 249.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-826 dan 827 mengasumsikan nilai awal Approval Scope dari hasil TC sebelumnya (precondition d TC-FA-RP-826 menyebut Origin only); spec memakai urutan nomor agar asumsi itu terpenuhi, dan urutan itu dicatat di Notes.
  - TC-FA-RP-828 Expected menyebut Object `Manage asset & TAG` "tanpa segmen User" sebagai bagian dari Verifikasi entri; spec menulisnya dalam satu Verifikasi entri.
