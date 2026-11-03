---
id: TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1
title: "Changelog Tab Total Control, Read Only, dan Group Manager (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-794
  - TC-FA-RP-795
  - TC-FA-RP-796
  - TC-FA-RP-797
coverage:
  web: automated
---

# Changelog Tab Total Control, Read Only, dan Group Manager (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #3 (Total Control kedua Rina Wulandari), #12 (target Read Only Maya Anggraeni), #15 (kolam pengguna Standard: Ahmad Fauzi), #24 (`Company Changelog`: log 25 entri campuran), #18 (pohon group). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Entri pembanding (8b.2): modal Changelog Tab `Read Only` yang diasersi absence memuat sedikitnya satu entri lama dari riwayat Pre-setup #24 (log 25 entri campuran) atau entri yang dibuat seeding API milik spec di hook `before` (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: Membaca modal Changelog lewat UI; waktu aksi dicatat sesudah aksi pemicu. Precondition TC-FA-RP-796 (Ahmad Fauzi berstatus Total Control) dipenuhi lewat seeding API di hook `before` dan oleh hasil TC-FA-RP-794.
- State yang diubah dan pemulihannya: Tingkat akses Ahmad Fauzi, Maya Anggraeni, dan Rina Wulandari diubah spec ini (Assign, Remove, Auto-Revert); dipulihkan ke Pre-setup di hook `after`.
- Waktu: jam server dan jam browser sinkron untuk asersi Date; waktu dicatat sesudah aksi pemicu dan Date dibandingkan dengan toleransi satu menit (S-12).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-794: Changelog Tab Total Control: Assign dari kosong

1. Klik `[+ Assign]` di Tab `Total Control`
2. Centang Ahmad Fauzi lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
3. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
4. Klik ikon Changelog di toolbar Tab `Total Control`
5. Verifikasi Modal `Changelog: Role & Permission > Total Control` memuat entri terbaru: Action `Assign`; User Name `Ahmad Fauzi`; Field `Access Level`; Old Value `—`; New Value `Total Control`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
6. Tutup modal Changelog

### TC-FA-RP-795: Changelog Tab Total Control: Assign upgrade dari Read Only menulis tepat satu entri

7. Klik `[+ Assign]` di Tab `Total Control`
8. Centang Maya Anggraeni lalu klik `[Assign]`, catat waktu sesudah `[Assign]`
9. Tunggu aksi selesai: popup Assign tertutup dan baris pengguna yang di-assign tampil di tabel
10. Klik ikon Changelog di toolbar Tab `Total Control`
11. Verifikasi Modal memuat tepat satu entri baru untuk Maya Anggraeni (entri dengan Date pada waktu aksi): Action `Assign`; User Name `Maya Anggraeni`; Field `Access Level`; Old Value `Read Only`; New Value `Total Control`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
12. Tutup modal Changelog lalu klik Tab `Read Only`
13. Klik ikon Changelog di toolbar Tab `Read Only`
14. Verifikasi Modal `Changelog: Role & Permission > Read Only` terbuka
15. Verifikasi Modal Changelog Tab `Read Only` memuat sedikitnya satu entri lama Tab `Read Only` (entri pembanding yang membuktikan modal tidak kosong)
16. Verifikasi Modal Changelog Tab `Read Only` tidak memuat entri baru untuk upgrade Maya Anggraeni (tidak ada entri Maya Anggraeni dengan Date pada waktu aksi)
17. Tutup modal Changelog lalu klik Tab `Total Control`

### TC-FA-RP-796: Changelog Tab Total Control: Remove

18. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
19. Klik `[Remove]`, catat waktu sesudah `[Remove]`
20. Tunggu aksi selesai: dialog Remove tertutup dan baris pengguna tidak lagi tampil di tabel
21. Klik ikon Changelog di toolbar Tab `Total Control`
22. Verifikasi Modal `Changelog: Role & Permission > Total Control` memuat entri terbaru: Action `Remove`; User Name `Ahmad Fauzi`; Field `Access Level`; Old Value `Total Control`; New Value `—`; Modified By `Siti R`; Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
23. Tutup modal Changelog

### TC-FA-RP-797: Changelog Tab Total Control: Auto-Revert

24. Klik Tab `System` lalu buka Detail Role `Manage accounting`
25. Hapus centang Delete pada baris Rina Wulandari
26. Klik `[Remove]` pada dialog, catat waktu sesudah `[Remove]`, lalu tunggu aksi selesai
27. Klik segmen `System` pada Breadcrumb lalu klik Tab `Total Control`
28. Klik ikon Changelog di toolbar Tab `Total Control`
29. Verifikasi Modal `Changelog: Role & Permission > Total Control` memuat entri terbaru: Action `Auto-Revert`; User Name `Rina Wulandari`; Field `Access Level`; Old Value `Total Control`; New Value `—`; Modified By `Siti R` (aktor pengedit, bukan System); Date berisi waktu aksi sesuai General Settings (selisih paling banyak satu menit dari waktu yang dicatat)
30. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 30 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 3, 6, 9, 12, 17, 20, 23, 24, 27, 30. Akun aktor pertama sudah login di hook `before` (S-07).
- Entri baru diidentifikasi lewat kombinasi kolom dan Date pada waktu aksi (S-12); jumlah total entri Changelog tidak diasersi.
- Anchor tambahan (S-03, bukan dari TC sumber): langkah 15 membuktikan sedikitnya satu entri pembanding tampil di modal Changelog Tab `Read Only` sebelum asersi absence pada langkah 16 (butir 8b.2).
- TC-FA-RP-798 sampai TC-FA-RP-801 (Changelog Tab Read Only dan Tab Group Manager) ada di spec 314; TC-FA-RP-802 sampai TC-FA-RP-805 ada di spec 244.
- Langkah aksi yang berakhir dengan "catat waktu" mencatat waktu sesudah aksi sebagai pembanding Date entri (S-12); pencatatan itu bukan langkah terpisah.
- Temuan untuk QA:
  - TC-FA-RP-797 langkah 3 menyebut "Klik Tab Total Control" dari Detail Role tanpa menyebut cara kembali; spec menambah klik segmen `System` pada Breadcrumb sebagai langkah penghubung.
  - TC-FA-RP-795 Expected "tepat satu entri baru" tidak menyebut cara menentukan entri baru pada audit trail permanen; spec memakai Date pada waktu aksi (toleransi satu menit).
  - TC-FA-RP-796 precondition d (Ahmad Fauzi Total Control) bertentangan dengan Pre-setup #15 (tanpa tingkat akses); spec memenuhinya lewat seeding API dan hasil TC-FA-RP-794.
