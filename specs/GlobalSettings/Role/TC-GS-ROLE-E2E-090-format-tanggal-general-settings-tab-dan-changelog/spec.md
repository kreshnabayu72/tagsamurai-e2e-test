---
id: TC-GS-ROLE-E2E-090-format-tanggal-general-settings-tab-dan-changelog
title: "Format Tanggal General Settings pada Tab Total Control dan Modal Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-238
  - TC-GS-ROLE-239
coverage:
  web: automated
---

# Format Tanggal General Settings pada Tab Total Control dan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- State global yang diubah: General Settings (Date Format, Time Format). Hook `before` menyetel General Settings ke Date Format `dd/MM/yy`, Time `24h (HH:mm)`, Timezone `Asia/Jakarta` lewat API (precondition b kedua TC). TC-GS-ROLE-238 mengubahnya menjadi `dd MMM yy` dan `12h (hh:mm a)`; langkah 20 memulihkannya dan hook `after` memulihkan ke nilai awal sebelum spec (dicatat di hook `before`) tanpa berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data: Changelog Tab System memuat sedikitnya satu entri. Hook `before` meng-assign baris Manage TAG ke Wawan Setiawan (Pre-setup #11, tanpa baris role) lewat API sehingga satu entri Changelog Tab System tercipta (TC tidak menyebut sumber entri; dipakai sebagai precondition, tidak diasersi). Hook `after` menghapus baris itu lewat API. Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log (log bersifat immutable).
- Kemampuan teknis: membaca dan menyetel General Settings lewat API; membaca nilai teks kolom Last Updated, kolom Date Modal Changelog, dan input filter rentang tanggal.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-GS-ROLE-239: Format tanggal mengikuti General Settings pada Modal Changelog dan filternya

1. Buka Tab System, klik `Changelog`
2. Verifikasi nilai kolom Date entri teratas berformat `dd/MM/yy HH:mm` (contoh `17/03/23 14:30`)
3. Buka filter Date, pilih rentang yang memuat tanggal entri teratas
4. Verifikasi nilai di input filter Date berformat `dd/MM/yy HH:mm`
5. Tutup Modal Changelog dengan `✕`

### TC-GS-ROLE-238: Format tanggal mengikuti General Settings pada Tab Total Control dan filternya

6. Buka Tab Total Control, ketik Search `Ahmad Fauzi`, tekan Enter
7. Verifikasi nilai kolom Last Updated baris Ahmad Fauzi berformat `dd/MM/yy HH:mm` (contoh `17/03/23 14:30`)
8. Klik `Filter`, pilih rentang Last Updated yang memuat Last Updated baris Ahmad Fauzi
9. Verifikasi nilai di input filter Last Updated berformat `dd/MM/yy HH:mm`
10. Tutup panel Filter
11. Buka Global Settings > General Settings
12. Ubah Date Format ke `dd MMM yy`
13. Ubah Time ke `12h (hh:mm a)`
14. Klik `[Save]`
15. Tunggu aksi selesai
16. Buka Role & Permission > Tab Total Control, muat ulang halaman, ketik Search `Ahmad Fauzi`, tekan Enter
17. Verifikasi nilai kolom Last Updated baris Ahmad Fauzi berformat `dd MMM yy hh:mm a` (contoh `17 Mar 23 02:30 PM`)
18. Klik `Filter`, pilih rentang Last Updated yang memuat Last Updated baris Ahmad Fauzi
19. Verifikasi nilai di input filter Last Updated berformat `dd MMM yy hh:mm a`
20. Pulihkan General Settings: ubah Date Format ke `dd/MM/yy` dan Time ke `24h (HH:mm)`, klik `[Save]`
21. Tunggu aksi selesai

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dibalik dari TC sumber: TC-GS-ROLE-239 (hanya membaca, memakai format awal) lebih dulu, TC-GS-ROLE-238 paling akhir karena mengubah state global General Settings (bagian 3 prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search baris Ahmad Fauzi (langkah 6, 16); menutup Modal Changelog dan panel Filter (langkah 5, 10); membuka General Settings dan mengubah format (langkah 11 sampai 14, bagian dari Langkah Uji 3 TC-GS-ROLE-238); "Tunggu aksi selesai" (langkah 15, 21); pemulihan General Settings (langkah 20 dan 21, S-09).
- Langkah 2, 4, 7, 9, 17, dan 19 memverifikasi pola teks nilai (pola `dd/MM/yy HH:mm` dan `dd MMM yy hh:mm a`) dengan contoh dari Expected TC.
- Temuan untuk QA:
  - TC-GS-ROLE-238 Langkah Uji 2 dan TC-GS-ROLE-239 Langkah Uji 2 ("pilih rentang") tidak menyebut nilai rentang; spec memilih rentang yang memuat tanggal baris atau entri yang diperiksa.
  - TC-GS-ROLE-238 Expected b ("Setelah diubah tampil dengan format ...") tidak menyebut subjeknya; spec mengasersi Last Updated dan input filter, sama seperti Expected a.
  - TC-GS-ROLE-239 tidak menyebut sumber entri Changelog Tab System; spec memakai satu entri hasil seeding di hook `before`.
  - TC-GS-ROLE-238 mengubah General Settings tanpa menyebut pemulihannya.
