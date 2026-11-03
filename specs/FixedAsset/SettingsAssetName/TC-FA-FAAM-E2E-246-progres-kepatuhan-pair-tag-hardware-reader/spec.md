---
id: TC-FA-FAAM-E2E-246-progres-kepatuhan-pair-tag-hardware-reader
title: "Progres Kepatuhan TAG Type: Pair TAG pada Aset Not Paired Yet dengan Reader USB"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-841
coverage:
  web: automated
---

# Progres Kepatuhan TAG Type: Pair TAG pada Aset Not Paired Yet dengan Reader USB

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before` (Tabel Data Uji Dinamis No. 114; salinan Pre-setup No. 40): `Pair Item 841 {runId}-246` dengan TAG Type `RFID` dan 3 aset `Active`: `Pair Item 841 {runId}-246 - 1` dan `Pair Item 841 {runId}-246 - 2` ber-Tag `Paired` RFID, `Pair Item 841 {runId}-246 - 3` (Group `Plant A`) `Not Paired Yet`; Tag RFID `RF-00420` berstatus Available di stok Global. Kode Tag mengikuti literal Tabel Dinamis (unik per salinan).
- Kemampuan teknis: simulator reader RFID/NFC USB tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader (disediakan tim BE/FE); Fixed Asset > TAG > Paired (Popup Detail, tombol `Show` di samping `Not Paired Yet`, row action `Pair TAG`, ButtonScan `Scan RFID` pada slot `RFID TAG`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini dan kembalikan Tag `RF-00420` ke stok Available.
- State global yang diubah: stok Tag Global (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-841: login sebagai Total Control dan berada di Fixed Asset > TAG > Paired.

## Test Steps

1. Buka Fixed Asset > Settings > Asset Master > Asset Name
2. Ketik Search `Pair Item 841 {runId}-246`, tekan Enter
3. Klik nama `Pair Item 841 {runId}-246`
4. Verifikasi baris progres `2 / 3 assets match the TAG type`
5. Tutup Popup Detail
6. Buka Fixed Asset > TAG > Paired
7. Ketik Search `Pair Item 841 {runId}-246`, tekan Enter
8. Klik Asset Name `Pair Item 841 {runId}-246` pada baris grup Plant A untuk membuka Popup Detail
9. Klik tombol teks `Show` di samping field `Not Paired Yet`
10. Klik row action `Pair TAG` pada baris `Pair Item 841 {runId}-246 - 3`
11. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
12. Pindai Tag `RF-00420` dengan simulator reader USB
13. Klik `[Submit]`
14. Buka Fixed Asset > Settings > Asset Master > Asset Name
15. Ketik Search `Pair Item 841 {runId}-246`, tekan Enter
16. Klik nama `Pair Item 841 {runId}-246`
17. Verifikasi baris progres `3 / 3 assets match the TAG type`
18. Verifikasi `[N]` tetap 3

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 6, 14 (navigasi), langkah 2, 7, 15 (Search untuk menemukan baris target), dan langkah 5 (menutup Popup Detail).
- Pembagian TC lintas spec: TC-FA-FAAM-839 dan 840 (Replace TAG dengan reader USB) ada di spec 230.
- Temuan untuk QA: TC-FA-FAAM-841 tidak menyebut cara menutup Popup Detail tab Paired sebelum pindah surface; spec berpindah lewat navigasi menu.
