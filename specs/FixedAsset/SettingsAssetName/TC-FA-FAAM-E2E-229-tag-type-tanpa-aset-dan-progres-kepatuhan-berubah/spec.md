---
id: TC-FA-FAAM-E2E-229-tag-type-tanpa-aset-dan-progres-kepatuhan-berubah
title: "TAG Type: Tanpa Aset Tidak Menambah Non-Standard dan Progres Kepatuhan Popup Detail Berubah Lalu Dipulihkan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-664
  - TC-FA-FAAM-838
coverage:
  web: automated
---

# TAG Type: Tanpa Aset Tidak Menambah Non-Standard dan Progres Kepatuhan Popup Detail Berubah Lalu Dipulihkan

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Akun aktor kedua (ganti akun eksplisit di langkah 35): Manage Asset & TAG `manageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 9b; `Spectra.env.FA_MAT_PASSWORD`, nama baru, didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik repo), dipakai untuk membuka Fixed Asset > TAG > Paired.
- Env var: `FA_TC_PASSWORD`, `FA_MAT_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-229`:
  - `Excavator 20 Ton 838 {runId}-229` (Tabel Data Uji Dinamis No. 111; salinan Pre-setup No. 38): TAG Type `RFID`, 40 aset `Active` (Group `Plant A` 20 aset: 18 ber-Tag `Paired` RFID, 2 `Not Paired Yet`; Group `Plant B` 20 aset: 15 ber-Tag `Paired` RFID, 5 ber-Tag `Paired` QR Non-standard); `[Compliant]` 33 dari `[N]` 40. Disediakan ulang ke keadaan Pre-setup No. 38 di hook `after`.
  - `Edit Target Item 664 {runId}-229` (Code `ETI664`; Tabel Dinamis No. 55): salinan fixture 13d, Total Asset 0, TAG Type `QR`.
- Kemampuan teknis: Popup Detail dengan baris progres kepatuhan TAG Type; Fixed Asset > TAG > Paired.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Edit Target Item 664 {runId}-229` dan sediakan ulang `Excavator 20 Ton 838 {runId}-229`.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-664 dan 838: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-838: Perubahan TAG Type memperbarui progres kepatuhan di Popup Detail dan pengembalian memulihkannya

1. Ketik Search `Excavator 20 Ton 838 {runId}-229`, tekan Enter
2. Klik nama `Excavator 20 Ton 838 {runId}-229`
3. Verifikasi baris progres `33 / 40 assets match the TAG type`
4. Tutup Popup Detail
5. Klik `⋯` baris `Excavator 20 Ton 838 {runId}-229` lalu `Edit`
6. Verifikasi Modal Edit memuat field TAG Type
7. Verifikasi Modal Edit tidak memuat baris progres
8. Lepas `RFID` dan pilih `NFC` pada TAG Type
9. Klik `[Save]`
10. Klik `[Save]` pada dialog Change TAG Type
11. Klik nama `Excavator 20 Ton 838 {runId}-229`
12. Verifikasi baris progres `0 / 40 assets match the TAG type`
13. Verifikasi `[N]` tetap 40 (Plant A 20 dan Plant B 20), tidak dipotong per group
14. Verifikasi tidak ada aset ber-Tag `Paired` NFC
15. Tutup Popup Detail
16. Klik `⋯` baris `Excavator 20 Ton 838 {runId}-229` lalu `Edit`
17. Verifikasi Modal Edit memuat field TAG Type
18. Verifikasi Modal Edit tidak memuat baris progres
19. Lepas `NFC` dan pilih `RFID` pada TAG Type
20. Klik `[Save]`
21. Klik `[Save]` pada dialog Change TAG Type
22. Klik nama `Excavator 20 Ton 838 {runId}-229`
23. Verifikasi baris progres kembali `33 / 40 assets match the TAG type`
24. Tutup Popup Detail
25. Buka Fixed Asset > TAG > Paired
26. Ketik Search `Excavator 20 Ton 838 {runId}-229`, tekan Enter
27. Verifikasi Tag RFID `Excavator 20 Ton 838 {runId}-229` tidak lagi Non-standard
28. Verifikasi 5 aset ber-Tag QR tetap Non-standard

### TC-FA-FAAM-664: Edit TAG Type tanpa aset tidak menambah grup atau Tag Non-standard di tab Paired

29. Buka Fixed Asset > Settings > Asset Master > Asset Name
30. Ketik Search `Edit Target Item 664 {runId}-229`, tekan Enter
31. Klik `⋯` baris `Edit Target Item 664 {runId}-229` lalu `Edit`
32. Ubah TAG Type dari `QR` menjadi `RFID`
33. Klik `[Save]`
34. Tunggu aksi selesai
35. Logout lalu login sebagai Manage Asset & TAG
36. Buka Fixed Asset > TAG > Paired
37. Verifikasi tabel tab Paired tampil dengan sedikitnya satu baris grup
38. Ketik Search `Edit Target Item 664 {runId}-229`, tekan Enter
39. Verifikasi tidak ada baris grup untuk `Edit Target Item 664 {runId}-229`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 26, 30, 38 (Search untuk menemukan baris target), langkah 4, 15, 24 (menutup Popup Detail), langkah 25, 29, 36 (navigasi), langkah 34 (menunggu `[Save]` selesai sebelum ganti akun), dan langkah 35 (ganti akun eksplisit; S-07).
- Di atas smell 35 langkah. Spec berisi 39 langkah, di atas ~35 hanya sedikit. Alasan: dua blok TAG Type yang berdiri sendiri dengan seed sendiri; langkah berulang pada TC-FA-FAAM-838 (dua kali Edit TAG Type) adalah isi TC.
- Langkah 7, 18, dan 39 adalah asersi absence dengan anchor positif langkah 6, 17, dan 37 pada surface yang sama (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-FAAM-665, 828 ada di spec 228; TC-FA-FAAM-829 ada di spec 245.
- Temuan untuk QA:
  - TC-FA-FAAM-838 butir c ("Tag RFID tidak lagi Non-standard, sedangkan 5 aset ber-Tag QR tetap Non-standard") tidak menyebut surface pengamatannya; spec mengamati di Fixed Asset > TAG > Paired.
  - TC-FA-FAAM-838 butir b mengacu "tidak ada aset ber-Tag `Paired` NFC" tanpa surface; spec mengasersi pada Popup Detail yang sama.
  - TC-FA-FAAM-664 memakai satu akun `Total Control` untuk Edit lalu `Manage Asset & TAG` untuk membaca tab Paired (Pre-setup No. 9b).
