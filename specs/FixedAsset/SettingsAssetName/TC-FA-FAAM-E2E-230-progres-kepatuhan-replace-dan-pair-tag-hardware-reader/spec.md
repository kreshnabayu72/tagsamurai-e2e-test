---
id: TC-FA-FAAM-E2E-230-progres-kepatuhan-replace-dan-pair-tag-hardware-reader
title: "Progres Kepatuhan TAG Type: Replace TAG dengan Reader USB, Popup Tidak Auto-Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-839
  - TC-FA-FAAM-840
coverage:
  web: automated
---

# Progres Kepatuhan TAG Type: Replace TAG dengan Reader USB, Popup Tidak Auto-Refresh

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini (sesi 1); halaman dibuka hook `beforeEach` suite. Konteks UI kedua (sesi 2, akun yang sama) dibuka dan ditutup di dalam TC-FA-FAAM-840. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-230` (Tabel Data Uji Dinamis No. 112 dan 113; salinan Pre-setup No. 39):
  - `Replace Item 839 {runId}-230`: TAG Type `RFID`, 40 aset `Active` (Group `Plant A` 20 dan `Plant B` 20); 39 aset ber-Tag `Paired` RFID dan `Replace Item 839 {runId}-230 - 42` (Plant A) ber-Tag `Paired` QR `QR-00230` (Non-standard); Tag RFID `RF-00412` berstatus Available di stok Global.
  - `Replace Item 840 {runId}-230`: sama, dengan aset `Replace Item 840 {runId}-230 - 42` ber-Tag QR `QR-00231` dan Tag RFID `RF-00415` Available.
  - Kode Tag mengikuti literal Tabel Dinamis (unik per salinan).
- Kemampuan teknis: simulator reader RFID/NFC USB tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader (disediakan tim BE/FE; TC menyebutnya pada precondition e); Fixed Asset > TAG > Paired (Popup Detail, row action `Replace TAG`, ButtonScan `Scan RFID` pada slot `RFID TAG`); konteks UI kedua untuk TC-FA-FAAM-840.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini, kembalikan Tag `RF-00412` dan `RF-00415` ke stok Available, dan tutup konteks UI kedua.
- State global yang diubah: stok Tag Global (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-839 dan 840: login sebagai Total Control dan berada di Fixed Asset > TAG > Paired untuk TC-FA-FAAM-839 dan di Fixed Asset > Settings > Asset Master > Asset Name untuk TC-FA-FAAM-840.

## Test Steps

### TC-FA-FAAM-839: Replace TAG pada Tag Non-standard di tag/ menambah progres kepatuhan

1. Ketik Search `Replace Item 839 {runId}-230`, tekan Enter
2. Klik nama `Replace Item 839 {runId}-230`
3. Verifikasi baris progres `39 / 40 assets match the TAG type`
4. Tutup Popup Detail
5. Buka Fixed Asset > TAG > Paired
6. Ketik Search `Replace Item 839 {runId}-230`, tekan Enter
7. Klik Asset Name `Replace Item 839 {runId}-230` pada baris grup Plant A untuk membuka Popup Detail
8. Klik row action `Replace TAG` pada baris `Replace Item 839 {runId}-230 - 42`
9. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
10. Pindai Tag `RF-00412` dengan simulator reader USB
11. Klik `[Submit]`
12. Buka Fixed Asset > Settings > Asset Master > Asset Name
13. Ketik Search `Replace Item 839 {runId}-230`, tekan Enter
14. Klik nama `Replace Item 839 {runId}-230`
15. Verifikasi baris progres `40 / 40 assets match the TAG type`
16. Verifikasi `[N]` 40 menghitung seluruh aset `Active` Asset Name itu (Plant A dan Plant B), tidak dipotong per group
17. Tutup Popup Detail

### TC-FA-FAAM-840: Popup Detail yang terbuka tidak diperbarui otomatis saat Tag diganti di tag/

18. Ganti isi kotak search dengan `Replace Item 840 {runId}-230`, tekan Enter
19. Sesi 1: klik nama `Replace Item 840 {runId}-230` dan biarkan popup terbuka
20. Verifikasi baris progres `39 / 40 assets match the TAG type`
21. Sesi 2: buka konteks UI kedua dan login sebagai Total Control
22. Sesi 2: buka Fixed Asset > TAG > Paired
23. Sesi 2: ketik Search `Replace Item 840 {runId}-230`, tekan Enter
24. Sesi 2: buka Popup Detail `Replace Item 840 {runId}-230` pada baris grup Plant A
25. Sesi 2: klik row action `Replace TAG` pada baris `Replace Item 840 {runId}-230 - 42`
26. Sesi 2: klik ButtonScan `Scan RFID` pada slot `RFID TAG`
27. Sesi 2: pindai Tag `RF-00415` dengan simulator reader USB
28. Sesi 2: klik `[Submit]` sampai berhasil
29. Tutup konteks UI kedua dan hapus sesi login browser terkait
30. Sesi 1: tunggu 5 detik tanpa memuat ulang halaman
31. Verifikasi baris progres sesi 1 tetap `39 / 40 assets match the TAG type` tanpa menutup atau memuat ulang popup
32. Sesi 1: tutup popup lalu klik nama `Replace Item 840 {runId}-230` lagi
33. Verifikasi baris progres `40 / 40 assets match the TAG type`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 6, 13, 18, 23 (Search untuk menemukan baris target), langkah 4, 17 (menutup Popup Detail), langkah 5, 12, 22 (navigasi), langkah 21 dan 29 (membuka dan menutup konteks UI kedua; S-09), dan langkah 30 (jendela standar 5 detik tanpa memuat ulang, bagian 6 konvensi; pilihan spec karena TC tidak menyebut durasinya).
- P-7: TC-FA-FAAM-839 dan 840 membutuhkan simulator reader USB RFID/NFC (kelas d) dan TC-FA-FAAM-840 juga membutuhkan dua sesi (kelas c); keduanya berada dalam satu spec karena sesi 2 hanya memicu penggantian Tag dengan reader, sedangkan objek asersi (popup sesi 1 tidak diperbarui otomatis) memakai sesi 1. TC-FA-FAAM-841 (Pair TAG, juga reader USB) ada di spec 246.
- Temuan untuk QA:
  - TC-FA-FAAM-839 butir b merujuk TC-FA-TAG-1152 ("selaras") tanpa menyebut nilai tambahan; spec mengasersi nilai yang tertulis di TC ini.
  - TC-FA-FAAM-840 tidak menyebut durasi jendela untuk memastikan popup tidak diperbarui otomatis; spec memakai 5 detik.
  - Kode Tag `QR-00230`, `QR-00231`, `RF-00412`, `RF-00415` tidak bersuffix `{runId}` karena kode Tag unik per salinan menurut Tabel Dinamis; hook `before` menghapus sisa dari run lama.
