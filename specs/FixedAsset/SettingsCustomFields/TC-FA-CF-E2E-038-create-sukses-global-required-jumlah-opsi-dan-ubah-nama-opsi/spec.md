---
id: TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi
title: "Create Sukses: Global Value, Required, Jumlah Opsi, dan Ubah Nama Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-105
  - TC-FA-CF-106
  - TC-FA-CF-107
  - TC-FA-CF-121
  - TC-FA-CF-122
coverage:
  web: automated
---

# Create Sukses: Global Value, Required, Jumlah Opsi, dan Ubah Nama Opsi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup (hanya dibaca): Asset Name `Generator` dan `Pump` Company Alpha (Pre-setup #11).
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit):
  - D-1: `Voltage Spec {runId}-038`, Data Type Text, Scope Specific `Generator` dan `Pump`, Value Type Global, `Generator`=`220V`, `Pump`=`110V`.
  - D-2: `Company Tagline {runId}-038`, Data Type Text, Scope General, Value Type Global, Value `Safety First`.
  - D-3: `Mandatory Tag {runId}-038`, Data Type Text, Required Yes.
  - D-4: `Many Options {runId}-038`, Data Type Dropdown, 150 opsi `Opt 001` sampai `Opt 150`.
  - Nilai yang hanya diketik dan tidak pernah tersimpan: opsi `Gold` yang diubah menjadi `Platinum` (TC-FA-CF-122).
- Kemampuan teknis: penambahan 150 opsi pada input Values lewat skrip (TC-FA-CF-121 membolehkan paste satu per satu atau skrip); klik badge opsi untuk mengubah nama.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-038`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-105: Create Value Type Global menyimpan nilai Global dan menampilkan Value Type Global di tabel

1. Klik `[+ Custom Field]`
2. Isi Field Name `Voltage Spec {runId}-038`, Data Type `Text`, Scope `Specific Asset Name` dengan `Generator` dan `Pump`, Value Type `Global`
3. Isi Value `Generator` = `220V` dan `Pump` = `110V`
4. Klik `[Submit]`
5. Verifikasi toast sukses: "Success, custom field has been created."
6. Ketik Search `Voltage Spec {runId}-038`, tekan Enter
7. Verifikasi baris `Voltage Spec {runId}-038` menampilkan Value Type `Global`
8. Klik row action `⋯` > `Edit` pada baris `Voltage Spec {runId}-038`
9. Verifikasi form Edit menampilkan `Generator` = `220V`
10. Verifikasi form Edit menampilkan `Pump` = `110V`
11. Klik `[✕]`

#### TC-FA-CF-106: Create Value Type Global Scope General menyimpan satu nilai shared

12. Klik `[+ Custom Field]`
13. Isi Field Name `Company Tagline {runId}-038`, Data Type `Text`, Scope `General`, Value Type `Global`, Value `Safety First`
14. Tunggu toast lama hilang otomatis
15. Klik `[Submit]`
16. Verifikasi toast sukses: "Success, custom field has been created."
17. Ganti isi kotak search dengan `Company Tagline {runId}-038`, tekan Enter
18. Buka Edit field tersebut lewat row action `⋯` > `Edit`
19. Verifikasi form Edit menampilkan satu input `Value` ber-pre-filled `Safety First`
20. Klik `[✕]`

#### TC-FA-CF-107: Toggle Required Yes tersimpan dan tampil sebagai badge Yes

21. Klik `[+ Custom Field]`
22. Isi Field Name `Mandatory Tag {runId}-038`, Data Type `Text`, ubah toggle Required ke Yes
23. Klik `[Submit]`
24. Ganti isi kotak search dengan `Mandatory Tag {runId}-038`, tekan Enter
25. Verifikasi baris `Mandatory Tag {runId}-038` menampilkan Required `Yes`

#### TC-FA-CF-121: Jumlah opsi per field tidak dibatasi atas

26. Klik `[+ Custom Field]`
27. Pilih Data Type `Dropdown`
28. Isi Field Name `Many Options {runId}-038`
29. Tambahkan 150 opsi berbeda `Opt 001` sampai `Opt 150` lewat skrip pada input Values
30. Verifikasi tidak ada pesan batas jumlah opsi
31. Tunggu toast lama hilang otomatis
32. Klik `[Submit]`
33. Verifikasi toast sukses: "Success, custom field has been created."

#### TC-FA-CF-122: Klik badge opsi mengubah nama opsi di form Create

34. Klik `[+ Custom Field]`
35. Pilih Data Type `Dropdown`
36. Ketik `Gold` pada input Values lalu tekan Enter
37. Klik badge `Gold`
38. Ubah menjadi `Platinum` lalu tekan Enter
39. Verifikasi badge menampilkan `Platinum` pada posisi yang sama
40. Klik `[✕]`
41. Verifikasi dialog `Unsaved Changes` tampil
42. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini 42 langkah, di atas smell 35 langkah (bagian 3 prinsip 13), dan dipertahankan karena lima TC Create sukses satu topik dengan satu akun dan satu dataset, kelas harness yang sama, dan berdiri sendiri: tiap TC membuat field bernama sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan tidak ada langkah yang dapat dihapus tanpa melepas klausa Expected.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16; langkah 6 dan Search berikutnya), membuka row action `⋯` > `Edit` pada TC-FA-CF-105 dan TC-FA-CF-106 untuk membaca nilai tersimpan, `Klik [✕]` yang menutup form Edit tanpa perubahan (tanpa dialog), dan penutupan form dirty pada langkah 40 dan dua langkah berikutnya (S-08). Kotak Search tidak dikosongkan di akhir karena hook `beforeEach` suite membuka layar awal untuk spec berikutnya.
- Field Dinamis bernama bersuffix `{runId}-038` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Langkah penghubung toast (S-03, R-22): langkah 14 dan 31 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-121 langkah 4 membolehkan 'paste satu per satu atau skrip'; spec memilih skrip dan menulisnya sebagai kemampuan teknis.
  - TC-FA-CF-105 butir c menyatakan nilai dilihat saat Edit; spec membuka form Edit dan menutupnya tanpa perubahan.
