---
id: TC-FA-RP-E2E-242-aksesibilitas-keyboard-fokus-dialog-dan-slot-toast
title: "Aksesibilitas keyboard, fokus dialog, dan slot toast"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1007
  - TC-FA-RP-1008
  - TC-FA-RP-1015
coverage:
  web: automated
---

# Aksesibilitas keyboard, fokus dialog, dan slot toast

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #18 (pohon group), #39 (Detail Role `Manage Open API` dan `Manage accounting` terisi, termasuk baris Ahmad Fauzi). Precondition TC: baris Ahmad Fauzi pada `Manage accounting` dengan Create dan Update tidak aktif (dipakai sebagai precondition TC, disiapkan lewat seeding API). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Navigasi keyboard (Tab dan Space), pembacaan indikator fokus dan posisi, serta pembacaan slot toast.
- State yang diubah dan pemulihannya: Create dan Update baris Ahmad Fauzi pada `Manage accounting` diubah spec ini; dipulihkan ke tidak aktif di hook `after` lewat fixture backend yang disediakan tim FE/BE (Last Updated baris itu berubah).
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1007: Checkbox Read Disabled dapat difokus keyboard dan tooltip muncul saat fokus

1. Klik Tab `System`
2. Buka Detail Role `Manage Open API`
3. Tekan Tab berulang sampai fokus berada pada checkbox Read baris Ahmad Fauzi tanpa menggerakkan mouse
4. Verifikasi checkbox Read berstatus Disabled
5. Verifikasi checkbox Read menerima fokus keyboard
6. Verifikasi indikator fokus tampil pada checkbox Read
7. Verifikasi tooltip `Read access is required and can only be removed by removing the role.` tampil saat fokus tanpa hover

### TC-FA-RP-1008: Checkbox CRUD dapat dioperasikan lewat keyboard (Tab dan Space)

8. Klik segmen `System` pada Breadcrumb
9. Buka Detail Role `Manage accounting`
10. Tekan Tab berulang sampai fokus berada pada checkbox Create baris Ahmad Fauzi
11. Verifikasi checkbox Create menerima fokus keyboard
12. Verifikasi indikator fokus tampil pada checkbox Create
13. Verifikasi checkbox Create rata tengah pada selnya
14. Tekan Space
15. Verifikasi Create tercentang
16. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
17. Tunggu toast lama hilang otomatis
18. Tekan Space lagi
19. Verifikasi Create tidak tercentang
20. Verifikasi muncul toast sukses: `Success, permissions have been updated.`

### TC-FA-RP-1015: Toast tampil dalam slot tunggal saat dua aksi berurutan cepat

21. Tunggu toast lama hilang otomatis
22. Centang Create pada baris Ahmad Fauzi
23. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
24. Sebelum toast pertama hilang, centang Update pada baris Ahmad Fauzi
25. Verifikasi muncul toast sukses: `Success, permissions have been updated.` pada slot toast yang sama
26. Verifikasi hanya satu toast yang tampil pada satu waktu (tidak bertumpuk)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 26 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 8, 17, 21. Akun aktor pertama sudah login di hook `before` (S-07).
- TC-FA-RP-1015 mulai dari Create dan Update tidak aktif (precondition d); baris Ahmad Fauzi pada `Manage accounting` berada pada keadaan itu karena langkah terakhir TC-FA-RP-1008 mengembalikan Create ke tidak aktif. TC-FA-RP-1015 tetap memakai Detail Role `Manage accounting` yang sudah terbuka dari TC-FA-RP-1008.
- TC-FA-RP-1009 (fokus terkunci di dalam dialog konfirmasi) ada di spec 313.
- Temuan untuk QA:
  - TC-FA-RP-1015 langkah 3 menyebut "sebelum toast pertama hilang" tanpa durasi toast; keandalan langkah bergantung pada kecepatan eksekusi dan lama tampil toast yang tidak disebut TC.
  - TC-FA-RP-1007 dan TC-FA-RP-1008 tidak menyebut cara mengamati indikator fokus dan posisi rata tengah; cara ukur ditentukan di tahap script.
  - TC-FA-RP-1007 precondition merujuk Pre-setup #39 untuk baris Ahmad Fauzi pada `Manage Open API`; Expected tidak menyebut hasil bila Read Disabled ditekan Space; tidak diasersi.
